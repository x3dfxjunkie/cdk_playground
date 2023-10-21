"""Tests for Helix KMS Key Construct"""
import json
import os

import pytest
from aws_cdk import App, Stack, assertions

from app.guest360_constructs.kms_key_v2 import Guest360KMSKey

TEST_CONTEXT = {
    "prefix": "lst-test_sns_topic-use1",
    "is_static_env": True,
    "stack_path": f"{os.path.dirname(os.path.realpath(__file__))}/../../..",
}

CFN_TYPE = "AWS::KMS::Key"


@pytest.fixture
def environment(request):
    """Build up a CDK App and Stack to use for testing"""
    TEST_CONTEXT["environment"] = request.param
    test_app = App(context=TEST_CONTEXT)
    stack_test = Stack(test_app)  # pylint: disable=W0621
    yield stack_test


@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["local", "latest", "stage", "load", "prod"], indirect=True)
def test_default_params(environment):  # pylint: disable=W0621
    """Test with default params"""
    local_env = environment.node.get_context("environment")
    pending_window = 7 if local_env != "prod" else 30
    Guest360KMSKey(environment, "KMSKey")
    template = assertions.Template.from_stack(environment)
    print(json.dumps(template.to_json()))
    template.resource_count_is(CFN_TYPE, 1)
    template.has_resource_properties(
        CFN_TYPE,
        {"Description": "Encrypting Data", "Enabled": True, "EnableKeyRotation": True, "PendingWindowInDays": pending_window},
    )


@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["local", "latest", "stage", "load", "prod"], indirect=True)
def test_tag_access(environment):  # pylint: disable=W0621
    """Basic test for tag based access"""
    Guest360KMSKey(environment, "KMSKey", {"tags_for_read": {"foo": "bar"}})
    template = assertions.Template.from_stack(environment)
    print(json.dumps(template.to_json()))
    template.resource_count_is(CFN_TYPE, 1)
    template.has_resource_properties(
        CFN_TYPE,
        {
            "Tags": [{"Key": "foo", "Value": "bar"}],
        },
    )
