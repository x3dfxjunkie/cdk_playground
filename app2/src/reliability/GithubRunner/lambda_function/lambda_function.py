""" This file contains the handler for the lambda webhook
"""

import json
import logging
import os
import sys

import boto3
from app.src.reliability.GithubRunner.lambda_function.models.api_gateway_event import ApiGatewayEvent
from app.src.reliability.GithubRunner.lambda_function.models.github_actions_event import GithubActionsEvent

sqs_client = None

LOGGER = logging.getLogger(__name__)
STREAMHANDLER = logging.StreamHandler(sys.stdout)
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
STREAMHANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(STREAMHANDLER)


def webhook_handler(event, _, client=None):
    # Memoize for warm lambdas
    # pylint: disable-next=redefined-outer-name
    sqs_client = client if client is not None else boto3.client("sqs")

    sqs_queue = os.environ["SQS_QUEUE_URL"]

    api_gateway_event = ApiGatewayEvent.from_dict(event)

    event_body = GithubActionsEvent.from_json(api_gateway_event.body)

    response = sqs_client.send_message(QueueUrl=sqs_queue, MessageBody=event_body.to_json())

    return {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": json.dumps(response)}


def scaler_handler(event, _):
    LOGGER.info(event)
    return event
