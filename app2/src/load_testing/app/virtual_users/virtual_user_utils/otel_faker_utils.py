"""
    Contains a Payload builder to construct open telemetry payloads and an OtelFakerUtils
"""
from __future__ import annotations

import json
import random
import string
from datetime import datetime
from typing import Dict, Any, List
from app.src.utils.otel.otel.otel_cloudevents import OtelCloudEvent


class PayloadBuilder:
    """
    A Builder class for constructing telemetry payloads.

    The PayloadBuilder class allows for incremental addition of payload attributes
    using the builder pattern. It offers methods to set common telemetry attributes
    with defaults provided, while also allowing custom values.
    """

    payload: Dict[str, Any]
    data: Any

    def __init__(self):
        self.payload = {}
        self.data = None

    def add_source(self, source: str = "lst-use1-guest360-kinesis-dmz") -> PayloadBuilder:
        """Add 'source' attribute to payload"""
        self.payload["source"] = source
        return self

    def add_type(self, type_value: str = "exception") -> PayloadBuilder:
        """Add 'type' attribute to the payload."""
        self.payload["type"] = type_value
        return self

    def add_test(self, test_value: bool = True) -> PayloadBuilder:
        """Add 'test' attribute to the payload."""
        self.payload["test"] = test_value
        return self

    def add_specversion(self, specversion_value: str = "1.0") -> PayloadBuilder:
        """Add 'specversion' attribute to the payload."""
        self.payload["specversion"] = specversion_value
        return self

    def add_time(self, time_value: str | None = None) -> PayloadBuilder:
        """Add 'time' attribute to the payload, defaults to current UTC time."""
        if not time_value:
            time_value = datetime.utcnow().isoformat(timespec="microseconds") + "+00:00"
        self.payload["time"] = time_value
        return self

    def add_subject(self, subject_value: str = "lst-use1-guest360-kinesis-dmz") -> PayloadBuilder:
        """Add 'subject' attribute to the payload."""
        self.payload["subject"] = subject_value
        return self

    def add_tracestate(self, tracestate_value: str | None = None) -> PayloadBuilder:
        """Add 'tracestate' attribute to the payload, with default randomized values."""
        if not tracestate_value:
            root = "".join(random.choices(string.hexdigits, k=32))  # NOSONAR
            parent = "".join(random.choices(string.hexdigits, k=16))  # NOSONAR
            tracestate_value = f"Root=1-{root};Parent={parent};Sampled=1"
        self.payload["tracestate"] = tracestate_value
        return self

    def add_traceparent(self, traceparent_value: str | None = None) -> PayloadBuilder:
        """Add 'traceparent' attribute to the payload, with default randomized value."""
        if not traceparent_value:
            traceparent_value = "".join(random.choices(string.hexdigits, k=32))  # NOSONAR
            traceparent_value = f"1-{traceparent_value}"
        self.payload["traceparent"] = traceparent_value
        return self

    def add_data(self, data_value: Any) -> PayloadBuilder:
        """Add 'data' attribute to the payload."""
        self.data = data_value
        return self

    def build(self) -> OtelCloudEvent:
        """Finalize and return the constructed payload."""
        return OtelCloudEvent.create(attributes=self.payload, data=self.data)


class OtelFakerUtils:
    """
    Utility class for generating OpenTelemetry payloads.

    The OtelFakerUtils class offers static method to create payloads using
    the PayloadBuilder class. It simplifies the process of generating multiple
    payloads based on provided data.
    """

    @staticmethod
    def add_otel_payload(data_list: List[Any]) -> List[OtelCloudEvent]:
        """
        Generate a list of OpenTelemetry payloads based on provided data.

        Args:
        - data_list (list): A list containing the data for each payload.

        Returns:
        - list: A list of OpenTelemetry payloads constructed using the PayloadBuilder.
        """
        payloads: List[OtelCloudEvent] = []

        for data in data_list:
            if isinstance(data, str) and (data.startswith("{") or data.startswith("[")):
                data = json.loads(data)

            builder = PayloadBuilder()
            payload = (
                builder.add_type()
                .add_test()
                .add_source()
                .add_specversion()
                .add_time()
                .add_subject()
                .add_tracestate()
                .add_traceparent()
                .add_data(data)
                .build()
            )
            payloads.append(payload)

        return payloads
