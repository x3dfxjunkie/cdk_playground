"""
    This construct contains the infrastructure required to create the identity graph table
"""
from typing import TypedDict, Union, cast

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.src.reliability.utils import KinesisStreamName
from aws_cdk import Duration, aws_dynamodb, aws_kinesis


class IdentityGraphProps(TypedDict):
    node_table_name: str
    edge_table_name: str


class FromTableArnProps(TypedDict):
    node_table_arn: str
    node_stream_arn: str
    edge_table_arn: str
    edge_stream_arn: str


class FromSsmProps(TypedDict):
    node_global_table: Guest360DynamodbGlobaltable
    edge_global_table: Guest360DynamodbGlobaltable
    node_kinesis_stream: Guest360KinesisDatastream
    edge_kinesis_stream: Guest360KinesisDatastream


class IdentityGraph(Construct360):
    """
    This class contains the identity graph table definitions
    """

    node_global_table: Guest360DynamodbGlobaltable
    node_table_stream: Guest360KinesisDatastream
    edge_global_table: Guest360DynamodbGlobaltable
    edge_table_stream: Guest360KinesisDatastream

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: Union[IdentityGraphProps, FromTableArnProps, FromSsmProps],
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if "node_global_table" in props and "edge_global_table" in props:
            props = cast(FromSsmProps, props)
            self.edge_global_table = props["edge_global_table"]
            self.node_global_table = props["node_global_table"]
            self.node_table_stream = props["node_kinesis_stream"]
            self.edge_table_stream = props["edge_kinesis_stream"]
            return

        if "node_table_arn" in props:
            props = cast(FromTableArnProps, props)

            self.node_global_table = Guest360DynamodbGlobaltable.from_attributes(
                self,
                "node_global_table",
                {
                    "table_arn": props["node_table_arn"],
                    "table_stream_arn": props["node_stream_arn"],
                },
            )

            self.node_table_stream = aws_kinesis.Stream.from_stream_arn(
                self, "node_global_table_stream", self.node_global_table.table.table_stream_arn  # type: ignore
            )

            self.edge_global_table = Guest360DynamodbGlobaltable.from_attributes(
                self,
                "edge_global_table",
                {
                    "table_arn": props["edge_table_arn"],
                    "table_stream_arn": props["edge_stream_arn"],
                },
            )

            self.edge_table_stream = aws_kinesis.Stream.from_stream_arn(
                self, "edge_global_table_stream", self.edge_global_table.table.table_stream_arn  # type: ignore
            )
            return

        props = cast(IdentityGraphProps, props)
        prefix = self.node.try_get_context("prefix")

        identity_nodes_table_name = props["node_table_name"]
        identity_edges_table_name = props["edge_table_name"]

        identity_node_table_kinesis_props: KinesisProps = {
            "retention_period": Duration.hours(24),
            "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            "stream_name": KinesisStreamName(prefix, identity_nodes_table_name).name(),
        }  # type: ignore

        self.node_table_stream = Guest360KinesisDatastream(
            self, construct_id="node_stream", props=identity_node_table_kinesis_props
        )

        self.node_global_table = Guest360DynamodbGlobaltable(
            self,
            construct_id=identity_nodes_table_name,
            table_name=identity_nodes_table_name,
            partition_key=aws_dynamodb.Attribute(name="node_id", type=aws_dynamodb.AttributeType.STRING),
            kinesis_stream=self.node_table_stream.kinesis_stream,
        )

        identity_edges_table_kinesis_props: KinesisProps = {
            "retention_period": Duration.hours(24),
            "stream_mode": aws_kinesis.StreamMode("ON_DEMAND"),
            "stream_name": KinesisStreamName(prefix, identity_edges_table_name).name(),
        }  # type: ignore

        self.edge_table_stream = Guest360KinesisDatastream(
            self, construct_id="edge_stream", props=identity_edges_table_kinesis_props
        )

        self.edge_global_table = Guest360DynamodbGlobaltable(
            self,
            construct_id=identity_edges_table_name,
            table_name=identity_edges_table_name,
            partition_key=aws_dynamodb.Attribute(name="source_node", type=aws_dynamodb.AttributeType.STRING),
            sort_key=aws_dynamodb.Attribute(name="target_node", type=aws_dynamodb.AttributeType.STRING),
            kinesis_stream=self.edge_table_stream.kinesis_stream,
        )

    @classmethod
    def from_arn(
        cls, scope, construct_id, node_table_arn: str, node_stream_arn: str, edge_table_arn: str, edge_stream_arn: str
    ):
        return cls(
            scope,
            construct_id,
            {
                "node_table_arn": node_table_arn,
                "node_stream_arn": node_stream_arn,
                "edge_table_arn": edge_table_arn,
                "edge_stream_arn": edge_stream_arn,
            },
        )

    def export_ssm(self) -> None:
        self.edge_global_table.export_ssm("edge_global_table")
        self.node_global_table.export_ssm("node_global_table")
        self.edge_table_stream.export_ssm("edge_table_stream")
        self.node_table_stream.export_ssm("node_table_stream")

    @classmethod
    def from_ssm(cls, scope: Construct360, construct_id: str, stack_name: str):
        node_table_stream = Guest360KinesisDatastream.from_ssm(
            scope, "node_table_stream", stack_name, "node_table_stream"
        )

        edge_table_stream = Guest360KinesisDatastream.from_ssm(
            scope, "edge_table_stream", stack_name, "edge_table_stream"
        )

        node_global_table = Guest360DynamodbGlobaltable.from_ssm(
            scope, "node_global_table", stack_name, "node_global_table"
        )

        edge_global_table = Guest360DynamodbGlobaltable.from_ssm(
            scope, "edge_global_table", stack_name, "edge_global_table"
        )

        return cls(
            scope,
            construct_id,
            {
                "node_global_table": node_global_table,
                "edge_global_table": edge_global_table,
                "node_kinesis_stream": node_table_stream,
                "edge_kinesis_stream": edge_table_stream,
            },
        )
