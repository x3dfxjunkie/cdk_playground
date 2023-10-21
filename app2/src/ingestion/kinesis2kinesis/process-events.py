import base64
import logging
import os
from datetime import datetime

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info("Start Lambda Time: %s" % datetime.now())

AWS_LAMBDA_FUNCTION_NAME = os.environ['AWS_LAMBDA_FUNCTION_NAME']
CROSS_ACCOUNT_ID = os.environ['cross_account_id']
CROSS_ACCOUNT_ROLE = os.environ['cross_account_g360_role_name']
REGION = os.environ['target_region']
ROLE_ARN = f"arn:aws:iam::{CROSS_ACCOUNT_ID}:role/{CROSS_ACCOUNT_ROLE}"
TARGET_KINESIS = os.environ['target_kinesis_stream']


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
    stsclient = boto3.client('sts')

    VAR_aws_account = stsclient.assume_role(
        RoleArn=role_arn,
        RoleSessionName=f'{function_name}-session',
    )

    VAR_aws_session = boto3.Session(
        aws_access_key_id=VAR_aws_account['Credentials']['AccessKeyId'],
        aws_secret_access_key=VAR_aws_account['Credentials']['SecretAccessKey'],
        aws_session_token=VAR_aws_account['Credentials']['SessionToken'],
        region_name=region_name
    )

    VAR_aws_kinesis = VAR_aws_session.client(
        service_name='kinesis', region_name=region_name)

    return VAR_aws_kinesis, VAR_aws_session, VAR_aws_account


aws_kinesis, aws_session, aws_account = set_kinesis_session(
    ROLE_ARN, REGION, AWS_LAMBDA_FUNCTION_NAME)


def lambda_handler(event, _context):

    global aws_session
    global aws_kinesis
    global aws_account

    logger.info("Start Lambda Function: %s" % datetime.now())
    logger.info("STS Expiration: %s, Time Left: %s" % (
        aws_account['Credentials']['Expiration'], aws_account['Credentials']['Expiration'].timestamp() - datetime.now().timestamp()))

    time_left = int(aws_account['Credentials']['Expiration'].timestamp(
    ) - datetime.now().timestamp())

    if time_left < 300:
        logger.info(
            "STS expiring in < 300 seconds. Obtaining new login session")
        try:

            # this will execute when a session needs to be re-created for cross account access
            aws_kinesis, aws_session, aws_account = set_kinesis_session(
                ROLE_ARN, REGION, AWS_LAMBDA_FUNCTION_NAME)

            logger.info("STS Expiration: %s, Time Left: %s" % (
                aws_account['Credentials']['Expiration'], aws_account['Credentials']['Expiration'].timestamp() - datetime.now().timestamp()))

        except:
            raise
    try:
        # collect the records
        records = []
        for record in event['Records']:

            records.append(
                {
                    'Data': base64.b64decode(record['kinesis']['data']),
                    'PartitionKey': record['kinesis']['partitionKey'],
                }
            )

        # add the record to kinesis
        aws_kinesis.put_records(
            Records=records,
            StreamName=TARGET_KINESIS
        )

    except:
        raise

    logger.info("End Lambda Function: %s" % datetime.now())
