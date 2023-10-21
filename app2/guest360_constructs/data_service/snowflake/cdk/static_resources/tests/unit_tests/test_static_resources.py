""" Tests for AwsSnowPipe """
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
# pylint: disable=protected-access testing purposes
# pylint: disable=unused-import

import copy
import logging
import sys

import yaml
import pytest
from aws_cdk import App, Aspects, Environment, Stack, aws_iam, aws_sqs
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

from app.guest360_constructs.data_service.snowflake.cdk.external_stage.tests.unit_tests.external_stage_fixtures import (
    bucket_test,
    user_test,
    sqs_test,
)
from app.guest360_constructs.data_service.snowflake.cdk.static_resources.static_resources import StaticResources


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
logger.setLevel(logging.INFO)

stack_name = "StackTest"
test_context = {
    "account_id": "0" * 12,
    "environment": "latest",
    "stack_name": "testapp",
    "prefix": "lst-testapp-use1",
    "prefix_global": "lst-testapp",
    "region": "us-east-1",
    "is_static_env": True,
    "s3_bucket_name": "test-bucket",
    "user_name_test": "DisneySnowFlakeUser",
}

test_external_stage_props = {
    "external_stage_name": "test_pipe-name",
    "s3_bucket_name": "test-bucket",
    "s3_bucket_prefix": "/foo",
}
test_notification_integration_props = {"notification_name": "test_notification"}

user_name_test = "DisneySnowFlakeUser"


@pytest.fixture
def stack_test():
    cdk_app = App(context=test_context)
    aspects = Aspects.of(cdk_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(
        cdk_app, stack_name, env=Environment(account=test_context["account_id"], region=test_context["region"])
    )
    yield stack_test


class TestSnowflakeStaticResources:
    """snowflake static resources tests"""

    def test_static_resources(self, stack_test, bucket_test, user_test, sqs_test):
        props = {
            "external_stage": {
                **test_external_stage_props,
                **{
                    "s3_bucket": bucket_test.bucket,
                    "iam_principal": user_name_test,
                    "snowflake_sqs_arn": sqs_test.queue_arn,
                },
            },
            "notification_integration": test_notification_integration_props,
        }
        StaticResources(stack_test, "StaticResourcesTest", props=props)
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(yaml.dump(template.to_json()))
