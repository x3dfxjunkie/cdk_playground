"""
Tests for Guest360IamRole
"""
import json
import yaml
import logging
import sys

import boto3
from moto import mock_iam
from app.guest360_constructs.iam_role import Guest360IamRole
from aws_cdk import aws_iam
from aws_cdk import App, Stack, assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
TEST_CONTEXT = {
    "prefix_global": "lst-pytest",
}


def test_iam_role_created():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    Guest360IamRole(
        scope=stack,
        construct_id="IAMRole",
        props={
            "assumed_by": aws_iam.ServicePrincipal("ec2.amazonaws.com"),
            "role_name": "foo_bar",
            "description": "Test IAM Role",
        },
    )
    template = assertions.Template.from_stack(stack)

    logger.debug(yaml.dump(template.to_json()))

    template.resource_count_is("AWS::IAM::Role", 1)
    template.has_resource_properties(
        "AWS::IAM::Role",
        {
            "Description": "Test IAM Role",
            "RoleName": "lst-pytest-foo_bar",
            "AssumeRolePolicyDocument": {
                "Statement": [{"Principal": {"Service": "ec2.amazonaws.com"}}],
            },
        },
    )

    return template


def test_iam_role_from_name():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    Guest360IamRole(
        scope=stack,
        construct_id="IAMRole",
        props={
            "assumed_by": aws_iam.ServicePrincipal("ec2.amazonaws.com"),
            "role_name": "foo_bar",
            "description": "Test IAM Role",
        },
    )
    from_role = Guest360IamRole.from_role_name(stack, "testid", "foo_bar")
    assert from_role.role_name == "lst-pytest-foo_bar"


@mock_iam
def test_iam_role_from_arn():
    client = boto3.client("iam", region_name="us-east-1")
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": ["123456789012"]},
                "Action": "sts:AssumeRole",
            }
        ],
    }

    role_response = client.create_role(
        RoleName="lst-pytest-foo_bar", AssumeRolePolicyDocument=json.dumps(trust_policy)
    )["Role"]
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    from_role = Guest360IamRole.from_role_arn(stack, "testid", role_response["Arn"])
    assert from_role.role_name == "lst-pytest-foo_bar"


if __name__ == "__main__":  # pragma: no cover
    _template = test_iam_role_created()
    print(yaml.dump(_template.to_json()))
