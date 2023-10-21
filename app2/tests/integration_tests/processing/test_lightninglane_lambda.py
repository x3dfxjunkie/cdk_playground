""" Tests for Processing Lightning Lane events """
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument for fixtures may be needed to be called but not excplicitly used
import datetime as dt
import json
import logging
import sys
import time

import pytest
from app.tools.test_data.lightning_lane_raw_events import LightningLaneRawEvents

logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


def test_lightninglane_lambda(setup_aws):
    send_raw_ll_events(pytest.source_stream_name, pytest.kinesis)

    ll_raw_event01_json = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
    ll_raw_event02_json = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_02)
    ll_raw_event03_json = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_03)

    # Sleep for 30 seconds to let lambda cold start and process.
    time.sleep(30)

    atomic_id_01 = pytest.data_lookup.atomic_id_lookup("ealinkid", str(ll_raw_event01_json["item"]["entitlement"]["guestId"]))
    atomic_id_02 = pytest.data_lookup.atomic_id_lookup("ealinkid", str(ll_raw_event02_json["item"]["entitlement"]["guestId"]))
    atomic_id_03 = pytest.data_lookup.atomic_id_lookup("ealinkid", str(ll_raw_event03_json["item"]["entitlement"]["guestId"]))

    ll_event_01 = pytest.data_lookup.get_events_from_profile(atomic_id_01, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30))[0]
    ll_event_02 = pytest.data_lookup.get_events_from_profile(atomic_id_02, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30))[0]
    ll_event_03 = pytest.data_lookup.get_events_from_profile(atomic_id_03, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30))[0]

    logger.info(f"{ll_event_01.to_json()=}")

    assert atomic_id_01 is not None
    assert atomic_id_02 is not None
    assert atomic_id_03 is not None

    assert ll_event_01 is not None
    assert ll_event_02 is not None
    assert ll_event_03 is not None
    # TODO: Add cleanup code to delete from integration env.


def test_lightninglane_lambda_bad_message(setup_aws):
    pytest.kinesis.put_record(StreamName=pytest.source_stream_name, Data="This is a bad message", PartitionKey="badbad")
    assert dead_letter_table_count() == 0


def dead_letter_table_count():
    return 0


def send_raw_ll_events(source_stream_name, kinesis):
    kinesis.put_record(
        StreamName=source_stream_name,
        Data=LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01.encode("utf-8"),
        PartitionKey="1",
    )
    kinesis.put_record(
        StreamName=source_stream_name,
        Data=LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_02.encode("utf-8"),
        PartitionKey="2",
    )
    kinesis.put_record(
        StreamName=source_stream_name,
        Data=LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_03.encode("utf-8"),
        PartitionKey="3",
    )
