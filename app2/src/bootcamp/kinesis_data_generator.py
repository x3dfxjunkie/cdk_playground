"""
module to generate fake records to a kinesis stream
"""
import boto3
import botocore
import uuid
from faker import Faker
import json
import logging

logging.basicConfig(level=logging.INFO)  # NOSONAR this script does not contain any sensitive values that can be logged
logger = logging.getLogger(__name__)
faker = Faker()


def get_paritition_value():
    return str(uuid.uuid4())


def send_batch_to_kinesis(client, stream_name, batch_records):
    api_records = [{"Data": x, "PartitionKey": get_paritition_value()} for x in batch_records]
    try:
        logger.debug("writing to kinesis...")
        client.put_records(StreamName=stream_name, Records=api_records)
    except botocore.exceptions.ClientError as e:
        logger.error(e)


def sample_record():
    return {
        "name": faker.first_name(),
        "age": faker.random_number(digits=2),
        "birthdate": faker.past_date().strftime("%m-%d-%y"),
    }


def sample_incorrect_records():
    return {
        "name": faker.first_name(),
        "age": faker.random_number(digits=2),
        "birthdate": faker.past_date().strftime("%Y-%m-%d"),
    }


def send_batch(stream_name, client):
    total_records_sent = 0
    multiplier = 1
    while total_records_sent < 5000 * multiplier:
        records = []
        for _ in range(250):
            rec = sample_record()
            records.append(json.dumps(rec, default=str) + "\n")

            rec_2 = sample_incorrect_records()
            records.append(json.dumps(rec_2, default=str) + "\n")

        send_batch_to_kinesis(client=client, stream_name=stream_name, batch_records=records)
        total_records_sent += len(records)
        logger.debug(f"Total records sent to kinesis: {total_records_sent}")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    kinesis_stream_name = "test_stream"
    kinesis_client = boto3.client(
        "kinesis",
        endpoint_url="http://localstack:4566",  # NOSONAR localstack uses http
        aws_access_key_id="localstack",
        aws_secret_access_key="localstack",  # pragma: allowlist secret
    )

    send_batch(kinesis_stream_name, kinesis_client)
