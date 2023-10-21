"""
Untagged Bucket Finder Lambda
"""
import json
import os
import logging

import boto3
import botocore.exceptions

logger = logging.getLogger()
logger.setLevel(logging.INFO)

region = os.getenv("AWS_REGION")
s3 = boto3.client("s3")
sns = boto3.client("sns", region_name=region)

TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")


def sns_publish(buckets: list):
    msg = {"UNTAGGED_BUCKET_COUNT": len(buckets), "UNTAGGED_BUCKETS": buckets}
    msg = json.dumps(msg, indent=2, default=str)
    logger.info(msg)
    if buckets:
        sns.publish(TopicArn=TOPIC_ARN, Message=msg)

    return msg


def lambda_handler(event: dict, context):
    untagged_buckets = []
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        bucket_name = bucket["Name"]
        try:
            s3.get_bucket_tagging(Bucket=bucket_name)
        except botocore.exceptions.ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchTagSet":
                untagged_buckets.append(bucket)

    return sns_publish(untagged_buckets)
