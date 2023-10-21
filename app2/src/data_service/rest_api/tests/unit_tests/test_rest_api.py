import json
import logging
import os
import sys
from collections import namedtuple

import boto3
import moto
import pytest

import app.src.data_service.rest_api.rest_api.request_handler as request_handler

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

# create a stdout logger
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)

def test_rest_api_response_all_defaults():
    response = request_handler.rest_api_response()
    expected = {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {"content-type": "application/json"},
        "body": ""
    }
    assert response == expected