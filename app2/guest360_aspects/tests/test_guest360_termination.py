import json
import logging
import sys

import aws_cdk
import pytest
from aws_cdk.assertions import Annotations, Template

from app.guest360_aspects.guest360_termination import Guest360Termination

LOGGER = logging.getLogger(__name__)
STREAMHANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
STREAMHANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(STREAMHANDLER)


@pytest.fixture
def app_stack(environment):
    # Set up a default app/stack and S3 Bucket
    app = aws_cdk.App(context={"environment": environment})
    stack = aws_cdk.Stack(app, "TestStack", termination_protection=True)
    aws_cdk.aws_s3.Bucket(stack, "testBucket")

    print(f"{stack.termination_protection=}")

    #  Set up AppConfig hosted configuration
    test_app = aws_cdk.aws_appconfig.CfnApplication(
        stack,
        "testApp",
        name="test-app",
    )
    test_profile = aws_cdk.aws_appconfig.CfnConfigurationProfile(
        stack,
        "testProfile",
        name="test-profile",
        location_uri="hosted",
        application_id=test_app.ref,
    )
    aws_cdk.aws_appconfig.CfnHostedConfigurationVersion(
        stack,
        "testCfg",
        application_id=test_app.ref,
        configuration_profile_id=test_profile.ref,
        content_type="application/json",
        content='{"boolEnableTest": true}',
    )

    # Apply our custom aspect
    aws_cdk.Aspects.of(stack).add(Guest360Termination())

    yield stack


@pytest.mark.parametrize("environment", ["latest"])
def test_aspect_non_prod(app_stack):
    # Synth the app
    aws_cdk.aws_logs.LogGroup(app_stack, "testLogGroup")
    template = Template.from_stack(app_stack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(app_stack)
    annotations.has_error("*", "Stack termination is not set correctly on: TestStack")

    # Ensure we have the expected count and params
    template.resource_count_is("AWS::S3::Bucket", 1)
    template.has_resource(
        "AWS::S3::Bucket",
        {
            "UpdateReplacePolicy": "Delete",
            "DeletionPolicy": "Delete",
        },
    )

    template.resource_count_is("AWS::Logs::LogGroup", 1)
    template.has_resource_properties(
        "AWS::Logs::LogGroup",
        {"RetentionInDays": 90},
    )


@pytest.mark.parametrize("environment", ["prod"])
def test_aspect_prod(app_stack):
    # Synth the app
    aws_cdk.aws_logs.LogGroup(app_stack, "testLogGroup", retention=aws_cdk.aws_logs.RetentionDays.THREE_DAYS)
    template = Template.from_stack(app_stack)
    LOGGER.debug(json.dumps(template.to_json(), indent=2))

    annotations = Annotations.from_stack(app_stack)
    annotations.has_no_error("*", "Stack termination is not set correctly on: TestStack")

    # Ensure we have the expected count and params
    template.resource_count_is("AWS::S3::Bucket", 1)
    template.has_resource(
        "AWS::S3::Bucket",
        {
            "UpdateReplacePolicy": "Delete",
            "DeletionPolicy": "Delete",
        },
    )

    template.resource_count_is("AWS::Logs::LogGroup", 1)
    template.has_resource_properties(
        "AWS::Logs::LogGroup",
        {"RetentionInDays": 3},
    )

    template.has_resource(
        "AWS::AppConfig::HostedConfigurationVersion",
        {"UpdateReplacePolicy": "Retain"},
    )
