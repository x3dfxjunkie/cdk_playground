"""
Tests for LogAggregator construct.
"""
import logging
from pathlib import Path
import os

import aws_cdk
from aws_cdk import assertions

from app.guest360_constructs.tests.utils import print_template_on_debug
from app.guest360_constructs.infrastructure.log_aggregator import LogAggregator

logger = logging.getLogger(__name__)

TEST_STACK_ID = "TestStack"


def test_cloudwatch_logs_to_kinesis_filter():
    """
    Tests that a log groups will be filtered and that filter patterns will be applied.

    This does not test the functionality of the filter pattern. That needs to be tested in dev console.
    """
    test_context = {
        "environment": "prod",
        "prefix": "prd-use1-guest360",
        "region": "us-east-1",
    }
    test_app = aws_cdk.App(context=test_context)
    stack = aws_cdk.Stack(test_app, TEST_STACK_ID)
    stream_name = "test-stream"
    stack_path = Path(os.getcwd()).parents[3]

    LogAggregator(
        scope=stack,
        construct_id="test-construct",
        stack_path=stack_path,
        create_stream_name=stream_name,
        group_patterns=["*api*", "*auth*"],
        not_group_patterns=None,
        event_patterns=["ERROR", "WARN", "FATAL"],
    )

    # Get cloudformation template
    template = assertions.Template.from_stack(stack)

    # Print template for debugging
    print_template_on_debug(
        template,
        logger,
        print_type="json",
        include_resource_types=[
            "AWS::Kinesis::Stream",
            "AWS::Lambda::Function",
            "AWS::Events::Rule",
            "AWS::IAM::Role",
            "AWS::IAM::Policy",
        ],
    )

    # Stream assertions
    template.resource_count_is("AWS::Kinesis::Stream", 1)
    template.has_resource_properties(
        "AWS::Kinesis::Stream",
        props={
            "Name": f"{test_context['prefix']}-{stream_name}",
            "RetentionPeriodHours": 24,
            "StreamEncryption": {
                "EncryptionType": "KMS",
            },
            "StreamModeDetails": {"StreamMode": "ON_DEMAND"},
        },
    )

    # Lambda assertions
    template.resource_count_is("AWS::Lambda::Function", 1)
    template.has_resource_properties(
        "AWS::Lambda::Function",
        props={
            "Handler": "lambda_function.lambda_handler",
            "Runtime": "python3.9",
            "Environment": {
                "Variables": {
                    "STREAM_ARN": {"Fn::GetAtt": ["LogAggregatorcb1abGuest360KinesisDatastreamc752b37251A35", "Arn"]},
                    "GROUP_PATTERNS": "*api*,*auth*",
                    "NOT_GROUP_PATTERNS": "",
                    "EVENT_PATTERNS": "ERROR,WARN,FATAL",
                }
            },
        },
    )

    # Event Rule assertions
    template.resource_count_is("AWS::Events::Rule", 2)
    # Trigger for log group creation
    template.has_resource_properties(
        "AWS::Events::Rule",
        props={
            "EventPattern": {
                "detail": {
                    "eventSource": ["logs.amazonaws.com"],
                    "eventName": ["CreateLogGroup"],
                },
                "source": ["aws.logs"],
            },
            "State": "ENABLED",
            "Targets": [
                {
                    "Arn": {"Fn::GetAtt": ["LogAggregatorcb1abGuest360LambdaFunction97bdb5D11ADA5", "Arn"]},
                    "Id": "Target0",
                }
            ],
        },
    )
    # Daily trigger
    template.has_resource_properties(
        "AWS::Events::Rule",
        props={
            "ScheduleExpression": "rate(1 day)",
            "State": "ENABLED",
            "Targets": [
                {
                    "Arn": {"Fn::GetAtt": ["LogAggregatorcb1abGuest360LambdaFunction97bdb5D11ADA5", "Arn"]},
                    "Id": "Target0",
                }
            ],
        },
    )


if __name__ == "__main__":  # pragma: no cover
    test_cloudwatch_logs_to_kinesis_filter()
    # test_filter_patterns()
