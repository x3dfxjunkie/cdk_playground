"""
unit test Target kinesis    
"""
import sys

# mock locust
from mock import MagicMock

mock_locust = MagicMock()
sys.modules["locust"] = mock_locust
# pylint: disable=C0413
import logging
import random
from unittest.mock import patch

import boto3
import pytest
from moto import mock_kinesis

from app.src.load_testing.app.targets.kinesis_stream_target import KinesisStreamTarget

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


@pytest.fixture
def mock_event_hook():
    with patch("app.src.load_testing.app.event_hook.guest360_event_hook.Guest360EventHook") as evnt:
        yield evnt


# pylint: disable=W0621,W0613
@mock_kinesis
def test_kinesis_write(mock_event_hook) -> None:
    logger.info("Testing KinesisStreamTarget")

    stream_name = "kinesis-load-test-target-stream"
    num_shards = 2
    max_records = 100

    client = boto3.client("kinesis", region_name="us-east-1")
    client.create_stream(StreamName=stream_name, ShardCount=num_shards)
    response = client.describe_stream(StreamName=stream_name)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    logger.info("Done creating test Kinesis DataStream")

    # write random data to the stream
    target = KinesisStreamTarget(stream_name)
    for _ in range(max_records):
        target.send_data({"message": f"{random.randint(0,100)} is a random value"})
    logger.info("Done writing test Kinesis DataStream")

    # Test to read all the records from kinesis
    response = client.describe_stream(StreamName=stream_name)

    def get_shard_iterator(shard_id):
        response = client.get_shard_iterator(StreamName=stream_name, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")
        return response["ShardIterator"]

    shard_ids = [shard["ShardId"] for shard in response["StreamDescription"]["Shards"]]
    shard_iterators = [get_shard_iterator(shard_id) for shard_id in shard_ids]

    record_count = 0
    for shard_iterator in shard_iterators:
        response = client.get_records(ShardIterator=shard_iterator, Limit=max_records)
        records = response["Records"]
        record_count += len(records)

    logger.info("Done reading from test Kinesis DataStream")
    assert record_count == max_records
