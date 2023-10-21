""" Tests for Otel """
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures

import json
import logging
from unittest import mock
import sys

import cloudevents
import pytest
from cloudevents.pydantic import CloudEvent
from app.src.utils.otel.otel import otel_helpers
from opentelemetry import trace
from opentelemetry.metrics import Meter
from opentelemetry.context import Context
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.util.types import Attributes
from typing import Callable

# set log levels for nozy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestOtelHelpers:
    """tests for otel helpers"""

    def test_get_tracer_aws_env(self, monkeypatch):
        """test tracer returns proper tracer with service name and service version set"""
        monkeypatch.setenv("AWS_LAMBDA_FUNCTION_NAME", "testing")
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        logger.debug(f"{dir(tracer)=}")
        logger.debug(f"{tracer._instrumentation_scope=}")  # pylint: disable=protected-access debugging
        assert isinstance(tracer, trace.Tracer)
        assert tracer._instrumentation_scope.name == __name__  # pylint: disable=protected-access

    def test_get_tracer_non_aws_env(self):
        """test tracer returns proper tracer with service name and service version set"""
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        logger.debug(f"{dir(tracer)=}")
        logger.debug(f"{tracer._instrumentation_scope=}")  # pylint: disable=protected-access debugging
        assert isinstance(tracer, trace.Tracer)
        assert tracer._instrumentation_scope.name == __name__  # pylint: disable=protected-access

    def test_otel_to_xray_id(self, mocker):
        """test given a span_context get a valid xray_trace_id
        298108097170045375835223835365441132080
        1-e04587f6-3247a1406f3396b9e9d5d630
        """
        given = int(298108097170045375835223835365441132080)
        expected = "1-e04587f6-3247a1406f3396b9e9d5d630"
        mock_span_ctx = mock.Mock()
        mock_span_ctx.is_valid = True
        mock_span_ctx.trace_id = given
        test_xray_id = otel_helpers.otel_to_xray_id(mock_span_ctx)
        assert test_xray_id == expected

    def test_otel_to_xray_id_invalid_context(self, mocker):
        """test given a span_context get a valid xray_trace_id
        298108097170045375835223835365441132080
        1-e04587f6-3247a1406f3396b9e9d5d630
        """
        given = int(298108097170045375835223835365441132080)
        expected = None
        mock_span_ctx = mock.Mock()
        mock_span_ctx.is_valid = False
        mock_span_ctx.trace_id = given
        test_xray_id = otel_helpers.otel_to_xray_id(mock_span_ctx)
        assert test_xray_id == expected

    def test_xray_to_otel_id(self, mocker):
        """test given an xray id return an otel trace_id
        298108097170045375835223835365441132080
        1-e04587f6-3247a1406f3396b9e9d5d630
        """
        given = "1-e04587f6-3247a1406f3396b9e9d5d630"
        expected = int(298108097170045375835223835365441132080)
        test_otel_id = otel_helpers.xray_to_otel_id(given)
        assert test_otel_id == expected

    def test_otel_context_from_cloudevent(self, mocker):
        """test extract aws propagator context tracestate from cloudevent
        Root=1-0f793514-53a2b96075d3fa2a6a941a9d;Parent=17e83e0a5d69f5c0;Sampled=1
        """
        attributes = {
            "source": "mysource",
            "type": "TEST",
            "subject": "testsubject",
            "tracestate": "Root=1-0f793514-53a2b96075d3fa2a6a941a9d;Parent=17e83e0a5d69f5c0;Sampled=1",
        }
        data = json.dumps({"foo": "bar"})
        cloudevent = CloudEvent(attributes=attributes, data=data)

        test_context = otel_helpers.otel_context_from_cloudevent(cloudevent)
        assert test_context is not None and isinstance(test_context, Context)

    def test_otel_context_from_cloudevent_is_none(self):
        attributes = {
            "source": "mysource",
            "type": "TEST",
            "subject": "testsubject",
        }
        data = json.dumps({"foo": "bar"})
        cloudevent = CloudEvent(attributes=attributes, data=data)
        test_context = otel_helpers.otel_context_from_cloudevent(cloudevent)
        assert test_context is None

    def test_otel_cloudevent(self):
        """test to validate packing a cloudevent with otel data"""
        trace.set_tracer_provider(TracerProvider())
        tracer = trace.get_tracer(__name__)
        with tracer.start_as_current_span("testspan") as span:
            attributes = {
                "source": "testspan",
                "type": "TEST",
                "subject": "testsubject",
            }
            data = json.dumps({"foo": "bar"})
            cloudevent = otel_helpers.otel_cloudevent(attributes=attributes, data=data, context=span)
            logger.debug(f"{cloudevents.conversion.to_json(cloudevent)=}")
            assert isinstance(cloudevent, CloudEvent)
            assert cloudevent.get_attributes().get("tracestate") is not None
            assert cloudevent.get_attributes().get("traceparent") is not None

    def test_otel_cloudevent_no_context(self):
        """test to validate packing a cloudevent with otel data"""
        attributes = {
            "source": "testspan",
            "type": "TEST",
            "subject": "testsubject",
        }
        data = json.dumps({"foo": "bar"})
        cloudevent = otel_helpers.otel_cloudevent(attributes=attributes, data=data, context=None)
        logger.debug(f"{cloudevents.conversion.to_json(cloudevent)=}")
        assert isinstance(cloudevent, CloudEvent)
        assert cloudevent.get_attributes().get("tracestate") is None
        assert cloudevent.get_attributes().get("traceparent") is None

    def test_otel_trace_context(self):
        """Test to validate that the trace context works as expected"""
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        with otel_helpers.TraceContext(name="SomeTrace", tracer=tracer) as trace_context:
            # Ensure that Trace was created
            assert trace_context.name == "SomeTrace"

            # Ensure end_time does not exist during context
            with pytest.raises(AttributeError):
                trace_context.end_time  # pylint: disable=pointless-statement

            # Ensure span exists
            assert isinstance(trace_context.span, trace.Span)

        # Ensure that end_time and start_time exists and are not zero
        assert trace_context.end_time - trace_context.start_time > 0

        # Ensure that Callback functions work as expected
        external_variable = None

        def some_callback_function(_):
            nonlocal external_variable
            external_variable = 1

        with otel_helpers.TraceContext(
            name="SomeTrace", tracer=tracer, on_exit=some_callback_function
        ) as trace_context:
            # Ensure that Trace was created
            assert trace_context.name == "SomeTrace"

    def test_otel_functional_trace_context(self):
        """Test to validate that the trace context works as expected"""
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        with otel_helpers.start_trace(name="SomeTrace", tracer=tracer) as trace_context:
            # Ensure that Trace was created
            assert trace_context.name == "SomeTrace"

            # Ensure end_time does not exist during context
            with pytest.raises(AttributeError):
                trace_context.end_time  # pylint: disable=pointless-statement

            # Ensure span exists
            assert isinstance(trace_context.span, trace.Span)

        # Ensure that end_time and start_time exists and are not zero
        assert trace_context.end_time - trace_context.start_time > 0

        # Ensure that Callback functions work as expected
        external_variable = None

        def some_callback_function(_):
            nonlocal external_variable
            external_variable = 1

        with otel_helpers.start_trace(name="SomeTrace", tracer=tracer, on_exit=some_callback_function) as trace_context:
            # Ensure that Trace was created
            assert trace_context.name == "SomeTrace"

    def test_otel_functional_hook_test(self):
        """Tests on_enter and on_exit hooks"""
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        # Used to check if on_enter function actually goes through
        on_enter_flag = False
        start_time = 0
        end_time = 0

        def on_enter_function(trace_context: otel_helpers.TraceContext):
            nonlocal on_enter_flag
            on_enter_flag = True

            # We need to ensure start time and end time are not accessable
            with pytest.raises(AttributeError):
                trace_context.start_time  # pylint: disable=pointless-statement

            with pytest.raises(AttributeError):
                trace_context.end_time  # pylint: disable=pointless-statement

        def on_exit_function(trace_context: otel_helpers.TraceContext):
            nonlocal end_time
            nonlocal start_time
            assert trace_context.start_time is not None
            assert trace_context.end_time is not None
            start_time = trace_context.start_time
            end_time = trace_context.end_time

        with otel_helpers.start_trace(
            name="SomeTrace", tracer=tracer, on_enter=on_enter_function, on_exit=on_exit_function
        ) as trace_context:
            assert trace_context.start_time is not None

            # Ensure end_time does not exist during context
            with pytest.raises(AttributeError):
                trace_context.end_time  # pylint: disable=pointless-statement

        assert trace_context.start_time == start_time
        assert trace_context.end_time == end_time

    def test_otel_meter(self):
        """Test to validate that meter is being returned"""
        some_meter = otel_helpers.get_meter("SomeMeter")

        assert isinstance(some_meter, Meter)

    def test_span_meter(self):
        tracer = otel_helpers.get_tracer(__name__, service_name="MyService", service_version="1.0.0")
        meter = otel_helpers.get_meter("SomeMeter")

        span_meter = meter.create_histogram(
            name="span_meter",
            description="Time it takes to run span",
            unit="ms",
        )

        span_time: int | float = 0
        intercepted_attributes: Attributes = None
        old_record = span_meter.record

        def monkey_patched_record(amount: int | float, attributes: Attributes = None) -> None:
            """Used to intercept that amount in the record for testing purposes only"""
            nonlocal span_time
            nonlocal old_record
            nonlocal intercepted_attributes
            intercepted_attributes = attributes
            span_time = amount
            old_record(amount, attributes)

        span_meter.record = monkey_patched_record

        expected_attributes = {"test": "test"}

        with otel_helpers.start_trace(
            name="SomeTrace", tracer=tracer, span_meter=span_meter, span_meter_attributes=expected_attributes
        ) as trace_context:
            pass # NOSONAR

        assert intercepted_attributes == expected_attributes
        assert ((trace_context.end_time - trace_context.start_time) / 1_000_000) == span_time
