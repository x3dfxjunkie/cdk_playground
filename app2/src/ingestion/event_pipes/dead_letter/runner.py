""" Lambda Function for dead letter queue using data contracts"""
import json
import os
import traceback
from typing import Any, Dict

import boto3
from app.src.ingestion.event_pipes.data_mapper.data_mapper import IngestionDataMapper
from app.src.ingestion.event_pipes.utils.app_config_utils import get_app_config_data
from app.src.ingestion.event_pipes.utils.cloudevent_utils import parse_cloudevent_metadata_if_necessary
from app.src.ingestion.event_pipes.utils.data_contract_utils import (
    generate_hash,
)
from app.src.utils.otel.otel import otel_helpers
from aws_lambda_powertools import Logger, Metrics
from botocore.exceptions import BotoCoreError, ClientError, ParamValidationError
from retry import retry
from app.src.ingestion.event_pipes.utils.process_data import (
    handle_metrics,
    process_data,
    HandledEventResponse,
    Status,
)
from cloudevents import conversion


logger = Logger(service=__name__)
tracer = otel_helpers.get_tracer(
    __name__, service_name=os.getenv("meter_service", "INGESTION_DLQ"), service_version="1.0"
)
# otel row_validation_duration is being flushed correctly so keeping it but using powertools for metrics
meter = otel_helpers.get_meter(os.getenv("AWS_LAMBDA_FUNCTION_NAME"))
powertool_meter = Metrics(namespace=os.getenv("OTEL_NAMESPACE"))
row_validation_duration = meter.create_histogram(
    name="row_validation_duration",
    description="The time it takes to validate a record including unpacking overhead",
    unit="ms",
)
kinesis_client = boto3.client("kinesis")

# Global values to be set during validate_input
TARGET_KINESIS = ""
DEFAULT_ROUTER_DATABASE = ""
APPCONFIG_URL_PATH = ""
DATACONTRACT_MAPPINGS = {}
TABLE_PATH = ""
SCHEMA_PATH = ""
DATA_MAPPER_TYPE = ""
data_mapper = None


class HealingError(Exception):
    """
    Dead Letter Queue lambda handler exception class
    """


@retry(kinesis_client.exceptions.ProvisionedThroughputExceededException, tries=5, delay=1, backoff=2)
def get_records(kinesis_batch_info: dict) -> list:
    records = []
    stream = get_dmz_stream_name(kinesis_batch_info)
    try:
        logger.info("Starting ShardIterator.")
        # Get the shard iterator using the shard and sequence IDs
        shard_iterator = kinesis_client.get_shard_iterator(
            StreamName=stream,
            ShardId=kinesis_batch_info["shardId"],
            ShardIteratorType="AT_SEQUENCE_NUMBER",
            StartingSequenceNumber=kinesis_batch_info["startSequenceNumber"],
        )["ShardIterator"]
        logger.info("boto3 get_shard_iterator function executed, shard_iterator is:%s", shard_iterator)
        # Get the record using the shard iterator
        response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=1)
        logger.info("boto3 get_records executed")
        records = response["Records"]
        if len(records) == 0:
            logger.info("0 records in response from boto3 kinesis get_records")
        logger.debug("Records are:%s", records)  # To use for troubleshooting purposes
    except ClientError as err:
        if err.response["Error"]["Code"] == "ProvisionedThroughputExceededException":
            raise err  # Reraise the exception to trigger the retry. @retry logs a default warning message
    except (KeyError, ParamValidationError) as err:
        logger.warning("Other error occurred in get_records: %s", err)
        raise err
    logger.info("Get Record successfully for StartingSequenceNumber:%s", kinesis_batch_info["startSequenceNumber"])
    return records


def send_to_kinesis_validated(records_list: list):
    """Send records to kinesis validator, called Once per execution"""
    try:
        logger.info("Sending records to %s", TARGET_KINESIS)
        response = kinesis_client.put_records(StreamName=TARGET_KINESIS, Records=records_list)
        logger.info("send_to_kinesis_validated response from put_records:%s", response)
        return response
    except (ClientError, KeyError, ParamValidationError) as err:
        logger.warning("Error sending events to validated kinesis: %s", err)
        raise err


