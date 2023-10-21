from moto import mock_kinesis
from app.src.bootcamp.kinesis_data_generator import send_batch
import boto3


@mock_kinesis
def test_send_batch():
    stream_name = "test-stream"

    client = boto3.client("kinesis", region_name="us-east-1")
    client.create_stream(StreamName=stream_name, ShardCount=1)

    stream = client.describe_stream(StreamName=stream_name)["StreamDescription"]

    shard_id = stream["Shards"][0]["ShardId"]

    send_batch("test-stream", client)

    resp = client.get_shard_iterator(StreamName=stream_name, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")
    shard_iterator = resp["ShardIterator"]

    resp = client.get_records(ShardIterator=shard_iterator)
    assert len(resp["Records"]) == 5000
