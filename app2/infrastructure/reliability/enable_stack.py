"""
This file contains the stack force_enable flag and audit enabled flag determined by the ephemeral-stack-config.yaml.
"""
import os
from typing import Any, Dict
import yaml
import json
from functools import cache

from app.infrastructure.utils import cli_to_python_bool

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/../../ephemeral-stack-config.yaml", "r", encoding="utf-8"
) as file:
    stack_config_yml = yaml.safe_load(file)


class DeployFlag:
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    @cache
    def is_stack_enabled(cls, scope, stack_name: str, stack_config: str = "") -> bool:
        """Function checks ephemeral-stack-config.yaml file in the app/
            directory to see if a stack is configured to be enabled
        Args:
            scope: Parent scope: Stage, Stack, Construct, etc.
            stack_name (_type_): the stack name
            stack_config (str): the ephemeral-stack-config, passed as string object for caching
        Returns:
            bool: Can the stack be enabled
        """
        if not stack_config:
            stack_config = stack_config_yml
        else:
            stack_config = json.loads(stack_config)

        stack_settings = stack_config["stacks"].get(stack_name, {})  # Get empty dict if not in main stack config

        # 1. Static Environment Activation
        is_static_env = scope.node.try_get_context("is_static_env")

        # 2. Release Check Activation. All stacks are considered enabled, e.g., merge of develop into main
        is_release_check = cli_to_python_bool(scope.node.try_get_context("release_check"))

        # 3. Manual Activation. Based on app/ephemeral-stack-config.yaml
        has_stack_config_flag = stack_settings.get("force_enable", False)

        # 4. Dynamic Stack Activation. Based on GitHub PR labels. E.g., file changes registered by Auto Labeling
        has_github_pr_label = stack_name in json.loads(scope.node.try_get_context("github_pr_labels"))

        # Summation of above conditions
        direct_activation = is_static_env or is_release_check or has_stack_config_flag or has_github_pr_label

        # 5. Dependency Activation. Determined by app/ephemeral-stack-config.yaml children and required_by fields
        any_dependent_stacks_enabled = False
        if not direct_activation:
            children_and_dependents = stack_settings.get("children", []) + stack_settings.get("required_by", [])
            if children_and_dependents:
                json_stack_config = json.dumps(stack_config)
                any_dependent_stacks_enabled = any(
                    cls.is_stack_enabled(scope, stack_name, stack_config=json_stack_config)
                    for stack_name in children_and_dependents
                )

        # Any of the following conditions will activate the input stack for deployment
        is_stack_activated = direct_activation or any_dependent_stacks_enabled

        return is_stack_activated

    @staticmethod
    def is_auditing_enabled(scope, stack_config: Dict[str, Any] = stack_config_yml) -> bool:
        """Function checks if cdk_nag is enabled.

            While deploying to localstack, it is sometime necessary to disable auditing.
            Changing the value of "auditing" from true to false in stack_config.yml will
            change this behavior.
        Args:
            scope: Parent scope: Stage, Stack, Construct, etc.
            stack_config (dict, optional): _description_. Defaults to stack_config_yml.
        Returns:
            bool: Is auditing enabled
        """
        is_static_env = scope.node.try_get_context("is_static_env")

        if is_static_env:
            return True

        is_enabled: bool = stack_config.get("auditing", None)

        match is_enabled:
            case False:
                return False
            case _:
                return True

        return True
