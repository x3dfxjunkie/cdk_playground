import logging
import os
import sys
import json

import boto3
import pytest
from moto import mock_sts, mock_sns, mock_s3

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

# create a stdout logger
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class TestUntaggedBucketFinder:
    @pytest.fixture
    def mock_os_environment(self, monkeypatch):
        """
        Monkeypatch all environment variables necessary w/out affecting OS environment
        """
        monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
        monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
        monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
        monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
        monkeypatch.setenv("AWS_REGION", "us-east-1")
        monkeypatch.setenv("TOPIC_NAME", "test_topic")

    @mock_sts
    @mock_sns
    @mock_s3
    def test_lambda(self, mock_os_environment):
        # Mock SNS setup - create topic
        sns = boto3.client("sns", region_name=os.environ["AWS_REGION"])
        topic = sns.create_topic(Name=os.environ["TOPIC_NAME"])
        topic_arn = topic.get("TopicArn")
        os.environ["SNS_TOPIC_ARN"] = topic_arn

        # Mock S3 setup
        s3 = boto3.client("s3")

        # Create a tagged bucket
        tagged_bucket_name = "tagged-bucket"
        s3.create_bucket(Bucket=tagged_bucket_name)
        s3.put_bucket_tagging(Bucket=tagged_bucket_name, Tagging={"TagSet": [{"Key": "TestTagKey", "Value": "TestTagVal"}]})
        # Create an untagged bucket
        untagged_bucket_name = "untagged-bucket"
        s3.create_bucket(Bucket=untagged_bucket_name)

        # must include package here due to global boto resource declarations
        from app.src.reliability.UntaggedBucketFinder.lambda_function import lambda_function

        response = lambda_function.lambda_handler({"test": "event"}, context=None)
        logger.info(response)
        response = json.loads(response)
        assert response["UNTAGGED_BUCKET_COUNT"] == 1
        assert response["UNTAGGED_BUCKETS"][0]["Name"] == untagged_bucket_name
