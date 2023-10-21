"""
    Test file for otel faker utils.
"""
# pylint: disable=redefined-outer-name
import pytest
from datetime import datetime

from typing import List

from app.src.load_testing.app.virtual_users.virtual_user_utils.otel_faker_utils import PayloadBuilder, OtelFakerUtils
from app.src.utils.otel.otel.otel_helpers import start_trace, get_tracer
from app.src.utils.otel.otel.otel_cloudevents import OtelCloudEvent, get_otel_cloudevent_meter
from opentelemetry.util.types import Attributes


def test_payload_builder_default_values():
    test_data_dict = {
        "auth_pin_encrpt_hash_vl": "VsOioTBhEoVBZlhQogVT",
        "chrg_grp_id": 3274,
        "chrg_grp_sts_nm": "HzxBaeghDkoqSppqLUXk",
        "chrg_grp_typ_nm": "uFrwEWHlakvJDaWIkpAZ",
        "chrg_grp_ds": "EouLpqDMHDcwhRlwhGww",
        "chrg_grp_strt_dts": "2017-11-22T17:14:48",
        "chrg_grp_end_dts": "2003-07-20T21:28:52",
        "txn_fac_id": 5494,
        "src_acct_ctr_id": 7856,
        "grp_dlgt_sml_bal_wrtoff_in": "hbApQXhISMMYhytEVOpM",
        "create_usr_id_cd": "CzNKUftVnKdZUCaQuKlF",
        "create_dts": "2016-08-23T02:41:07",
        "updt_usr_id_cd": "vwcHBFhhcRPzFYwDhVbU",
        "updt_dts": "2001-10-06T11:06:27",
        "jdo_seq_nb": 8295,
        "chrg_grp_actv_in": "YckYxXYMeWikzRYBFdgl",
    }

    builder = (
        PayloadBuilder()
        .add_source()
        .add_type()
        .add_test()
        .add_specversion()
        .add_time()
        .add_subject()
        .add_tracestate()
        .add_traceparent()
        .add_data(test_data_dict)
    )
    payload = builder.build().dict(by_alias=True)

    assert payload["type"] == "exception"
    assert payload["test"] is True
    assert payload["specversion"] == "1.0"
    assert payload["subject"] == "lst-use1-guest360-kinesis-dmz"
    assert "Root=1-" in payload["tracestate"]
    assert "Parent=" in payload["tracestate"]
    assert "Sampled=1" in payload["tracestate"]
    assert "1-" in payload["traceparent"]
    assert payload["data"] == test_data_dict
    assert isinstance(payload["time"], datetime)


def test_open_telemetry_utils():
    data_list = [{"key": "value"}, '{"key": "value_in_str"}']
    payloads = OtelFakerUtils.add_otel_payload(data_list)

    payloads_dict = [payload.dict(by_alias=True) for payload in payloads]

    assert len(payloads) == 2
    for payload in payloads_dict:
        assert payload["data"]["key"] in ["value", "value_in_str"]


@pytest.mark.parametrize(
    "data_input, expected_output",
    [
        (["data1", "data2"], ["data1", "data2"]),
        ([{"key1": "value1"}, {"key2": "value2"}], [{"key1": "value1"}, {"key2": "value2"}]),
    ],
)
def test_open_telemetry_utils_varied_input(data_input, expected_output):
    payloads = OtelFakerUtils.add_otel_payload(data_input)
    payloads_dict = [payload.dict(by_alias=True) for payload in payloads]
    for index, payload in enumerate(payloads_dict):
        assert payload["data"] == expected_output[index]


@pytest.fixture
def dummy_data_input() -> List[OtelCloudEvent]:
    payloads = OtelFakerUtils.add_otel_payload(["data1", "data2"])
    return payloads


def test_open_telemetry_helpers_with_traces_data_attribute(dummy_data_input):
    tracer = get_tracer(__name__, service_name="test", service_version="test")

    for event in dummy_data_input:
        with start_trace(tracer, "test_trace", cloudevent=event) as trace_context:
            assert trace_context.__attributes__ is not None
            assert trace_context.__attributes__.get("test")


def test_otel_cloud_event_counter(dummy_data_input):
    meter = get_otel_cloudevent_meter(__name__)

    counter = meter.create_counter("test_counter")

    old_add = counter.add

    def monkey_patched_add(amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None) -> None:
        nonlocal counter
        nonlocal old_add
        updated_attributes = counter.__add_cloudevent_attributes__(otel_cloudevent, attributes)
        assert updated_attributes is not None
        assert updated_attributes.get("test") is True
        old_add(amount, otel_cloudevent, attributes)

    counter.add = monkey_patched_add

    for event in dummy_data_input:
        counter.add(1, event)


def test_otel_cloud_event_up_down_counter(dummy_data_input):
    meter = get_otel_cloudevent_meter(__name__)

    counter = meter.create_up_down_counter("test_counter")

    old_add = counter.add

    def monkey_patched_add(amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None) -> None:
        nonlocal counter
        nonlocal old_add
        updated_attributes = counter.__add_cloudevent_attributes__(otel_cloudevent, attributes)
        assert updated_attributes is not None
        assert updated_attributes.get("test") is True
        old_add(amount, otel_cloudevent, attributes)

    counter.add = monkey_patched_add

    for event in dummy_data_input:
        counter.add(1, event)


def test_otel_cloud_event_histogram(dummy_data_input):
    meter = get_otel_cloudevent_meter(__name__)

    counter = meter.create_histogram("test_counter")

    old_record = counter.record

    def monkey_patched_record(
        amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None
    ) -> None:
        nonlocal counter
        nonlocal old_record
        updated_attributes = counter.__add_cloudevent_attributes__(otel_cloudevent, attributes)
        assert updated_attributes is not None
        assert updated_attributes.get("test") is True
        old_record(amount, otel_cloudevent, attributes)

    counter.record = monkey_patched_record

    for event in dummy_data_input:
        counter.record(1, event)
