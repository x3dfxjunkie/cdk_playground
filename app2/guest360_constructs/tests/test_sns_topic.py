"""
SNS Topic Construct Test
"""
import pytest
from app.guest360_constructs.sns_topic import Guest360SNSTopic
from aws_cdk import App, Stack, assertions

TEST_CONTEXT = {"prefix": "lst-test_sns_topic-use1", "environment": "local"}
CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


@pytest.mark.timeout(30, method="signal")
def test_sns_topic_created():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    Guest360SNSTopic(stack, "KMSKey", {"topic_name": "test_sns_topic"})
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::SNS::Topic", 1)


@pytest.mark.timeout(30, method="signal")
def test_sns_topic_metrics_created():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)
    Guest360SNSTopic(
        stack,
        "KMSKey",
        {
            "topic_name": "test_sns_topic",
        },
    )
    template = assertions.Template.from_stack(stack)
    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 1)
    template.has_resource_properties(
        CLOUDWATCH_ALARM_RESOURCE,
        {
            "ComparisonOperator": "GreaterThanOrEqualToThreshold",
            "EvaluationPeriods": 1,
            "DatapointsToAlarm": 1,
            "MetricName": "NumberOfNotificationsFailed",
            "Namespace": "AWS/SNS",
            "Period": 120,
            "Statistic": "Sum",
            "Threshold": 1,
            "Unit": "Count",
        },
    )
