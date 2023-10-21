"""Tests lightning lane events"""
import boto3
import datetime as dt
from moto import mock_dynamodb, mock_kinesis

from app.src.data_structures.object_lookup import dynamodb_datastore, lookup
import app.src.processing.realtime.module.domains.lightning_lane.event_generator as ll_event_generator
from app.src.data_structures.events.lightning_lane_event import LightningLaneEvent
from app.tools.test_data.lightning_lane_raw_events import LightningLaneScenarios
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator(monkeypatch):
    dynamodb_resource, lookup_engine, generator, event_table_name = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.all_ll_events()
    generator.process_records_batch(raw_lls)

    event_01_atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")
    event_03_atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADBAFXT3DUKPPBVYMYNGW5E")

    table = dynamodb_resource.Table(event_table_name)
    response = table.get_item(
        Key={"atomic_id#event_name": event_01_atomic_id + "#lightning_lane", "event_time": 1665577707199}
    )
    event_01 = response["Item"]["event"]

    response = table.get_item(
        Key={"atomic_id#event_name": event_03_atomic_id + "#lightning_lane", "event_time": 1666518564625}
    )
    event_03 = response["Item"]["event"]
    ll_event_01 = LightningLaneEvent.schema().loads(event_01)
    ll_event_03 = LightningLaneEvent.schema().loads(event_03)

    assert ll_event_01.atomic_id == event_01_atomic_id
    assert ll_event_01.experience.experience_id == "353305"
    assert ll_event_01.experience.location_id == "353305"

    assert ll_event_03.experience.experience_id == "19193461"
    assert ll_event_03.experience.location_id == "19193461"

    assert ll_event_01.event_status == "BOOKED"
    assert ll_event_01.curated_status == "Booked"
    assert ll_event_01.curated_confidence_score == 100
    assert ll_event_01.curated_confidence_label == "High"


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator_curated_status_not_experienced(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_cancelled()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )
    event_01 = events[0]

    assert event_01.curated_status == "Not Experienced"
    assert event_01.curated_confidence_score == 100
    assert event_01.curated_confidence_label == "High"


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator_curated_status_experienced(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_redeemed()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )
    event_01 = events[0]

    assert event_01.curated_status == "Experienced"
    assert event_01.curated_confidence_score == 90
    assert event_01.curated_confidence_label == "High"


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator_curated_status_invalid(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_bad()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )
    event_01 = events[0]

    assert event_01.curated_status == "Invalid"
    assert event_01.curated_confidence_score == 0
    assert event_01.curated_confidence_label == "Zero"


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator_no_status_change(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_no_status_change()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )

    assert len(events) == 1


@mock_dynamodb
@mock_kinesis
def test_lighting_lane_event_generator_noninventory_redemptions(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_noninventory_redemptions()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )

    assert len(events) == 2


@mock_dynamodb
@mock_kinesis
def test_lightning_lane_event_generator_50_different_events_same_status(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_bulk_different_event_ids(50)
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )

    assert len(events) == 50


@mock_dynamodb
@mock_kinesis
def test_lightning_lane_event_generator_150_events_100_limit_enforced(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_bulk_different_event_ids(150)
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    events = lookup_engine.get_events_from_profile(
        atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30)
    )

    assert len(events) == 100


@mock_dynamodb
@mock_kinesis
def test_update_profile_rode_one_ride(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_redeemed()
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    lookup_engine.get_events_from_profile(atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30))

    profile = lookup_engine.profile_lookup(atomic_id)

    assert profile.attraction_ride_histories[0].attraction_ride_count == 1
    assert profile.attraction_ride_histories[0].attraction_name == "Casey Jr. Circus Train"


@mock_dynamodb
@mock_kinesis
def test_update_profile_redeemed_none_booked_two(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_bulk_different_event_ids(2)
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    profile = lookup_engine.profile_lookup(atomic_id)

    assert profile.attraction_ride_histories[0].attraction_ride_count == 0


@mock_dynamodb
@mock_kinesis
def test_update_profile_redeemed_two_booked_two(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_bulk_different_event_ids(
        2
    ) + LightningLaneScenarios.ll_events_bulk_different_event_ids(2, ll_status="REDEEMED")
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    profile = lookup_engine.profile_lookup(atomic_id)

    assert profile.attraction_ride_histories[0].attraction_ride_count == 2
    assert profile.attraction_ride_histories[0].attraction_name == "Casey Jr. Circus Train"


@mock_dynamodb
@mock_kinesis
def test_update_profile_two_redeemed_duplicated_rode_once(monkeypatch):
    _, lookup_engine, generator, *_ = setup_aws(monkeypatch)
    raw_lls = LightningLaneScenarios.ll_events_no_status_change(status="REDEEMED")
    generator.process_records_batch(raw_lls)

    atomic_id = lookup_engine.atomic_id_lookup("ealinkid", "AAAADA6M4LV52JPUBGU33JT77A")

    profile = lookup_engine.profile_lookup(atomic_id)

    assert profile.attraction_ride_histories[0].attraction_ride_count == 1
    assert profile.attraction_ride_histories[0].attraction_name == "Casey Jr. Circus Train"


@mock_dynamodb
@mock_kinesis
def setup_aws(monkeypatch):
    event_table_name = "guest360-ea-test"
    identity_table_name = "identity"
    identity_nodes_table_name = "identity_nodes"
    identity_edges_table_name = "identity_edges"
    profile_table_name = "profile_lookup"
    identity_notification_stream_name = "identity_notification"
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
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
    generator = ll_event_generator.LightningLaneEventGenerator(
        dynamo_resource=dynamodb_resource,
        kinesis_client=kinesis_client,
        profile_table_name=profile_table_name,
        identity_table_name=identity_table_name,
        identity_nodes_table_name=identity_nodes_table_name,
        identity_edges_table_name=identity_edges_table_name,
        event_table_name=event_table_name,
        identity_notification_stream_name=identity_notification_stream_name,
    )

    return dynamodb_resource, lookup_engine, generator, event_table_name
