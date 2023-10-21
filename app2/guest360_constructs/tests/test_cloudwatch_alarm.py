"""
Tests for Guest360Alarm
"""
import logging
import os
from pathlib import Path

import aws_cdk
import pytest
import strongtyping
import yaml
from aws_cdk import assertions, aws_cloudwatch

from app.guest360_constructs.cloudwatch_alarm import AlarmPropError, Guest360Alarm
from app.guest360_constructs.tests.utils import print_template_on_debug

logger = logging.getLogger(__name__)

TEST_STACK_ID = "TestStack"
RESOURCE = "AWS::CloudWatch::Alarm"
TOPIC_SHORT_ENV = {
    "latest": "dev",
    "load": "tst",
    "stage": "tst",
    "prod": "prd",
}

GENERIC_ALARM_VALUES = {
    "metric_name": "NEW_SQS_QUEUE_CREATED",
    "namespace": "AWS/SQS",
    "evaluation_periods": 1,
    "threshold": 1,
}

GENERIC_REQUIRED_ALARM_INPUT_PROPS = {
    "metric": aws_cloudwatch.Metric(
        namespace=GENERIC_ALARM_VALUES["namespace"],
        metric_name=GENERIC_ALARM_VALUES["metric_name"],
    ),
    "evaluation_periods": GENERIC_ALARM_VALUES["evaluation_periods"],
    "threshold": GENERIC_ALARM_VALUES["threshold"],
}

GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS = {
    "ComparisonOperator": "GreaterThanOrEqualToThreshold",  # cloudwatch_alarm default
    "EvaluationPeriods": GENERIC_ALARM_VALUES["evaluation_periods"],
    "MetricName": GENERIC_ALARM_VALUES["metric_name"],
    "Namespace": GENERIC_ALARM_VALUES["namespace"],
    "Period": 300,  # cloudwatch_alarm default
    "Statistic": "Average",  # cloudwatch_alarm default
    "Threshold": GENERIC_ALARM_VALUES["threshold"],
}

file_path = os.path.realpath(__file__)
config = Path(file_path).parents[2] / "infrastructure" / "reliability" / "configs" / "alarm_defaults.yaml"
config = yaml.safe_load(config.open(mode="r"))
SNS_SNOW_SETTINGS = config["sns_snow_settings"]
TOPIC_SUFFIX = "alarm-notifications"
PROD_DEFAULT_TOPIC = "prd-use1-guest360-alarm-notifications"  #  SNS_SNOW_SETTINGS["prod"]["default_topic"]


def test_default_alarm():
    """
    Basic instantiation - no alarm action attached
    """
    test_context = {
        "environment": "local",
        "prefix": "test-prefix-use1",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={**GENERIC_REQUIRED_ALARM_INPUT_PROPS},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={"ActionsEnabled": False, **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS, "TreatMissingData": "ignore"},
    )


def test_default_prod_alarm():
    """
    Testing that the prod default alarms go to topic `wdpr-guest360-prd-snow-pri3`
    19 Jul 2023: updated to temporarily go to `prd-use1-guest360-alarm-notifications`
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={**GENERIC_REQUIRED_ALARM_INPUT_PROPS},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": True,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            f":{PROD_DEFAULT_TOPIC}",
                        ],
                    ],
                }
            ],
            "AlarmDescription": (
                "[SNOWAG:app-global-Guest360]"
                "[SNOWCI:WDPR Guest360 - AWS Production]"
                "[SNOWDESC:TestStack failed on NEW_SQS_QUEUE_CREATED ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1]"
                "TestStack failed on NEW_SQS_QUEUE_CREATED ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1"
            ),
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


@pytest.mark.skip(reason="19 Jul 2023: this will come back in the future.")
def test_elevated_prod_alarm():
    """
    Testing that, in prod, manually set p2 alarms go to topic `wdpr-guest360-prd-snow-pri2`
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={
            "p_level_in_prod": "p2",
            **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
        },
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": True,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            f":prd-use1-guest360-{TOPIC_SUFFIX}",
                        ],
                    ],
                }
            ],
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


@pytest.mark.skip(reason="19 Jul 2023: this will come back in the future.")
def test_lower_environments_cant_elevate():
    """
    Testing that the non-prod default alarms go to topic `wdpr-guest360-{short_env}-snow-pri4`. They can't "elevate"

    Exception is 'local' which does not map to a topic.
    """
    for environment in ["latest", "load", "stage"]:
        for p_level in ["2", "3"]:  # P-Levels
            test_context = {
                "environment": environment,
                "prefix": "prd-usw2-guest360",
                "region": "us-west-2",
            }
            test_app = aws_cdk.App(context=test_context)
            stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
            Guest360Alarm(
                stack,
                f"{TEST_STACK_ID}",
                props={
                    "p_level_in_prod": f"p{p_level}",
                    **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
                },
            )
            template = assertions.Template.from_stack(stack)
            print_template_on_debug(template, logger, print_type="yaml")
            template.resource_count_is(RESOURCE, 1)
            # Check alarm has a P3 SNS Action attached
            template.has_resource_properties(
                RESOURCE,
                props={
                    "ActionsEnabled": True,
                    "AlarmActions": [
                        {
                            "Fn::Join": [
                                "",
                                [
                                    "arn:aws:sns:",
                                    {"Ref": "AWS::Region"},
                                    ":",
                                    {"Ref": "AWS::AccountId"},
                                    f":prd-usw2-guest360-{TOPIC_SUFFIX}",
                                ],
                            ],
                        }
                    ],
                    **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
                },
            )


