""" Pytest to test Processing Firehose """

import aws_cdk
import sys
import logging
import pytest
from aws_cdk import assertions, Duration, aws_kinesis
from app.guest360_constructs.processing.processing_firehose import (
    ProcessingFirehose,
    ProcessingFirehoseProps,
    S3Destination,
)
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.mark.timeout(30, method="signal")
def test_processing_firehose():
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("environment", "local")
    stack.node.set_context("prefix", "test-prefix-use1")
    stack.node.set_context("prefix_global", "test-prefix")
    stack.node.set_context("region", "us-east-1")

    s3_bucket = Guest360S3Bucket(stack, "firehose_bucket", region="us-east-1", props={"bucket_name": "test-bucket"})

    kinesis_source: aws_kinesis.IStream = Guest360KinesisDatastream(
        stack,
        "kinesis_stream",
        props={"retention_period": Duration.hours(24), "stream_mode": aws_kinesis.StreamMode("ON_DEMAND")},
    ).kinesis_stream

    s3_destination = S3Destination(bucket=s3_bucket)

    assert s3_destination["bucket"] == s3_bucket

    props = ProcessingFirehoseProps(destination=s3_destination, kinesis_source=kinesis_source, prefix="some/prefix")

    ProcessingFirehose(stack, "processing-firehose", props=props)

    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::KinesisFirehose::DeliveryStream", 1)
