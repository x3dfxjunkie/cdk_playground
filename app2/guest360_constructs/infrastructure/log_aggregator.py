"""
Construct which adds subscription filters to log groups and sends log events to a Kinesis Data Stream.
"""
from typing import List
from pathlib import Path

from aws_cdk import (
    aws_kinesis,
    aws_iam,
    aws_events,
    aws_events_targets,
    aws_lambda,
    Duration,
)
from constructs import Construct
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.src.reliability.LogAggregator.lambda_function.env_keys import EnvKeys


class LogAggregator(Construct360):
    """
    Construct that groups resources for Cloudwatch log subscription and filter to Kinesis Data Stream.

    It is triggered by two event types:
    1. Cloudwatch log group creation trigger
    2. Daily EventBridge trigger to check for new log groups
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        stack_path: Path,
        create_stream_name: str,
        group_patterns: List[str] = None,
        not_group_patterns: List[str] = None,
        event_patterns: List[str] = None,
        **kwargs,
    ) -> None:
        """
        Args:
            scope (Construct): CDK Construct scope
            construct_id (str): CDK Construct ID
            stack_path (Path): Path to the stack instantiating this construct
            create_stream_name (str): Name of the destination Kinesis Data Stream
            group_patterns (List[str], optional): List of log group patterns to match. Case-insensitive. Defaults to None.
            not_group_patterns (List[str], optional): List of log group patterns to exclude. Case-insensitive. Defaults to None.
            event_patterns (List[str], optional): List of log event patterns to match. Defaults to None.
        """
        super().__init__(scope, construct_id, **kwargs)

        # Destination stream
        kinesis_stream = Guest360KinesisDatastream(
            self,
            "KinesisDataStream",
            props={
                "stream_mode": aws_kinesis.StreamMode.ON_DEMAND,
                "shard_count": None,
                "stream_name": create_stream_name,
            },
        ).stream

        # Role for subscription filters to write to Kinesis Data Stream
        subscription_filter_role = aws_iam.Role(
            self,
            "SubscriptionFilterRole",
            assumed_by=aws_iam.ServicePrincipal("logs.amazonaws.com"),
            description="Role for subscription filters to write to Kinesis Data Stream",
        )
        subscription_filter_role.add_to_policy(
            aws_iam.PolicyStatement(
                actions=[
                    "kinesis:DescribeStream",
                    "kinesis:PutRecord",
                    "kinesis:PutRecords",
                ],
                resources=[kinesis_stream.stream_arn],
            )
        )

        # Lambda to add subscription filter to log groups
        code_path = f"{stack_path}/bazel-bin/app/src/reliability/LogAggregator/lambda_archive.zip"
        lambda_function = Guest360LambdaFunction(
            self,
            "LambdaFunction",
            props={
                "code": aws_lambda.Code.from_asset(str(code_path)),
                "handler": "lambda_function.lambda_handler",
                "description": "Adds subscription filters to log groups",
                "allow_public_subnet": False,
                "environment": {
                    EnvKeys.STREAM_ARN.value: kinesis_stream.stream_arn,
                    EnvKeys.SUBSCRIPTION_FILTER_ROLE_ARN.value: subscription_filter_role.role_arn,
                    EnvKeys.GROUP_PATTERNS.value: ",".join(group_patterns) if group_patterns else "",
                    EnvKeys.NOT_GROUP_PATTERNS.value: ",".join(not_group_patterns) if not_group_patterns else "",
                    EnvKeys.EVENT_PATTERNS.value: ",".join(event_patterns) if event_patterns else "",
                },
            },
        ).lambda_function

        # Permit the Lambda to add subscription filters to any log groups
        subscription_filter_policy_statement = aws_iam.PolicyStatement(
            actions=["logs:PutSubscriptionFilter"],
            resources=["*"],
            effect=aws_iam.Effect.ALLOW,
        )
        subscription_filter_policy = aws_iam.Policy(
            self,
            "SubscriptionFilterPolicy",
            statements=[subscription_filter_policy_statement],
        )
        lambda_function.role.attach_inline_policy(subscription_filter_policy)

        # Permit CloudWatch Events to invoke the Lambda function
        lambda_function.add_permission(
            "AllowCloudWatchEvents", principal=aws_iam.ServicePrincipal("events.amazonaws.com")
        )

        # CreateLogGroup triggers Lambda
        aws_events.Rule(
            self,
            "LogGroupCreateRule",
            event_pattern=aws_events.EventPattern(
                source=["aws.logs"],
                detail={
                    "eventSource": ["logs.amazonaws.com"],
                    "eventName": ["CreateLogGroup"],
                },
            ),
        ).add_target(aws_events_targets.LambdaFunction(lambda_function))

        # Daily Lambda trigger
        aws_events.Rule(self, "DailyTrigger", schedule=aws_events.Schedule.rate(Duration.days(1))).add_target(
            aws_events_targets.LambdaFunction(lambda_function)
        )

        # Suppress CDK Nag warnings
        NagSuppressions().add_resource_suppressions(
            subscription_filter_policy,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Lambda needs to be able to add subscription filters to all log groups.",
                }
            ],
        )
