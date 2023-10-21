"""Base class for workstreams"""
from typing import List, Any
from pathlib import Path
import os
import yaml
from dataclasses import dataclass
from enum import Enum

from aws_cdk import Stack, App, Tags, aws_ssm
from cdk_nag import NagSuppressions

from app.infrastructure.utils import cli_to_python_bool

app_dir = Path(os.path.realpath(__file__)).parents[1]
with open(f"{app_dir}/configs/constants.yaml", "r", encoding="utf-8") as file:
    CONSTANTS = yaml.safe_load(file)


class EnvNames(str, Enum):
    LOCAL: str = "local"
    LATEST: str = "latest"
    TEST: str = "test"
    STAGE: str = "stage"
    LOAD: str = "load"
    PROD: str = "prod"

    def __repr__(self):
        return self.value


@dataclass
class Account:
    id: str
    name: str


@dataclass
class Accounts:
    local = Account(id=CONSTANTS["account_ids"][EnvNames.LOCAL], name=EnvNames.LOCAL)
    latest = Account(id=CONSTANTS["account_ids"][EnvNames.LATEST], name=EnvNames.LATEST)
    test = Account(id=CONSTANTS["account_ids"][EnvNames.TEST], name=EnvNames.TEST)
    stage = Account(id=CONSTANTS["account_ids"][EnvNames.STAGE], name=EnvNames.STAGE)
    load = Account(id=CONSTANTS["account_ids"][EnvNames.LOAD], name=EnvNames.LOAD)
    prod = Account(id=CONSTANTS["account_ids"][EnvNames.PROD], name=EnvNames.PROD)


class WorkstreamStack(Stack):
    """
    Base class for workstreams
    """

    EnvNames = EnvNames
    UpperEnvNames = [EnvNames.STAGE, EnvNames.LOAD, EnvNames.PROD]
    DockerEnvNames = [EnvNames.LATEST, EnvNames.STAGE]
    Accounts = Accounts
    this_file_path = Path(__file__)
    app_dir = str(this_file_path.parents[1])
    project_dir = str(this_file_path.parents[2])

    def __init__(self, scope: Stack | App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # This block can be used for ci testing and troubleshooting stack instantiation.
        stub_for_test = cli_to_python_bool(self.node.try_get_context("stub_workstream_stacks"))
        if stub_for_test:
            return

        environment = self.node.try_get_context("environment")
        stack = Stack.of(self)
        prefix = self.node.try_get_context("prefix")
        is_static_env = self.node.try_get_context("is_static_env")
        if not is_static_env and prefix is not None:
            self.node.set_context("is_static_env", "guest360" in prefix)
            is_static_env = self.node.try_get_context("is_static_env")

        # Tags
        Tags.of(stack).add("environment", environment)
        if is_static_env:
            Tags.of(stack).add("environment_type", "static")
        else:
            Tags.of(stack).add("environment_type", "ephemeral")

        if prefix is not None:
            self.export_commit_id(_prefix=prefix, _stack=stack)

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                },
                {
                    "id": "AwsSolutions-L1",
                    "reason": "CDK makes a bunch of latest runtime version.",
                },
            ],
        )

    def export_commit_id(self, _prefix: str, _stack: Stack) -> None:
        """Export the commit ID to SSM parameter, if one is defined"""

        short_name = _stack.stack_name.replace(f"{_prefix}-", "")

        # Default priorities: - per CDK docs 50 for tags added directly to CloudFormation resources.  https://docs.aws.amazon.com/cdk/v2/guide/tagging.html#w53aac21c26c25
        default_cloudformation_resource_tag = 50
        commit_id = _stack.tags.tag_values().get("commit_id", None)
        if commit_id is not None:
            aws_ssm.StringParameter(
                self, "commit_id", parameter_name=f"/stacks/{_prefix}/{short_name}/commit_id", string_value=commit_id
            )
            _stack.tags.remove_tag("commit_id", priority=default_cloudformation_resource_tag)

    def ssm_export(
        self, resource_name: str, resource: str, construct_name: str | None = None
    ) -> aws_ssm.IStringParameter:
        """Export AWS SSM Properties"""
        prefix = self.node.try_get_context("prefix")
        stack_name = Stack.of(self).stack_name

        parameter_name = (
            f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"
            if construct_name is not None
            else f"/{prefix}/{stack_name}/{resource_name}"
        )

        return aws_ssm.StringParameter(self, resource_name, parameter_name=parameter_name, string_value=resource)

    def ssm_list_export(self, resource_name: str, construct_name: str, values: List[str]):
        prefix = self.node.try_get_context("prefix")
        stack_name = Stack.of(self).stack_name

        parameter_name = (
            f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"
            if construct_name is not None
            else f"/{prefix}/{stack_name}/{resource_name}"
        )
        return aws_ssm.StringListParameter(self, resource_name, parameter_name=parameter_name, string_list_value=values)

    def ssm_import(self, resource_name: str, stack_name: str, construct_name: str | None = None) -> str:
        """Import an ARN from an AWS SSM Property"""
        prefix = self.node.try_get_context("prefix")
        parameter_name = (
            f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"
            if construct_name is not None
            else f"/{prefix}/{stack_name}/{resource_name}"
        )

        return aws_ssm.StringParameter.value_for_string_parameter(self, parameter_name)

    def ssm_list_import(self, resource_name: str, stack_name: str, construct_name: str | None = None) -> List[str]:
        prefix = self.node.try_get_context("prefix")
        parameter_name = (
            f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"
            if construct_name is not None
            else f"/{prefix}/{stack_name}/{resource_name}"
        )
        return aws_ssm.StringListParameter.value_for_typed_list_parameter(self, parameter_name)

    @property
    def app_constants(self) -> dict[str, Any]:
        return CONSTANTS

    @property
    def primary_region(self) -> str:
        return self.app_constants["regions"]["primary"]

    @property
    def is_primary_region(self) -> bool:
        return self.region == self.primary_region

    @property
    def global_region(self) -> str:
        return self.app_constants["regions"]["global"]

    @property
    def is_global_region(self) -> bool:
        return self.region == self.global_region

    @property
    def deployment_environment(self) -> str:
        return self.node.try_get_context("environment")

    @property
    def is_static_env(self) -> bool:
        return self.node.try_get_context("is_static_env")

    @property
    def prefix(self) -> str:
        return self.node.try_get_context("prefix")
