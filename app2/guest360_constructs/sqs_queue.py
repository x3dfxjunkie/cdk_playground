"""
Logic for Guest360's base construct for SQS Queues
"""
from typing import TypedDict

from aws_cdk import Duration, aws_kms, aws_sqs, aws_cloudwatch
from typing_extensions import NotRequired

# from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs import kms_key
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.src.reliability.utils import QueueName
from strongtyping.strong_typing import match_class_typing
from cdk_nag import NagSuppressions


@match_class_typing
class SQSQueueProps(TypedDict):
    """
    encryption_key (Optional[aws_kms.IKey]): KMS encryption key to use for queue.
    queue_name str: Name of queue
    """

    queue_name: str
    encryption_key: NotRequired[aws_kms.Key]


class Guest360SQSQueue(Construct360):
    """

    __init__.
    Example:
        Guest360SQSQueue(stack, "MySQSQueue", "TheQueueName")
    Args:
        scope (Construct): scope
        id (str): id
        props (SQSQueueProps): properties to use for SQS queue.
        kwargs (dict): kwargs dict to pass to construct init.

    Returns:
        None
    """

    def __init__(self, scope: Construct360, construct_id: str, props: SQSQueueProps, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        SQSQueueProps(props)
        encryption_key = props.get("encryption_key")
        prefix = self.node.try_get_context("prefix")
        queue_name = props["queue_name"]

        # if no encryption set create custom encryption key using Guest360KMSKey
        if encryption_key is None:
            encryption_key = kms_key.Guest360KMSKey(
                self,
                "SQSQueueEncryptionKey",
                {
                    "alias": construct_id,
                    "description": f"{prefix}-{construct_id}-SQSQueueEncryptionKey",
                },
            ).key

        self.queue = aws_sqs.Queue(
            self,
            f"{prefix}-{construct_id}-SQSQueue",
            queue_name=QueueName(prefix, queue_name).name(),
            encryption=aws_sqs.QueueEncryption.KMS,
            encryption_master_key=encryption_key,
            enforce_ssl=True,
        )

        default_alarms = [
            # The first metric should check that the oldest message in the queue
            # has not been in the queue up until the retention period of 4 days
            # meaning that the messages in the queue are being processed really
            # slowly if they're in the queue that long
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/SQS",
                    metric_name="ApproximateAgeOfOldestMessage",
                    statistic=aws_cloudwatch.Statistic.MAXIMUM.value,
                    unit=aws_cloudwatch.Unit.SECONDS,
                    period=Duration.hours(1),
                ),
                "evaluation_periods": 2,
                "threshold": 345_600,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            # The second metric is checking that we don't hit the AWS limit of
            # 120,000 in-flight messages for a particular queue
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/SQS",
                    metric_name="ApproximateNumberOfMessagesNotVisible",
                    statistic=aws_cloudwatch.Statistic.MAXIMUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 2,
                "threshold": 115_000,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
        ]

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{QueueName(prefix, queue_name).name()}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

        NagSuppressions.add_resource_suppressions(
            self.queue,
            [
                {
                    "id": "AwsSolutions-SQS3",
                    "reason": "Prevent warnings when SQS is used as an event bridge pipe DLQ",
                }
            ],
        )

        # # CloudWatch Default Alarms
        # self.some_default_metric = aws_cloudwatch.Metric(
        #     namespace="AWS/SQS",
        #     metric_name="A REAL METRIC HERE",
        # )
        # self.some_default_alarm = Guest360Alarm(
        #     self,
        #     f"{construct_id}-SQSQueue",
        #     props={
        #         "metric": self.some_default_metric,
        #         "evaluation_periods": 1,
        #         "threshold": 1,
        #     }
        # )
