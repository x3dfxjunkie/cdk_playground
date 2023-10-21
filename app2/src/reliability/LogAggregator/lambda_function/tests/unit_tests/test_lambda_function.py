"""
Unit tests for the Lambda function code for the LogAggregator construct.
"""
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
import logging
import importlib
import sys
import os
from enum import Enum
from typing import Union

import pytest
import boto3
from moto import mock_logs

from app.src.reliability.LogAggregator.lambda_function.env_keys import EnvKeys

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)

# create a stdout logger
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

BASE_ENVIRONMENT_VARS = {
    "AWS_REGION": "us-east-1",
    "AWS_ACCESS_KEY_ID": "testing",
    "AWS_SECRET_ACCESS_KEY": "testing",
    "AWS_SECURITY_TOKEN": "testing",
    "AWS_SESSION_TOKEN": "testing",
    EnvKeys.STREAM_ARN.value: "aws:kinesis:us-east-1:123456789012:stream/test-stream",
    EnvKeys.SUBSCRIPTION_FILTER_ROLE_ARN.value: "arn:aws:iam::123456789012:role/test-role",
}


def set_environment_variables(monkeypatch, env_vars: Union[dict, None] = None) -> None:
    environment_vars = BASE_ENVIRONMENT_VARS.copy()
    if env_vars:
        environment_vars.update(env_vars)
    for k, v in environment_vars.items():
        monkeypatch.setenv(k, v)


@pytest.fixture(name="logs")
def fixture_logs():
    """Create a mock CloudWatch Logs client"""
    os.environ.update(BASE_ENVIRONMENT_VARS)  # Need to set these for moto to work
    return boto3.client("logs", region_name="us-east-1")


def load_lambda_with_environment(monkeypatch, env_vars: Union[dict, None] = None):
    """Import the Lambda function in the context of the test environment"""
    set_environment_variables(monkeypatch, env_vars)
    from app.src.reliability.LogAggregator.lambda_function import lambda_function

    importlib.reload(lambda_function)  # To avoid caching envrionment variables declared in the Lambda function
    return lambda_function


class LogGroups(Enum):
    GROUP1 = "test-group1"
    GROUP2 = "test-group2"
    GROUP3 = "test-group3"
    GROUPX = "exclude-group"


class TestLogAggregator:
    """Test the Lambda function"""

    @mock_logs
    def test_default_environment(self, monkeypatch, logs):
        """If no matching or exluded log groups are specified, all log groups should be matched"""
        logs.create_log_group(logGroupName=LogGroups.GROUP1.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP2.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP3.value)

        lambda_function = load_lambda_with_environment(monkeypatch)
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
            LogGroups.GROUP3.value,
        ]

    @mock_logs
    def test_match_groups_only(self, monkeypatch, logs):
        """If only matching log groups are set, only those log groups should be matched"""
        logs.create_log_group(logGroupName=LogGroups.GROUP1.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP2.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP3.value)  # This group should not be matched
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={EnvKeys.GROUP_PATTERNS.value: f"{LogGroups.GROUP1.value},{LogGroups.GROUP2.value}"},
        )
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
        ]

    @mock_logs
    def test_exclude_groups_only(self, monkeypatch, logs):
        """If only excluded log groups are set, only those log groups should be excluded"""
        logs.create_log_group(logGroupName=LogGroups.GROUP1.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP2.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP3.value)
        logs.create_log_group(logGroupName=LogGroups.GROUPX.value)  # This group should not be matched
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={EnvKeys.NOT_GROUP_PATTERNS.value: f"{LogGroups.GROUPX.value}"},
        )
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
            LogGroups.GROUP3.value,
        ]

    @mock_logs
    def test_both_groups_set(self, monkeypatch, logs):
        """If both matching and excluded log groups are set, only those matching_log_groups should be matched"""
        logs.create_log_group(logGroupName=LogGroups.GROUP1.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP2.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP3.value)
        logs.create_log_group(logGroupName=LogGroups.GROUPX.value)
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={
                EnvKeys.GROUP_PATTERNS.value: f"{LogGroups.GROUP1.value},{LogGroups.GROUP2.value}",
                EnvKeys.NOT_GROUP_PATTERNS.value: f"{LogGroups.GROUPX.value}",
            },
        )
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
        ]

    @mock_logs
    def test_wildcards_for_groups(self, monkeypatch, logs):
        """If wildcards are used in the matching or excluded log groups, they should be expanded"""
        logs.create_log_group(logGroupName=LogGroups.GROUP1.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP2.value)
        logs.create_log_group(logGroupName=LogGroups.GROUP3.value)
        logs.create_log_group(logGroupName=LogGroups.GROUPX.value)

        # Including
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={
                EnvKeys.GROUP_PATTERNS.value: LogGroups.GROUP1.value[:-1] + "*",
            },
        )
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
            LogGroups.GROUP3.value,
        ]

        # Excluding
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={
                EnvKeys.NOT_GROUP_PATTERNS.value: "*xclude*",
            },
        )
        assert lambda_function.get_filtered_log_groups() == [
            LogGroups.GROUP1.value,
            LogGroups.GROUP2.value,
            LogGroups.GROUP3.value,
        ]

    @mock_logs
    def test_complicated_group_filters(self, monkeypatch, logs):
        """More realistic wildcards and filters on log groups"""
        desired_capture_groups = {
            "/aws/lambda/lst-use1-guest360-authorizer-lambda",
            "/aws/other-service/other-serviceAuthorizer",
            "/aws/lambda/lst-use1-guest360-experience-api-lambda",
            "/aws/apigateway/myAPI",
            "lst-use1-guest360-dataservice-Guest360APIGatewayc649fguest360restapiloggroup61B22EED-HXed1MOXetRU ",
            "API-Gateway-Execution-Logs_b2mvdt1s36/latest",
        }
        desired_exlude_groups = [
            "/aws/apigateway/welcome",
        ]

        # Create mock log groups
        for log_group in desired_capture_groups:
            logs.create_log_group(logGroupName=log_group)
        for log_group in desired_exlude_groups:
            logs.create_log_group(logGroupName=log_group)

        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={
                EnvKeys.GROUP_PATTERNS.value: "*api*,*auth*",
                EnvKeys.NOT_GROUP_PATTERNS.value: "/aws/apigateway/welcome*",
            },
        )
        assert set(lambda_function.get_filtered_log_groups()) == desired_capture_groups

    def test_event_pattern_construction(self, monkeypatch):
        lambda_function = load_lambda_with_environment(
            monkeypatch,
            env_vars={
                EnvKeys.EVENT_PATTERNS.value: "ERROR,WARN,FATAL",
            },
        )
        assert lambda_function.filter_pattern == "?ERROR ?WARN ?FATAL"
