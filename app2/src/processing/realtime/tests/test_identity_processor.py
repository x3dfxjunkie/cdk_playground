"""This module tests identity processor script"""

import json

import boto3
from moto import mock_dynamodb, mock_kinesis

from app.src.processing.realtime.module.domains.gam import identity_processor

from app.src.data_structures.object_lookup import dynamodb_datastore, lookup
from app.tools.test_data.gam_raw import GamRawEvents, GamRawScenarios
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb


@mock_dynamodb
@mock_kinesis
def test_identity_processor_add_new_guest(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_NEW_GUEST)]
    new_guest_raw = json.loads(GamRawEvents.GAM_NEW_GUEST)
    processor.process_records_batch(raw_gam_events)

    atomic_id_1 = lookup_engine.atomic_id_lookup(
        new_guest_raw["resultingGuestIdentifiers"][0]["type"], new_guest_raw["resultingGuestIdentifiers"][0]["value"]
    )
    atomic_id_2 = lookup_engine.atomic_id_lookup(
        new_guest_raw["resultingGuestIdentifiers"][1]["type"], new_guest_raw["resultingGuestIdentifiers"][1]["value"]
    )
    assert atomic_id_1 == atomic_id_2


@mock_dynamodb
@mock_kinesis
def test_identity_processor_add_new_identifier_existing_guest(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST)]
    new_identifier_existing_guest_raw = json.loads(GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST)
    processor.process_records_batch(raw_gam_events)

    atomic_id = lookup_engine.atomic_id_lookup(
        new_identifier_existing_guest_raw["resultingGuestIdentifiers"][0]["type"],
        new_identifier_existing_guest_raw["resultingGuestIdentifiers"][0]["value"],
    )
    assert atomic_id is not None
    for identifier in new_identifier_existing_guest_raw["resultingGuestIdentifiers"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id


@mock_dynamodb
def test_identity_processor_snapshot(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_SNAPSHOT)]
    gam_snapshot = json.loads(GamRawEvents.GAM_SNAPSHOT)
    processor.process_records_batch(raw_gam_events)

    atomic_id = lookup_engine.atomic_id_lookup(
        gam_snapshot["resultingGuestIdentifiers"][0]["type"], gam_snapshot["resultingGuestIdentifiers"][0]["value"]
    )
    assert atomic_id is not None
    for identifier in gam_snapshot["resultingGuestIdentifiers"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id


@mock_dynamodb
@mock_kinesis
def test_identity_processor_merge_non_swid(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_MERGE_GUESTS_NON_SWID)]
    merge_guests_non_swid = json.loads(GamRawEvents.GAM_MERGE_GUESTS_NON_SWID)
    processor.process_records_batch(raw_gam_events)

    atomic_id = lookup_engine.atomic_id_lookup(
        merge_guests_non_swid["resultingGuestIdentifiers"][0]["type"],
        merge_guests_non_swid["resultingGuestIdentifiers"][0]["value"],
    )
    assert atomic_id is not None
    # Check to make sure all identifiers link to the same atomic_id after the game merge, including the old xid
    for identifier in merge_guests_non_swid["previousGuestIdentifiers1"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id
    for identifier in merge_guests_non_swid["previousGuestIdentifiers2"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id


@mock_dynamodb
@mock_kinesis
def test_identity_processor_merge_swid(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_MERGE_GUESTS_SWID)]
    merge_guests_swid = json.loads(GamRawEvents.GAM_MERGE_GUESTS_SWID)
    processor.process_records_batch(raw_gam_events)

    atomic_id = lookup_engine.atomic_id_lookup(
        merge_guests_swid["resultingGuestIdentifiers"][0]["type"],
        merge_guests_swid["resultingGuestIdentifiers"][0]["value"],
    )
    assert atomic_id is not None
    # Check to make sure all identifiers link to the same atomic_id after the game merge, including the old xid
    for identifier in merge_guests_swid["previousGuestIdentifiers1"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id
    for identifier in merge_guests_swid["previousGuestIdentifiers2"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id


@mock_dynamodb
@mock_kinesis
def test_identity_processor_remove(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = [json.loads(GamRawEvents.GAM_REMOVE_GUEST_IDENTIFIER)]
    removed_guests = json.loads(GamRawEvents.GAM_REMOVE_GUEST_IDENTIFIER)
    processor.process_records_batch(raw_gam_events)

    atomic_id = lookup_engine.atomic_id_lookup(
        removed_guests["resultingGuestIdentifiers"][0]["type"], removed_guests["resultingGuestIdentifiers"][0]["value"]
    )
    assert atomic_id is not None
    # Check to make sure all identifiers link to the same atomic_id after the game merge, including the old xid
    for identifier in removed_guests["resultingGuestIdentifiers"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert atomic_id == result_atomic_id
    for identifier in removed_guests["removedGuestIdentifiers"]:
        result_atomic_id = lookup_engine.atomic_id_lookup(identifier["type"], identifier["value"])
        assert result_atomic_id is None


@mock_dynamodb
@mock_kinesis
def test_identity_processor_two_atomic_ids(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = GamRawScenarios.two_different_guests_add_events()

    processor.process_records_batch(raw_gam_events)

    first_record = raw_gam_events[0]
    second_record = raw_gam_events[1]
    first_atomic_id = lookup_engine.atomic_id_lookup(
        first_record["resultingGuestIdentifiers"][0]["type"], first_record["resultingGuestIdentifiers"][0]["value"]
    )
    second_atomic_id = lookup_engine.atomic_id_lookup(
        second_record["resultingGuestIdentifiers"][0]["type"], second_record["resultingGuestIdentifiers"][0]["value"]
    )

    assert first_atomic_id is not None
    assert second_atomic_id is not None
    assert first_atomic_id != second_atomic_id


@mock_dynamodb
@mock_kinesis
def test_identity_processor_two_atomic_ids_then_merged(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = GamRawScenarios.two_different_guests_add_events_and_merge()

    processor.process_records_batch(raw_gam_events[:2])

    first_record = raw_gam_events[0]
    second_record = raw_gam_events[1]
    first_atomic_id = lookup_engine.atomic_id_lookup(
        first_record["resultingGuestIdentifiers"][0]["type"], first_record["resultingGuestIdentifiers"][0]["value"]
    )
    second_atomic_id = lookup_engine.atomic_id_lookup(
        second_record["resultingGuestIdentifiers"][0]["type"], second_record["resultingGuestIdentifiers"][0]["value"]
    )

    assert first_atomic_id is not None
    assert second_atomic_id is not None
    assert first_atomic_id != second_atomic_id

    processor.process_records_batch(raw_gam_events[-1:])
    first_atomic_id = lookup_engine.atomic_id_lookup(
        first_record["resultingGuestIdentifiers"][0]["type"], first_record["resultingGuestIdentifiers"][0]["value"]
    )
    second_atomic_id = lookup_engine.atomic_id_lookup(
        second_record["resultingGuestIdentifiers"][0]["type"], second_record["resultingGuestIdentifiers"][0]["value"]
    )
    assert first_atomic_id is not None
    assert second_atomic_id is not None
    assert first_atomic_id == second_atomic_id


@mock_dynamodb
@mock_kinesis
def test_identity_processor_two_atomic_ids_then_merged_then_deleted(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    lookup_engine, processor = setup_tests(monkeypatch)

    raw_gam_events = GamRawScenarios.two_different_guests_add_events_and_merge_then_removed()

    processor.process_records_batch(raw_gam_events[:2])

    first_record = raw_gam_events[0]
    second_record = raw_gam_events[1]
    first_atomic_id = lookup_engine.atomic_id_lookup(
        first_record["resultingGuestIdentifiers"][0]["type"], first_record["resultingGuestIdentifiers"][0]["value"]
    )
    second_atomic_id = lookup_engine.atomic_id_lookup(
        second_record["resultingGuestIdentifiers"][0]["type"], second_record["resultingGuestIdentifiers"][0]["value"]
    )

    assert first_atomic_id is not None
    assert second_atomic_id is not None
    assert first_atomic_id != second_atomic_id

    processor.process_records_batch([raw_gam_events[2]])
    first_atomic_id = lookup_engine.atomic_id_lookup(
        first_record["resultingGuestIdentifiers"][0]["type"], first_record["resultingGuestIdentifiers"][0]["value"]
    )
    second_atomic_id = lookup_engine.atomic_id_lookup(
        second_record["resultingGuestIdentifiers"][0]["type"], second_record["resultingGuestIdentifiers"][0]["value"]
    )
    assert first_atomic_id is not None
    assert second_atomic_id is not None
    assert first_atomic_id == second_atomic_id

    processor.process_records_batch([raw_gam_events[3]])
    first_atomic_id = lookup_engine.atomic_id_lookup("swid", "swid_1")
    second_atomic_id = lookup_engine.atomic_id_lookup("swid", "swid_2")
    assert first_atomic_id is not None
    assert second_atomic_id is None
    assert first_atomic_id != second_atomic_id


@mock_dynamodb
@mock_kinesis
def setup_tests(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    event_table_name = "guest360-ea-test"
    identity_table_name = "identity"
    identity_nodes_table_name = "identity_nodes"
    identity_edges_table_name = "identity_edges"
    profile_table_name = "profile_lookup"
    identity_notification_stream_name = "identity_notification"
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
    processor = identity_processor.IdentityProcessor(
        dynamo_resource=dynamodb_resource,
        kinesis_client=kinesis_client,
        profile_table_name=profile_table_name,
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        event_table_name=event_table_name,
        identity_notification_stream_name=identity_notification_stream_name,
    )

    return lookup_engine, processor
