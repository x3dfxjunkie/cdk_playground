"""
Guest360 AWS DynamoDB construct library
"""
import json
import logging
import sys

import aws_cdk
import pytest
from aws_cdk import aws_dynamodb
from aws_cdk.assertions import Template

from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


class TestDynamodbGlobalTableConstruct:
    """
    Guest360 AWS DyanomoDB test construct
    """

    test_context = {
        "environment": "stage",
        "stack_name": "testStack",
        "prefix": "lst-TestApiGateway-use1",
    }

    stack_id = "TestStack"
    region = "us-east-1"
    construct_id = "TestConstruct"

    @pytest.mark.timeout(30, method="signal")
    def test_instantiate_construct_default_params(self):
        test_app = aws_cdk.App(context=self.test_context)
        test_stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(region=self.region))
        prefix = test_stack.node.try_get_context("prefix")

        Guest360DynamodbGlobaltable(
            test_stack,
            self.construct_id,
            partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING),
        )
        # render template
        template = Template.from_stack(test_stack)
        logger.debug(json.dumps(template.to_json(), indent=2))

        # ensure kinesis stream created with kms encryption and on_demand
        template.has_resource_properties(
            "AWS::DynamoDB::Table",
            {
                "SSESpecification": {
                    "SSEEnabled": True,
                    "SSEType": "KMS",
                }
            },
        )

        # ensure kms cdk auto creates kms key
        template.has_resource_properties(
            "AWS::KMS::Key",
            {
                "Description": f"{prefix}-{self.construct_id}-DynamodbGlobaltableEncryptionKey",
                "EnableKeyRotation": True,
            },
        )

        # ensure point in time recovery is enabled
        template.has_resource_properties(
            "AWS::DynamoDB::Table", {"PointInTimeRecoverySpecification": {"PointInTimeRecoveryEnabled": True}}
        )

        # CloudWatch Metrics will only be available in latest for now until UserErrors lesson
        if self.test_context["environment"] == "latest":
            template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 6)
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 5,
                    "DatapointsToAlarm": 5,
                    "MetricName": "UserErrors",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Sum",
                    "Threshold": 1,
                    "Unit": "Count",
                },
            )
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 1,
                    "DatapointsToAlarm": 1,
                    "MetricName": "SystemErrors",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Sum",
                    "Threshold": 1,
                    "Unit": "Count",
                },
            )
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 3,
                    "DatapointsToAlarm": 3,
                    "MetricName": "SuccessfulRequestLatency",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Average",
                    "Threshold": 100,
                    "Unit": "Milliseconds",
                },
            )
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 10,
                    "DatapointsToAlarm": 10,
                    "MetricName": "ThrottledRequests",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Sum",
                    "Threshold": 10,
                    "Unit": "Count",
                },
            )
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 1,
                    "DatapointsToAlarm": 1,
                    "MetricName": "WriteThrottledEvents",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Sum",
                    "Threshold": 1,
                    "Unit": "Count",
                },
            )
            template.has_resource_properties(
                CLOUDWATCH_ALARM_RESOURCE,
                {
                    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                    "EvaluationPeriods": 1,
                    "DatapointsToAlarm": 1,
                    "MetricName": "ReadThrottledEvents",
                    "Namespace": "AWS/DynamoDB",
                    "Period": 60,
                    "Statistic": "Sum",
                    "Threshold": 1,
                    "Unit": "Count",
                },
            )

    def test_static_environment(self):
        self.test_context = {
            "environment": "stage",
            "stack_name": "guest360",
            "prefix": "test-guest360-use1",
        }
        test_app = aws_cdk.App(context=self.test_context)
        test_stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(region=self.region))

        Guest360DynamodbGlobaltable(
            test_stack,
            self.construct_id,
            partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING),
        )
        # render template
        template = Template.from_stack(test_stack)
        logger.debug(json.dumps(template.to_json(), indent=2))

        # ensure point in time recovery is enabled
        template.has_resource_properties("AWS::ApplicationAutoScaling::ScalableTarget", {"MaxCapacity": 1000})
        template.has_resource_properties(
            "AWS::ApplicationAutoScaling::ScalingPolicy",
            {"TargetTrackingScalingPolicyConfiguration": {"TargetValue": 75}},
        )
