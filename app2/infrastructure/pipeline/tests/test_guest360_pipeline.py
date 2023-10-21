"""
Tests for Guest360PipelineStack — Static Codepipeline
"""
import logging
import yaml
import json
from pathlib import Path
from unittest.mock import patch
import pytest
from enum import Enum

import aws_cdk
from aws_cdk import assertions, aws_lambda, Stack
from constructs import Construct

from app.infrastructure.workstream_stack import WorkstreamStack
from app.guest360_constructs.tests.utils import print_template_on_debug

logger = logging.getLogger(__name__)

APP_FOLDER = Path(__file__).parents[3]
CDK_JSON = APP_FOLDER / "cdk.json"
DEFAULT_CONTEXT = json.load(CDK_JSON.open())["context"]
TEST_STACK_ID = "TestPipelineStack"
CDK_ENV = aws_cdk.Environment(account="123456789", region="us-east-1")
REGION = "us-east-1"
ENV_NAMES = WorkstreamStack.EnvNames
DOCKER_ENV_NAMES = WorkstreamStack.DockerEnvNames


class CFType(str, Enum):
    LAMBDA_FUNCTION: str = "AWS::Lambda::Function"
    SNS_TOPIC: str = "AWS::SNS::Topic"
    CODEPIPELINE_PIPELINE: str = "AWS::CodePipeline::Pipeline"
    CODESTAR_NOTIFICATIONS_NOTIFICATION_RULE: str = "AWS::CodeStarNotifications::NotificationRule"

    def __repr__(self):
        return self.value


# Mock — skeleton stack structure for our application
# Note that infrastructure and docker stacks are not directly mocked, to provide more realism
class MockWorkstreamStack(Stack):
    streams = []  # This is needed because ingestion stack as a stream attribute for dashboards in guest360_stack.py
    stack_extension_dms = (
        []
    )  # This is needed because ingestion stack as a dms_stack_extension attribute for loadtest in guest360_stack.py
    construct_id = "dummy_id"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args)


@pytest.fixture(autouse=True)
def mock_data_service_stack():
    with patch("app.infrastructure.data_service.data_service.DataService", new=MockWorkstreamStack):
        yield


@pytest.fixture(autouse=True)
def mock_identity_stack():
    with patch("app.infrastructure.identity.identity.Identity", new=MockWorkstreamStack):
        yield


@pytest.fixture(autouse=True)
def mock_ingestion_stack():
    with patch("app.infrastructure.ingestion.ingestion.Ingestion", new=MockWorkstreamStack):
        yield


@pytest.fixture(autouse=True)
def mock_load_testing_static_stack():
    with patch(
        "app.infrastructure.load_testing.static.load_testing_static.LoadTestingStaticStack", new=MockWorkstreamStack
    ):
        yield


@pytest.fixture(autouse=True)
def mock_processing_stack():
    with patch("app.infrastructure.processing.processing.Processing", new=MockWorkstreamStack):
        yield


class MockLambdaAssetCode(aws_lambda.Code):
    # TODO: Investigate.Should be an extension of aws_lambda.AssetCode, but aws_lambda.Code seems to work easier
    def bind(self, scope: Construct) -> aws_lambda.CodeConfig:
        return aws_lambda.CodeConfig(s3_location={"bucket_name": "dummy_bucket", "object_key": "dummy_key"})


@pytest.fixture(autouse=True)
def mock_code_from_asset():
    with patch("aws_cdk.aws_lambda.Code.from_asset", return_value=MockLambdaAssetCode()):
        yield


@pytest.mark.parametrize("environment", ["latest", "stage", "load", "prod"])
def test_pipeline(environment):
    # Mocked classes within scope of test must be imported withing scope of mock
    from app.infrastructure.pipeline.guest360_pipeline import Guest360PipelineStack

    test_context = {
        **DEFAULT_CONTEXT,
        "environment": environment,
        "region": REGION,
    }
    environment_config_dir = APP_FOLDER / "configs"
    with (environment_config_dir / f"{environment}-environment.yaml").open() as file:
        environment_config = yaml.safe_load(file)
    test_app = aws_cdk.App(context=test_context)
    pipeline_stack = Guest360PipelineStack(
        test_app,
        f"{TEST_STACK_ID}",
        environment_config=environment_config,
        env=CDK_ENV,
        stack_name=f"guest360-{environment}",
    )
    template = assertions.Template.from_stack(pipeline_stack)
    print_template_on_debug(
        template,
        logger=logger,
        print_type="both",
        exclude_resource_types=[
            # This list is nice because you can toggle on/off resources you're working with
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::CodeBuild::Project",
            "AWS::EC2::SecurityGroup",
            CFType.CODEPIPELINE_PIPELINE,
            CFType.SNS_TOPIC,
            "AWS::SNS::TopicPolicy",
            "AWS::CloudWatch::Alarm",
            "AWS::S3::BucketPolicy",
            "AWS::S3::Bucket",
            "AWS::KMS::Key",
            # CFType.LAMBDA_FUNCTION,
            CFType.CODESTAR_NOTIFICATIONS_NOTIFICATION_RULE,
            "Custom::S3AutoDeleteObjects",
            "Custom::S3BucketNotifications",
        ],
    )
    pipeline_resource = template.find_resources(CFType.CODEPIPELINE_PIPELINE)
    stages = pipeline_resource["guest360staticpipelinePipeline56B760B5"]["Properties"]["Stages"]
    stage_order = [stage["Name"] for stage in stages]
    print(json.dumps(stage_order, indent=4))
    expected_first_four_stages = [
        "Source",
        "Build",
        "UpdatePipeline",
        "Assets",
    ]

    # Confirmations that general stage order is preserved
    assert stage_order[:4] == expected_first_four_stages
    if environment in DOCKER_ENV_NAMES:
        assert f"{environment}-guest360-docker-us-east-1" == stage_order[4]
    assert f"{environment}-guest360-pipeline-us-east-1" == stage_order[-2]
    assert f"{environment}-guest360-pipeline-us-west-2" == stage_order[-1]

    # Confirm CodePipeline
    template.resource_count_is(CFType.CODEPIPELINE_PIPELINE, 1)
    template.has_resource_properties(
        CFType.CODEPIPELINE_PIPELINE,
        {
            "RestartExecutionOnUpdate": True,
        },
    )

    # Confirm Lambda Infra
    # Note that one lambda is a managed bucket notification lambda and in the other is an auto-delete lambda
    if environment == ENV_NAMES.LATEST:
        template.resource_count_is(CFType.LAMBDA_FUNCTION, 2)
    else:
        template.resource_count_is(CFType.LAMBDA_FUNCTION, 1)

    # Confirm SNS + Codestar
    if environment == ENV_NAMES.LATEST:
        template.resource_count_is(CFType.SNS_TOPIC, 1)
        template.resource_count_is(CFType.CODESTAR_NOTIFICATIONS_NOTIFICATION_RULE, 1)
    else:
        template.resource_count_is(CFType.SNS_TOPIC, 2)
        template.resource_count_is(CFType.CODESTAR_NOTIFICATIONS_NOTIFICATION_RULE, 2)
        template.has_resource_properties(
            CFType.SNS_TOPIC,
            {
                "TopicName": f"{pipeline_stack.prefix}-cdk-pipeline-change-requests",
            },
        )

    template.has_resource_properties(
        CFType.SNS_TOPIC,
        {
            "TopicName": f"{pipeline_stack.prefix}-cdk-pipeline-approval",
        },
    )
