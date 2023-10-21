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
from app.guest360_constructs.processing.source_lightning_lane import SourceLightningLane
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.identity.identity_graph import IdentityGraph
from app.guest360_constructs.identity.keyring_table import KeyringTable

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def lambda_assets():
    zip_files = []
    stack_path = str(Path(os.getcwd()).parents[0])
    base_dir = Path(f"{stack_path}/bazel-bin/app/src/processing/realtime/")

    if not os.path.exists(base_dir):
        base_dir.mkdir(parents=True, exist_ok=True)

    empty_zip_data = b"PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    lambda_file = f"{base_dir}/processing_realtime_lambda.zip"
    with open(lambda_file, "wb") as zip_file:
        zip_file.write(empty_zip_data)
        zip_files.append(zip_file)

    yield zip_files


@pytest.mark.timeout(30, method="signal")
def test_source_lightning_lane(lambda_assets):
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("environment", "local")
    stack.node.set_context("prefix", "test-prefix-source-use1")
    stack.node.set_context("prefix_global", "test-prefix-global")
    stack.node.set_context("region", "us-east-1")

    kinesis_source: aws_kinesis.IStream = Guest360KinesisDatastream(
        stack,
        "test_kinesis_stream",
        props={"retention_period": Duration.hours(24), "stream_mode": aws_kinesis.StreamMode("ON_DEMAND")},
    ).kinesis_stream

    curated_experience_events_table = Guest360DynamodbGlobaltable(
        stack,  # type:ignore
        construct_id="test_curated_experience_events_table",
        table_name="test_curated_experience_events_table",
        partition_key=aws_dynamodb.Attribute(name="atomic_id#event_name", type=aws_dynamodb.AttributeType.STRING),
        sort_key=aws_dynamodb.Attribute(name="event_time", type=aws_dynamodb.AttributeType.NUMBER),
    )

    identity_graph = IdentityGraph.from_ssm(cast(Construct360, stack), "identity_graph", "test_identity_stack_name")
    identity_nodes_table = identity_graph.node_global_table
    identity_edges_table = identity_graph.edge_global_table
    keyring_table = KeyringTable.from_ssm(cast(Construct360, stack), "keyring_table", "test_identity_stack_name")

    SourceLightningLane(
        stack,
        "test-source-lightning-lane-processor",  # type:ignore
        lightning_lane_source_stream=kinesis_source,  # type:ignore
        profile_table=curated_experience_events_table,
        curated_events_table=curated_experience_events_table,
        identity_table=keyring_table.global_table,
        identity_nodes_table=identity_nodes_table,
        identity_edges_table=identity_edges_table,
        environment_config={"env"},
    )

    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::Lambda::Function", 2)
