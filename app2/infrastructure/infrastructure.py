"""This file contains the Infrastructure Stack"""
import logging
from typing import Any, Dict

import yaml
from aws_cdk import CfnOutput, Duration, Stack, aws_config, aws_iam, aws_lambda
from cdk_nag import NagSuppressions
from constructs import Construct

from app.guest360_constructs.iam_role import Guest360IamRole, IAMProps
from app.guest360_constructs.infrastructure.dms_infra_roles import DMSRoles
from app.guest360_constructs.infrastructure.log_aggregator import LogAggregator
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.infrastructure.reliability.chatbot import ChatBot
from app.infrastructure.snowflake.snowflake_networking import Guest360SnowflakeNetworking
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.reliability.utils import LambdaFunctionName, StackName

logger = logging.getLogger(__name__)


class Infrastructure(WorkstreamStack):
    """Infrastructure Stack
    Contains resources pertaining to reliability
    """

    # pylint: disable-next=unused-argument
    def __init__(self, scope: Stack, id_: str, environment_config: dict, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)

        self._environment = self.deployment_environment
        self._stack = Stack.of(self)
        self._stack_path = self.project_dir
        termination_protection = self.node.try_get_context("termination_protection")

        self.detect_drift()
        self.chatbot()
        self.resource_deleter(kwargs)
        self.rollback_ranger(environment_config)
        self.snowflake_networking()
        self.developer_roles()

        # Begin - Untagged Bucket Finder
        short_env = environment_config["short_env"]
        short_region = environment_config["networking"][self._stack.region]["short_region"]
        sns_topic_arn = f"arn:aws:sns:{self._stack.region}:{self._stack.account}:{short_env}-{short_region}-guest360-cdk-pipeline-approval"
        sns_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW, actions=["sns:Publish"], resources=[sns_topic_arn]
        )
        s3_policy = aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess")
        untagged_bucket_lambda = Guest360LambdaFunction(
            self,
            LambdaFunctionName(prefix=self.prefix, base_name="untagged-bucket-finder").name(),
            LambdaFunctionProps(
                description="Untagged bucket finder",
                timeout=Duration.minutes(5),
                code=aws_lambda.Code.from_asset(
                    f"{self._stack_path}/bazel-bin/app/src/reliability/UntaggedBucketFinder/lambda_archive.zip"
                ),
                handler="lambda_function.lambda_handler",
                environment={
                    "SNS_TOPIC_ARN": sns_topic_arn,
                },
                allow_public_subnet=False,
                initial_policy=[sns_policy],
            ),
        ).function
        untagged_bucket_lambda.role.add_managed_policy(s3_policy)

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for BucketNotificationsHandler"},
            ],
        )

        # DMS account level roles
        if self.is_primary_region and self.is_static_env and self._environment in ["latest", "stage", "prod"]:
            dms_config_path = f"{self._stack_path}/app/infrastructure/dms_infra_roles/config/dms_roles.yaml"
            with open(dms_config_path, "r", encoding="UTF-8") as file:
                dms_roles_config = yaml.unsafe_load(file)
                dms_roles_props = dms_roles_config["resources"]

                DMSRoles(self, f"{self.prefix}-DMSRoles", dms_roles_props)

        # Splunk Integration Stack instantiation
        # if self.is_static_env:
        if False:  # pylint: disable=using-constant-test
            self.g360_infrastructure_stack = SplunkIntegration(
                self,
                "splunk_integration",
                stack_name=StackName(self.prefix, "SplunkIntegration").name(),
                tags=self._stack.tags.tag_values(),
                termination_protection=termination_protection,
            )

    def developer_roles(self) -> None:
        """Create common roles used across the platform, or by developer tools"""

        if self.is_static_env and self.is_primary_region:
            try:
                with open(
                    f"{self._stack_path}/app/infrastructure/reliability/configs/{self._environment}-{self._stack.region}-developer-workflow.yaml",
                    "r",
                    encoding="UTF-8",
                ) as file:
                    developer_config = yaml.unsafe_load(file)

                    for role in developer_config["stack_roles"]:
                        # Create app-level roles
                        iam_props = IAMProps(**developer_config["stack_roles"][role]["role"])
                        iam_props["role_name"] = role
                        guest360_iam_role = Guest360IamRole(self, f"{role}-role", iam_props).role
                        CfnOutput(self, f"{role}-output", value=guest360_iam_role.role_arn)

                        # Create initial policies
                        if "policies" in developer_config["stack_roles"][role].keys():
                            sid = 0
                            statements = []
                            for policy in developer_config["stack_roles"][role]["policies"]:
                                aws_iam_policy_statement = aws_iam.PolicyStatement(
                                    actions=policy["actions"],
                                    sid=str(sid),
                                    resources=policy["resources"],
                                )
                                statements.append(aws_iam_policy_statement)
                                sid += 1
                            github_actions_iam_policy = aws_iam.Policy(
                                self, f"{role}-policy-{sid}", statements=statements
                            )
                            guest360_iam_role.attach_inline_policy(github_actions_iam_policy)
                            NagSuppressions().add_resource_suppressions(
                                github_actions_iam_policy,
                                [{"id": "AwsSolutions-IAM5", "reason": "Required for Runner"}],
                            )

                        # Add additional assume role policies
                        if "assumed_by" in developer_config["stack_roles"][role].keys():
                            for assumed_by in developer_config["stack_roles"][role]["assumed_by"]:
                                guest360_iam_role.assume_role_policy.add_statements(
                                    aws_iam.PolicyStatement(principals=[assumed_by], actions=["sts:AssumeRole"])
                                )

            except FileNotFoundError:
                # These are only for developer workflows. Not all environments / regions apply.
                pass

    def detect_drift(self) -> None:
        # Once per AWS account, create a config rule to check for CloudFormation Drift.
        # By default, this runs once every 24 hours.
        if self._environment in ["latest", "stage", "prod"] and self.is_static_env:
            aws_config.CloudFormationStackDriftDetectionCheck(self, "DriftDetection", description="Detect CF Drift")

    def chatbot(self) -> None:
        if self.is_primary_region and self._environment != self.EnvNames.LOCAL and self.is_static_env:
            stack_name = StackName(self.prefix, "chatbot").name()
            ChatBot(
                self,
                "chatbot_stack",
                stack_name=stack_name,
                tags=self._stack.tags.tag_values(),
                termination_protection=self._environment == "prod",
            )

    def resource_deleter(self, kwargs) -> None:
        if self.is_primary_region and self._environment != self.EnvNames.LOCAL and self.is_static_env:
            resource_deleter = Guest360LambdaFunction(
                self,
                LambdaFunctionName(prefix=self.prefix, base_name="resource-deleter").name(),
                LambdaFunctionProps(
                    function_name=LambdaFunctionName(prefix=self.prefix, base_name="resource-deleter").name(),
                    description="Lambda Resource Deleter",
                    # arbitrary but 2 seems like enough time to delete a resource
                    timeout=Duration.minutes(2),
                    code=aws_lambda.Code.from_asset(
                        f"{self._stack_path}/bazel-bin/app/src/reliability/ResourceDeleter/lambda_archive.zip"
                    ),
                    handler="lambda_function.lambda_handler",
                    environment={},
                    allow_public_subnet=False,
                ),
            ).function

            cloud_control_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "cloudformation:ListResources",
                    "cloudformation:DeleteResource",
                    "cloudformation:GetResource",
                    "cloudformation:UpdateResource",
                    "cloudformation:GetResourceRequestStatus",
                    "cloudformation:ListResourceRequests",
                ],
                resources=[f"arn:aws:cloudformation:*:{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
            )
            tags: Dict[str, Any] = kwargs.get("tags", {})
            guest360_tagged_resource_policy_statement = aws_iam.PolicyStatement(
                actions=["*"],
                resources=[f"arn:aws:iam::{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
                conditions={
                    "StringEquals": {"aws:ResourceTag/bapp_id": tags.get("bapp_id")},
                    "ForAllValues:StringEquals": {
                        "aws:ResourceTag/environment": tags.get("environment"),
                        "aws:ResourceTag/bapp_id": tags.get("bapp_id"),
                    },
                },  # Hacky but ensures that if none are present it returns false
            )
            guest360_dynamodb_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "dynamodb:DeleteTable",
                    "dynamodb:DeleteItem",
                    "dynamodb:DeleteBackup",
                    "dynamodb:ListGlobalTables",
                    "dynamodb:ListBackups",
                    "dynamodb:ListTables",
                ],
                resources=[f"arn:aws:dynamodb:*:{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
            )
            guest360_dms_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "dms:DeleteEndpoint",
                    "dms:DeleteDataMigration",
                    "dms:DeleteReplicationInstance",
                    "dms:DeleteInstanceProfile",
                    "dms:DeleteReplicationTask",
                    "dms:DescribeReplicationInstances",
                    "dms:DescribeReplicationTasks",
                    "dms:DescribeEndpoints",
                ],
                resources=[f"arn:aws:dms:*:{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
            )
            guest360_appconfig_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "appconfig:DeleteApplication",
                    "appconfig:DeleteConfigurationProfile",
                    "appconfig:DeleteDeploymentStrategy",
                    "appconfig:DeleteExtension",
                    "appconfig:DeleteExtensionAssociation",
                    "appconfig:GetApplication",
                    "appconfig:GetConfiguration",
                    "appconfig:GetConfigurationProfile",
                    "appconfig:GetDeployment",
                    "appconfig:GetDeploymentStrategy",
                    "appconfig:GetExtension",
                ],
                resources=[f"arn:aws:appconfig:*:{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
            )
            guest360_keypair_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "ec2:DeleteKeyPair",
                    "ec2:DescribeKeyPairs",
                ],
                resources=[f"arn:aws:ec2:*:{self._stack.account}:*"],
                effect=aws_iam.Effect.ALLOW,
            )
            guest360_tagged_resource_policy = aws_iam.Policy(
                self,
                f"${self.prefix}-tagged-resource-policy",
                statements=[
                    guest360_tagged_resource_policy_statement,
                    guest360_appconfig_policy_statement,
                    guest360_dynamodb_policy_statement,
                    guest360_dms_policy_statement,
                    guest360_keypair_policy_statement,
                ],
            )
            cloud_control_policy = aws_iam.Policy(
                self, f"${self.prefix}-cloud-control-policy", statements=[cloud_control_policy_statement]
            )
            resource_deleter.role.attach_inline_policy(cloud_control_policy)
            resource_deleter.role.attach_inline_policy(guest360_tagged_resource_policy)
            resource_deleter.role.add_managed_policy(
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("ReadOnlyAccess")
            )
            NagSuppressions.add_resource_suppressions(
                resource_deleter.role,
                [
                    {
                        "id": "AwsSolutions-IAM4",
                        "reason": "Managed Policies are fine",
                    }
                ],
            )
            NagSuppressions().add_resource_suppressions(
                cloud_control_policy,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Cloud Control Requires Resource=[*], All delete policies require additional permissions",
                    }
                ],
            )
            NagSuppressions().add_resource_suppressions(
                guest360_tagged_resource_policy,
                [{"id": "AwsSolutions-IAM5", "reason": "Allowed all access only with tagged resouce with repo"}],
            )

    def rollback_ranger(self, environment_config) -> None:
        """calls rollback ranger lambda fxn in infra stack"""

        # Setup prefix for bucket name
        short_region = environment_config["networking"][self._stack.region]["short_region"]

        if short_region == "use1":
            # if in us-east-1 deploy rollback lambda
            short_env = environment_config["short_env"]
            bucket_prefix = f"{short_env}-{short_region}-guest360"

            rollback_ranger = Guest360LambdaFunction(
                self,
                LambdaFunctionName(prefix=self.prefix, base_name="rollback-ranger").name(),
                LambdaFunctionProps(
                    function_name=LambdaFunctionName(prefix="", base_name="rollback-ranger").name(),
                    description="Lambda to rollback to previously successful deployment",
                    # uncomment to enable versioning and add statement from aws_cdk import RemovalPolicy
                    # current_version_options=aws_lambda.VersionOptions(removal_policy=RemovalPolicy.RETAIN),
                    # Allow 10 minutes to overwrite app.zip with app_deployment.zip
                    timeout=Duration.minutes(10),
                    code=aws_lambda.Code.from_asset(
                        f"{self._stack_path}/bazel-bin/app/src/reliability/RollbackRanger/lambda_archive.zip"
                    ),
                    handler="lambda_function.lambda_handler",
                    environment={
                        "PREFIX": bucket_prefix,
                    },
                    allow_public_subnet=False,
                ),
            ).function
            guest360_s3_policy_statement = aws_iam.PolicyStatement(
                actions=[
                    "s3:DeleteObject",
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:GetObject",
                    "s3:GetBucket",
                    "s3:GetBucketLocation",
                    "s3:ListBucket",
                    "s3:ListObject",
                    "s3:ListObjects",
                ],
                # s3 cannot contain region or account name
                resources=[
                    f"arn:aws:s3:::{bucket_prefix}-build-pipeline-bucket/*",
                    f"arn:aws:s3:::{bucket_prefix}-build-pipeline-bucket",
                ],
                effect=aws_iam.Effect.ALLOW,
            )

            guest360_s3_policy = aws_iam.Policy(
                self, f"${self.prefix}-s3-policy", statements=[guest360_s3_policy_statement]
            )

            rollback_ranger.role.attach_inline_policy(guest360_s3_policy)

    def snowflake_networking(self) -> None:
        if self.is_primary_region and self._environment != self.EnvNames.LOCAL and self.is_static_env:
            stack_name = StackName(self.prefix, "snowflake_networking").name()
            Guest360SnowflakeNetworking(
                self,
                "snowflake_networking_stack",
                stack_name=stack_name,
                tags=self._stack.tags.tag_values(),
                termination_protection=self._environment == "prod",
            )


class SplunkIntegration(WorkstreamStack):
    """
    Constructs and resources for Splunk integration
    """

    def __init__(self, scope: Construct, id_: str, **kwargs) -> None:
        super().__init__(scope, id_, **kwargs)
        stack_path = self.node.try_get_context("stack_path")

        # DPEP Splunk
        LogAggregator(
            self,
            "dpep-app-logger",
            stack_path=stack_path,
            create_stream_name="dpep-app-logger",
            group_patterns=["*"],
            event_patterns=["ERROR", "WARN", "FATAL"],
        )

        # GIS Splunk
        LogAggregator(
            self,
            "gis-logger",
            stack_path=stack_path,
            create_stream_name="gis-logger",
            group_patterns=["*api*", "*auth*"],
            not_group_patterns=["/aws/api-gateway/Welcome*"],
        )
