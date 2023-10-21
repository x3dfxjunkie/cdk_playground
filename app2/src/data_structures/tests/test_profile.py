"""
Collection of tests for serializing and deserializing profile class structures.
"""
import datetime
import json

from marshmallow_jsonschema import JSONSchema

import app.src.data_structures.events.attraction_ridden_event as attraction_ridden_event
import app.src.data_structures.profiles.profile as profile


def test_attraction_profile_schema_valid():
    """
    Tests that a profile can be serialized to json as expected.
    """
    test_profile = build_test_profile()

    schema = test_profile.schema()
    json_schema = JSONSchema()
    generated_json_schema = json_schema.dump(schema)["definitions"]
    expected_profile_schema = json.loads(EXPECTED_PROFILE_SCHEMA)
    assert generated_json_schema == expected_profile_schema


def test_attraction_profile_to_json():
    """
    Tests that a profile can be serialized to json as expected.
    """
    test_profile = build_test_profile().to_json().replace(" ", "")
    assert test_profile == TEST_PROFILE_JSON


def test_attraction_ridden_event_to_json():
    """
    Tests that a profile can be serialized to json as expected.
    """
    test_ride_event = build_test_attraction_ridden_event()
    test_ride_event_json_temp = test_ride_event.to_json()
    assert test_ride_event.to_json().replace(" ", "") == TEST_RIDE_EVENT_JSON


def build_test_profile() -> profile.Profile:
    """
    Helper function to build profiles.
    """
    fun_mountain_ride_history = attraction_ridden_event.AttractionRideHistory(
        "abc123", "Fun Mountain", 150
    )
    unfun_mountain_ride_history = attraction_ridden_event.AttractionRideHistory(
        "def456", "Unfun Mountain", 600
    )
    test_profile = profile.Profile(
        "abc", ["123", "456"], [fun_mountain_ride_history, unfun_mountain_ride_history]
    )

    return test_profile


def build_test_attraction_ridden_event() -> attraction_ridden_event.AttractionRiddenEvent:
    """
    Helper function to build attraction ridden events.
    """
    event_timestamp = (datetime.datetime(2000, 1, 1, 1, 1, 1, 1) - datetime.datetime(1970, 1, 1)).total_seconds()
    fun_mountain_ride_event = attraction_ridden_event.AttractionRiddenEvent(
        "abc", "abc123", "Fun Mountain", event_timestamp
    )

    return fun_mountain_ride_event


TEST_PROFILE_JSON = """
{
    "atomicId": "abc",
    "associatedIds": [
        "123",
        "456"
    ],
    "attractionRideHistories": [
        {   "attractionId": "abc123",
            "attractionName": "Fun Mountain",
            "attractionRideCount": 150 
        },
        {   "attractionId": "def456",
            "attractionName": "Unfun Mountain",
            "attractionRideCount": 600
        }
    ]
}
""".replace(
    "\n", ""
).replace(
    " ", ""
)

TEST_RIDE_EVENT_JSON = """
{
    "className": "AttractionRiddenEvent",
    "atomicId": "abc",
    "attractionId": "abc123",
    "attractionName": "Fun Mountain",
    "attractionRiddenTimestamp": 946688461.000001
}
""".replace(
    "\n", ""
).replace(
    " ", ""
)

EXPECTED_PROFILE_SCHEMA = """
{
  "AttractionridehistorySchema": {
    "type": "object",
    "required":[
        "attractionId",
        "attractionName",
        "attractionRideCount"
        ],
    "properties": {
      "attractionId": {
        "title": "attraction_id",
        "type": "string"
      },
      "attractionName": {
        "title": "attraction_name",
        "type": "string"
      },
      "attractionRideCount": {
        "title": "attraction_ride_count",
        "type": "integer"
      }
    },
    "additionalProperties": false
  },
  "ProfileSchema": {
    "type": "object",
    "required":[
        "associatedIds",
        "atomicId",
        "attractionRideHistories"
        ],
    "properties": {
      "associatedIds": {
        "title": "associated_ids",
        "type": "array",
        "items": {
          "title": "associated_ids",
          "type": "string"
        }
      },
      "atomicId": {
        "title": "atomic_id",
        "type": "string"
      },
      "attractionRideHistories": {
        "title": "attraction_ride_histories",
        "type": "array",
        "items": {
          "type": "object",
          "$ref": "#/definitions/AttractionridehistorySchema",
          "field_many": true
        }
      }
    },
    "additionalProperties": false
  }
}
""".replace(
    "\n", ""
).replace(
    " ", ""
)
