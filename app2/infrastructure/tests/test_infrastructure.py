"""Unit tests for app/infrastructure/infrastructure.py
This will not work in Bazel until it can support at least aws-cdk-lib>=2.70.0
"""
import logging
import os
import sys
from pathlib import Path
import yaml
from unittest.mock import patch
from itertools import product

import aws_cdk
from aws_cdk import aws_lambda
from constructs import Construct
import pytest
from aws_cdk.assertions import Template

from app.infrastructure.infrastructure import Infrastructure
from app.guest360_constructs.tests.utils import print_template_on_debug
from app.infrastructure.workstream_stack import WorkstreamStack


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class MockLambdaAssetCode(aws_lambda.Code):
    # TODO: Investigate.Should be an extension of aws_lambda.AssetCode, but aws_lambda.Code seems to work easier
    def bind(self, scope: Construct) -> aws_lambda.CodeConfig:
        return aws_lambda.CodeConfig(s3_location={"bucket_name": "dummy_bucket", "object_key": "dummy_key"})


@pytest.fixture(autouse=True)
def mock_code_from_asset():
    with patch("aws_cdk.aws_lambda.Code.from_asset", return_value=MockLambdaAssetCode()):
        yield


static_environments = ["latest", "stage", "load", "prod"]
ephemeral_environments = ["latest"]
static_prefixes = ["guest360"]
ephemeral_prefixes = ["pr-1234"]
regions = ["us-east-1", "us-west-2"]
static_parameters = product(static_environments, static_prefixes, regions)
ephemeral_parameters = product(ephemeral_environments, ephemeral_prefixes, regions)


@pytest.mark.parametrize("environment,prefix,region", static_parameters)
def test_static_infrastructure_stacks(environment: str, prefix: str, region: str, constants: dict):
    project_dir = WorkstreamStack.project_dir
    test_context = {
        "environment": environment,
        "prefix_global": prefix,
        "prefix": prefix,
        "stack_path": project_dir,
    }

    with open(f"{project_dir}/app/configs/{environment}-environment.yaml", "r", encoding="utf-8") as file:
        environment_config = yaml.safe_load(file)

    app = aws_cdk.App(context=test_context)
    stack_env = aws_cdk.Environment(account="123456789", region=region)
    guest360_stack = aws_cdk.Stack(
        app,
        "TestStack",
        env=stack_env,
    )

    infrastructure_stack = Infrastructure(
        guest360_stack,
        "infrastructure",
        stack_name="infrastructure",
        env=stack_env,
        environment_config=environment_config,
    )

    template = Template.from_stack(infrastructure_stack)
    app_synth = app.synth()
    synthesized_infrastructure_template = app_synth.get_stack_by_name("infrastructure").template
    print_template_on_debug(template, logger, include_resource_types=[constants["AWSIAMROLE"]], print_type="yaml")

    # Chatbot Stack
    if region == infrastructure_stack.primary_region:
        # Chatbot stack should exist us-east-1 environments (static)
        chatbot_stack = app_synth.get_stack_by_name("guest360-chatbot").template
    else:
        # Chatbot should not exist in us-west-2
        with pytest.raises(RuntimeError):
            app_synth.get_stack_by_name("guest360-chatbot")

    # Drift detection and IAM Roles #TODO: refactor into own resource sections or by component
    match prefix:
        case "guest360" if environment in ["latest", "stage", "prod"]:
            template.has_resource_properties(
                "AWS::Config::ConfigRule",
                {
                    "Description": "Detect CF Drift",
                    "Scope": {"ComplianceResourceTypes": ["AWS::CloudFormation::Stack"]},
                    "Source": {"Owner": "AWS", "SourceIdentifier": "CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK"},
                },
            )

            # Drift detection role
            assert "DriftDetectionRole9E6D18B2" in synthesized_infrastructure_template["Resources"]

            # Lambda basic execution role - with policy/AmazonS3ReadOnlyAccess
            assert "Guest360LambdaFunctionab2afServiceRoleD1ABB16D" in synthesized_infrastructure_template["Resources"]

            # us-east-1
            if region == infrastructure_stack.primary_region:
                # Lambda basic execution role - with policy/ReadOnlyAccess
                assert (
                    "Guest360LambdaFunction6889cServiceRole1738AC33" in synthesized_infrastructure_template["Resources"]
                )

                # DMS CloudWatch Logs role
                template.has_resource_properties(
                    constants["AWSIAMROLE"],
                    {"RoleName": "dms-cloudwatch-logs-role"},
                )

                # DMS VPC role
                template.has_resource_properties(
                    constants["AWSIAMROLE"],
                    {"RoleName": "dms-vpc-role"},
                )

                # 6. In latest only - GitHub Action IAM role
                if environment == "latest":
                    template.has_resource_properties(
                        constants["AWSIAMROLE"],
                        {"RoleName": "guest360-github_action_iam_role"},
                    )
                    template.resource_count_is(constants["AWSIAMROLE"], 7)
                else:
                    template.resource_count_is(constants["AWSIAMROLE"], 6)

            # us-west-2
            else:
                template.resource_count_is(constants["AWSIAMROLE"], 2)
        case _:
            template.resource_count_is("AWS::Config::ConfigRule", 0)
