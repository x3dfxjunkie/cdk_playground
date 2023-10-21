"""Snowflake Notification Integration construct tests
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
# pylint: disable=protected-access testing purposes
# pylint: disable=unused-import

import copy
import logging
import sys

import pytest
import yaml
from aws_cdk import App, Environment, Stack
from aws_cdk.assertions import Annotations, Match, Template

from app.guest360_constructs.data_service.snowflake.cdk.notification_integration.tests.unit_tests.notification_integration_fixtures import (
    stack_test,
    stack_test_us_west,
)

from app.guest360_constructs.data_service.snowflake.cdk.notification_integration.notification_integration import (
    NotificationIntegration,
)

# set log levels for noisy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

sni_task_id = "TestSNITask"
notification_name = "SNI-Example"
test_props = {"notification_name": notification_name}

test_context = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
    "is_static_env": True,
}


class TestSnowflakeNotificationIntegration:
    """Guest360 TestSnowflakeNotificationIntegration"""

    @pytest.mark.timeout(30, method="signal")
    def test_notification_attributes(self, stack_test):
        sni_task_props = {"notification_name": notification_name}

        sni_object = NotificationIntegration(stack_test, sni_task_id, props=sni_task_props)
        assert sni_object.sns_topic_name == "lst-teststack-use1-ingestion_raw_notifications"

    @pytest.mark.timeout(30, method="signal")
    def test_notification_sns_topic(self, stack_test):
        props = copy.deepcopy(test_props)

        NotificationIntegration(stack_test, sni_task_id, props=props)

        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.resource_count_is("AWS::SNS::Topic", 1)

    @pytest.mark.timeout(30, method="signal")
    def test_notification_role(self, stack_test):
        props = copy.deepcopy(test_props)

        NotificationIntegration(stack_test, sni_task_id, props=props)

        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            "AWS::IAM::Role",
            {
                "AssumeRolePolicyDocument": {
                    "Statement": [
                        {"Action": "sts:AssumeRole", "Effect": "Allow", "Principal": {"Service": "sns.amazonaws.com"}}
                    ],
                    "Version": "2012-10-17",
                },
                "MaxSessionDuration": 3600,
                "Path": "/",
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_notification_role_with_user_and_arn_secret_external_id(self, stack_test):
        props = copy.deepcopy(test_props)
        props.update(
            {
                "iam_user_arn": f'arn:aws:iam::{"0"*12}:user/test_user',
                "arn_secret_iam_external_id": f'arn:aws:secretsmanager:us-east-1:{"0"*12}:secret:test_secret-xxxxxx',
            }
        )
        NotificationIntegration(stack_test, sni_task_id, props=props)

        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.resource_count_is("AWS::IAM::Role", 1)

    @pytest.mark.timeout(30, method="signal")
    def test_notification_output(self, stack_test):
        props = copy.deepcopy(test_props)

        NotificationIntegration(stack_test, sni_task_id, props=props)

        # render template.
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))

        template.has_output("*", props={"Description": "SNS Topic ARN for the Snowflake Notification Integration"})

    @pytest.mark.timeout(30, method="signal")
    def test_notification_us_west(self, stack_test_us_west):
        props = copy.deepcopy(test_props)

        NotificationIntegration(stack_test_us_west, sni_task_id, props=props)

        # render template.
        template = Template.from_stack(stack_test_us_west)
        logger.debug(yaml.dump(template.to_json()))

        template.resource_count_is("AWS::SNS::Topic", 0)
        template.resource_count_is("AWS::IAM::Role", 0)
