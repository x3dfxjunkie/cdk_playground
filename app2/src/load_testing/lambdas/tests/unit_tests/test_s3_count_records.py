"""
units for S3Consumer
"""
import os
from datetime import datetime

import boto3
from app.src.load_testing.lambdas.evaluator_system_test.s3_consumer import S3Consumer
from moto import mock_s3


@mock_s3
def test_count_objects():
    prefix = "some-prefix"
    bucket_name = "some-test-bucket"
    start_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    object_key = "some-prefix/" + datetime.utcnow().strftime("%Y/%m/%d/%H/") + "test_file.json.gz"

    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket=bucket_name)
    _ = s3_client.upload_file(
        f"{os.path.dirname(os.path.realpath(__file__))}/test_file.json.gz", bucket_name, object_key
    )

    checker = S3Consumer(bucket_name, prefix + "/", start_time, "CountOfObjects")
    assert checker.validate_parameter() == 1


@mock_s3
def test_count_records():
    prefix = "some-prefix"
    bucket_name = "some-test-bucket"
    start_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    object_key = "some-prefix/" + datetime.utcnow().strftime("%Y/%m/%d/%H/") + "test_file.json.gz"

    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket=bucket_name)
    _ = s3_client.upload_file(
        f"{os.path.dirname(os.path.realpath(__file__))}/test_file.json.gz", bucket_name, object_key
    )

    checker = S3Consumer(bucket_name, prefix + "/", start_time, "CountOfRecords", "hello")
    assert checker.validate_parameter() == 1000
