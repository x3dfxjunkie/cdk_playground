#!/usr/bin/env python
# -*- coding: utf-8 -*-

from botocore.exceptions import ClientError
from boto3 import client, resource
from moto import mock_kinesis, mock_s3
from pytest import raises

from app.guest360_docker.ingestion.google_pubsub.runner import put_record_into_kinesis, write_stream_to_s3


@mock_kinesis
def test_put_record():
    conn = client("kinesis", region_name="us-west-2")
    stream_name = "my_stream"
    data = b"0303456"
    conn.create_stream(StreamName=stream_name, ShardCount=1)

    stream = conn.describe_stream(StreamName=stream_name)["StreamDescription"]
    shard_id = stream["Shards"][0]["ShardId"]

    put_record_into_kinesis(data, conn, kinesis_stream=stream_name)

    resp = conn.get_shard_iterator(StreamName=stream_name, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")
    shard_iterator = resp["ShardIterator"]

    resp = conn.get_records(ShardIterator=shard_iterator)
    assert len(resp["Records"]) == 1
    record = resp["Records"][0]

    assert record["Data"] == data
    assert record["SequenceNumber"] == "1"


@mock_s3
def test_write_stream():
    data = b"0303456"
    failed_msg_bucket_path = "/path/no/exist"
    failed_msg_bucket_name = "failed_buckets"

    with raises(ClientError) as e:
        write_stream_to_s3(
            data, failed_msg_bucket_name=failed_msg_bucket_name, failed_msg_bucket_path=failed_msg_bucket_path
        )
    assert "NoSuchBucket" in str(e)

    s3_resource = resource("s3")
    s3_resource.create_bucket(Bucket=failed_msg_bucket_name)
    write_stream_to_s3(
        data, failed_msg_bucket_name=failed_msg_bucket_name, failed_msg_bucket_path=failed_msg_bucket_path
    )

    buckets = [bucket.name for bucket in s3_resource.buckets.all()]
    assert failed_msg_bucket_name in buckets

    obj = [elem.key for elem in s3_resource.Bucket(failed_msg_bucket_name).objects.all()]
    content = [elem.get()["Body"].read() for elem in s3_resource.Bucket(failed_msg_bucket_name).objects.all()]

    assert len(obj) == 1
    assert failed_msg_bucket_path in str(obj)
    assert data == content.pop()
