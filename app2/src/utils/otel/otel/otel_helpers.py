"""guest360 hellper functions for opentelem/xray
"""
from __future__ import annotations

import logging
import os
from typing import Optional, Type, Callable, Any, cast, Dict

from cloudevents.pydantic import CloudEvent
from opentelemetry import trace
from opentelemetry.context import Context
from opentelemetry.propagators.aws import aws_xray_propagator
from opentelemetry.sdk.extension.aws.trace.aws_xray_id_generator import AwsXRayIdGenerator
from opentelemetry.sdk.resources import Resource
from opentelemetry.metrics import get_meter as _get_meter
from opentelemetry.util import types
import time
import contextlib
from opentelemetry.metrics import Meter, Histogram
from opentelemetry.util.types import Attributes
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.trace.span import SpanContext, Span
from types import TracebackType

from app.src.utils.otel.otel.otel_cloudevents import OtelCloudEvent

logger = logging.getLogger(__name__)


def get_tracer(
    instrumenting_module_name: str, *args, service_name: str, service_version: str, **kwargs
) -> trace.Tracer:
    resource = Resource(
        attributes={
            "service.name": service_name,
            "service.version": service_version,
        }
    )
    # configure the trace provider based on if running inside a lambda or not
    if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") is not None:
        trace.set_tracer_provider(TracerProvider(resource=resource, id_generator=AwsXRayIdGenerator()))
    else:
        trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer = trace.get_tracer(instrumenting_module_name, *args, **kwargs)
    return tracer


def get_meter(name: str) -> Meter:
    return _get_meter(name)


def otel_to_xray_id(span_context: SpanContext) -> Optional[str]:
    if not span_context.is_valid:
        logger.debug("Invalid span context")
        return

    otel_trace_id = f"{span_context.trace_id:032x}"
    xray_trace_id = aws_xray_propagator.TRACE_ID_DELIMITER.join(
        [
            aws_xray_propagator.TRACE_ID_VERSION,
            otel_trace_id[: aws_xray_propagator.TRACE_ID_FIRST_PART_LENGTH],
            otel_trace_id[aws_xray_propagator.TRACE_ID_FIRST_PART_LENGTH :],
        ]
    )
    return xray_trace_id


def xray_to_otel_id(xray_id: str) -> int:
    timestamp_subset = xray_id[
        aws_xray_propagator.TRACE_ID_DELIMITER_INDEX_1 + 1 : aws_xray_propagator.TRACE_ID_DELIMITER_INDEX_2
    ]
    unique_id_subset = xray_id[aws_xray_propagator.TRACE_ID_DELIMITER_INDEX_2 + 1 : aws_xray_propagator.TRACE_ID_LENGTH]
    return int(timestamp_subset + unique_id_subset, 16)


def otel_context_from_cloudevent(cloudevent: CloudEvent) -> Optional[Context]:
    tracestate = cloudevent.get_attributes().get("tracestate")
    if tracestate is None:
        return
    # create a dummy carrier because cloudevents keys are downcased and want to use standard tracestate
    data = {"X-Amzn-Trace-Id": tracestate}
    context = aws_xray_propagator.AwsXRayPropagator().extract(data)
    return context


def otel_cloudevent(attributes: dict, data: Any, context: Span | None = None) -> CloudEvent:
    if context is not None:
        carrier = {}
        aws_xray_propagator.AwsXRayPropagator().inject(carrier=carrier, context=trace.set_span_in_context(context))
        attributes["traceparent"] = carrier["X-Amzn-Trace-Id"].split(";")[0].replace("Root=", "")
        attributes["tracestate"] = carrier["X-Amzn-Trace-Id"]
    # if datacontenttype is not set default to application/json
    if not attributes.get("datacontenttype"):
        attributes["datacontenttype"] = "application/json"
    cloudevent = CloudEvent(attributes=attributes, data=data)
    return cloudevent


