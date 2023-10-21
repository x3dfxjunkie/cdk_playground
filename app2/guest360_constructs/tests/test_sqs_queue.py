"""
SQS Queue Construct Test
"""
import pytest
import logging
import sys

from app.guest360_constructs.sqs_queue import Guest360SQSQueue, SQSQueueProps
from app.guest360_constructs.tests.utils import print_template_on_debug
from app.guest360_constructs.kms_key import Guest360KMSKey

from aws_cdk import App, Stack, assertions
from strongtyping.strong_typing_utils import TypeMisMatch

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix": "lst-test_sqs_queue-use1", "environment": "local"}
CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


@pytest.fixture(name="stack")
def fixture_stack():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    yield stack


@pytest.mark.timeout(30, method="signal")
def test_sqs_queue_created(stack):
    Guest360SQSQueue(stack, "TestSQSQueue", {"queue_name": "test_sqs_queue"})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)

    template.resource_count_is("AWS::SQS::Queue", 1)


@pytest.mark.timeout(30, method="signal")
def test_sqs_queue_with_kms_encryption_created(stack):
    kms_key = Guest360KMSKey(
        stack,
        "SqsQueueEncryptionKey",
        {"alias": "test_key", "description": "test_key"},
    ).key
    Guest360SQSQueue(stack, "TestSQSQueue", {"queue_name": "test_sqs_queue", "encryption_key": kms_key})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)

    template.has_resource_properties(
        "AWS::SQS::Queue", {"KmsMasterKeyId": {"Fn::GetAtt": [assertions.Match.any_value(), "Arn"]}}
    )


@pytest.mark.timeout(30, method="signal")
def test_sqs_queue_cw_alarms_created(stack):
    Guest360SQSQueue(stack, "TestSQSQueue", {"queue_name": "test_sqs_queue"})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)

    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 2)
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 2,
            "DatapointsToAlarm": 2,
            "MetricName": "ApproximateAgeOfOldestMessage",
            "Namespace": "AWS/SQS",
            "Period": 3600,
            "Statistic": "Maximum",
            "Threshold": 345_600,
            "Unit": "Seconds",
        },
    )

    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 2,
            "DatapointsToAlarm": 2,
            "MetricName": "ApproximateNumberOfMessagesNotVisible",
            "Namespace": "AWS/SQS",
            "Period": 60,
            "Statistic": "Maximum",
            "Threshold": 115_000,
            "Unit": "Count",
        },
    )


def test_sqs_queue_props_raises_exception():
    props = {"some_invalid_key": "some_invalid_config_value"}
    with pytest.raises(TypeMisMatch):
        SQSQueueProps(props)
