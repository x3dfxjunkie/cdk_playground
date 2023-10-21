"""Script to get kinesis samples
Works only locally in the dev container using aws-saml-auth
"""

import boto3
import json
import time
import argparse
import os

from app.src.data_structures.data_contracts.tests.unit_testing_utils.global_unit_test_utils import (
    get_data_contracts_info,
    write_sample_file,
)

# User defined constants
USER_ROLE_ARN = "arn:aws:iam::543276908693:role/WDPR-GUEST360_DEVELOPER"
KINESIS_STREAM_ARN = "arn:aws:kinesis:us-east-1:543276908693:stream/"
SAMPLE_SIZE = 10000  # Final number of samples
KINESIS_MAX = 10000  # Records to pull from kinesis if the stream have different payloads
SHARDS = ["shardId-000000000000"]

# Constants
DATA_CONTRACT_MAPPING = get_data_contracts_info()


def get_kinesis_client():
    """Function to generate the kinesis client"""
    try:
        session = boto3.Session()
        sts = session.client("sts")
        response = sts.assume_role(RoleArn=USER_ROLE_ARN, RoleSessionName="kinesis-extractor")
    except:
        os.system("aws-saml-auth")

    session = boto3.Session()
    sts = session.client("sts")
    response = sts.assume_role(RoleArn=USER_ROLE_ARN, RoleSessionName="kinesis-extractor")
    new_session = boto3.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
    )
    kinesis_client = new_session.client("kinesis", region_name="us-east-1")
    return kinesis_client


def get_records(stream_arn: str, shard_id: str, limit: int) -> dict:
    """Function to get records from kinesis"""
    kinesis_client = get_kinesis_client()
    shard_iterator = kinesis_client.get_shard_iterator(
        ShardId=shard_id, ShardIteratorType="TRIM_HORIZON", StreamARN=stream_arn
    )["ShardIterator"]

    kinesis_response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=limit, StreamARN=stream_arn)

    records = kinesis_response["Records"]

    return json.loads(
        json.dumps(list(map(lambda record: record["Data"].decode("utf-8"), records)))
        .replace("\\n", "")
        .replace("\\t", "")
    )


def get_stream_data_directly(stream_name: str, kinesis_sample_size: int) -> list:
    """Function to iter over shards and append kinesis records"""
    sample = []
    for shard in SHARDS:
        sample.append(
            get_records(
                f"{KINESIS_STREAM_ARN}{stream_name}",
                shard,
                kinesis_sample_size,
            )
        )
        time.sleep(1)
    return sample


def get_key_value(item: dict, key: str) -> str:
    """Function to get the payload identifier value, for example the table_name value"""
    key_value = item
    for key_name in key.split("."):
        key_value = key_value[key_name]
    return str(key_value)


def filter_data(sample_data: list, key: str, value: str) -> list:
    """Function to filter data from a non filter stream data"""
    sample_filtered = []
    count = 0
    for shard_data in sample_data:  # Iter over all the shards
        if count == SAMPLE_SIZE:  # If the filtered sample have the right size
            break
        for item in shard_data:  # Iter of the records of the shard
            json_item = json.loads(item)
            item_value = get_key_value(json_item, key)  # Return the payload identifier

            if item_value == value:  # Is payload identifier the expected one?
                sample_filtered.append(json_item)  # Append the record
                count += 1
            if count == SAMPLE_SIZE:  # If the filtered sample have the right size
                break

    return sample_filtered


def get_stream_data_filtered(stream_name: str, key: str, value: str, kinesis_sample_size: int) -> list:
    """Function to get a non filter stream data and then apply a filter"""
    full_sample = get_stream_data_directly(stream_name, kinesis_sample_size)
    filtered_data = filter_data(full_sample, key, value)
    return filtered_data


def get_kinesis_data(metadata):
    """Function get kinesis data including the logic to filter if needed"""
    samples = []

    for stream in metadata["kinesis-stream"].keys():
        key_path_name = metadata["kinesis-stream"][stream]["key-path-name"]
        key_path_value = metadata["kinesis-stream"][stream]["key-path-value"]

        if (key_path_value == None) or (key_path_name == None):
            samples = get_stream_data_directly(stream, SAMPLE_SIZE)
        else:
            samples = get_stream_data_filtered(stream, key_path_name, key_path_value, KINESIS_MAX)
    return samples


def get_sample_from_stream(model_name: str) -> bool:
    """Function to get a sample file"""
    status = False

    if model_name in DATA_CONTRACT_MAPPING.keys():
        metadata = DATA_CONTRACT_MAPPING[model_name]
        samples = get_kinesis_data(metadata)

        if len(samples) > 0:
            write_sample_file(model_name, samples)
            status = True
        else:
            print(f"{model_name}: Couldn't find records for the model in the Kinesis stream.")
    else:
        print(f"{model_name}: Model is not mapped to a Kinesis stream in the mapping file.")

    return status


def main():
    # Define the program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, required=True)
    ARGS = parser.parse_args()
    get_sample_from_stream(ARGS.model_name)


if __name__ == "__main__":
    main()
