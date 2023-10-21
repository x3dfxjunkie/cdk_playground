"""Snowflake Notification Integration construct fixtures
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

from aws_cdk import App, Aspects, Environment, Stack
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

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

test_context = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
    "is_static_env": True,
}
stack_id = "TestSNI"


@pytest.fixture
def stack_test():
    test_app = App(context=test_context)
    aspects = Aspects.of(test_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
    yield stack_test


@pytest.fixture
def stack_test_us_west():
    test_app = App(context=test_context)
    aspects = Aspects.of(test_app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack_test = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-west-1"))
    yield stack_test
