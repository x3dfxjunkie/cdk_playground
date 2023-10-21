"""
    This module is to test_otel_cloudevents to ensure that all the functions work properly
"""
from app.src.utils.otel.otel.otel_cloudevents import OtelCloudEvent


def test_otel_cloudevent():
    otel_cloudevent = OtelCloudEvent.create(
        attributes={
            "traceparent": "some trace_parent",
            "tracestate": "some trace_state",
            "test": True,
            "type": "exception",
            "source": "some source",
        },
        data=None,
    )

    otel_cloudevent_dict = otel_cloudevent.dict(by_alias=True)
    assert otel_cloudevent.trace_parent == otel_cloudevent_dict["traceparent"]
    assert otel_cloudevent.trace_state == otel_cloudevent_dict["tracestate"]
    assert otel_cloudevent.test
