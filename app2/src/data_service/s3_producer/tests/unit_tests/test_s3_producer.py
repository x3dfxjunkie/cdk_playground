"""
pytests for validating kinesis_producer lambda code
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
import datetime
import json
import logging
import sys
import uuid
from collections import namedtuple

import app.src.processing.realtime.module.domains.lightning_lane.event_generator as ll_event_generator
import aws_cdk
import boto3
import moto
import pytest
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.tools.test_data.lightning_lane_raw_events import LightningLaneRawEvents
from aws_cdk import aws_dynamodb as dynamodb
from aws_lambda_context import LambdaContext
from test_helpers.mock_dynamodb_table import mock_boto3_dynamodb_table_args
from test_helpers.mock_kinesis_events import mock_kinesis_events

# set log levels for nozy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

DynamodbTuple = namedtuple("dynamodb", "client, resource, stream")


class TestS3Producer:
    """Test Class for Kinesis Producer"""

    identity_table_name = "IdentityTable"
    identity_nodes_table_name = "IdentityNodesTable"
    identity_edges_table_name = "IdentityEdgesTable"
    identity_notification_stream_name = "IdentityNotificationStream"
    event_table_name = "EventTable"
    profile_table_name = "ProfileTable"
    stream_name = "producer_stream"
    prefix = "test-prefix"
    shard_count = 50
    stream_mode_details = {"StreamMode": "ON_DEMAND"}
    dlq_name = "LambdaDeadLetterQueue"
    bad_kinesis_record = {
        "eventSourceARN": "arn:aws:kinesis:us-east-1:000000000000:stream/DynamodbKinesis",
        "eventSource": "aws:kinesis",
        "eventVersion": "1.0",
        "eventId": "shardId-000000000001:0",
        "eventName": "aws:kinesis:record",
        "awsRegion": "us-east-1",
        "kinesis": {
            "partitionKey": "1",
            "sequenceNumber": 0,
            "kinesisSchemaVersion": "1.0",
            "approximateArrivalTimestamp": 1676244024.2427223,
            "data": "eyJldmVudElEIjogImJiZGEwOGMzMWZjNTQ0Mjg4ZmEzYzUxNDVkNGQyZGM0IiwgImV2ZW50TmFtZSI6ICJJTlNFUlQiLCAiZXZlbnRWZXJzaW9uIjogIjEuMCIsICJldmVudFNvdXJjZSI6ICJhd3M6ZHluYW1vZGIiLCAiYXdzUmVnaW9uIjogInVzLWVhc3QtMSIsICJkeW5hbW9kYiI6IHsiQXBwcm94aW1hdGVDcmVhdGlvbkRhdGVUaW1lIjogIjIwMjItMTEtMjkgMTk6NDM6MjQuNzM2NjA4IiwgIktleXMiOiB7ImF0b21pY19pZCI6IHsiUyI6ICI3NjkyMTRhNS05ODc3LTQ0ODktOWEyYi1jZjc2YjBhNjEzYWYifX0sICJOZXdJbWFnZSI6IHsiYXRvbWljX2lkIjogeyJTIjogIjc2OTIxNGE1LTk4NzctNDQ4OS05YTJiLWNmNzZiMGE2MTNhZiJ9LCAiZXZlbnQiOiB7IlMiOiAie1wiZXZlbnRUeXBlXCI6IFwibGlnaHRuaW5nX2xhbmVcIiwgXCJhdG9taWNJZFwiOiBcIjc2OTIxNGE1LTk4NzctNDQ4OS05YTJiLWNmNzZiMGE2MTNhZlwiLCBcImd1ZXN0SWRcIjogXCJBQUFBREJBRlhUM0RVS1BQQlZZTVlOR1c1RVwiLCBcInRyYW5zYWN0aW9uSWRcIjogXCJjNDUyYjg3ZjI3ZTA3NzFmMDBhZmJlNTc4MzI1MGE4MVwiLCBcImV4cGVyaWVuY2VcIjoge1wiZXhwZXJpZW5jZUlkXCI6IFwiMTkxOTM0NjFcIiwgXCJleHBlcmllbmNlQ2F0ZWdvcnlcIjogXCJFeHBlcmllbmNlIENhdGVnb3J5IE4vQVwiLCBcImV4cGVyaWVuY2VOYW1lXCI6IFwiRXhwZXJpZW5jZSBOYW1lIE4vQVwiLCBcImxvY2F0aW9uSWRcIjogXCIxOTE5MzQ2MVwiLCBcImxvY2F0aW9uTmFtZVwiOiBcIkxvY2F0aW9uIE5hbWUgTi9BXCIsIFwibG9jYXRpb25IaWVyYXJjaHlcIjoge1wiZGVzdGluYXRpb25cIjoge1wiZmFjaWxpdHlJZFwiOiBcIkZhY2lsaXR5IElkIE4vQVwiLCBcImZhY2lsaXR5TmFtZVwiOiBcIkZhY2lsaXR5IE5hbWUgTi9BXCJ9LCBcInJlc29ydEFyZWFcIjoge1wiZmFjaWxpdHlJZFwiOiBcIkZhY2lsaXR5IElkIE4vQVwiLCBcImZhY2lsaXR5TmFtZVwiOiBcIkZhY2lsaXR5IE5hbWUgTi9BXCJ9LCBcInBhcmtPclJlc29ydFwiOiB7XCJmYWNpbGl0eUlkXCI6IFwiRmFjaWxpdHkgSWQgTi9BXCIsIFwiZmFjaWxpdHlOYW1lXCI6IFwiRmFjaWxpdHkgTmFtZSBOL0FcIn0sIFwibGFuZFwiOiB7XCJmYWNpbGl0eUlkXCI6IFwiRmFjaWxpdHkgSWQgTi9BXCIsIFwiZmFjaWxpdHlOYW1lXCI6IFwiRmFjaWxpdHkgTmFtZSBOL0FcIn0sIFwicGF2aWxsaW9uXCI6IHtcImZhY2lsaXR5SWRcIjogXCJGYWNpbGl0eSBJZCBOL0FcIiwgXCJmYWNpbGl0eU5hbWVcIjogXCJGYWNpbGl0eSBOYW1lIE4vQVwifX19LCBcImV2ZW50VGltZVwiOiAxNjY5NzUxMDA0LjcyODI2NywgXCJjcmVhdGVkVGltZVwiOiAxNjY2NTMyOTY0LjYyNTUxLCBcImxhc3RNb2RpZmllZFwiOiAxNjY2NTMyOTY0LjYyNTUxLCBcImJ1c2luZXNzRGF0ZVwiOiAxNjY2NDk3NjAwLjAsIFwiZXhwZXJpZW5jZVN0YXJ0XCI6IDE2NjY1MzMwMDAuMCwgXCJleHBlcmllbmNlRW5kXCI6IDE2NjY1MzY2MDAuMCwgXCJldmVudFN0YXR1c1wiOiBcIkJPT0tFRFwifSJ9fSwgIk9sZEltYWdlIjoge30sICJTZXF1ZW5jZU51bWJlciI6ICIxMTAwMDAwMDAwMDE3NDU0NDIzMDExIiwgIlNpemVCeXRlcyI6IDE0ODgsICJTdHJlYW1WaWV3VHlwZSI6ICJORVdfQU5EX09MRF9JTUFHRVMifX0_added_to_force_base64_error_=",  # pragma: allowlist secret
        },
        "timestamp": "2022-11-29 14:43:24,816-0500",
        "service": "app.src.data_service.kinesis_producer.kinesis_producer.producer",
    }

    @pytest.fixture
    def mock_lambda_context(self):
        lambda_context = LambdaContext()
        lambda_context.function_name = "function_name"
        lambda_context.function_version = "function_version"
        lambda_context.invoked_function_arn = "invoked_function_arn"
        lambda_context.memory_limit_in_mb = "memory_limit_in_mb"
        lambda_context.aws_request_id = "aws_request_id"
        yield lambda_context

    @pytest.fixture
    def mock_os_environment(self, monkeypatch):
        # monkeypatch all environment variables necessary w/out affecting OS environment
        monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
        monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
        monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
        monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
        monkeypatch.setenv("KINESIS_STREAM_NAME", self.stream_name)
        monkeypatch.setenv("IDENTITY_TABLE_NAME", f"{self.prefix.lower()}-{self.identity_table_name.lower()}")
        monkeypatch.setenv("PROFILE_TABLENAME", f"{self.prefix.lower()}-{self.profile_table_name.lower()}")
        monkeypatch.setenv("EXPERIENCE_EVENT_TABLE_NAME", f"{self.prefix.lower()}-{self.event_table_name.lower()}")

    @pytest.fixture
    def mock_kinesis(self, mock_os_environment):
        moto.mock_kinesis().start()
        yield boto3.client("kinesis")

    @pytest.fixture
    def mock_dynamodb(self, mock_os_environment):
        moto.mock_dynamodb().start()
        moto.mock_dynamodbstreams().start()

        yield DynamodbTuple(
            boto3.client("dynamodb"),
            boto3.resource("dynamodb"),
            boto3.client("dynamodbstreams"),
        )
        moto.mock_dynamodb().stop()
        moto.mock_dynamodbstreams().stop()

    @pytest.fixture
    def mock_sqs(self, mock_os_environment):
        moto.mock_sqs().start()
        yield boto3.client("sqs")

    @pytest.fixture
    def mock_stream(self, mock_kinesis):
        stream = mock_kinesis.create_stream(
            StreamName=self.stream_name,
            ShardCount=self.shard_count,
            StreamModeDetails=self.stream_mode_details,
        )
        yield stream

    @pytest.fixture
    def mock_dlq(self, mock_sqs):
        sqs = mock_sqs.create_queue(
            QueueName=self.dlq_name,
        )
        yield sqs

    @pytest.fixture
    def mock_table(self, mock_dynamodb):
        # start mock services for all types
        logger.info(f"{self.prefix=}")
        logger.info(f"{self.event_table_name.lower()=}")
        logger.info(f"{self.identity_table_name.lower()=}")
        self.setup_dynamodb(
            mock_dynamodb,
            self.event_table_name.lower(),
            self.identity_table_name.lower(),
            self.identity_nodes_table_name.lower(),
            self.identity_edges_table_name.lower(),
            self.profile_table_name.lower(),
        )

    def setup_dynamodb(
        self,
        dynamodb_tuple,
        event_table_name,
        identity_table_name,
        identity_nodes_table_name,
        identity_edges_table_name,
        profile_table_name,
        prefix=prefix,
    ):
        # TODO: The source stacks should be refactored so that stateful resources are separated from stateless
        # This would then allow stacks to be directly imported w/out changes or copy/paste of code
        # This would then remove this dummy stack class from needing to exist
        class MyStack(aws_cdk.Stack):
            """_summary_
            in the future this should be an imported construct/stack instead of copy/paste cdk
            """

            def __init__(self, scope: Construct360, construct_id: str, prefix=self.prefix, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                self.node.set_context("prefix", prefix)

                identity_table = Guest360DynamodbGlobaltable(
                    self,
                    construct_id=identity_table_name,
                    table_name=identity_table_name,
                    partition_key=dynamodb.Attribute(name="type#id-PK", type=dynamodb.AttributeType.STRING),
                )
                identity_table.table.add_global_secondary_index(
                    partition_key=dynamodb.Attribute(name="atomic_id", type=dynamodb.AttributeType.STRING),
                    index_name=f"{identity_table_name}-atomic_id_index",
                    projection_type=dynamodb.ProjectionType.ALL,
                )

                Guest360DynamodbGlobaltable(
                    self,
                    construct_id=profile_table_name,
                    table_name=profile_table_name,
                    partition_key=dynamodb.Attribute(name="atomic_id", type=dynamodb.AttributeType.STRING),
                )

                Guest360DynamodbGlobaltable(
                    self,
                    construct_id=event_table_name,
                    table_name=event_table_name,
                    partition_key=dynamodb.Attribute(name="atomic_id#event_name", type=dynamodb.AttributeType.STRING),
                    sort_key=dynamodb.Attribute(name="event_time", type=dynamodb.AttributeType.NUMBER),
                )

                Guest360DynamodbGlobaltable(
                    self,
                    construct_id=identity_nodes_table_name,
                    table_name=identity_nodes_table_name,
                    partition_key=dynamodb.Attribute(name="node_id", type=dynamodb.AttributeType.STRING),
                )

                Guest360DynamodbGlobaltable(
                    self,
                    construct_id=identity_edges_table_name,
                    table_name=identity_edges_table_name,
                    partition_key=dynamodb.Attribute(name="source_node", type=dynamodb.AttributeType.STRING),
                    sort_key=dynamodb.Attribute(name="target_node", type=dynamodb.AttributeType.STRING),
                )

        tables_attributes = mock_boto3_dynamodb_table_args(
            MyStack,
            [],
            {
                "env": aws_cdk.Environment(
                    account="0" * 12,
                    region="us-east-1",
                )  # environment needed to send to stack to resolve env specific resources (dynamodb)
            },
            [
                {
                    "table_id": Guest360DynamodbGlobaltable.to_passing_id(identity_table_name),
                    "table_name": identity_table_name,
                },
                {
                    "table_id": Guest360DynamodbGlobaltable.to_passing_id(identity_nodes_table_name),
                    "table_name": identity_nodes_table_name,
                },
                {
                    "table_id": Guest360DynamodbGlobaltable.to_passing_id(identity_edges_table_name),
                    "table_name": identity_edges_table_name,
                },
                {
                    "table_id": Guest360DynamodbGlobaltable.to_passing_id(profile_table_name),
                    "table_name": profile_table_name.lower(),
                },
                {
                    "table_id": Guest360DynamodbGlobaltable.to_passing_id(event_table_name),
                    "table_name": event_table_name,
                },
            ],
        )
        for table_attributes in tables_attributes:
            logger.debug(f"boto3 creating table with {table_attributes=}")
            dynamodb_tuple.client.create_table(**table_attributes)
            assert (
                dynamodb_tuple.client.describe_table(TableName=table_attributes["TableName"])["Table"]["TableName"]
                == table_attributes["TableName"]
            )

    @pytest.fixture
    def kinesis_records(self, mock_dynamodb, mock_table, mock_kinesis, mock_stream):
        stream_arn = mock_dynamodb.client.describe_table(
            TableName=f"{self.prefix.lower()}-{self.event_table_name.lower()}"
        )["Table"]["LatestStreamArn"]
        logger.debug(f"{stream_arn=}")
        logger.info(
            f"fixture:kinesis_records inserting records into table_name={self.prefix.lower()}-{self.event_table_name.lower()}"
        )
        generator = ll_event_generator.LightningLaneEventGenerator(
            event_table_name=f"{self.prefix.lower()}-{self.event_table_name.lower()}",
            dynamo_resource=mock_dynamodb.resource,
            kinesis_client=boto3.client("kinesis"),
            profile_table_name=f"{self.prefix.lower()}-{self.profile_table_name.lower()}",
            identity_table_name=f"{self.prefix.lower()}-{self.identity_table_name.lower()}",
            identity_nodes_table_name=f"{self.prefix.lower()}-{self.identity_nodes_table_name.lower()}",
            identity_edges_table_name=f"{self.prefix.lower()}-{self.identity_edges_table_name.lower()}",
            identity_notification_stream_name=f"{self.prefix.lower()}-{self.identity_notification_stream_name.lower()}",
        )

        # insert records
        raw_lls = [
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01),
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_02),
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_03),
        ]
        generator.process_records_batch(raw_lls)

        # get stream data
        dynamo_stream = mock_dynamodb.stream.describe_stream(StreamArn=stream_arn)
        shard_id = dynamo_stream["StreamDescription"]["Shards"][0]["ShardId"]

        dynamo_iter = mock_dynamodb.stream.get_shard_iterator(
            StreamArn=stream_arn,
            ShardId=shard_id,
            ShardIteratorType="TRIM_HORIZON",
        )
        iterator_id = dynamo_iter["ShardIterator"]

        resp = mock_dynamodb.stream.get_records(ShardIterator=iterator_id)
        assert len(resp["Records"]) == 3
        kinesis_records = mock_kinesis_events("DynamodbKinesis", resp["Records"])
        yield kinesis_records

    @pytest.fixture
    def firehose_event(self, kinesis_records):
        firehose_event = {
            "invocationId": str(uuid.uuid4()),
            "approximateArrivalTimestamp": datetime.datetime.now().timestamp(),
            "deliveryStreamArn": "arn:aws:blah",
            "region": "us-east-1",
            "records": [
                {
                    "recordId": str(uuid.uuid4()),
                    "approximateArrivalTimestamp": datetime.datetime.now().timestamp(),
                    "data": i["kinesis"]["data"],
                }
                for i in kinesis_records["Records"]
            ],
        }
        yield firehose_event

    def test_firehose_event(self, firehose_event):
        logger.info(f"{firehose_event=}")
        assert len(firehose_event["records"]) == 3

    def test_produce(self, firehose_event):
        from app.src.data_service.s3_producer.s3_producer import producer

        records = firehose_event["records"]
        dynamodb_event_types = ["INSERT"]
        logger.info(f"{records=}")
        logger.info(f"{dynamodb_event_types=}")
        success, fail = producer.produce(records, dynamodb_event_types)

        logger.info(f"{success=}")
        logger.info(f"{fail=}")

        assert len(success) == 3
        assert len(fail) == 0

    def test_produce_success_and_fail(self, firehose_event):
        from app.src.data_service.s3_producer.s3_producer import producer

        records = firehose_event["records"]
        records.append(
            {
                "recordId": str(uuid.uuid4()),
                "approximateArrivalTimestamp": datetime.datetime.now().timestamp(),
                "data": self.bad_kinesis_record["kinesis"]["data"],
            }
        )
        dynamodb_event_types = ["INSERT"]
        logger.info(f"{records=}")
        logger.info(f"{dynamodb_event_types=}")
        success, fail = producer.produce(records, dynamodb_event_types)

        logger.info(f"{success=}")
        logger.info(f"{fail=}")

        assert len(success) == 3
        assert len(fail) == 1

    def test_handler_success_and_fail(self, monkeypatch, firehose_event):
        from app.src.data_service.s3_producer.s3_producer import producer

        monkeypatch.setenv("dynamodb_event_types", "INSERT")
        records = firehose_event["records"]
        records.append(
            {
                "recordId": str(uuid.uuid4()),
                "approximateArrivalTimestamp": datetime.datetime.now().timestamp(),
                "data": self.bad_kinesis_record["kinesis"]["data"],
            }
        )
        event = {
            "invocationID": str(uuid.uuid4()),
            "sourceKinesisStreamArn": "kinesis_stream_arn",
            "region": "us-east-1",
            "records": records,
        }
        logger.info(f"{event=}")
        output = producer.lambda_handler(event, None)

        logger.info(f"{output=}")
        assert output.get("records") is not None
        assert len(output["records"]) == 4
