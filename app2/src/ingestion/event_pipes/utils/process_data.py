# utilities for handle/processing data pipelines
from enum import Enum
from typing import Any, Dict, List, Optional, TypedDict
from collections import Counter
from cloudevents.pydantic import CloudEvent
from typing_extensions import NotRequired
from opentelemetry.context import Context
from opentelemetry.trace import Link, SpanKind
from aws_lambda_powertools import Logger
from aws_lambda_powertools.metrics import MetricUnit
from opentelemetry import trace
from app.src.ingestion.event_pipes.utils.data_contract_utils import (
    DataContractNotFoundException,
    DataValidationError,
    validate_record_conforms_to_data_contract,
)
from app.src.utils.helpers.dict_lookup import dict_lookup
from app.src.utils.otel.otel import otel_helpers


class Status(Enum):
    SUCCESS = "success"
    WARNING = "warning"
    FAILED = "failed"


class ProcessDataResponse(TypedDict):
    status: Status
    cloudevent: CloudEvent


class HandledEventResponse(TypedDict):
    status: Status
    cloudevent: NotRequired[Dict[Any, Any]]


def process_data(
    _: str,
    event_id: str,
    cloudevent_attributes: dict,
    data: dict,
    DEFAULT_ROUTER_DATABASE,
    DATACONTRACT_MAPPINGS,
    TABLE_PATH,
    SCHEMA_PATH,
    data_mapper,
    logger: Logger,
    tracer: trace.Tracer,
    context: Optional[Context] = None,
) -> ProcessDataResponse:
    consumer_context = trace.get_current_span().get_span_context()
    links = [Link(consumer_context)] if context else None
    with tracer.start_as_current_span(
        f"INGESTION_PROCESS_DATA-{event_id}", context=context, kind=SpanKind.INTERNAL, links=links
    ) as span_process_data:
        # config_object : it has the object from data_contract_mappings with the right data contract to use
        try:
            logger.debug("process_data cloudevent_attributes=%s data=%s", cloudevent_attributes, data)
            config_object = data_mapper.match_data_to_contract(data)
            logger.info("config_object=%s", config_object)

            # Add router table,schema,database , sequence_id and shard_id as dimensions for metrics
            router_keys = ("router_table", "router_schema", "router_database")
            router_keys_values = {router_key: config_object[router_key] for router_key in router_keys}

            # If we get a valid data contract add routing params before pydantic validation
            cloudevent_attributes.update(router_keys_values)

            # Validate if data passes the pydantic validation
            validated_data_contract = validate_record_conforms_to_data_contract(config_object, data, logger)

            cloudevent_attributes.update(
                {
                    "validated": True,
                    "type": validated_data_contract,
                    "data_contract_version": config_object["data_contract_version"],
                }
            )
            status = Status.SUCCESS

        except DataContractNotFoundException as err:
            cloudevent_attributes["router_database"] = DEFAULT_ROUTER_DATABASE or "failed_database"
            cloudevent_attributes["router_schema"] = dict_lookup(data, SCHEMA_PATH) or DATACONTRACT_MAPPINGS.get(
                "default_schema"
            )
            cloudevent_attributes["router_table"] = dict_lookup(data, TABLE_PATH) or DATACONTRACT_MAPPINGS.get(
                "default_table"
            )
            cloudevent_attributes["exception_error"] = type(err).__name__ + ":" + str(err)
            logger.warning("%s:%s", type(err).__name__, str(err))
            status = Status.FAILED

        except DataValidationError as err:
            logger.warning(err)
            cloudevent_attributes["exception_error"] = str(err)
            status = Status.WARNING
        except Exception as err:  # pylint: disable=broad-exception-caught
            logger.error(err)
            status = Status.FAILED

        # Create cloudevent with otel propagation
        cloudevent = otel_helpers.otel_cloudevent(
            attributes=cloudevent_attributes, data=data, context=span_process_data
        )

        processed_event = ProcessDataResponse(status=status, cloudevent=cloudevent)
        logger.debug("processed_event=%s", processed_event)
        return processed_event


def handle_metrics(
    powertool_metrics,
    logger: Logger,
    handled_events: List[HandledEventResponse],
    function_name: str,
    event_source_arn: str,
):
    otel_attributes = {
        "OTelLib": function_name,
        "subject": event_source_arn.split("/")[-1],
    }
    powertool_metrics.set_default_dimensions(**otel_attributes)

    # Declarative Counts
    row_count = len(handled_events)
    status_counts = Counter(handled_event["status"] for handled_event in handled_events)

    success_count = status_counts[Status.SUCCESS]
    warning_count = status_counts[Status.WARNING]
    failed_count = status_counts[Status.FAILED]

    # send the counts to the appropriate counters
    # set the default dimensions used across all metric names
    powertool_metrics.add_metric(name="rows_success", unit=MetricUnit.Count, value=success_count)
    powertool_metrics.add_metric(name="rows_warning", unit=MetricUnit.Count, value=warning_count)
    powertool_metrics.add_metric(name="rows_failed", unit=MetricUnit.Count, value=failed_count)
    powertool_metrics.add_metric(name="rows_started", unit=MetricUnit.Count, value=row_count)

    logger.info(
        "Processed Row Counts:: success=%s, warning=%s, failed=%s, count=%s parsed",
        success_count,
        warning_count,
        failed_count,
        row_count,
    )
