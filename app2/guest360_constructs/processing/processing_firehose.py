"""Processing Firehose Construct and Properties"""
from typing import TypedDict

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from aws_cdk import aws_iam, aws_kinesis, aws_kinesisfirehose, aws_lambda, aws_logs
from cdk_nag import NagSuppressions
from typing_extensions import NotRequired


class S3Destination(TypedDict):
    bucket: Guest360S3Bucket


class ProcessingFirehoseProps(TypedDict):
    destination: S3Destination
    lambda_transformer: NotRequired[aws_lambda.IFunction]
    prefix: str | None
    kinesis_source: aws_kinesis.IStream


class ProcessingFirehose(Construct360):
    """Generates Firehose Construct"""

    delivery_stream: aws_kinesisfirehose.CfnDeliveryStream

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: ProcessingFirehoseProps,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        firehose_delivery_role = Guest360IamRole(
            self,
            "firehose_delivery_role",
            {"assumed_by": aws_iam.ServicePrincipal("firehose.amazonaws.com"), "description": "Firehose Deliver Role"},
        ).role

        props["destination"]["bucket"].bucket.grant_read_write(firehose_delivery_role)

        props["kinesis_source"].grant_read(firehose_delivery_role)

        firehose_policy = aws_iam.Policy(
            self,
            "firehose-policy",
            roles=[firehose_delivery_role],  # type: ignore
            statements=[
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    resources=[props["kinesis_source"].stream_arn],
                    actions=[
                        "kinesis:DescribeStream",
                        "kinesis:GetShardIterator",
                        "kinesis:GetRecords",
                        "kinesis:ListShards",
                    ],
                )
            ],
        )

        if "lambda_transformer" in props and props["lambda_transformer"] is not None:
            props["lambda_transformer"].grant_invoke(firehose_delivery_role)

        lambda_configuration = (
            {
                "type": "Lambda",
                "parameters": [
                    {"parameterName": "LambdaArn", "parameterValue": props["lambda_transformer"].function_arn}
                ],
            }
            if "lambda_transformer" in props and props["lambda_transformer"] is not None
            else {
                "type": "AppendDelimiterToRecord",
                "parameters": [{"parameterName": "Delimiter", "parameterValue": "\\n"}],
            }
        )

        delivery_stream_log_group = aws_logs.LogGroup(self, "delivery_stream_logs_group")
        delivery_stream_log_stream = aws_logs.LogStream(
            self, "delivery_stream_logs_stream", log_group=delivery_stream_log_group
        )

        self.delivery_stream = aws_kinesisfirehose.CfnDeliveryStream(
            self,
            "delivery_stream",
            delivery_stream_type="KinesisStreamAsSource",
            extended_s3_destination_configuration=aws_kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                bucket_arn=props["destination"]["bucket"].bucket.bucket_arn,
                prefix=props["prefix"],
                role_arn=firehose_delivery_role.role_arn,
                dynamic_partitioning_configuration={"enabled": True},
                error_output_prefix=props["kinesis_source"].stream_name + "_error/",
                processing_configuration={
                    "enabled": True,
                    "processors": [lambda_configuration],
                },
                cloud_watch_logging_options=aws_kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                    enabled=True,
                    log_group_name=delivery_stream_log_group.log_group_name,
                    log_stream_name=delivery_stream_log_stream.log_stream_name,
                ),
                encryption_configuration=aws_kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                    kms_encryption_config=aws_kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                        awskms_key_arn=props["destination"]["bucket"].kms_key.key_arn
                    )
                )
                if props["destination"]["bucket"].kms_key
                else None,
            ),
            kinesis_stream_source_configuration=aws_kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                kinesis_stream_arn=props["kinesis_source"].stream_arn, role_arn=firehose_delivery_role.role_arn
            ),
        )

        self.delivery_stream.node.add_dependency(firehose_policy.node.default_child)

        NagSuppressions.add_resource_suppressions(
            firehose_delivery_role,
            [{"id": "AwsSolutions-IAM5", "reason": "Read Only Wildcard permissions is okay"}],
            apply_to_children=True,
        )

        NagSuppressions.add_resource_suppressions(
            self.delivery_stream,
            [
                {
                    "id": "AwsSolutions-KDF1",
                    "reason": "Enabling encryption fails as it says it only supports DirectPut",
                    "applies_to": "[Resource::*]",
                }
            ],
            True,
        )
