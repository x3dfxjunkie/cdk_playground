"""
    This tests the Lambda function from a mock event
"""

import json
import os
import pathlib

import boto3
import pytest
from app.src.reliability.GithubRunner.lambda_function.lambda_function import webhook_handler
from app.src.reliability.GithubRunner.lambda_function.tests.utils.test_utils import modified_environ
from moto import mock_sqs


@mock_sqs
def test_lambda_function():
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "lambda_event.json"), "r", encoding="UTF-8") as outfile:
        example_event = json.load(outfile)

    client = boto3.client("sqs", region_name="us-east-1")

    response = client.create_queue(QueueName="webhook_queue")

    # SQS_QUEUE_URL is not set so this should fail
    with pytest.raises(Exception):
        webhook_handler(example_event, {}, client=client)

    with modified_environ(SQS_QUEUE_URL=response.get("QueueUrl")):
        response = webhook_handler(example_event, {}, client=client)
        assert response.get("statusCode") == 200
