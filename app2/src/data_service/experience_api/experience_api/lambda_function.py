"""
This module contains the lambda which processes requests for Experience API events.
"""
# import re

import os
import typing

import boto3
from aws_lambda_powertools import Logger

from app.src.data_service.experience_api.experience_api.request_handler import ExperienceRestAPIRequestHandler

logger = Logger(service=__name__)

dynamodb_table_resource = boto3.resource("dynamodb")
kinesis_client = boto3.client("kinesis")


def lambda_handler(event: dict, _context, request_handler: typing.Optional[ExperienceRestAPIRequestHandler] = None):
    """Lambda function handler for Experiences API endpoint.

    Args:
        event (dict): Event payload for AWS lambda function
        context: Lambda function context.
        request_handler (ExperienceRestAPIRequestHandler, optional): Class with business
        logic for processing the event. Defaults to None.

    Returns:
        dict: http response payload
    """

    # TODO: Grab OS variables for processing table names and pass to handler.
    events_table_name = os.environ.get("EXPERIENCE_EVENT_TABLE_NAME")
    identity_table_name = os.environ.get("IDENTITY_TABLE_NAME")
    identity_nodes_table_name = os.environ.get("IDENTITY_NODES_TABLE_NAME")
    identity_edges_table_name = os.environ.get("IDENTITY_EDGES_TABLE_NAME")
    profile_table_name = os.environ.get("PROFILE_TABLENAME")
    identity_notification_stream_name = os.environ.get("IDENTITY_NOTIFICATION_STREAM_NAME")

    request_handler = request_handler or ExperienceRestAPIRequestHandler(lambda_event=event, dynamodb_resource=dynamodb_table_resource, kinesis_client=kinesis_client, identity_table_name=identity_table_name, identity_nodes_table_name=identity_nodes_table_name, identity_edges_table_name=identity_edges_table_name, profile_table_name=profile_table_name, events_table_name=events_table_name, identity_notification_stream_name=identity_notification_stream_name)
    # request_params = request_handler.request_params

    # Commenting out until SWID can be implemented / GAM data is loaded.  For now, we'll be using ealinkid for POC.

    # TODO - move validate logic to request handler?
    # if request_params.id_type != "swid":
    #     return rest_api_response(status_code=400,
    #                              body={"error": "Invalid idType provided.  Only 'swid' currently supported."})

    # Validade SWID:
    # if not request_params.id or not re.match("^{[a-z|A-Z|\d|-]+}$", request_params.id):
    #     return rest_api_response(status_code=400,
    #                              body={"error": "Invalid SWID provided."})

    return request_handler.process()