def handle_event(event: Dict[str, Any], kinesis_batch_info: Dict[str, Any]) -> HandledEventResponse:
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
        shard_id = kinesis_batch_info.get("shardId")
        sequence_number = event.get("SequenceNumber")
        event_id = f"{shard_id}-{sequence_number}"
        partition_key = event.get("PartitionKey")

        # add fields to all log entries that process this message
        logger_event_fields = {"sequence_id": sequence_number, "shard_id": event_id}
        logger.append_keys(**logger_event_fields)

        dmz_stream_name = get_dmz_stream_name(kinesis_batch_info)
        event_data = event.get("Data").decode("utf-8")

        data = data_mapper._parse_payload(
            event_data, logger
        )  # don't call `parse_payload`, as `Data` is not b64 encoded
        data, cloudevent_attributes, otel_parent_context = parse_cloudevent_metadata_if_necessary(data, logger)

        # Common structure for cloudevent_attributes regardless if it matches any datacontract or not
        # CloudEvent Required attributes: specversion(str),type(str),source(uri-reference),id(str)
        cloudevent_attributes.update(
            {
                "id": event_id,
                "type": "exception",
                "source": kinesis_batch_info["streamArn"],
                "subject": dmz_stream_name,
                "stream": dmz_stream_name,
                "partition_key": partition_key,
                "check_sum": generate_hash(json.dumps(data)),
                "validated": False,
                "dlq": True,
            }
        )

        try:
            processed_data_response = process_data(
                event_id,
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


def get_dmz_stream_name(kinesis_batch_info: Dict[str, Any]) -> str:
    dmz_stream_arn = kinesis_batch_info["streamArn"]
    dmz_stream_name = dmz_stream_arn.split("/")[1]
    return dmz_stream_name


def validate_inputs(event: list):
    try:
        assert os.getenv("AWS_LAMBDA_FUNCTION_NAME") is not None
        assert os.getenv("OTEL_NAMESPACE") is not None
        assert os.getenv("APPCONFIG_URL_PATH") is not None
        # todo check keys of event keys to ensure event payload is valid

        # get appconfig input and set appropriate global vars
        globals()["TARGET_KINESIS"] = os.getenv("KINESIS_STREAM_NAME")
        globals()["APPCONFIG_URL_PATH"] = os.getenv("APPCONFIG_URL_PATH")
        globals()["DATACONTRACT_MAPPINGS"] = get_app_config_data(
            url_path=APPCONFIG_URL_PATH, timeout=30  # type: ignore
        )  # Get datacontracts info from parameter store

        globals()["TABLE_PATH"] = DATACONTRACT_MAPPINGS.get("table_path", "")
        globals()["SCHEMA_PATH"] = DATACONTRACT_MAPPINGS.get("schema_path", "")
        globals()["DATA_MAPPER_TYPE"] = DATACONTRACT_MAPPINGS.get("data_mapper_type")
        globals()["DEFAULT_ROUTER_DATABASE"] = DATACONTRACT_MAPPINGS.get("default_router_database")
        globals()["data_mapper"] = IngestionDataMapper.get_data_mapper(DATA_MAPPER_TYPE)(DATACONTRACT_MAPPINGS)
    except Exception as err:  # pylint: disable=broad-exception-caught
        # ensure any exception is caught so that it is handled without causing an unhandled exception
        raise ValueError("Input validation error") from err


@powertool_meter.log_metrics()  # ensure metrics are flushed upon close of requet # type: ignore
@tracer.start_as_current_span("INGESTION_LAMBDA_HANDLER_DLQ")
def lambda_handler(event: list, context) -> list:  # pylint: disable=W0613
    logger.debug("event list:%s", event)
    handled_events = []
    processed_messages = []
    try:
        validate_inputs(event)
        for data in event:
            # get kinesis data
            kinesis_data = json.loads(data["body"])
            kinesis_batch_info = kinesis_data["KinesisBatchInfo"]
            records = get_records(kinesis_batch_info)
            # check if there is any record in the response
            handled_events = [handle_event(record, kinesis_batch_info) for record in records]
    except KeyError as err:
        logger.warning("An error occurred: %s - %s, Context: %s", type(err).__name__, err, vars(context))
        logger.warning("Error traceback: %s", traceback.format_exc())
        raise HealingError("Data healing error") from err

    except (ClientError, BotoCoreError, ParamValidationError) as err:
        logger.warning("An error occurred: %s - %s, Context: %s", type(err).__name__, err, vars(context))
        raise HealingError("Data healing error") from err

    except ValueError as err:
        logger.exception("An error occurred: %s - %s, Context: %s", type(err).__name__, err, vars(context))

    finally:
        logger.debug("handled_events=%s", handled_events)
        processed_messages = [
            {
                "Data": json.dumps(handled_event["cloudevent"]),
                "PartitionKey": handled_event["cloudevent"]["partition_key"],
            }
            for handled_event in handled_events
            if "cloudevent" in handled_event
        ]
        logger.debug("processed_messages=%s", processed_messages)

        # send metrics to telemetry collector
        handle_metrics(
            powertool_meter,
            logger,
            handled_events,
            function_name=os.getenv("AWS_LAMBDA_FUNCTION_NAME", "DEFAULT"),
            event_source_arn=os.getenv("eventSourceARN", "DEFAULT"),
        )
        if len(processed_messages) > 0:
            send_to_kinesis_validated(records_list=processed_messages)
            logger.info(
                "%s of %s record(s) were successfully sent to %s", len(processed_messages), len(event), TARGET_KINESIS
            )
        else:
            logger.info("No records were sent to %s", TARGET_KINESIS)

    return processed_messages
