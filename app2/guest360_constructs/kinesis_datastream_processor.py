import aws_cdk.aws_kinesis as kinesis
import aws_cdk.aws_lambda as aws_lambda
from aws_cdk import Stack
from aws_cdk.aws_lambda_event_sources import KinesisEventSource

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable


class Guest360KinesisDatastreamProcessor(Construct360):
    """
    Construct for processing pipeline which reads from kinesis data stream and writes into processing dynamodb table via lambda consumer.

    Args:
        source_stream_consumer_lambda: Lambda instance which will consume from kinesis and write to dynamodb
        source_stream: IStream instance of kinesis stream to be used as lambda's event source
        grant_read_tables: List of dynamodb tables in which the lambda function should have read rights to
        grant_write_tables: List of dynamodb tables in which the lambda function should have write rights to
        grant_read_write_tables: List of dynamodb tables in which the lambda function should have read and write rights to
        environment_config: Configuration dictionary passed by parent stack
        lambda_kinesis_fetch_batch_size: Batch size for lambda fetch from kinesis stream
    """

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        source_stream_consumer_lambda: aws_lambda.Function,
        source_stream: kinesis.IStream,
        grant_read_tables: list[Guest360DynamodbGlobaltable] = [],
        grant_write_tables: list[Guest360DynamodbGlobaltable] = [],
        grant_read_write_tables: list[Guest360DynamodbGlobaltable] = [],
        environment_config: dict = {},
        lambda_kinesis_fetch_batch_size=100,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function_name = construct_id
        stack = Stack.of(self)
        account_id = stack.account
        region = stack.region

        source_stream_consumer_lambda.add_event_source(
            KinesisEventSource(
                stream=source_stream,
                batch_size=lambda_kinesis_fetch_batch_size,
                starting_position=aws_lambda.StartingPosition.TRIM_HORIZON,
            )
        )

        # Lambda requires read access to the source kinesis stream:
        source_stream.grant_read(source_stream_consumer_lambda)

        # Grant read/write/both access for the lambda function to any specified dynamodb tables:
        for grant_read_table in grant_read_tables:
            grant_read_table.table.grant_read_data(source_stream_consumer_lambda)

        for grant_write_table in grant_write_tables:
            grant_write_table.table.grant_write_data(source_stream_consumer_lambda)

        for grant_read_write_table in grant_read_write_tables:
            grant_read_write_table.table.grant_read_write_data(source_stream_consumer_lambda)
