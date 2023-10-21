""" Pytest to test Source Lightning Lane """

import aws_cdk
import sys
import os
import logging
import pytest
from typing import cast
from pathlib import Path
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import aws_kinesis, aws_dynamodb, Duration, assertions
from app.guest360_constructs.processing.dynamodb_kinesis import DynamodbKinesisConstruct

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def lambda_assets():
    zip_files = []
    stack_path = str(Path(os.getcwd()).parents[0])
    base_dir = Path(f"{stack_path}/bazel-bin/app/src/data_service/msk_producer/")

    if not os.path.exists(base_dir):
        base_dir.mkdir(parents=True, exist_ok=True)

    empty_zip_data = b"PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    lambda_file = f"{base_dir}/lambda_archive.zip"
    with open(lambda_file, "wb") as zip_file:
        zip_file.write(empty_zip_data)
        zip_files.append(zip_file)

    yield zip_files


@pytest.mark.timeout(30, method="signal")
def test_dynamodb_kinesis(lambda_assets):
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("environment", "local")
    stack.node.set_context("prefix", "test-prefix-source-use1")
    stack.node.set_context("prefix_global", "test-prefix-global")
    stack.node.set_context("region", "us-east-1")

    DynamodbKinesisConstruct(
        stack,
        "test_hello",
        stream_name="test_dynamodb_stream_name",
        days_retention=15,
        environment_config={
            "region": "local",
            "networking": {
                "local": {
                    "short_region": "use1",
                    "vpc": {"id": "vpc-771156a5", "cidr": "0.0.0.0/8"},
                    "subnets": {
                        "private": [
                            {"id": "subnet-e0e7bc90", "cidr": "0.0.0.0/8"},
                        ],
                        "non-routable": [
                            {"id": "subnet-e0e7bc90", "cidr": "0.0.0.0/16"},
                        ],
                    },
                    "endpoints": [{"id": "vpce-08900cd41ebaa4322", "service_name": "events", "type": "Interface"}],
                },
            },
        },
    )  # environment_config["networking"][region_name]["subnets"]["non-routable"]

    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::DynamoDB::Table", 2)
    template.resource_count_is("AWS::Lambda::Function", 1)
