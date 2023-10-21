import os

import boto3


def get_dynamodb_client():
    """
    Utility function to abstract away the boto3 client creation
    """
    aws_region = os.environ.get("AWS_DEFAULT_REGION")
    return boto3.client("dynamodb")


def get_dynamodb_resource(endpoint_url=None):
    aws_region = os.environ.get("AWS_DEFAULT_REGION")
    return boto3.resource("dynamodb", endpoint_url=endpoint_url, region_name=aws_region)


def get_kinesis_client(endpoint_url=None):
    aws_region = os.environ.get("AWS_DEFAULT_REGION")
    return boto3.client("kinesis", endpoint_url=endpoint_url, region_name=aws_region)


def get_dynamodb_client_testing():
    return boto3.client(
        "dynamodb",
        endpoint_url=os.environ["ENDPOINT_URL"],
        region_name=os.environ["AWS_DEFAULT_REGION"],
        aws_access_key_id=os.environ["ACCESS_ID"],
        aws_secret_access_key=os.environ["ACCESS_KEY"],
    )
