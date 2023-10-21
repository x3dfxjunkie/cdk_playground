"""
lambda function to post process dynamodb events and publish to kinesis
using atomicId as the partion key
"""
import base64
import builtins
import json
import os
import traceback

from app.src.data_service.curated_event import curated_event
from aws_lambda_powertools import Logger

logger = Logger(service=__name__)


def produce(messages: list, dynamodb_event_types: list) -> tuple:
    """produce records for firehose

    Args:
        messages (list): messages to process
        dynamodb_event_types (list): dynamodb record event types to process

    Returns:
        tuple(list, list) success, failed records
    """
    success_records = []
    error_records = []
    for message in messages:
        logger.debug("raw kinesis message=%s", message)
        try:
            event = curated_event.deserialize(message["data"], dynamodb_event_types)
            logger.debug("event deserialized=%s", event.to_dict())
            record = {
                "recordId": message.get("recordId"),
                "result": "Ok",
                "data": base64.b64encode(json.dumps(event.to_dict(), default=str).encode()),
            }
            success_records.append(record)
        except (builtins.ValueError, builtins.KeyError, json.JSONDecodeError):
            traceback_error = traceback.format_exc()
            message["errorMessage"] = traceback_error
            # append message to error records and continue producing to kinesis
            record = {
                "recordId": message.get("recordId"),
                "result": "ProcessingFailed",
                "data": base64.b64encode(json.dumps(message, default=str).encode()),
            }
            error_records.append(record)
            continue
    return success_records, error_records


def validate_inputs() -> None:
    if os.environ.get("dynamodb_event_types") is None:
        raise ValueError('os.environ["dynamodb_event_types"] not set')


def lambda_handler(event: dict, context) -> dict:
    """
    https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html
    {
        "invocationId":
        "sourceKinesisStreamArn":
        "deliveryStreamArn":
        "region": "us-east-1",
        "records": [
            {
                "recordId":
                "approximateArrivalTimestamp":
                "data":
                "kinesisRecordMetadata": {
                    "sequenceNumber":
                    "subsequenceNumber":
                    "partitionKey": "
                    "shardId":
                    "approximateArrivalTimestamp":
                }
            }
        ]
    }
    """
    logger.debug("event=%s", event)
    logger.debug("context=%s", context)
    # uncaught exceptions will cause the entire set of records to be sent to the dlq
    validate_inputs()
    successful_records, failed_records = produce(
        event["records"], os.environ.get("dynamodb_event_types", "").split(",")
    )
    return_dict = {"records": [*successful_records, *failed_records]}
    logger.debug("return_dict=%s", return_dict)
    return return_dict
