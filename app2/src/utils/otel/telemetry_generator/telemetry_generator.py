import time
from app.src.utils.otel.otel import otel_helpers
from opentelemetry import metrics
import uuid

job_id = str(uuid.uuid4())
meter = metrics.get_meter("telemetry_generator")
tracer = otel_helpers.get_tracer(__name__, service_name="TESTING", service_version="1.0")

rows_completed = meter.create_counter(name="rows_completed", description="The numbers of rows successfully completed")
rows_completed_updown = meter.create_up_down_counter(name="rows_completed_updown")

print("incrementing 1 to rows_completed")
rows_completed.add(1)
print("incrementing 5 to rows_completed_updown")
rows_completed_updown.add(5)
with tracer.start_as_current_span("sleeping"):
    time.sleep(1)
print("done")
