"""
tests for lookup module
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=W0621
import datetime as dt
import logging
import sys
import time

import boto3
import pytest
from app.src.data_structures.events import attraction_ridden_event
from app.src.data_structures.events import lightning_lane_event as ll_event
from app.src.data_structures.object_lookup import dynamodb_datastore, lookup, memory_datastore
from app.src.data_structures.profiles import profile
from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb
from moto import mock_dynamodb, mock_kinesis

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture(scope="module")
def datastore():
    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    yield dynamodb_datastore.DynamoDBDatastore(
        resource,
        kinesis_client,
        identity_table_name="identity",
        identity_nodes_table_name="identity_nodes",
        identity_edges_table_name="identity_edges",
        profile_table_name="profile",
        events_table_name="events",
    )


def test_profile_lookup_from_atomic_id_exists(lookup_engine):
    test_profile = lookup_engine.profile_lookup("12345")
    assert test_profile.atomic_id == "12345"


def test_profile_not_exists(lookup_engine):
    test_profile = lookup_engine.profile_lookup("67890")
    assert test_profile is None


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_does_not_exist():
    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    with pytest.raises(boto3.client("dynamodb").exceptions.ResourceNotFoundException):
        datastore = dynamodb_datastore.DynamoDBDatastore(
            resource,
            kinesis_client,
            identity_table_name="identity",
            identity_nodes_table_name="identity_nodes",
            identity_edges_table_name="identity_edges",
            profile_table_name="profile",
            events_table_name="events",
        )
        my_lookup_engine = lookup.Lookup(datastore)
        my_lookup_engine.profile_lookup("12345")


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_exists():
    resource = boto3.resource("dynamodb")
    kinesis_client = boto3.client("kinesis")
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )
    dynamodb_datastore.DynamoDBDatastore(
        resource,
        kinesis_client,
        identity_table_name="identity",
        identity_nodes_table_name="identity_nodes",
        identity_edges_table_name="identity_edges",
        profile_table_name="profile",
        events_table_name="events",
    )


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_get_profile(datastore):
    setup_dynamodb("identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream")

    my_lookup_engine = lookup.Lookup(datastore)
    create_profile()
    test_profile = build_test_profile()
    dynamo_profile = my_lookup_engine.profile_lookup("12345")
    assert dynamo_profile == test_profile


@mock_kinesis
@mock_dynamodb
def test_dynamodb_table_get_profile_not_exists(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_profile()

    my_lookup_engine = lookup.Lookup(datastore)
    dynamo_profile = my_lookup_engine.profile_lookup("67890")
    assert dynamo_profile is None


@mock_dynamodb
@mock_kinesis
def test_get_events_from_profile_single_event(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_test_event()
    events = my_lookup_engine.get_events_from_profile("12345", dt.datetime(1970, 1, 1, 0, 0), dt.datetime.now())
    assert len(events) == 1
    event = events[0]
    assert event.atomic_id == "12345"


@mock_kinesis
@mock_dynamodb
def test_get_events_from_profile_no_events(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_test_event()
    events = my_lookup_engine.get_events_from_profile(
        "12345", dt.datetime(1970, 1, 1, 0, 0), dt.datetime(1970, 1, 1, 0, 30)
    )
    assert len(events) == 0


@mock_kinesis
@mock_dynamodb
def test_get_events_from_profile_two_events_return_one(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_test_event(dt.datetime(1970, 1, 1, 0, 10))
    create_test_event(dt.datetime(1970, 1, 1, 0, 20))
    events = my_lookup_engine.get_events_from_profile(
        "12345", dt.datetime(1970, 1, 1, 0, 15), dt.datetime(1970, 1, 1, 0, 30)
    )
    assert len(events) == 1


@mock_kinesis
@mock_dynamodb
def test_get_events_from_profile_two_identitcal_events_return_one(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_test_event(dt.datetime(1970, 1, 1, 0, 20))
    create_test_event(dt.datetime(1970, 1, 1, 0, 20))
    events = my_lookup_engine.get_events_from_profile(
        "12345", dt.datetime(1970, 1, 1, 0, 15), dt.datetime(1970, 1, 1, 0, 30)
    )
    assert len(events) == 1


@mock_kinesis
@mock_dynamodb
def test_get_events_from_profile_two_events_return_two(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    create_test_event(dt.datetime(1970, 1, 1, 0, 11))
    create_test_event(dt.datetime(1970, 1, 1, 0, 20))
    events = my_lookup_engine.get_events_from_profile(
        "12345", dt.datetime(1970, 1, 1, 0, 10), dt.datetime(1970, 1, 1, 0, 30)
    )
    newest_event = events[0]
    oldest_event = events[1]
    assert len(events) == 2
    assert newest_event.event_time > oldest_event.event_time


def test_atomic_id_lookup_from_swid_exists(lookup_engine):
    assert lookup_engine.atomic_id_lookup("swid", "{abcde}") == "12345"


def test_atomic_id_lookup_from_swid_not_exists(lookup_engine):
    assert lookup_engine.atomic_id_lookup("swid", "{fghij}") is None


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_get_atomic_id(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    assert my_lookup_engine.atomic_id_lookup("swid", "{abcde}") == "12345"


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_get_atomic_id_no_swid(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    assert my_lookup_engine.atomic_id_lookup("swid", "{fghij}") is None


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_get_or_create_atomic_id(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    assert my_lookup_engine.atomic_id_lookup("swid", "{fghij}") is None
    atomic_id = my_lookup_engine.fetch_or_create_atomic_id("swid", "{fghij}")
    assert atomic_id is not None


@mock_dynamodb
@mock_kinesis
def test_dynamodb_table_get_or_create_atomic_id_same_atomic_id_multiple_calls(datastore):
    setup_dynamodb(
        "identity", "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    my_lookup_engine = lookup.Lookup(datastore)
    first_atomic_id = my_lookup_engine.fetch_or_create_atomic_id("swid", "{fghij}")
    second_atomic_id = my_lookup_engine.fetch_or_create_atomic_id("swid", "{fghij}")
    assert first_atomic_id == second_atomic_id


@pytest.fixture
def lookup_engine():
    memory_store = memory_datastore.MemoryDatastore()
    test_profile_json = build_test_profile().to_json()
    memory_store.add_keyvalue("12345", test_profile_json)
    memory_store.add_keyvalue("swid#{abcde}", "12345")
    my_lookup_engine = lookup.Lookup(memory_store)
    return my_lookup_engine


def create_profile():
    table = boto3.resource("dynamodb").Table("profile")
    test_profile_json = build_test_profile().to_json()
    table.put_item(Item={"atomic_id": "12345", "profile": test_profile_json})


def build_test_profile() -> profile.Profile:
    fun_mountain_ride_history = attraction_ridden_event.AttractionRideHistory("abc123", "Fun Mountain", 150)
    unfun_mountain_ride_history = attraction_ridden_event.AttractionRideHistory("def456", "Unfun Mountain", 600)
    test_profile = profile.Profile(
        "12345",
        ["123", "456"],
        [fun_mountain_ride_history, unfun_mountain_ride_history],
    )

    return test_profile


def create_test_event(event_time=None):
    table = boto3.resource("dynamodb").Table("events")

    if event_time is None:
        test_event = build_test_event("2022-01-01T00:00:00.0")
        event_time_key = int(
            time.mktime(dt.datetime.strptime("2022-01-01T00:00:00.0", "%Y-%m-%dT%H:%M:%S.%f").timetuple()) * 1000
        )
    else:
        event_time_key = int(time.mktime(event_time.timetuple()) * 1000)
        test_event = build_test_event(event_time.strftime("%Y-%m-%dT%H:%M:%S.%f"))
    test_event_json = test_event.to_json()
    table.put_item(
        Item={"atomic_id#event_name": "12345#lightning_lane", "event_time": event_time_key, "event": test_event_json}
    )


def build_test_event(event_time) -> ll_event.LightningLaneEvent:
    created_time = dt.datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%S.%f")
    business_date = dt.datetime.strptime("2022-01-01", "%Y-%m-%d")
    experience_start = dt.datetime.strptime("2022-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
    experience_end = dt.datetime.strptime("2022-01-01T01:00:00", "%Y-%m-%dT%H:%M:%S")
    facility = ll_event.Facility("Facility Id N/A", "Facility Name N/A")
    location_hierarchy = ll_event.LocationHierarchy(facility, facility, facility, facility, facility)

    guest_id = "abcde"
    event_status = "BOOKED"
    event_type = "NONINVENTORY"
    experience = ll_event.Experience(
        "experience_id_value",
        "Experience Category N/A",
        "Experience Name N/A",
        "location_id_value",
        "Location Name N/A",
        location_hierarchy=location_hierarchy,
    )
    lightning_lane_event = ll_event.LightningLaneEvent(
        "lightning_lane",
        event_type,
        "12345",
        guest_id,
        "transaction_id_value",
        experience,
        1,
        created_time,
        created_time,
        business_date,
        experience_start,
        experience_end,
        event_status,
        "Not Experienced",
        100,
        "High",
    )
    return lightning_lane_event


def setup_monkeypatch(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")


def test_event_deserializer_lightening_lane():
    event = {
        "atomic_id#event_name": {"S": "75a2042e-4c63-4339-9798-daf965a4d09c#lightning_lane"},
        "event_time": {"N": "1665592107199"},
        "event": {
            "S": '{"className": "LightningLaneEvent", "objectType": "lightning_lane", "eventType": "NONINVENTORY", "atomicId": "75a2042e-4c63-4339-9798-daf965a4d09c", "guestId": "AAAADA6M4LV52JPUBGU33JT77A", "transactionId": "f0be3034472a5bf4ed0741e3ed0ff40f", "experience": {"experienceId": "353305", "experienceCategory": "Experience Category N/A", "experienceName": "Experience Name N/A", "locationId": "353305", "locationName": "Location Name N/A", "locationHierarchy": {"destination": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "resortArea": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "parkOrResort": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "land": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "pavillion": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}}}, "remainingCount": 1, "eventTime": 1675954207.095388, "createdTime": 1665592107.1995, "lastModified": 1665592107.1995, "experienceStart": 1665592380.0, "experienceEnd": 1665640800.0, "eventStatus": "BOOKED", "curatedStatus": "Booked", "curatedConfidenceScore": 100, "curatedConfidenceLabel": "High"}'  # pragma: allowlist secret
        },  # pragma: allowlist secret
    }
    event_obj = lookup.EventDeserializer.get_event_from_dynamo(event)
    logger.debug(f"{event_obj=}")


def test_event_deserializer_import_failure():
    with pytest.raises(ValueError):
        event = {
            "atomic_id#event_name": {"S": "75a2042e-4c63-4339-9798-daf965a4d09c#lightning_lane"},
            "event_time": {"N": "1665592107199"},
            "event": {
                "S": '{"className": "NoClass", "objectType": "lightning_lane", "eventType": "NONINVENTORY", "atomicId": "75a2042e-4c63-4339-9798-daf965a4d09c", "guestId": "AAAADA6M4LV52JPUBGU33JT77A", "transactionId": "f0be3034472a5bf4ed0741e3ed0ff40f", "experience": {"experienceId": "353305", "experienceCategory": "Experience Category N/A", "experienceName": "Experience Name N/A", "locationId": "353305", "locationName": "Location Name N/A", "locationHierarchy": {"destination": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "resortArea": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "parkOrResort": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "land": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "pavillion": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}}}, "remainingCount": 1, "eventTime": 1675954207.095388, "createdTime": 1665592107.1995, "lastModified": 1665592107.1995, "experienceStart": 1665592380.0, "experienceEnd": 1665640800.0, "eventStatus": "BOOKED", "curatedStatus": "Booked", "curatedConfidenceScore": 100, "curatedConfidenceLabel": "High"}'  # pragma: allowlist secret
            },
        }
        lookup.EventDeserializer.get_event_from_dynamo(event)  # pragma: allowlist secret


def test_event_deserializer_json_deserailize_error():
    with pytest.raises(ValueError):
        event = {
            "atomic_id#event_name": {"S": "75a2042e-4c63-4339-9798-daf965a4d09c#lightning_lane"},
            "event_time": {"N": "1665592107199"},
            "event": {
                "S": '{"jsondeserializeerror", True, "className": "NoClass", "objectType": "lightning_lane", "eventType": "NONINVENTORY", "atomicId": "75a2042e-4c63-4339-9798-daf965a4d09c", "guestId": "AAAADA6M4LV52JPUBGU33JT77A", "transactionId": "f0be3034472a5bf4ed0741e3ed0ff40f", "experience": {"experienceId": "353305", "experienceCategory": "Experience Category N/A", "experienceName": "Experience Name N/A", "locationId": "353305", "locationName": "Location Name N/A", "locationHierarchy": {"destination": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "resortArea": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "parkOrResort": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "land": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "pavillion": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}}}, "remainingCount": 1, "eventTime": 1675954207.095388, "createdTime": 1665592107.1995, "lastModified": 1665592107.1995, "experienceStart": 1665592380.0, "experienceEnd": 1665640800.0, "eventStatus": "BOOKED", "curatedStatus": "Booked", "curatedConfidenceScore": 100, "curatedConfidenceLabel": "High"}'  # pragma: allowlist secret
            },
        }
        lookup.EventDeserializer.get_event_from_dynamo(event)


def test_event_deserializer_key_error():
    with pytest.raises(ValueError):
        event = {
            "atomic_id#event_name": {"S": "75a2042e-4c63-4339-9798-daf965a4d09c#lightning_lane"},
            "event_time": {"N": "1665592107199"},
            "event": {
                "NONE": '{"jsondeserializeerror", True, "className": "NoClass", "objectType": "lightning_lane", "eventType": "NONINVENTORY", "atomicId": "75a2042e-4c63-4339-9798-daf965a4d09c", "guestId": "AAAADA6M4LV52JPUBGU33JT77A", "transactionId": "f0be3034472a5bf4ed0741e3ed0ff40f", "experience": {"experienceId": "353305", "experienceCategory": "Experience Category N/A", "experienceName": "Experience Name N/A", "locationId": "353305", "locationName": "Location Name N/A", "locationHierarchy": {"destination": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "resortArea": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "parkOrResort": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "land": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}, "pavillion": {"facilityId": "Facility Id N/A", "facilityName": "Facility Name N/A"}}}, "remainingCount": 1, "eventTime": 1675954207.095388, "createdTime": 1665592107.1995, "lastModified": 1665592107.1995, "experienceStart": 1665592380.0, "experienceEnd": 1665640800.0, "eventStatus": "BOOKED", "curatedStatus": "Booked", "curatedConfidenceScore": 100, "curatedConfidenceLabel": "High"}'  # pragma: allowlist secret
            },  # pragma: allowlist secret
        }
        lookup.EventDeserializer.get_event_from_dynamo(event)