def test_p1_should_fail():
    """
    Test that the mapping of p-levels can't be easily hacked.
    """
    for environment in ["latest", "load", "stage", "prod"]:
        test_context = {
            "environment": environment,
            "prefix": "test-prefix-guest360",
            "region": "us-east-1",
        }
        test_app = aws_cdk.App(context=test_context)
        stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
        with pytest.raises(strongtyping.strong_typing_utils.TypeMisMatch):
            Guest360Alarm(
                stack,
                f"{TEST_STACK_ID}",
                props={
                    "p_level_in_prod": "p1",
                    **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
                },
            )


def test_ephemeral_cant_publish_default_incident():
    """
    Ephemeral environments don't need sns action. Test that they can't create one
    """
    test_context = {
        "environment": "latest",
        "prefix": "lst-use1-test",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={**GENERIC_REQUIRED_ALARM_INPUT_PROPS},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": False,  # This is the key property for the test
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


def test_ephemeral_can_publish_to_custom_sns():
    """
    Custom SNS topics can be used in ephemeral environments
    """
    test_context = {
        "environment": "latest",
        "prefix": "lst-use1-blah-blah",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    custom_topic_name = "custom-test-topic"
    custom_alarm_description = "My custom alarm description"
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={
            "custom_sns_alarm_topic_name": custom_topic_name,  # To be configured by user
            "alarm_description": custom_alarm_description,
            **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
        },
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": True,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            f":{custom_topic_name}",
                        ],
                    ],
                }
            ],
            "AlarmDescription": (
                f"TestStack failed on NEW_SQS_QUEUE_CREATED "
                f"ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1. "
                f"{custom_alarm_description}"
            ),
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


def test_ephemeral_wont_publish_snow_incident():
    """
    Even providing a real SNOW topic, ephemeral will not publish an incident
    """
    test_context = {
        "environment": "latest",
        "prefix": "lst-use1-blah-blah",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    custom_topic_name = "wdpr-guest360-dev-snow-pri4"  # This is the key line
    custom_alarm_description = "Custom alarm description"
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={
            "custom_sns_alarm_topic_name": custom_topic_name,  # To be configured by user
            "alarm_description": custom_alarm_description,
            **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
        },
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": False,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            ":lst-use1-blah-blah-alarm-notifications",
                        ],
                    ],
                }
            ],
            "AlarmDescription": (
                f"TestStack failed on NEW_SQS_QUEUE_CREATED "
                f"ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1. "
                f"{custom_alarm_description}"
            ),
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


@pytest.mark.skip(reason="19 Jul 2023: this will come back in the future.")
def test_custom_snow_incident():
    """
    Stacks should be able to constrol what topics alarms go to (e.g., load testing stack).
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    custom_snow_assignment_group = "custom-assignment-group"
    custom_alarm_description = "My custom alarm description"
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={
            "snow_assignment_group": custom_snow_assignment_group,  # To be configured by user
            "alarm_description": custom_alarm_description,
            "p_level_in_prod": "P3",
            **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
        },
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": True,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            ":prd-use1-guest360-alarm-notifications",
                        ],
                    ],
                }
            ],
            "AlarmDescription": (
                "[SNOWAG:app-global-Guest360]"
                "[SNOWCI:WDPR Guest360 - AWS Production]"
                "[SNOWDESC:TestStack failed on NEW_SQS_QUEUE_CREATED ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1]"
                f"{custom_alarm_description}"
            ),
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


def test_can_sns_without_snow_incident():
    """
    Stacks can set alarms to write to SNS in static environments without opening SNOW incidents
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    custom_topic_name = "custom-test-topic"
    custom_alarm_description = "My custom alarm description"
    Guest360Alarm(
        stack,
        f"{TEST_STACK_ID}",
        props={
            "custom_sns_alarm_topic_name": custom_topic_name,  # To be configured by user
            "alarm_description": custom_alarm_description,
            **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
        },
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(RESOURCE, 1)
    template.has_resource_properties(
        RESOURCE,
        props={
            "ActionsEnabled": True,
            "AlarmActions": [
                {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:sns:",
                            {"Ref": "AWS::Region"},
                            ":",
                            {"Ref": "AWS::AccountId"},
                            f":{custom_topic_name}",
                        ],
                    ],
                }
            ],
            "AlarmDescription": (
                f"TestStack failed on NEW_SQS_QUEUE_CREATED "
                f"ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 1. "
                f"{custom_alarm_description}"
            ),
            **GENERIC_ALARM_TEMPLATE_OUTPUT_PROPS,
        },
    )


def test_parameter_errors():
    """
    Parameter combos that don't make sense must raise errors.
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    custom_topic_name = "custom-test-topic"
    custom_snow_assignment_group = "custom-assignment-group"

    # Can't have snow_integration_enabled and alarm_actions_disabled
    with pytest.raises(AlarmPropError):
        Guest360Alarm(
            stack,
            f"{TEST_STACK_ID}",
            props={
                "custom_sns_alarm_topic_name": custom_topic_name,  # To be configured by user
                "snow_assignment_group": custom_snow_assignment_group,  # To be configured by user
                "snow_integration_enabled": True,
                "alarm_actions_disabled": True,
                **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
            },
        )

    # Can't have SNOW incident via custom topic unless assignment group given
    with pytest.raises(AlarmPropError):
        Guest360Alarm(
            stack,
            f"{TEST_STACK_ID}",
            props={
                "custom_sns_alarm_topic_name": custom_topic_name,  # To be configured by user
                "snow_integration_enabled": True,
                **GENERIC_REQUIRED_ALARM_INPUT_PROPS,
            },
        )


if __name__ == "__main__":  # pragma: no cover
    # test_default_alarm()
    # test_default_prod_alarm()
    # test_elevated_prod_alarm()
    # test_lower_environments_cant_elevate()
    # test_p1_should_fail()
    # test_ephemeral_cant_publish_incident()
    test_custom_snow_incident()
