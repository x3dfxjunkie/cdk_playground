"""
This AWS Lambda function is designed to execute the sfn from the scheduled rule
"""
import json
import boto3
import os


def lambda_handler(event, handler):
    # pylint: disable=unused-argument
    bucket_path = event.get("bucket_path")
    test_type = event.get("test_type")

    stepfunction_arn = os.getenv("SFN_ARN")
    client = boto3.client("stepfunctions", region_name="us-east-1")

    input_ = {"bucket_path": bucket_path, "test_type": test_type, "send_s3": "True"}
    client.start_execution(stateMachineArn=f"{stepfunction_arn}", input=json.dumps(input_))
