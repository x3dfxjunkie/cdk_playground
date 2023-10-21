""" Pytest to test Processing Firehose """

import aws_cdk
import sys
import logging
from pathlib import Path
import pytest
from aws_cdk import assertions, Duration, aws_kinesis
from app.guest360_constructs.processing.analytics_datalake import AnalyticsDatalake, AnalyticsDatalakeProps, Target
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
import os

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.mark.timeout(30, method="signal")
def test_analytics_datalake():
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("environment", "local")
    stack.node.set_context("prefix", "test-prefix-use1")
    stack.node.set_context("prefix_global", "test-prefix")
    stack.node.set_context("region", "us-east-1")

    kinesis_source: aws_kinesis.IStream = Guest360KinesisDatastream(
        stack,
        "kinesis_stream",
        props={"retention_period": Duration.hours(24), "stream_mode": aws_kinesis.StreamMode("ON_DEMAND")},
    ).kinesis_stream

    kinesis_source_2: aws_kinesis.IStream = Guest360KinesisDatastream(
        stack,
        "second_kinesis_stream",
        props={"retention_period": Duration.hours(24), "stream_mode": aws_kinesis.StreamMode("ON_DEMAND")},
    ).kinesis_stream

    analytics_datalake_target: Target = Target(stream=kinesis_source, partitioning="test/")

    analytics_datalake_target_2: Target = Target(stream=kinesis_source_2, partitioning="test/")

    props = AnalyticsDatalakeProps(targets=[analytics_datalake_target])

    stack_path = str(Path(os.getcwd()).parents[0])

    lambda_path = f"{stack_path}/bazel-bin/app/src/processing/firehose_transformer/"
    lambda_file = f"{lambda_path}lambda_archive.zip"

    if not os.path.exists(lambda_path):
        os.makedirs(lambda_path)

    empty_zip_data = b"PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    with open(lambda_file, "wb") as zip_file:
        zip_file.write(empty_zip_data)

    analytics_datalake = AnalyticsDatalake(stack, "analytics_datalake", props=props)

    analytics_datalake.add_target(analytics_datalake_target_2)

    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::KinesisFirehose::DeliveryStream", 2)
