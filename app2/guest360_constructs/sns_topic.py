"""
Logic for Guest360's base construct for SQS Queues
"""
from typing import TypedDict

import aws_cdk
from aws_cdk import Stack
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import QueueName
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm


@match_class_typing
class Guest360SNSTopicProps(TypedDict):
    topic_name: str
    content_based_deduplication: NotRequired[bool]
    display_name: NotRequired[str]
    fifo: NotRequired[bool]
    master_key: NotRequired[aws_cdk.aws_kms.IKey]


class Guest360SNSTopic(Construct360):
    """Guest360 Construct for SNS Topics.

    This includes some hard-coded values, as well as some overrideable defaults.
    Required props:
        {
            "topic_name": string,
        }

    Optional props:
        {
            "content_based_deduplication": bool # Enables content-based deduplication for FIFO topics. Default: None
            "display_name": string # A developer-defined string that can be used to identify this SNS topic. Default: None
            "fifo": bool # Set to true to create a FIFO topic. Default: None
            "master_key": IKey # A KMS Key, either managed by this CDK app, or imported. Default: 'alias/aws/sns'
        }

    Usage:
        Guest360SNSTopic(self, f"{self.stack_name}-notification-topic",
                        {
                            'topic_name': f"{stack_name}-notifications",
                        })
    """

    @property
    def topic(self) -> aws_cdk.aws_sns.Topic:
        return self._topic

    @property
    def topic_name(self) -> str:
        return self._topic_name

    def __init__(self, scope: Construct360 | Stack, construct_id: str, props: Guest360SNSTopicProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        Guest360SNSTopicProps(props)

        prefix = self.node.try_get_context("prefix")
        self.props_default = {
            "content_based_deduplication": None,
            "display_name": None,
            "fifo": None,
            "master_key": None,
        }

        self.props_dict = {1: self.props_default, 2: props}
        self.props_merged = {**self.props_dict[1], **self.props_dict[2]}

        self._topic_name = QueueName(prefix, props["topic_name"]).name()
        self._topic = aws_cdk.aws_sns.Topic(
            self,
            f"{prefix}-{construct_id}-{props['topic_name']}-sns-topic",
            topic_name=self._topic_name,
            content_based_deduplication=self.props_merged["content_based_deduplication"],
            display_name=self.props_merged["display_name"],
            fifo=self.props_merged["fifo"],
            master_key=self.props_merged["master_key"],
        )

        sns_policy_ssl = aws_cdk.aws_iam.PolicyStatement(
            actions=["sns:Publish"],
            effect=aws_cdk.aws_iam.Effect.DENY,
            principals=[aws_cdk.aws_iam.AnyPrincipal()],
            resources=["*"],
            conditions={"Bool": {"aws:SecureTransport": False}},
        )

        self._topic.add_to_resource_policy(sns_policy_ssl)

        default_metrics = [
            {
                "metric": aws_cdk.aws_cloudwatch.Metric(
                    namespace="AWS/SNS",
                    metric_name="NumberOfNotificationsFailed",
                    statistic=aws_cdk.aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cdk.aws_cloudwatch.Unit.COUNT,
                    period=aws_cdk.Duration.minutes(2),
                ),
                "evaluation_periods": 1,
                "threshold": 1,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cdk.aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            }
        ]

        for cw_alarm in default_metrics:
            Guest360Alarm(
                self,
                f"{props['topic_name']}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )
