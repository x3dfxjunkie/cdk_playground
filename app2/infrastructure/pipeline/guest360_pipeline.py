"""
Guest360Pipeline Module
"""
import os
from pathlib import Path

import yaml
from aws_cdk import (
    Aspects,
    Environment,
    Stack,
    Tags,
    aws_codebuild,
    aws_codestarnotifications,
    aws_ec2,
    aws_ecr,
    aws_iam,
    pipelines,
)
from cdk_nag import NagSuppressions
from constructs import Construct

from app.guest360_aspects.guest360_cw_alarms import Guest360CWAlarms
from app.guest360_aspects.guest360_tagging import Guest360PathTagger
from app.guest360_aspects.guest360_termination import Guest360Termination
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.guest360_constructs.sns_topic import Guest360SNSTopic
from app.infrastructure.pipeline.guest360_stage import Guest360Stage
from app.infrastructure.reliability.enable_stack import DeployFlag
from app.infrastructure.workstream_stack import WorkstreamStack
from app.infrastructure.utils import cli_to_python_bool


class Guest360PipelineStack(WorkstreamStack):
    """Guest360PipelineStack

    Args:
        Stack (aws_cdk.Stack): AWS CDK stack
    """

    def __init__(self, scope: Construct, construct_id: str, environment_config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # =====================================================================
        # Begin environment variable setup
        # =====================================================================
        environment = self.node.try_get_context("environment")
        self._stack = Stack.of(self)
        self._stack_name = self.node.try_get_context("stack_name")

        self.node.set_context(
            "prefix",
            "-".join(
                [
                    environment_config["short_env"],
                    environment_config["networking"][self._stack.region]["short_region"],
                    self._stack_name,
                ]
            ).lower(),
        )
        prefix = self.node.try_get_context("prefix")
        self.node.set_context("is_static_env", "guest360" in prefix)
        is_static_env = self.node.try_get_context("is_static_env")
        is_docker_account = environment in ["latest", "stage"]
        self.node.set_context("is_docker_account", is_docker_account)

        # Tags
        Tags.of(self._stack).add("environment", environment)
        if is_static_env:
            Tags.of(self._stack).add("environment_type", "static")
        else:
            Tags.of(self._stack).add("environment_type", "ephemeral")

        file_path = Path(os.path.realpath(__file__))
        pipeline_dir = str(file_path.parent)

        self._subnet_selection(environment_config)

        # Load pipeline environment variables
        with open(f"{pipeline_dir}/configs/{environment}-pipeline.yml", "r", encoding="utf-8") as file:
            pipeline_config = yaml.safe_load(file)
        # =====================================================================
        # End environment variable setup
        # =====================================================================

        # S3 Bucket for pipeline entry point.
        self.bucket = Guest360S3Bucket(
            self,
            f"{self._stack_name}-pipeline-bucket",
            self._stack.region,
            {
                "bucket_name": "build-pipeline-bucket",
                "bucket_key_enabled": False,
            },
        )

        if environment in ("latest", "stage"):
            # Grant write access to GitHub Actions.
            self.bucket.bucket.grant_read_write(aws_iam.AccountRootPrincipal())
            self.bucket.bucket.grant_put_acl(aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn"]))
            self.bucket.bucket.grant_put_acl(aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn_codebuild"]))
            self.bucket.bucket.grant_write(aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn"]))
            self.bucket.bucket.grant_write(aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn_codebuild"]))
            self.bucket.kms_key.grant_encrypt_decrypt(aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn"]))
            self.bucket.kms_key.grant_encrypt_decrypt(
                aws_iam.ArnPrincipal(pipeline_config["github_action_role_arn_codebuild"])
            )

        self.s3_source = pipelines.CodePipelineSource.s3(
            self.bucket.bucket,
            object_key="CodeBuild/Guest360/app.zip",
        )

        """
        Deployment pipeline
        """

        # Allow writes from the previous environment for promotion of code artifact.
        if pipeline_config is not None and "previous_environment_iam" in pipeline_config.keys():
            # Add permissions from the previous environment to the current environment bucket.
            self.bucket.bucket.grant_read_write(aws_iam.ArnPrincipal(pipeline_config["previous_environment_iam"]))
            self.bucket.bucket.grant_put_acl(aws_iam.ArnPrincipal(pipeline_config["previous_environment_iam"]))

        self._bucket_access(pipeline_config)

        # Create the main pipeline object
        synth_policy = aws_iam.PolicyStatement(
            actions=[
                "ec2:Describe*",
                "ec2:Get*",
                "ec2:Search*",
                "sts:AssumeRole",
            ],
            resources=[
                "*",
            ],
        )

        # Build docker ecr credentials
        ecr_repos = []
        for source_repo in self.app_constants["ecr"]["source_repos"]:
            if source_repo["type"] == "internal":
                repo_arn = f"arn:aws:ecr:us-east-1:{self.account}:repository/" + source_repo["prefix"]
            else:
                repo_arn = source_repo["arn"]
            ecr_repos.append(aws_ecr.Repository.from_repository_arn(self, source_repo["name"], repo_arn))
        docker_creds = [pipelines.DockerCredential.ecr([repo]) for repo in ecr_repos]

        # Pipeline object
        self.pipeline = pipelines.CodePipeline(
            self,
            "guest360-static-pipeline",
            docker_credentials=docker_creds,
            code_build_defaults=pipelines.CodeBuildOptions(
                build_environment={
                    "build_image": aws_codebuild.LinuxBuildImage.STANDARD_6_0,
                    "compute_type": aws_codebuild.ComputeType.LARGE,
                },
                subnet_selection=self._subnets,
                vpc=self._vpc,
            ),
            synth=pipelines.CodeBuildStep(
                "Synth",
                input=self.s3_source,
                commands=[
                    "cd ${CODEBUILD_SRC_DIR}",
                    "export PYTHONPATH=$(pwd):${PYTHONPATH}",
                    "export AWS_USE_FIPS_ENDPOINT=true",
                    "env | sort",
                    "cd $(dirname $(find . -maxdepth 2 -type f -name cdk.json))",
                    "pip install -r requirements.txt",
                    f"npx aws-cdk synth '**' --verbose --debug --trace --context environment={environment} --context stack_name={self._stack_name}",
                ],
                primary_output_directory="app/cdk.out",
                role_policy_statements=[synth_policy],
            ),
        )

        # Dynamically get the regions from environment configs
        self._regions = list(environment_config["networking"].keys())
        self._stages = {}
        self._waves = {}

        # Docker Activation Logic
        docker_stack_activated = DeployFlag.is_stack_enabled(self, stack_name="Docker")
        is_docker_context = cli_to_python_bool(self.node.get_context("docker_enabled"))
        is_docker_ephemeral_target = is_docker_context and docker_stack_activated
        is_docker_account = environment in ["latest", "stage"]
        docker_conditions_met = is_docker_account and (is_static_env or is_docker_ephemeral_target)

        # Create docker wave
        if docker_conditions_met:
            self._waves["docker"] = self.pipeline.add_wave(f"{environment}-docker")
            self._stages["docker"] = Guest360Stage(
                self,
                f"{environment.lower()}-{self._stack_name.lower()}-docker-us-east-1",
                env=Environment(
                    account=self._stack.account,
                    region="us-east-1",
                ),
                environment_config=environment_config,
                stack_tags=self._stack.tags.tag_values(),
                stage_name="docker",
            )

        # Add a step for SQL Generation
        self.promote.append(
            pipelines.CodeBuildStep(
                "sql generation",
                commands=[
                    "cd ${CODEBUILD_SRC_DIR}",
                    "pip install -r app/src/data_service/marketplace/sql_generator/requirements.txt",
                    "export PYTHONPATH=$(pwd):${PYTHONPATH}",
                    "python3 app/src/data_service/marketplace/sql_generator/data_contract_to_sql.py",
                    f"aws s3 sync --sse AES256 app/src/data_service/marketplace/sql_generator/generated_sql/{environment}/ s3://{self.bucket.bucket.bucket_name}/data_service/generated_sql/",
                ],
                role_policy_statements=[self.bucket_access_policies[self.bucket.bucket.bucket_name]],
            ),
        )

        self._make_waves(environment_config=environment_config)
        self._setup_stages(docker=docker_conditions_met, promote=self.promote)
        self._grant_bucket_permissions()

        # =====================================================================
        # Pipeline Notifications
        # =====================================================================
        self.pipeline.build_pipeline()

        # Approval Notifications
        sns_topic_approval = Guest360SNSTopic(
            self, f"{environment}-pipeline-notifier", {"topic_name": "cdk-pipeline-approval"}
        )
        sns_topic_approval.topic.grant_publish(aws_iam.AccountRootPrincipal())
        self._approval_notifications(sns=sns_topic_approval)

        # Change Request Notifications
        if environment in self.UpperEnvNames:
            sns_topic_change_requests = Guest360SNSTopic(
                self, f"{environment}-pipeline-change-requests", {"topic_name": "cdk-pipeline-change-requests"}
            )
            sns_topic_change_requests.topic.grant_publish(aws_iam.AccountRootPrincipal())
            self._change_request_notifications(sns=sns_topic_change_requests)

        # =====================================================================

        # Nag Suppressions
        self._nag_suppressions(sns=sns_topic_approval)

    def _bucket_access(self, pipeline_config: dict | None) -> None:
        """Bucket access and promote step creation.

        For any buckets that are listed as promote buckets, grant access and copy the deployment artifact.

        Args:
            pipeline_config (dict): Pipeline configuration object

        Returns:
            None
        """
        self.buckets = [self.bucket.bucket.bucket_name]
        self.bucket_access_policies = {}
        self.promote = []

        if pipeline_config is not None and "promote_bucket" in pipeline_config.keys():
            self.buckets.append(pipeline_config["promote_bucket"])

        self.buckets.sort()

        for bucket in self.buckets:
            # If the bucket is the same as the current environment source bucket,
            # add a suffix of "_deployed".
            if bucket == self.bucket.bucket.bucket_name:
                suffix = "_deployed"
            else:
                suffix = ""

            # Create a map of bucket access policies, for use with other tasks.
            self.bucket_access_policies[bucket] = aws_iam.PolicyStatement(
                actions=[
                    "s3:Abort*",
                    "s3:GetBucket*",
                    "s3:GetObject*",
                    "s3:List*",
                    "s3:PutObject*",
                ],
                resources=[f"arn:aws:s3:::{bucket}/*", f"arn:aws:s3:::{bucket}"],
            )

            # Append a CodeBuild step for copying the deployment artifact.
            self.promote.append(
                pipelines.CodeBuildStep(
                    f"promote-{self.buckets.index(bucket)}",
                    build_environment={
                        "build_image": aws_codebuild.LinuxBuildImage.STANDARD_6_0,
                        "compute_type": aws_codebuild.ComputeType.LARGE,
                    },
                    commands=[
                        "cd ${CODEBUILD_SRC_DIR}",
                        "ls -lhFa",
                        "zip -r app.zip .",
                        f"aws s3 cp --sse AES256 app.zip s3://{bucket}/CodeBuild/Guest360/app{suffix}.zip"
                        + " --acl bucket-owner-full-control",
                    ],
                    role_policy_statements=[self.bucket_access_policies[bucket]],
                )
            )

    def _make_waves(self, environment_config: dict) -> None:
        """Create a wave (parallel deployment) in each region and create the stacks in that region."""
        for region in self._regions:
            self._waves[region] = self.pipeline.add_wave(f"{self.deployment_environment}-{region}")
            self._stages[region] = Guest360Stage(
                self,
                f"{self.deployment_environment}-{self._stack_name.lower()}-pipeline-{region}",
                env=Environment(
                    account=self._stack.account,
                    region=region,
                ),
                environment_config=environment_config,
                stack_tags=self._stack.tags.tag_values(),
                stage_name="main",
            )

    def _setup_stages(self, docker: bool, promote: pipelines.CodeBuildStep | None) -> None:
        """Deploy each region with extra steps in the stage"""
        deploy_waves = ["docker", *self._regions] if docker else [*self._regions]
        match self.deployment_environment:
            case "prod":
                # show manual approval step
                pre = [pipelines.ManualApprovalStep(f"Deploy{self.deployment_environment.title()}")]
            case "latest":
                # forced sleep, to bunch up executions behind (due to rate limiting of CloudFormation lookups)
                pre = [pipelines.ShellStep("sleep", commands=["sleep 600"])]
            case _:
                pre = []
        for wave in deploy_waves:
            self._waves[wave].add_stage(
                self._stages[wave],
                pre=pre,
                # Copy artifact to input bucket for next environment, if configured
                # and not "us-east-1" region (eg final region).
                post=None if wave in ["docker", "us-east-1"] else promote,
            )

    def _grant_bucket_permissions(self) -> None:
        """Grant access to the deployment bucket object"""
        self.bucket.bucket.grant_read(aws_iam.AccountRootPrincipal())
        self.bucket.bucket.encryption_key.grant_decrypt(aws_iam.AccountRootPrincipal())

        self.bucket.bucket.add_to_resource_policy(
            aws_iam.PolicyStatement(
                actions=[
                    "s3:GetObject*",
                ],
                principals=[aws_iam.AccountRootPrincipal()],
                resources=[self.bucket.bucket.arn_for_objects("CodeBuild/Guest360/app.zip")],
            )
        )

    def _approval_notifications(self, sns: Guest360SNSTopic) -> None:
        """SNS Notifications regarding deployment status"""
        aws_codestarnotifications.NotificationRule(
            self,
            f"{self.prefix}-notification-rule",
            events=[
                "codepipeline-pipeline-manual-approval-failed",
                "codepipeline-pipeline-manual-approval-needed",
                "codepipeline-pipeline-manual-approval-succeeded",
                "codepipeline-pipeline-pipeline-execution-canceled",
                "codepipeline-pipeline-pipeline-execution-failed",
                "codepipeline-pipeline-pipeline-execution-resumed",
                "codepipeline-pipeline-pipeline-execution-started",
                "codepipeline-pipeline-pipeline-execution-succeeded",
            ],
            source=self.pipeline.pipeline,
            targets=[sns.topic],
        )

    def _change_request_notifications(self, sns: Guest360SNSTopic) -> None:
        """
        Notifications for change request
        https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-pipeline
        """
        aws_codestarnotifications.NotificationRule(
            self,
            f"{self.prefix}-notification-rule-cr",
            events=[
                "codepipeline-pipeline-manual-approval-needed",
            ],
            source=self.pipeline.pipeline,
            targets=[sns.topic],
        )

    def _nag_suppressions(self, sns: Guest360SNSTopic) -> None:
        """Add nag suppression"""
        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-CB4", "reason": "No configurable way to enable KMS with aws_cdk.pipelines."},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok."},
                {
                    "id": "AwsSolutions-L1",
                    "reason": "Lambdas in this stack are created by CDK directly as helper functions.",
                },
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Most of the CI/CD pipeline policies require * and have other errors with suppressions.",
                },
                {"id": "AwsSolutions-S1", "reason": "CodePipeline bucket does not need logging."},
            ],
        )

        NagSuppressions.add_resource_suppressions(
            self.bucket.bucket, [{"id": "AwsSolutions-S2", "reason": "This bucket needs to be cross-account."}], True
        )

        NagSuppressions.add_resource_suppressions(
            sns.topic, [{"id": "AwsSolutions-SNS2", "reason": "No sensitive data"}], True
        )
        self.aspects = Aspects.of(self)
        self.aspects.add(Guest360PathTagger())
        self.aspects.add(Guest360Termination())
        self.aspects.add(Guest360CWAlarms())

    def _subnet_selection(self, environment_config: dict) -> None:
        """Determine VPC and Subnet info for Codebuild within CodePipeline"""
        vpc_id = environment_config["networking"][self._stack.region]["vpc"]["id"]
        self._vpc = aws_ec2.Vpc.from_lookup(self, "pipeline_vpc", vpc_id=vpc_id)
        subnet_ids = [
            aws_ec2.Subnet.from_subnet_id(self, subnet["id"], subnet["id"])
            for subnet in environment_config["networking"][self._stack.region]["subnets"]["non-routable"]
        ]
        self._subnets = aws_ec2.SubnetSelection(subnets=subnet_ids)
