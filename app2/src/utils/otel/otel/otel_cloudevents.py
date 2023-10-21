"""
    Module that contains the class definition of a cloud event with otel attributes
"""
from __future__ import annotations

from cloudevents.pydantic import CloudEvent
from pydantic import Field
from typing import Optional, Dict, Any, cast
from opentelemetry.metrics import Meter, Counter, UpDownCounter, Histogram, get_meter
from opentelemetry.util.types import Attributes


class OtelCloudEvent(CloudEvent):
    """
    CloudEvent with addition parameter to be compatible with Otel
    - trace_parent: Required[str] - traceparent id for tracing
    - trace_state: Required[str] - trace state for tracing
    - test: NotRequired[bool] - test flag
    """

    trace_parent: Optional[str] = Field(..., alias="traceparent")
    trace_state: Optional[str] = Field(..., alias="tracestate")
    test: Optional[bool]

    @classmethod
    def create(cls, attributes: Dict[str, Any], data: Optional[Any]) -> OtelCloudEvent:
        return cls(attributes, data)

    def __init__(
        self,
        attributes: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        **kwargs,
    ) -> None:
        super().__init__(attributes, data, **kwargs)


class CloudEventInstrument:
    """
    CloudEvent Base Instrument
    """

    def __add_cloudevent_attributes__(
        self, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None
    ) -> Attributes:
        updated_attributes: Dict[str, Any] = {
            **(cast(Dict[str, Any], attributes) if attributes is not None else {}),
            **({"test": otel_cloudevent.test} if otel_cloudevent.test is not None else {}),
        }
        return cast(Attributes, updated_attributes)


class CloudEventCounter(CloudEventInstrument):
    """
    Counter Class Specifically catered to cloudevents
    """

    __counter__: Counter

    def __init__(self, counter: Counter) -> None:
        super().__init__()
        self.__counter__ = counter

    def add(self, amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None) -> None:
        self.__counter__.add(amount, self.__add_cloudevent_attributes__(otel_cloudevent, attributes))


class CloudEventUpDownCounter(CloudEventInstrument):
    """
    Up Down Counter Class specifically catered to cloudevents
    """

    __up_down_counter__: UpDownCounter

    def __init__(self, up_down_counter: UpDownCounter) -> None:
        super().__init__()
        self.__up_down_counter__ = up_down_counter

    def add(self, amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None) -> None:
        self.__up_down_counter__.add(amount, self.__add_cloudevent_attributes__(otel_cloudevent, attributes))


class CloudEventHistogram(CloudEventInstrument):
    """
    Histogram Meter specifically catered to cloudevents
    """

    __histogram__: Histogram

    def __init__(self, histogram: Histogram) -> None:
        super().__init__()
        self.__histogram__ = histogram

    def record(self, amount: int | float, otel_cloudevent: OtelCloudEvent, attributes: Attributes = None) -> None:
        self.__histogram__.record(amount, self.__add_cloudevent_attributes__(otel_cloudevent, attributes))


class CloudEventMeter:
    """
    Meter that is specifically created for cloud events
    Only works for synchronous counters
    If Async Counters are needed, feel free to create async counters and update docs
    """

    __meter__: Meter

    def __init__(self, meter: Meter) -> None:
        self.__meter__ = meter

    def create_counter(self, name: str, unit: str = "", description: str = "") -> CloudEventCounter:
        return CloudEventCounter(self.__meter__.create_counter(name, unit, description))

    def create_up_down_counter(self, name: str, unit: str = "", description: str = "") -> CloudEventUpDownCounter:
        return CloudEventUpDownCounter(self.__meter__.create_up_down_counter(name, unit, description))

    def create_histogram(self, name: str, unit: str = "", description: str = "") -> CloudEventHistogram:
        return CloudEventHistogram(self.__meter__.create_histogram(name, unit, description))


def get_otel_cloudevent_meter(name: str) -> CloudEventMeter:
    meter = get_meter(name)
    return CloudEventMeter(meter)
