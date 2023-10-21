"""
    This file contains the infrastructre required to create the keychain table
"""
from typing import List, Optional, TypedDict, Union, cast

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.src.reliability.utils import KinesisStreamName
from aws_cdk import Duration, Stack, aws_dynamodb, aws_kinesis, aws_ssm


class KeychainRingProps(TypedDict):
    table_name: str


class FromArnProps(TypedDict):
    table_arn: str
    stream_ssm_import: str


class FromAttributesProps(TypedDict):
    global_table: Guest360DynamodbGlobaltable
    kinesis_stream: Guest360KinesisDatastream


class KeyringTable(Construct360):
    """
    This class contains the keychain table definition
    """

    global_table: Guest360DynamodbGlobaltable
    kinesis_stream: Guest360KinesisDatastream
    ssm_export: Optional[List[aws_ssm.StringParameter]]

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: Union[KeychainRingProps, FromArnProps, FromAttributesProps],
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.ssm_export = None
        if "table_arn" in props:
            props = cast(FromArnProps, props)

            self.kinesis_stream = Guest360KinesisDatastream.from_ssm(
                self, "identity_stream", Stack.of(scope).stack_name, props["stream_ssm_import"]
            )

            self.global_table = Guest360DynamodbGlobaltable.from_attributes(
                self,
                "keyring_table",
                {
                    "table_arn": props["table_arn"],
                    "global_indexes": ["atomic_id_index"],
                    "table_stream_arn": self.kinesis_stream.stream.stream_arn,
                },
            )
            if not self.global_table.table.table_stream_arn:
                raise ValueError("Keyring Table must have stream")

            return

        if "global_table" in props:
            props = cast(FromAttributesProps, props)

            self.global_table = props["global_table"]
            self.kinesis_stream = props["kinesis_stream"]
            return

        props = cast(KeychainRingProps, props)

        prefix = self.node.try_get_context("prefix")

        table_name: str = props["table_name"]

        identity_table_kinesis_props: KinesisProps = {
            "retention_period": Duration.hours(24),
            "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            "stream_name": KinesisStreamName(prefix, table_name).name(),
            "shard_count": None,
        }

        self.kinesis_stream = Guest360KinesisDatastream(
            self, construct_id="identity_stream", props=identity_table_kinesis_props
        )

        self.global_table = Guest360DynamodbGlobaltable(
            self,
            construct_id=table_name,
            table_name=table_name,
            partition_key=aws_dynamodb.Attribute(name="type#id-PK", type=aws_dynamodb.AttributeType.STRING),
            kinesis_stream=self.kinesis_stream.kinesis_stream,
        )

        self.global_table.table.add_global_secondary_index(  # type: ignore
            partition_key=aws_dynamodb.Attribute(name="atomic_id", type=aws_dynamodb.AttributeType.STRING),
            index_name="atomic_id_index",
            projection_type=aws_dynamodb.ProjectionType.ALL,
        )

    def export_ssm(self) -> None:
        self.global_table.export_ssm("keyring_table")
        self.kinesis_stream.export_ssm("keyring_kinesis_stream")

    @classmethod
    def from_ssm(cls, scope: Construct360, construct_id: str, stack_name: str):
        kinesis_stream = Guest360KinesisDatastream.from_ssm(
            scope, "keyring_kinesis_stream", stack_name, "keyring_kinesis_stream"
        )
        global_table = Guest360DynamodbGlobaltable.from_ssm(scope, "keyring_table", stack_name, "keyring_table")

        return cls(scope, construct_id, {"global_table": global_table, "kinesis_stream": kinesis_stream})

    @classmethod
    def from_arn(cls, scope: Construct360, construct_id: str, table_arn: str, stream_ssm_import):
        return cls(scope, construct_id, {"table_arn": table_arn, "stream_ssm_import": stream_ssm_import})
