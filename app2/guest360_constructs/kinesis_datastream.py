"""Guest360KinesisDatastream Construct
"""
from typing import TypedDict, Union, cast

from app.guest360_constructs import kms_key
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import KinesisStreamName
from aws_cdk import Duration, Stack, aws_cloudwatch, aws_iam, aws_kinesis, aws_kms, aws_ssm
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired


@match_class_typing
class KinesisProps(TypedDict):
    shard_count: Union[int, float, None]
    stream_mode: aws_kinesis.StreamMode
    retention_period: NotRequired[Duration]
    stream_name: NotRequired[str]
    encryption_key: NotRequired[aws_kms.Key]


class SsmImportProps(TypedDict):
    stream_arn: str
    kms_arn: str


class Guest360KinesisDatastream(Construct360):
    """Guest360 Construct for Kinesis Data Stream"""

    @property
    def kinesis_stream(self) -> aws_kinesis.Stream:
        return self.stream

    @property
    def kinesis_stream_name(self) -> str:
        return self._stream_name

    def __init__(self, scope: Construct360, construct_id: str, props: Union[KinesisProps, dict], **kwargs) -> None:
        """__init__.
        Guest360KinesisDatastream
            * Enforces encryption using aws_kms.Ikey
                * if Ikey is not supplied one is created using the Guest360KMSKey
            * retention_period for 'latest' environment set to 24 hours for cost savings
            * stream_mode set to PROVISIONED for 'latest' environment for cost savings
            * shard_count set to 1 for 'latest' environment for cost savings
        Example:
            Guest360KinesisDatastream(stack, "MyKinesisDatastream")
        Args:
            scope (Construct360): scope
            construct_id (str): construct ID
            encryption_key (Optional[aws_kms.IKey]): encryption_key
            retention_period (aws_cdk.Duration): retention_period
            shard_count (Union[int, float, None]): shard_count
            stream_mode (aws_kinesis.StreamMode): stream_mode
            stream_name (Optional[str]): stream_name
            kwargs:
        Returns:
            None
        """
        super().__init__(scope, construct_id)

        self.ssm_export = None

        if kwargs.get("ssm_props", False):
            ssm_props: SsmImportProps = cast(SsmImportProps, kwargs.get("ssm_props"))
            aws_kms_key = aws_kms.Key.from_key_arn(self, "kms_key", ssm_props["kms_arn"])
            self.stream = aws_kinesis.Stream.from_stream_attributes(
                self, "kinesis_stream", stream_arn=ssm_props["stream_arn"], encryption_key=aws_kms_key
            )
            self._stream_name = self.stream.stream_name
            return

        props = cast(KinesisProps, props)

        # Check that props matches proper input structure
        KinesisProps(props)

        prefix = self.node.try_get_context("prefix")

        if props["stream_mode"] == aws_kinesis.StreamMode("ON_DEMAND"):
            props["shard_count"] = None

        # if no encryption set create custom encryption key using Guest360KMSKey
        if props.get("encryption_key") is None:
            props["encryption_key"] = kms_key.Guest360KMSKey(
                self,
                "KinesisEncryptionKey",
                {"alias": construct_id, "description": f"{prefix}-{construct_id}-KinesisEncryptionKey"},
            ).key

            props["encryption_key"].grant_encrypt_decrypt(aws_iam.AccountRootPrincipal())

        if props.get("stream_name") is not None:
            props["stream_name"] = KinesisStreamName(prefix, props["stream_name"]).name()

        if props.get("encryption") is None:
            props["encryption"] = aws_kinesis.StreamEncryption.KMS

        default_metrics = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/Kinesis",
                    metric_name="GetRecords.IteratorAgeMilliseconds",
                    statistic=aws_cloudwatch.Statistic.MAXIMUM.value,
                    period=Duration.minutes(5),
                ),
                "evaluation_periods": 3,
                "threshold": 60_000,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            }
        ]

        if props.get("stream_mode") == aws_kinesis.StreamMode("PROVISIONED"):
            default_metrics.extend(
                [
                    {
                        "metric": aws_cloudwatch.Metric(
                            namespace="AWS/Kinesis",
                            metric_name="WriteProvisionedThroughputExceeded",
                            statistic=aws_cloudwatch.Statistic.SUM.value,
                            period=Duration.minutes(1),
                        ),
                        "evaluation_periods": 3,
                        "threshold": 1,
                        "datapoints_to_alarm": 2,
                        "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
                    },
                    {
                        "metric": aws_cloudwatch.Metric(
                            namespace="AWS/Kinesis",
                            metric_name="ReadProvisionedThroughputExceeded",
                            statistic=aws_cloudwatch.Statistic.SUM.value,
                            period=Duration.minutes(1),
                        ),
                        "evaluation_periods": 3,
                        "threshold": 1,
                        "datapoints_to_alarm": 2,
                        "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
                    },
                ]
            )

        self.stream = aws_kinesis.Stream(
            self,
            self.pass_id,
            **props,
        )
        self._stream_name = props.get("stream_name")

        for cw_alarm in default_metrics:
            Guest360Alarm(
                self,
                f"{self._stream_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

        NagSuppressions.add_resource_suppressions(
            self.stream,
            [
                {
                    "id": "AwsSolutions-KDS3",
                    "reason": "Using a custom key is acceptable.",
                }
            ],
        )

    def export_ssm(self, resource_name: str) -> str:
        prefix = self.node.try_get_context("prefix")
        stack_name = Stack.of(self).stack_name
        construct_name = "Guest360KinesisDatastream"
        resource_prefix = f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"

        def parameter_name(componenet_name: str):
            return f"{resource_prefix}/{componenet_name}"

        encryption_key_arn = self.stream.encryption_key.key_arn if self.stream.encryption_key else ""

        self.ssm_export = (
            [
                aws_ssm.StringParameter(
                    self,
                    "stream_arn_parameter",
                    parameter_name=parameter_name("stream_arn"),
                    string_value=self.stream.stream_arn,
                ),
                aws_ssm.StringParameter(
                    self,
                    "kms_arn_parameter",
                    parameter_name=parameter_name("kms_arn"),
                    string_value=encryption_key_arn,
                ),
            ]
            if self.ssm_export is None
            else self.ssm_export
        )

        return resource_prefix

    @classmethod
    def from_ssm(cls, scope: Construct360, construct_id: str, stack_name: str, resource: str):
        stack = Stack.of(scope)
        prefix = stack.node.try_get_context("prefix")
        construct_name = "Guest360KinesisDatastream"

        def parameter_name(componenet_name):
            return f"/{prefix}/{stack_name}/{construct_name}/{resource}/{componenet_name}"

        kinesis_stream_arn = aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("stream_arn"))
        kms_arn = aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("kms_arn"))
        return cls(scope, construct_id, {}, ssm_props={"stream_arn": kinesis_stream_arn, "kms_arn": kms_arn})