class TraceContext:
    """
    This Context is created to easily add callbacks and to use accurate time since span.start_time is deprecated
    """

    name: str
    start_time: int
    span: trace.Span
    end_time: int
    __tracer__: trace.Tracer
    __context__: Context | None
    __kind__: trace.SpanKind
    __attributes__: types.Attributes
    __links__: trace._Links
    __record_exception__: bool
    __set_status_on_exception__: bool
    __on_exit__: Optional[Callable[[TraceContext], None]]
    __on_enter__: Optional[Callable[[TraceContext], None]]
    __span_meter__: Optional[Histogram]
    __span_meter_attributes__: Optional[Attributes]
    __cloudevent__: Optional[OtelCloudEvent]

    def __init__(
        self,
        tracer: trace.Tracer,
        name: str,
        context: Context | None = None,
        kind: trace.SpanKind = trace.SpanKind.INTERNAL,
        attributes: types.Attributes = None,
        links: trace._Links = None,
        record_exception: bool = True,
        set_status_on_exception: bool = True,
        on_exit: Optional[Callable[[TraceContext], None]] = None,
        on_enter: Optional[Callable[[TraceContext], None]] = None,
        span_meter: Optional[Histogram] = None,
        span_meter_attributes: Optional[Attributes] = None,
        cloudevent: Optional[OtelCloudEvent] = None,
    ):
        self.name = name
        self.__tracer__ = tracer
        self.__context__ = context
        self.__kind__ = kind
        self.__attributes__ = attributes
        self.__links__ = links
        self.__record_exception__ = record_exception
        self.__set_status_on_exception__ = set_status_on_exception
        self.__on_exit__ = on_exit
        self.__on_enter__ = on_enter
        self.__span_meter__ = span_meter
        self.__span_meter_attributes__ = span_meter_attributes
        self.__cloudevent__ = cloudevent
        self.__add_cloudevent_attributes__()

    def __add_cloudevent_attributes__(self):
        if self.__cloudevent__ is not None:
            attributes: Dict[str, Any] = {
                **(cast(Dict[str, Any], self.__attributes__) if self.__attributes__ is not None else {}),
                **({"test": self.__cloudevent__.test} if self.__cloudevent__.test is not None else {}),
            }
            self.__attributes__ = cast(Attributes, attributes)

    def __enter__(self) -> TraceContext:
        if self.__on_enter__ is not None:
            self.__on_enter__(self)

        self.start_time = time.time_ns()

        self.span = self.__tracer__.start_span(
            name=self.name,
            context=self.__context__,
            kind=self.__kind__,
            attributes=self.__attributes__,
            links=self.__links__,
            record_exception=self.__record_exception__,
            set_status_on_exception=self.__set_status_on_exception__,
        )
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        exception_traceback: Optional[TracebackType],
    ) -> bool:
        self.end_time = time.time_ns()
        self.span.end(end_time=self.end_time)

        if self.__on_exit__ is not None:
            self.__on_exit__(self)

        if self.__span_meter__ is not None:
            self.__span_meter__.record(
                (self.end_time - self.start_time) / 1_000_000, attributes=self.__span_meter_attributes__
            )

        if exception_type is not None:
            raise exception_type(exception_value).with_traceback(exception_traceback)

        return True


@contextlib.contextmanager
def start_trace(
    tracer: trace.Tracer,  # NOSONAR
    name: str,  # NOSONAR
    context: Context | None = None,  # NOSONAR
    kind: trace.SpanKind = trace.SpanKind.INTERNAL,  # NOSONAR
    attributes: types.Attributes = None,  # NOSONAR
    links: trace._Links = None,  # NOSONAR
    record_exception: bool = True,  # NOSONAR
    set_status_on_exception: bool = True,  # NOSONAR
    on_exit: Optional[Callable[[TraceContext], None]] = None,  # NOSONAR
    on_enter: Optional[Callable[[TraceContext], None]] = None,  # NOSONAR
    span_meter: Optional[Histogram] = None,  # NOSONAR
    span_meter_attributes: Optional[Attributes] = None,  # NOSONAR
    cloudevent: Optional[OtelCloudEvent] = None,  # NOSONAR
):
    """
    Drop in Replacement for start_trace using the Trace Context and additional callback function

    Functional Method since its easier


    Args:
        name: The name of the span to be created.
        context: An optional Context containing the span's parent. Defaults to the
            global context.
        kind: The span's kind (relationship to parent). Note that is
            meaningful even if there is no parent.
        attributes: The span's attributes.
        links: Links span to other spans
        start_time: Sets the start time of a span
        record_exception: Whether to record any exceptions raised within the
            context as error event on the span.
        set_status_on_exception: Only relevant if the returned span is used
            in a with/context manager. Defines wether the span status will
            be automatically set to ERROR when an uncaught exception is
            raised in the span with block. The span status won't be set by
            this mechanism if it was previously set manually.
        callback: The callback function that happens prior to ending the function.
            This can be used to add time to metrics.

    Yield:
        The newly-created Trace Context which includes a span.
    """
    with TraceContext(
        tracer=tracer,
        name=name,
        context=context,
        kind=kind,
        attributes=attributes,
        links=links,
        record_exception=record_exception,
        set_status_on_exception=set_status_on_exception,
        on_exit=on_exit,
        on_enter=on_enter,
        span_meter=span_meter,
        span_meter_attributes=span_meter_attributes,
        cloudevent=cloudevent,
    ) as trace_context:
        yield trace_context
