""" Lambda Function for data validation using data contracts"""
import json
import os
from typing import Any, Dict

from app.src.ingestion.event_pipes.data_mapper.data_mapper import IngestionDataMapper
from app.src.ingestion.event_pipes.utils.app_config_utils import get_app_config_data
from app.src.ingestion.event_pipes.utils.cloudevent_utils import parse_cloudevent_metadata_if_necessary
from app.src.ingestion.event_pipes.utils.data_contract_utils import (
    generate_hash,
)
from app.src.ingestion.event_pipes.utils.process_data import (
    handle_metrics,
    process_data,
    HandledEventResponse,
    Status,
)
from app.src.ingestion.event_pipes.utils.event_processing_utils import get_event_items
from app.src.utils.otel.otel import otel_helpers
from aws_lambda_powertools import Logger, Metrics
from cloudevents import conversion


APPCONFIG_URL_PATH = os.getenv("APPCONFIG_URL_PATH")
assert APPCONFIG_URL_PATH is not None
DATACONTRACT_MAPPINGS = get_app_config_data(
    url_path=APPCONFIG_URL_PATH, timeout=30
)  # Get datacontracts info from AppConfig
TABLE_PATH = DATACONTRACT_MAPPINGS.get("table_path", "")
SCHEMA_PATH = DATACONTRACT_MAPPINGS.get("schema_path", "")
DEFAULT_ROUTER_DATABASE = DATACONTRACT_MAPPINGS.get("default_router_database")

logger = Logger(service=__name__)
tracer = otel_helpers.get_tracer(__name__, service_name="INGESTION_VALIDATION", service_version="1.0")
# otel row_validation_duration is being flushed correctly so keeping it but using powertools for metrics
meter = otel_helpers.get_meter(os.environ["AWS_LAMBDA_FUNCTION_NAME"])

row_validation_duration = meter.create_histogram(
    name="row_validation_duration",
    description="The time it takes to validate a record including unpacking overhead",
    unit="ms",
)
powertool_metrics = Metrics(namespace=os.getenv("OTEL_NAMESPACE"))

DATA_MAPPER_TYPE = DATACONTRACT_MAPPINGS.get("data_mapper_type")
data_mapper = IngestionDataMapper.get_data_mapper(DATA_MAPPER_TYPE)(DATACONTRACT_MAPPINGS)  # type: ignore


@powertool_metrics.log_metrics()  # ensure metrics are flushed upon close of request # type: ignore
@tracer.start_as_current_span("INGESTION_LAMBDA_HANDLER")
def lambda_handler(events: list, context) -> list:  # pylint: disable=W0613
    logger.debug("events=%s", events)
    logger.info("The event has %s object(s).", len(events))

    handled_events = [handle_event(event) for event in events]
    processed_messages = [
        handled_event["cloudevent"] for handled_event in handled_events if "cloudevent" in handled_event
    ]
    logger.debug("processed_messages=%s", processed_messages)

    # send metrics to telemetry collector
    handle_metrics(
        powertool_metrics,
        logger,
        handled_events,
        function_name=os.getenv("AWS_LAMBDA_FUNCTION_NAME", "DEFAULT"),
        event_source_arn=os.getenv("eventSourceARN", "DEFAULT"),
    )

    return processed_messages


def handle_event(event: Dict[Any, Any]) -> HandledEventResponse:
    otel_attributes = {
        "subject": os.getenv("eventSourceARN", "DEFAULT").split("/")[-1],
    }
    with otel_helpers.start_trace(
        tracer=tracer,
        name="ingest_row",
        span_meter=row_validation_duration,
        attributes=otel_attributes,
        span_meter_attributes=otel_attributes,
    ):
        event_data, sequence_number, event_id, partition_key = get_event_items(event, logger)
        # add fields to all log entries that process this message
        logger_event_fields = {"sequence_id": sequence_number, "shard_id": event_id}
        logger.append_keys(**logger_event_fields)

        data = data_mapper.parse_payload(event_data, logger)
        data, cloudevent_attributes, otel_parent_context = parse_cloudevent_metadata_if_necessary(data, logger)

        # Common structure for cloudevent_attributes regardless if it matches any datacontract or not
        # CloudEvent Required attributes: specversion(str),type(str),source(uri-reference),id(str)
        cloudevent_attributes.update(
            {
                "id": event_id,
                "type": "exception",
                "source": event["eventSourceARN"],
                "subject": event["eventSourceARN"].split("/")[-1],
                "stream": event["eventSourceARN"].split("/")[-1],
                "partition_key": partition_key,
                "check_sum": generate_hash(json.dumps(data)),
                "validated": False,
            }
        )

        try:
            processed_data_response = process_data(
                sequence_number,
                event_id,
                cloudevent_attributes,
                data,
                DEFAULT_ROUTER_DATABASE,
                DATACONTRACT_MAPPINGS,
                TABLE_PATH,
                SCHEMA_PATH,
                data_mapper,
                logger,
                tracer,
                otel_parent_context,
            )
            status = processed_data_response["status"]

        except Exception as err:  # pylint: disable=broad-exception-caught
            logger.warning(err)
            status = Status.FAILED
            return HandledEventResponse(status=status)

        cloudevent = processed_data_response["cloudevent"]
        cloudevent_dict = conversion.to_dict(cloudevent)
        response = HandledEventResponse(status=status, cloudevent=cloudevent_dict)
        logger.debug("handle_event response=%s", response)
        # ensure the event specific keys are removed not not persisted
        logger.remove_keys(logger_event_fields.keys())
        return response
