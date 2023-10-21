# otel helper libraries
otel helper libraries to make working with otel and aws adot easier
Cloudevents library: https://github.com/cloudevents/sdk-python/tree/main
## Usage And Examples

#### Get an Opentelemetry Tracer

Getting a tracer and setting the service name and version is a multi-step process and should be done once at the top of the script as a global variable.  Once a tracer is configured you can utilize it to start trace spans either through the context or function decorator

```python
from app.src.utils.otel.otel import otel_helpers
tracer = otel_helpers.get_tracer(service_name="MyService", service_version="1.0.0")

def trace_with_context():
    with tracer.start_as_current_span("testspan") as span
        print("hello world")

@tracer.start_as_current_span("test")
def trace_with_decorator():
    print("hello world")
```

#### Create CloudEvent and Propagate Opentelemetry
This projects utilizes the cloudevents spec and cloudevents python library to wrap wrap and move data through the system.  In order to propagate telemetry data across boundaries, the trace data needs to be injected into the cloudevent data.

```python
from cloudevents import pydantic, conversion
from app.src.utils.otel.otel import otel_helpers
with tracer.start_as_current_span("testspan") as span:
    # Set the appropriate cloudevent attributes
    attributes = {
        "source": "testspan",
        "type": "TEST",
        "subject": "testsubject",
    }
    # set the data for the cloudevent and serialize the data
    data = json.dumps({"foo": "bar"})
    cloudevent = otel_helpers.otel_cloudevent(attributes=attributes, data=data, context=span)
    # to serialize the cloudevent to a downstream consumer, convert the cloudevent to json
    cloudevent_json = conversion.to_json(cloudevent)
    # cloudevent_json is now a binary json string and is ready to be transported
```

#### Get Context from CloudEvent if Exists
In this example, a cloudevent is deserialized from json to a cloudevent object and the otel context extracted from the propagation.

```python
from cloudevents import pydantic, conversion
from app.src.utils.otel.otel import otel_helpers
json = { 
    "specversion": "1.0", 
    "id": "34568752-cf10-4153-9f48-d5d4ff718563", 
    "source": "tsource", 
    "type": "ttype", 
    "subject": "tsubject", 
    "time": "2023-06-07T16:52:04.700708+00:00", 
    "tracestate": "Root=1-0f793514-53a2b96075d3fa2a6a941a9d;Parent=17e83e0a5d69f5c0;Sampled=1",
    "data": "{\\"foo\\": \\"bar\\"}"
}

cloudevent = pydantic.from_json(json)
otel_context = otel_helpers.otel_context_from_cloudevent(cloudevent)
```

#### Translate opentelemetry trace_id to xray id

```python
from app.src.utils.otel.otel import otel_helpers
# first start a span
with tracer.start_as_current_span("testspan") as span
    # the span context object contains the details of the span
    span_ctx = span.get_span_context()
    xray_id = otel_helpers.otel_to_xray_id(span_ctx)
```

#### Translate xray id to opentelemetry trace_id

```python
from app.src.utils.otel.otel import otel_helpers
xrayid = "1-e04587f6-3247a1406f3396b9e9d5d630"
otel_trace_id = otel_helpers.xray_to_otel_id(xrayid)
```
