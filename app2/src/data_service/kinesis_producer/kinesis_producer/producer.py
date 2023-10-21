"""
lambda function to post process dynamodb events and publish to kinesis
using atomicId as the partion key
"""
import base64
import binascii
import datetime
import json
import os
import traceback
from collections import namedtuple

import app.src.data_structures.object_lookup.lookup as profile_lookup
import boto3
import botocore
from aws_lambda_powertools import Logger

logger = Logger(service=__name__)

kinesis_client = boto3.client("kinesis")
sqs_client = boto3.client("sqs")

EventTuple = namedtuple("EventTuple", ["partition_key", "data"])


def produce(messages: list) -> list:
    error_records = []
    for message in messages:
        logger.debug("raw kinesis message=%s", message)
        try:
            kinesis_data = base64_decode(message["kinesis"]["data"])
            event = deserialize_data(kinesis_data)
        except (ValueError, KeyError):
            traceback_error = traceback.format_exc()
            message["errorMessage"] = traceback_error
            # append message to error records and continue producing to kinesis
            error_records.append(message)
            continue

        try:
            kinesis_write_response = kinesis_client.put_record(
                StreamName=os.environ["KINESIS_STREAM_NAME"],
                PartitionKey=event.partition_key,
                Data=event.data.encode("utf-8"),
            )
            logger.debug(kinesis_write_response)
        except (
            botocore.exceptions.ParamValidationError,
            botocore.exceptions.ClientError,
        ):
            # swallow error and continue
            message["errorMessage"] = traceback.format_exc()
            error_records.append(message)
            continue
    return error_records


def base64_decode(data: bytes) -> str:
    try:
        # load the base64 decoded kinesis data
        decoded_data = base64.b64decode(data).decode("UTF-8")
        return decoded_data
    except (
        UnicodeDecodeError,
        binascii.Error,
    ) as error:
        raise ValueError("Failed base64 decode of data") from error


def deserialize_data(kinesis_data: str) -> EventTuple:
    try:
        # load the base64 decoded kinesis data
        kinesis_data = json.loads(kinesis_data)
        logger.debug("deserialized kinesis data kinesis_data=%s", kinesis_data)
        # convert object to dict

        event = profile_lookup.EventDeserializer.get_event_from_dynamo(kinesis_data["dynamodb"]["NewImage"]).to_dict()
        partition_key = event["atomicId"]
        # sanitize output by deleting atomicId
        del event["atomicId"]
        # return string version of dict
        return EventTuple(partition_key, json.dumps(event, default=str))
    except (
        KeyError,
        TypeError,
        json.JSONDecodeError,
    ) as error:
        raise ValueError(f"DynamoDB NewImage not detected in {error=}") from error


def validate_inputs() -> None:
    if os.environ.get("KINESIS_STREAM_NAME") is None:
        raise ValueError('os.environ["KINESIS_STREAM_NAME"] not set')
    if os.environ.get("DEADLETTER_QUEUE_URL") is None:
        raise ValueError('os.environ["DEADLETTER_QUEUE_URL"] not set')


def dlq_messages(error_messages: list, context) -> None:
    error_queue_url = os.environ["DEADLETTER_QUEUE_URL"]
    delay_seconds = os.environ.get("DLQ_DELAY_SECONDS", 0)
    for message in error_messages:
        logger.warning("Bad message found, sending to dlq message=%s", message)
        message_body = encode_dlq_message(message, context)
        try:
            response = sqs_client.send_message(
                QueueUrl=error_queue_url,
                DelaySeconds=delay_seconds,
                MessageBody=message_body,
            )
            logger.debug(response)
        except botocore.exceptions.ClientError as error:
            # swallow the error so that the batch of records are not sent back to kinesis
            logger.exception("Error sending to dlq error=%s", error)
            pass


def encode_dlq_message(message: dict, context) -> str:
    """_summary_
    https://docs.aws.amazon.com/lambda/latest/dg//with-kinesis.html#services-kinesis-errors
    {
    "requestContext": {
        "requestId": "c9b8fa9f-5a7f-xmpl-af9c-0c604cde93a5",
        "functionArn": "arn:aws:lambda:us-east-2:123456789012:function:myfunction",
        "condition": "RetryAttemptsExhausted",
        "approximateInvokeCount": 1
    },
    "responseContext": {
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Unhandled"
    },
    "version": "1.0",
    "timestamp": "2019-11-14T00:38:06.021Z",
    "KinesisBatchInfo": {
        "shardId": "shardId-000000000001",
        "startSequenceNumber": "49601189658422359378836298521827638475320189012309704722",
        "endSequenceNumber": "49601189658422359378836298522902373528957594348623495186",
        "approximateArrivalOfFirstRecord": "2019-11-14T00:38:04.835Z",
        "approximateArrivalOfLastRecord": "2019-11-14T00:38:05.580Z",
        "batchSize": 500,
        "streamArn": "arn:aws:kinesis:us-east-2:123456789012:stream/mystream"
    }
    }
    """
    response = {
        "requestContext": {
            "requestId": context.aws_request_id,
            "functionArn": context.invoked_function_arn,
            "condition": "Error",
            "approximateInvokeCount": 1,
        },
        "responseContext": {
            "statusCode": 200,
            "executedVersion": context.function_version,
            "functionError": message.get("errorMessage"),
        },
        "version": message.get("eventVersion"),
        "timestamp": str(datetime.datetime.now()),
        "KinesisBatchInfo": {
            "shardId": message.get("eventId"),
            "startSequenceNumber": message.get("kinesis", {}).get("sequenceNumber"),
            "endSequenceNumber": message.get("kinesis", {}).get("sequenceNumber"),
            "batchSize": 1,
            "approximateArrivalTimestampOfFirstRecord": message.get("kinesis", {}).get("approximateArrivalTimestamp"),
            "approximateArrivalTimestampOfLastRecord": message.get("kinesis", {}).get("approximateArrivalTimestamp"),
            "streamArn": message.get("eventSourceARN"),
        },
    }
    return json.dumps(response, default=str)


def lambda_handler(event: dict, context):
    logger.debug(event)
    # uncaught exceptions will cause the entire set of records to be sent to the dlq
    validate_inputs()
    failed_records = produce(event["Records"])
    dlq_messages(failed_records, context)
