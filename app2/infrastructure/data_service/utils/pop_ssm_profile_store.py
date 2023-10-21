import json
import logging
import os
import sys

import aws_cdk as core
import aws_cdk.assertions as assertions
import boto3
import botocore
from aws_lambda_powertools import Logger

# sys.path.append("/workspace/code/infrastructure/cdk/stack/profile-api/profile_api")
# from profile_api.profile_api_stack import ProfileApiStack

AWS_REGION = os.environ["AWS_DEFAULT_REGION"]
# ENDPOINT_URL = "http://host.docker.internal:4566"
# os.environ["AWS_ACCESS_KEY_ID"] = "test"
# os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
# os.environ["AWS_DEFAULT_REGION"] = AWS_REGION
stack_name = os.environ["STACK"]

# ssm_client = boto3.client(
#     "ssm", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

ssm_client = boto3.client("ssm", region_name=AWS_REGION)
ssm_param_store_name = f"/{stack_name}/data-services/profile-lambda/config"


def create_stub():

    snowflake_conn = {
        "account": os.environ.get("account"),
        "user": os.environ.get("user"),
        "warehouse": os.environ.get("warehouse"),
        "database": os.environ.get("database"),
        "schema": os.environ.get("schema"),
        "private_key": os.environ.get("private_key"),
        "private_key_passphrase": os.environ.get("private_key_passphrase"),
    }

    # Create SSM param store for testing:
    try:
        ssm_client.put_parameter(
            Name=ssm_param_store_name,
            Value=json.dumps(snowflake_conn),
            Type="SecureString",
            Overwrite=True,
        )
    except Exception as error:
        # TODO - figure out class for botocore.errorfactory.ParameterAlreadyExists
        # logger.info("Parameter store already exists, no need to create.")
        print("error creating ssm params %s", error)

    #  ssm_client.delete_parameter(Name=ssm_param_store_name)


create_stub()


def test_cdk_env(cdk_env):
    print(f"cdk_env={cdk_env}")
