""" Kinesis_Consumer - consumer stream construct
Creates lambda producer and kinesis stream to produce consumer events
"""
import logging
from typing import TypedDict, Union
from typing_extensions import NotRequired

from aws_cdk import Duration, Stack, aws_iam, aws_kinesis, aws_kms, aws_lambda, aws_lambda_event_sources, aws_sqs
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.sqs_queue import Guest360SQSQueue
from app.src.reliability.utils import LambdaFunctionName


logger = logging.getLogger(__name__)


class KinesisStreamProps(TypedDict):
    """Kinesis Stream Properties"""

    stream_name: str
    retention_period: Duration
    encryption_key: NotRequired[aws_kms.IKey]
    shard_count: Union[int, None]
    stream_mode: aws_kinesis.StreamMode


class KinesisKclRoleConfigProps(TypedDict):
    """Kinesis Role Config Properties"""

    id: str
    role_arns: list[str]


class KinesisLambdaProducerProps(TypedDict):
    """Kinesis Lambda producer properties"""

    runtime: str
    code_path: str
    handler: str
    timeout: Duration
    environment: dict


class KinesisEventSourceProps(TypedDict):
    """kinesis event source props"""

    stream: aws_kinesis.Stream


class KinesisConsumerStream(Construct360):
    """Guest360 Construct for Kinesis Consumer Stream"""

    @property
    def stream(self) -> aws_kinesis.Stream:
        return self._kinesis_stream

    @property
    def producer_dlq(self) -> aws_sqs.Queue:
        return self._lambda_dlq

    @property
    def producer(self) -> aws_lambda.Function:
        return self._lambda_function

    kinesis_kcl_additional_grant_actions = (
        "kinesis:ListStreams",
        "kinesis:ListShards",
        "kinesis:DeregisterStreamConsumer",
        "kinesis:RegisterStreamConsumer",
    )

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        stream_props: KinesisStreamProps,
        lambda_producer_props: KinesisLambdaProducerProps,
        event_source_props: KinesisEventSourceProps,
        role_configs: list[KinesisKclRoleConfigProps],
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)
        prefix = self.node.try_get_context("prefix")
        stream_name = stream_props["stream_name"]

        #####
        # Kinesis Data Stream for Consumption by External Sources
        #####
        props: KinesisStreamProps = stream_props
        self._kinesis_stream = Guest360KinesisDatastream(self, construct_id="KinesisConsumerStream", props=props).stream

        #####
        # Add Kinesis Regional Resource Grants to global IAM roles
        #####
        role_configs = role_configs if isinstance(role_configs, list) else []
        for role_config in role_configs:
            # add resource policy level grants utilizing Role from role_name object
            role = Guest360IamRole.from_role_name(
                self,
                f'{stack.region}-{role_config["id"]}',
                role_name=f'{stream_name}_{role_config["id"]}',
                mutable=True,
            )
            self._kinesis_stream.grant_read(role)
            # additional acctions required for kcl to utilize consumer groups and kinesis fan-out
            for action in self.kinesis_kcl_additional_grant_actions:
                self._kinesis_stream.grant(role, action)

        #####
        # Lambda Configuration
        ####
        self._lambda_dlq = Guest360SQSQueue(
            self,
            construct_id="KinesisConsumerDLQ",
            props={"queue_name": f"{stream_name}-KinesisConsumerLambdaDLQ"},
        ).queue

        lambda_producer_props["environment"] = {
            **lambda_producer_props.get("environment", {}),
            **{
                "KINESIS_STREAM_NAME": self._kinesis_stream.stream_name,
                "DEADLETTER_QUEUE_URL": self._lambda_dlq.queue_url,
            },
        }

        # convert values to cdk
        lambda_producer_props["runtime"] = aws_lambda.Runtime(lambda_producer_props["runtime"])
        lambda_producer_props["code"] = aws_lambda.Code.from_asset(lambda_producer_props["code_path"])
        del lambda_producer_props["code_path"]

        self._lambda_function = Guest360LambdaFunction(
            self,
            "KinesisConsumerLambda",
            {
                "function_name": LambdaFunctionName(prefix, f"{stream_name}-KinesisConsumerLambda").name(),
                "description": f'{stream_props["stream_name"]}-KinesisConsumerLambda',
                **lambda_producer_props,
            },
        ).function

        #####
        # add lambda event source for kinesis event source
        #####
        # add defaults and convert to cdk objects
        if event_source_props.get("max_batching_window"):
            event_source_props["max_batching_window"] = Duration.seconds(event_source_props["max_batching_window"])

        if event_source_props.get("starting_position"):
            event_source_props["starting_position"] = aws_lambda.StartingPosition(
                event_source_props["starting_position"]
            )
        else:
            event_source_props["starting_position"] = aws_lambda.StartingPosition.TRIM_HORIZON

        self._lambda_function.add_event_source(aws_lambda_event_sources.KinesisEventSource(**event_source_props))

        # Add grants to producer
        self.stream.grant_write(self.producer)
        self.producer_dlq.grant_send_messages(self.producer)
        self.producer_dlq.encryption_master_key.grant_encrypt_decrypt(self.producer)
        self.producer_dlq.encryption_master_key.add_to_resource_policy(
            aws_iam.PolicyStatement(
                principals=[self.producer.role],
                actions=["kms:Decrypt"],
                resources=["*"],
            )
        )
        # nag suppression
        NagSuppressions.add_resource_suppressions(
            self._lambda_function.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "kms:GenerateDataKey* and kms:ReEncrypt* are acceptable when \
                                adding with specific resource.",
                },
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "AWS managed policies are acceptable.",
                },
            ],
            True,
        )

        NagSuppressions.add_resource_suppressions(
            self._lambda_dlq,
            [
                {
                    "id": "AwsSolutions-SQS3",
                    "reason": "SQS Queue is actually a DLQ itself (for Kinesis stream).",
                }
            ],
            True,
        )
