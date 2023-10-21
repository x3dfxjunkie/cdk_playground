"""Tests for Guest360S3Bucket"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
import json
import logging
import sys

import pytest
from app.guest360_constructs.coverage_construct import CoverageConstruct
from aws_cdk import App, Stack, assertions

# set log levels for nozy calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.mark.timeout(30, method="signal")
def test_coverage_construct():
    test_context = {
        "environment": "local",
        "stack_name": "dummyTestStack",
        "prefix": "lst-testStack-use1",
    }
    app = App(context=test_context)
    stack = Stack(app)

    CoverageConstruct(stack, "DummyConstruct")
    template = assertions.Template.from_stack(stack)
    logger.debug(json.dumps(template.to_json(), indent=2))

    template.resource_count_is("AWS::S3::Bucket", 1)
