"""Unit tests for app/infrastructure/load_testing/static/load_testing_static.py
This will not work in Bazel until it can support at least aws-cdk-lib>=2.70.0
"""
import logging
import os
import sys
import json
from pathlib import Path
import yaml
from unittest.mock import patch
from itertools import product

import aws_cdk
from aws_cdk import aws_lambda
from constructs import Construct
import pytest
from aws_cdk.assertions import Template

from app.infrastructure.load_testing.static.load_testing_static import LoadTestingStaticStack
from app.guest360_constructs.tests.utils import print_template_on_debug
from app.infrastructure.workstream_stack import WorkstreamStack


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

static_environments = ["latest"]
ephemeral_environments = ["latest"]
static_prefixes = ["guest360"]
ephemeral_prefixes = ["pr-1234"]
regions = ["us-east-1"]
static_parameters = product(static_environments, static_prefixes, regions)
ephemeral_parameters = product(ephemeral_environments, ephemeral_prefixes, regions)


class MockLambdaAssetCode(aws_lambda.Code):
    def bind(self, scope: Construct) -> aws_lambda.CodeConfig:
        return aws_lambda.CodeConfig(s3_location={"bucket_name": "dummy_bucket", "object_key": "dummy_key"})


@pytest.fixture(autouse=True)
def mock_code_from_asset():
    with patch("aws_cdk.aws_lambda.Code.from_asset", return_value=MockLambdaAssetCode()):
        yield


@pytest.mark.parametrize("environment,prefix,region", static_parameters)
def test_static_infrastructure_stacks(environment: str, prefix: str, region: str, constants: dict):
    project_dir = WorkstreamStack.project_dir
    test_context = {
        "environment": environment,
        "prefix_global": prefix,
        "prefix": prefix,
        "stack_path": project_dir,
        "github_pr_labels": json.dumps(["LoadTesting/KinesisIngest"]),
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
    dms_stack_extension = ["cme-dlr"]

    load_testing_static_stack = LoadTestingStaticStack(
        guest360_stack,
        "LoadTestingStatic",
        stack_name="loadtestingstatic",
        env=stack_env,
        environment_config=environment_config,
        dms_stack_extension=dms_stack_extension,
    )

    template = Template.from_stack(load_testing_static_stack)

    print_template_on_debug(template, logger, include_resource_types=[constants["AWSIAMROLE"]], print_type="yaml")
    template.resource_count_is("AWS::Lambda::Function", 9)
    template.resource_count_is("AWS::IAM::Role", 7)
    template.resource_count_is("AWS::DynamoDB::Table", 2)
    template.resource_count_is("AWS::KMS::Key", 3)
