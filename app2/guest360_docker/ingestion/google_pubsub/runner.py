#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boto3 import resource
from http import HTTPStatus
from json import dumps
from logging import INFO, basicConfig, error, info
from time import time
from uuid import uuid1, uuid4


from pubsub_interface import PubSubtoKinesis


basicConfig(level=INFO)  # NOSONAR


def write_stream_to_s3(stream, **kwargs):
    """Write stream to a S3 bucket defined in the environmental variables"""

    try:
        file_name = str(uuid1())
        folder_name = str(int(time() * 1000))
        file_key = f"{kwargs['failed_msg_bucket_path']}{folder_name}/{file_name}"
        info(f"Full path is: {kwargs['failed_msg_bucket_name']}{file_key}")

        s3_resource = resource("s3")

        s3_object = s3_resource.Object(bucket_name=kwargs["failed_msg_bucket_name"], key=file_key)
        s3_put_result = s3_object.put(Body=stream)
        s3_put_result_status = s3_put_result.get("ResponseMetadata")

        if s3_put_result_status.get("HTTPStatusCode") == HTTPStatus.OK:
            info("Message %s was written to S3 ", file_name)
        else:
            error(f"Failed to write message {file_name}, the S3 response was: {dumps(s3_put_result_status),}")

    except Exception as e:
        error(f"Failed to write to S3, error: {e}")
        raise e


def put_record_into_kinesis(stream_message, kinesis_client, **kwargs):
    """Writes the input record into the Kinesis data stream."""

    partition_key = str(uuid4())

    try:
        response = kinesis_client.put_records(
            Records=[
                {"Data": stream_message, "PartitionKey": partition_key},
            ],
            StreamName=kwargs["kinesis_stream"],
        )

        if "ErrorCode" in response["Records"][0]:
            info("Message was not delivered to Kinesis")
            write_stream_to_s3(stream_message, **kwargs)
    except Exception as e:
        error(f"Failed to put message into kinesis. Error: {e}")
        raise e


def main():
    # Load environment variables into docker environment
    env_vars_keys = [
        "PUB_SUB_PROJECT",
        "PUB_SUB_SUBSCRIPTION",
        "GOOGLE_APPLICATION_CREDENTIALS",
        "FAILED_MSG_BUCKET_NAME",
        "FAILED_MSG_BUCKET_PATH",
        "KINESIS_STREAM",
    ]

    # Create clients for Kinesis and pubsub
    pk_interface = PubSubtoKinesis(env_vars=env_vars_keys, pubsub_stream_publisher=put_record_into_kinesis)

    # start digestion
    pk_interface.start_consuming_pubsub()


if __name__ == "__main__":
    main()
