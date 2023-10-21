"""external_stage fixtures
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
# pylint: disable=protected-access testing purposes
# pylint: disable=unused-import

import logging
import sys

import pytest
from aws_cdk import App, Aspects, Environment, Stack, aws_iam, aws_sqs
from cdk_nag import AwsSolutionsChecks

from app.guest360_constructs.s3_bucket import Guest360S3Bucket

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


@pytest.fixture
def stack_test():
    cdk_app = App(context=test_context)
    aspects = Aspects.of(cdk_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(
        cdk_app, stack_name, env=Environment(account=test_context["account_id"], region=test_context["region"])
    )
    yield stack_test


@pytest.fixture
def stack_west_test():
    cdk_app = App(context=test_context)
    aspects = Aspects.of(cdk_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(cdk_app, stack_name, env=Environment(account=test_context["account_id"], region="us-west-2"))
    yield stack_test


@pytest.fixture
def bucket_test(stack_test):
    bucket = Guest360S3Bucket(
        stack_test, "BucketTest", region="us-east-1", props={"bucket_name": test_context["s3_bucket_name"]}
    )
    yield bucket


@pytest.fixture
def user_test(stack_test):
    user = aws_iam.User(stack_test, "ExternalStageUserTest", user_name=test_context["user_name_test"])
    yield user


@pytest.fixture
def sqs_test(stack_test):
    sqs = aws_sqs.Queue(stack_test, "SnowFlakeSqs")
    yield sqs
