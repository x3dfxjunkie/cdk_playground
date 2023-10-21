"""
unit tests for lambda_function
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
import boto3
import json
import logging
import os
import sys

import pytest
import strongtyping
from moto import mock_lambda
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from aws_cdk import App, RemovalPolicy, Stack, Aspects, aws_lambda
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

# set log levels for nozy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix_global": "lst-teststack", "prefix": "lst-teststack-use1", "environment": "local"}
TEST_CONSTRUCT_ID = "lambda_function_id"
TEST_LAMBDA_NAME = "lambda_function_name"
CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


@pytest.fixture
def app_stack():
    app = App(context=TEST_CONTEXT)
    aspects = Aspects.of(app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack = Stack(app)
    yield stack


def test_lambda_function_obj(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "runtime": aws_lambda.Runtime.PYTHON_3_10,
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    assert isinstance(mylambda, Guest360LambdaFunction)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert mylambda.function_name is None

    template = Template.from_stack(app_stack)
    logger.debug("app_stack=%s", json.dumps(template.to_json(), indent=2))

    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 4)
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 3,
            "DatapointsToAlarm": 2,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Errors",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 5,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "DeadLetterErrors",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 2,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Throttles",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 5,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 3,
            "DatapointsToAlarm": 3,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Duration",
            "Namespace": "AWS/Lambda",
            "Period": 300,
            "ExtendedStatistic": "p99",
            "Threshold": 10,
            "Unit": "Count",
        },
    )
    # validate that template does not contain any nag rules
    annotations = Annotations.from_stack(app_stack)
    errors = annotations.find_error(
        "*",
        Match.string_like_regexp(r"AwsSolutions-.*"),
    )
    assert len(errors) == 0


def test_lambda_function_obj_with_adot(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "runtime": aws_lambda.Runtime.PYTHON_3_10,
        "enable_otel_tracing": True,
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    assert isinstance(mylambda, Guest360LambdaFunction)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert mylambda.function_name is None

    template = Template.from_stack(app_stack)
    logger.debug("app_stack=%s", json.dumps(template.to_json(), indent=2))

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Environment": {
                "Variables": {
                    "AWS_LAMBDA_EXEC_WRAPPER": "/opt/otel-instrument",
                    "OPENTELEMETRY_COLLECTOR_CONFIG_FILE": "/var/task/otel-config.yaml",
                    "OTEL_INSTRUMENTATION_AWS_LAMBDA_FLUSH_TIMEOUT": "900",
                    "OTEL_PROPAGATORS": "xray",
                    "OTEL_PYTHON_ID_GENERATOR": "xray",
                }
            },
        },
    )
    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 4)
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 3,
            "DatapointsToAlarm": 2,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Errors",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 5,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "DeadLetterErrors",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 2,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Throttles",
            "Namespace": "AWS/Lambda",
            "Period": 60,
            "Statistic": "Sum",
            "Threshold": 5,
            "Unit": "Count",
        },
    )
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 3,
            "DatapointsToAlarm": 3,
            "Dimensions": [{"Name": "FunctionName", "Value": {"Ref": Match.any_value()}}],
            "MetricName": "Duration",
            "Namespace": "AWS/Lambda",
            "Period": 300,
            "ExtendedStatistic": "p99",
            "Threshold": 10,
            "Unit": "Count",
        },
    )
    # validate that template does not contain any nag rules
    annotations = Annotations.from_stack(app_stack)
    errors = annotations.find_error(
        "*",
        Match.string_like_regexp(r"AwsSolutions-.*"),
    )
    assert len(errors) == 0


def test_lambda_docker_function_obj(app_stack):
    props = {
        "code": aws_lambda.DockerImageCode.from_image_asset(
            directory=f"{os.path.realpath(__file__).replace('.py', '')}"
        ),
        "description": "my test lambda",
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    assert isinstance(mylambda, Guest360LambdaFunction)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert mylambda.function_name is None

    template = Template.from_stack(app_stack)
    logger.debug(json.dumps(template.to_json(), indent=2))
    # validate that template does not contain any nag rules
    annotations = Annotations.from_stack(app_stack)
    errors = annotations.find_error(
        "*",
        Match.string_like_regexp(r"AwsSolutions-.*"),
    )
    assert len(errors) == 0


def test_lambda_function_wrong_typedict(app_stack):
    props = {
        "code": "blah",
        "description": [],
    }
    with pytest.raises(strongtyping.strong_typing_utils.TypeMisMatch):
        Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)


def test_lambda_function_alias(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "runtime": aws_lambda.Runtime.PYTHON_3_10,
        "description": "my test lambda",
        "function_name": TEST_LAMBDA_NAME,
        "current_version_options": aws_lambda.VersionOptions(removal_policy=RemovalPolicy.RETAIN),
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    template = Template.from_stack(app_stack)
    template.resource_count_is("AWS::Lambda::Alias", 1)
    template.resource_count_is("AWS::Lambda::Version", 1)
    template.has_resource("AWS::Lambda::Version", {"DeletionPolicy": "Retain"})


def test_lambda_function_name(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "runtime": aws_lambda.Runtime.PYTHON_3_10,
        "description": "my test lambda",
        "function_name": TEST_LAMBDA_NAME,
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    assert isinstance(mylambda, Guest360LambdaFunction)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert isinstance(mylambda.function_name, str)
    assert mylambda.function_name == f'{TEST_CONTEXT["prefix"]}-{TEST_LAMBDA_NAME}'


def test_lambda_function_family_python(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "description": "my test lambda",
        "function_name": TEST_LAMBDA_NAME,
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert mylambda is not None
    assert isinstance(mylambda, Guest360LambdaFunction)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert isinstance(mylambda.function.runtime, aws_lambda.Runtime)
    assert mylambda.function.runtime.family == aws_lambda.RuntimeFamily("PYTHON")
    assert isinstance(mylambda.function_name, str)
    assert mylambda.function_name == f'{TEST_CONTEXT["prefix"]}-{TEST_LAMBDA_NAME}'


def test_runtime_family_props(app_stack):
    props = {
        "handler": f"index.{TEST_LAMBDA_NAME}",
        "code": aws_lambda.Code.from_inline("""mytestcode"""),
        "runtime_family": "PYTHON",
        "function_name": TEST_LAMBDA_NAME,
    }
    mylambda = Guest360LambdaFunction(app_stack, construct_id=TEST_CONSTRUCT_ID, props=props)
    assert isinstance(mylambda.function, aws_lambda.Function)
    assert isinstance(mylambda.function.runtime, aws_lambda.Runtime)
    assert mylambda.function.runtime.family == aws_lambda.RuntimeFamily("PYTHON")


def test_get_python_latest_version():
    runtime = Guest360LambdaFunction.get_latest_version("python")
    logger.debug(f"{runtime.family=} {runtime.name=}")
    assert isinstance(runtime, aws_lambda.Runtime)


def test_get_nodejs_latest_version():
    runtime = Guest360LambdaFunction.get_latest_version("nodejs")
    logger.debug(f"{runtime.family=} {runtime.name=}")
    assert isinstance(runtime, aws_lambda.Runtime)


def test_get_dotnet_latest_version():
    runtime = Guest360LambdaFunction.get_latest_version("dotnet")
    logger.debug(f"{runtime.family=} {runtime.name=}")
    assert isinstance(runtime, aws_lambda.Runtime)
