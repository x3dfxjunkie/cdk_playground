"""Module for cross account lambda App code

    Returns:
        None
"""
import base64
import logging
from datetime import datetime

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_kinesis_session(role_arn: str, region_name: str, function_name: str):
    """Method to consistently set boto3 connections for cross account AWS work.

    Args:
        role_arn (str): The Amazon Resource Name (ARN) of the role to assume. Other Account
        region_name (str): The region of the target account.
        function_name (str): The function being executed. Used for role tracing. https://stackoverflow.com/a/60805113

    Returns:
        Union[boto3.client.kinesis, boto3.session, boto3.client.sts]:
            A connection to kinesis, with a temporary session credential, and the sts component of the account.
    """
    stsclient = boto3.client("sts")

    var_aws_account = stsclient.assume_role(
        RoleArn=role_arn,
        RoleSessionName=f"{function_name}-session",
    )

    var_aws_session = boto3.Session(
        aws_access_key_id=var_aws_account["Credentials"]["AccessKeyId"],
        aws_secret_access_key=var_aws_account["Credentials"]["SecretAccessKey"],
        aws_session_token=var_aws_account["Credentials"]["SessionToken"],
        region_name=region_name,
    )

    var_aws_kinesis = var_aws_session.client(service_name="kinesis", region_name=region_name)

    return var_aws_kinesis, var_aws_session, var_aws_account


def check_time_left(aws_account: dict, aws_kinesis, role_arn: str, region_name: str, function_name: str):
    """Method to check remaining time on boto3 connection and reset connection if session expires in < 300 seconds.

    Args:
        aws_account (dict): a boto3 client sts session, including credentials and experiation time
        aws_kinesis: botocore kinesis client class object
        role_arn (str): The Amazon Resource Name (ARN) of the role to assume. Other Account
        region_name (str): The region of the target account.
        function_name (str): The function being executed. Used for role tracing. https://stackoverflow.com/a/60805113


    Returns:
        Union[boto3.client.kinesis, boto3.client.sts]:
            A connection to kinesis and the sts component of the account.
    """
    expiration = aws_account["Credentials"]["Expiration"]
    logger.info("STS Expiration: %s, Time Left: %s", expiration, expiration.timestamp() - datetime.now().timestamp())

    time_left = int(aws_account["Credentials"]["Expiration"].timestamp() - datetime.now().timestamp())

    if time_left < 300:
        logger.info("STS expiring in < 300 seconds. Obtaining new login session")
        try:
            # this will execute when a session needs to be re-created for cross account access
            aws_kinesis, aws_session, aws_account = set_kinesis_session(role_arn, region_name, function_name)
            logger.info("aws_session created: %s", aws_session)

            logger.info(
                "STS Expiration: %s, Time Left: %s",
                aws_account["Credentials"]["Expiration"],
                aws_account["Credentials"]["Expiration"].timestamp() - datetime.now().timestamp(),
            )

        except Exception as e:
            raise RuntimeError("Could not check session") from e

    return aws_kinesis, aws_account


def put_kinesis(aws_kinesis, event: dict, stream_name: str):
    """
        Method process records from an kinesis stream event that triggers a lambda that will
        process each record an push into a target kinesis stream

    Args:
        aws_kinesis: botocore kinesis client class object
        event (dict): an event from a kinesis stream that is setup to trigger lambda
        stream_name (str): name of the target kinesis stream we are pushing records

    Returns:
        None
    """
    try:
        # collect the records
        records = []
        for record in event["Records"]:
            records.append(
                {
                    "Data": base64.b64decode(record["kinesis"]["data"]),
                    "PartitionKey": record["kinesis"]["partitionKey"],
                }
            )

        # add the record to kinesis
        aws_kinesis.put_records(Records=records, StreamName=stream_name)

    except Exception as e:
        raise RuntimeError("Could not put records into stream") from e
