"""testing processing lambda"""
import base64

import boto3
from moto import mock_dynamodb, mock_kinesis

from app.src.data_structures.object_lookup import dynamodb_datastore, lookup
from app.src.processing.realtime import processing_lambda
from app.tools.test_data.lightning_lane_raw_events import LightningLaneRawEvents
from app.tools.test_data.gam_raw import GamRawEvents
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb


@mock_dynamodb
@mock_kinesis
def test_processing_lambda(monkeypatch):
    event_table_name = "guest360-ea-test"
    gam_table_name = "gam"
    identity_table_name = "identity"
    identity_nodes_table_name = "identity_nodes"
    identity_edges_table_name = "identity_edges"
    profile_table_name = "profile_lookup"
    identity_notification_stream_name = "identity_notification"
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch.setenv("EXPERIENCE_EVENT_TABLE_NAME", event_table_name)
    monkeypatch.setenv("PROFILE_TABLENAME", profile_table_name)
    monkeypatch.setenv("IDENTITY_TABLE_NAME", identity_table_name)
    monkeypatch.setenv("IDENTITY_NODES_TABLE_NAME", identity_nodes_table_name)
    monkeypatch.setenv("IDENTITY_EDGES_TABLE_NAME", identity_edges_table_name)
    monkeypatch.setenv("IDENTITY_NOTIFICATION_STREAM_NAME", identity_notification_stream_name)
    setup_dynamodb(
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        event_table_name=event_table_name,
        profile_table_name=profile_table_name,
        identity_notification_stream=identity_notification_stream_name,
    )
    dynamodb_resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    datastore = dynamodb_datastore.DynamoDBDatastore(
        dynamodb_resource=dynamodb_resource,
        kinesis_client=kinesis_client,
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        events_table_name=event_table_name,
        profile_table_name=profile_table_name,
        identity_notification_stream_name=identity_notification_stream_name,
    )
    lookup_engine = lookup.Lookup(datastore)
    processing_lambda.handler(
        {
            "Records": [
                record_mock(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01, event_table_name),
                record_mock(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_02, event_table_name),
                record_mock(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_03, event_table_name),
            ]
        },
        None,
    )
    processing_lambda.handler(
        {
            "Records": [
                record_mock(GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST, gam_table_name),
                record_mock(GamRawEvents.GAM_REMOVE_GUEST_IDENTIFIER, gam_table_name),
                record_mock(GamRawEvents.GAM_NEW_GUEST, gam_table_name),
                record_mock(GamRawEvents.GAM_MERGE_GUESTS_NON_SWID, gam_table_name),
                record_mock(GamRawEvents.GAM_MERGE_GUESTS_SWID, gam_table_name),
                record_mock(GamRawEvents.GAM_SNAPSHOT, gam_table_name),
            ]
        },
        None,
    )

    dynamodb_table_description = boto3.client("dynamodb").describe_table(TableName=identity_table_name)

    atomic_id_1 = lookup_engine.atomic_id_lookup("admission-link-id", "07100927241300268")
    atomic_id_2 = lookup_engine.atomic_id_lookup("transactional-guest-id", "236728560")
    atomic_id_3 = lookup_engine.atomic_id_lookup("cast-link-id", "38055")
    assert dynamodb_table_description["Table"]["ItemCount"] == 10
    assert atomic_id_1 is None
    assert atomic_id_2 is not None
    assert atomic_id_2 == atomic_id_3


def record_mock(data: str, event_table_name: str):
    """
    Returns a mock record for the processing lambda
    It doesn't exhaustively constructs the object (it only builds the attributes that are being used by the processing functions)
    """
    event_source_arn = f"arn:aws:kinesis:us-east-1:000000000000:stream/{event_table_name}"

    return {
        "eventSourceARN": event_source_arn,
        "kinesis": {"data": base64.b64encode(data.encode("utf-8")).decode("utf-8")},
    }
