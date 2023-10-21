"""
This AWS Lambda function is designed to publish the results of the load/system test in s3 if the execution is from scheduled rule
"""
import os
import boto3
import logging
from datetime import datetime
from boto3.dynamodb.conditions import Key
from botocore.exceptions import BotoCoreError, ClientError

# Constants
TABLE_NAME = os.getenv("DDB_TABLE_RESULT")
DYNAMODB = boto3.resource("dynamodb", "us-east-1")
TABLE = DYNAMODB.Table(TABLE_NAME)
S3_BUCKET_NAME = "lst-use1-guest360-load-testing"
logger = logging.getLogger(__name__)


def lambda_handler(event, _):
    execution_name = event["executionid"]
    items = None

    # DDB
    try:
        key_condition_expression = Key("execution_name").eq(execution_name)
        response = TABLE.query(KeyConditionExpression=key_condition_expression)
        if not response["Items"]:
            return "No results tests were found in the test results table with the provided execution name."
        items = response["Items"]

    except (BotoCoreError, ClientError) as e:
        logger.error("An error occurred while retrieving values from the DynamoDB: %s", str(e))
        return "An error occurred while retrieving values from the DynamoDB."

    try:
        # S3
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_split = current_datetime.split(" ")
        year, month, day, hour = date_split[0].split("-") + [date_split[1].split(":")[0]]

        s3 = boto3.client("s3")
        s3_key = f"scheduled_executions/{year}/{month}/{day}/{hour}/execution-{current_datetime}.json"
        s3.put_object(Body=str(items), Bucket=S3_BUCKET_NAME, Key=s3_key)
        return "Items successfully uploaded to S3."

    except (BotoCoreError, ClientError) as e:
        logger.error("An error occurred while putting object in s3: %s", str(e))
        return "An error occurred while putting object in s3."
