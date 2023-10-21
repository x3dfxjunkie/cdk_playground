"""Docker building stack
"""
import os
import logging
from pathlib import Path
import sys
import yaml

import cdk_ecr_deployment
from aws_cdk import aws_ecr_assets, Aspects, Stack, Stage, aws_ecr, aws_iam

from app.infrastructure.workstream_stack import WorkstreamStack
from app.infrastructure.reliability.enable_stack import DeployFlag
from app.infrastructure.utils import cli_to_python_bool
from app.guest360_aspects.guest360_tagging import Guest360PathTagger
from app.guest360_aspects.guest360_termination import Guest360Termination
from app.guest360_constructs.ecr_repository import Guest360ECRRepository
from app.src.reliability.utils import StackName

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class Docker(Stack):
    """Guest360Docker

    This stack is meant to spawn other stacks for docker images; one stack per directory under "app/guest360_docker".
    """

    def __init__(
        self,
        scope: Stage,
        construct_id: str,
        environment_config: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        environment = self.node.try_get_context("environment").lower()
        stack = Stack.of(self)
        stack_name = self.node.try_get_context("stack_name").lower()
        self.aspects = Aspects.of(self)

        file_path = os.path.realpath(__file__)
        self.node.set_context("docker_basedir", str(Path(file_path).parents[2] / "guest360_docker"))
        self.node.set_context("termination_protection", environment == "prod")
        self.node.set_context(
            "prefix",
            "-".join(
                [
                    environment_config["short_env"],
                    environment_config["networking"][stack.region]["short_region"],
                    stack_name,
                ]
            ).lower(),
        )
        self.node.set_context(
            "prefix_global",
            "-".join([environment_config["short_env"], stack_name]).lower(),
        )

        docker_basedir = self.node.try_get_context("docker_basedir")
        prefix = self.node.try_get_context("prefix")
        termination_protection = self.node.try_get_context("termination_protection")

        # Loop through the directories found at docker_basedir
        special_replication_rules = []
        for docker_dir in os.listdir(docker_basedir):
            # Transform directory name to match ephemeral-stack-config and github labeler
            stack_pr_label = f"Docker/{docker_dir.title().replace('_', '')}"
            if os.path.isdir(f"{docker_basedir}/{docker_dir}") and DeployFlag.is_stack_enabled(self, stack_pr_label):
                # Create a stack for each workstreams directory of docker images
                workstream_docker_stack = Guest360DockerBuild(
                    self,
                    docker_dir,
                    stack_name=StackName(prefix, f"{docker_dir}-docker").name(),
                    termination_protection=termination_protection,
                )
                special_replication_rules += workstream_docker_stack.special_replication_rules

        # ECR Private Registry Stack
        if self.node.get_context("is_static_env"):
            ECRPrivateRegistry(
                self,
                "ecr_private_registry",
                special_replication_rules=special_replication_rules,
                stack_name=StackName(prefix, "ECRPrivateRegistry").name(),
                tags=self.tags.tag_values(),
                termination_protection=termination_protection,
            )

        self.aspects.add(Guest360PathTagger())
        self.aspects.add(Guest360Termination())


class Guest360DockerBuild(WorkstreamStack):
    """Maintain workstream images"""

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        docker_basedir = self.node.try_get_context("docker_basedir")
        stack_name = self.node.try_get_context("stack_name")
        is_ephemeral_env = not self.is_static_env

        docker_name = construct_id

        # Open the config file for each workstream
        with open(f"{docker_basedir}/{docker_name}/images_config.yaml", "r", encoding="utf-8") as file:
            repository_and_image_config = yaml.safe_load(file)

        # Loop over each top-level key in images_config.yaml.
        # Per iteration, define 1 target repo, 1 image, and 1 "copy deployment" from default repo to target repo.
        self.special_replication_rules = []
        for image_name, image_settings in repository_and_image_config.items():
            # Handle build & deployment feature flags
            build_disabled_totally = not image_settings["enabled"]
            ephemeral_build_disabled = not image_settings["ephemeral_enabled"]
            if build_disabled_totally:
                # Do not build and deploy image at all (repo will still be built)
                continue
            elif is_ephemeral_env and ephemeral_build_disabled:
                # Do not build and deploy image in ephemeral environments
                continue

            # Define the repo
            ecr_repo_props = {}
            if image_settings.get("special_replication"):
                ecr_repo_props["repository_name"] = f"spec/{stack_name}/{docker_name}/{image_name}".lower()
                ecr_repo_props["image_replication_props"] = image_settings["special_replication_props"]
            else:
                ecr_repo_props["repository_name"] = f"{stack_name}/{docker_name}/{image_name}".lower()
            repo = Guest360ECRRepository(
                self,
                f"{image_name}-repo",
                props=ecr_repo_props,
            )
            self.special_replication_rules += repo.replication_rules

            # Define the image
            self.build_args = {
                "REPO_NAME": image_settings["base_repo"],
                "IMAGE_TAG": image_settings["base_tag"],
            }
            self.build_ecr_link(image_name)
            ecr_image = aws_ecr_assets.DockerImageAsset(
                self,
                f"{image_name}-image",
                directory=f"{docker_basedir}/{docker_name}/{image_settings['directory']}/",
                file=image_settings["file"],
                build_args=self.build_args,
                # Turn str Platform into proper ENUM
                platform=eval(image_settings["platform"]),
            )

            # Define Copier Construct, to copy images from CDK Default Repo to Target Repo
            image_copier_role = aws_iam.Role(
                self,
                f"CustomECRDeploymentRole-{ecr_repo_props['repository_name']}",
                assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            )
            repo.grant_pull_push(image_copier_role)
            repo.grant(image_copier_role, "ecr:DescribeRepositories")

            # Target image tags
            target_version = image_settings["target_version"]
            v_major, minor, patch = target_version.split(".")
            build_hash = ecr_image.asset_hash[:4]
            target_tags = [
                "latest",
                f"{v_major}.x",  # e.g. v1.x
                f"{v_major}.{minor}.x",  # e.g. v1.0.x
                f"{v_major}.{minor}.{patch}-{build_hash}",  # e.g. v1.0.0-abcd
            ]
            for tag in target_tags:
                image_copier = cdk_ecr_deployment.ECRDeployment(
                    self,
                    f"copy-to-ecr-{ecr_repo_props['repository_name']}-{tag}",
                    dest=cdk_ecr_deployment.DockerImageName(repo.repository_uri_for_tag(tag)),
                    src=cdk_ecr_deployment.DockerImageName(ecr_image.image_uri),
                    role=image_copier_role,
                )
                # Define dependencies - image copies depends on repo and image existence
                image_copier.node.add_dependency(repo)
                image_copier.node.add_dependency(ecr_image)

    def build_ecr_link(self, image_name: str) -> None:
        if self.build_args["REPO_NAME"].startswith("guest360"):
            self.build_args[
                "REPO_NAME"
            ] = f"{self.account}.dkr.ecr.{self.region}.amazonaws.com/{self.build_args['REPO_NAME']}"
        else:
            pass


class ECRPrivateRegistry(WorkstreamStack):
    """
    Constructs and resources for ECR Private Registry. Controls replication rules.
    """

    def __init__(
        self,
        scope,
        id_,
        special_replication_rules: list[aws_ecr.CfnReplicationConfiguration.ReplicationRuleProperty],
        **kwargs,
    ) -> None:
        super().__init__(scope, id_, **kwargs)

        # Latest and Stage Replication Rules
        if self.deployment_environment in [self.EnvNames.LATEST, self.EnvNames.STAGE] and self.is_primary_region:
            # Default Latest and Stage replication destinations (targets)
            default_replication_destinations = [
                aws_ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                    **destination,
                )
                for destination in self.app_constants["ecr"]["standard_replications"][self.deployment_environment]
            ]
            default_replication_rule = aws_ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                destinations=default_replication_destinations,
                repository_filters=[
                    aws_ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                        filter="guest360/", filter_type="PREFIX_MATCH"
                    ),
                ],
            )
            combined_replication_rules = [default_replication_rule] + special_replication_rules
            aws_ecr.CfnReplicationConfiguration(
                self,
                "ReplicationConfiguration",
                replication_configuration=aws_ecr.CfnReplicationConfiguration.ReplicationConfigurationProperty(
                    rules=combined_replication_rules,
                ),
            )
        elif self.deployment_environment == self.EnvNames.PROD:
            # Prod is not a replication source, only a destination (from source test account)
            replication_permissions = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "ReplicationFromTestAccount",
                        "Effect": "Allow",
                        "Principal": {"AWS": f"arn:aws:iam::{self.Accounts.test.id}:root"},
                        "Action": ["ecr:CreateRepository", "ecr:ReplicateImage"],
                        "Resource": [
                            f"arn:aws:ecr:*:{self.Accounts.prod.id}:repository/guest360/*",
                        ],
                    }
                ],
            }
            aws_ecr.CfnRegistryPolicy(self, "RegistryPolicy", policy_text=replication_permissions)
