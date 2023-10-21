"""
This module contains implementation classes for the RestAPIRequestHandler ABC.
These are used to incapsulate the busines logic for processing rest api requests
in lambdas.
"""
import datetime as dt
import typing
from dataclasses import dataclass

from app.src.data_service.rest_api.rest_api.request_handler import RestAPIRequestHandler, rest_api_response
from app.src.data_structures.object_lookup import lookup


@dataclass
class ExperienceRestAPIRequestParams:
    """Typed representation of URL params passed in the API request."""

    id: str
    id_type: str


class ExperienceRestAPIRequestHandler(RestAPIRequestHandler):
    """
    Request handler implementation for experience events.  Primary purpose is to process a Rest API
    event from an AWS lambda.

    Init Args:
        lambda_event (dict): AWS lambda event.
        identity_table_resource (boto3.resource("dynamodb")): boto3 resource for identity resolution dynamodb table.
        experience_table_resource (boto3.resource("dynamodb")): boto3 resource for experience events dynamodb table.
    """

    def __init__(self, lambda_event: dict, dynamodb_resource, kinesis_client, identity_table_name, identity_nodes_table_name, identity_edges_table_name, events_table_name, profile_table_name, identity_notification_stream_name):
        query_params = lambda_event["queryStringParameters"]

        self.lambda_event = lambda_event
        self._request_params = ExperienceRestAPIRequestParams(id=query_params.get("id"), id_type=query_params.get("idType"))

        # Boto3 resources for identity and experience dynamodb tables:
        self.identity_table_resource = dynamodb_resource
        self.experience_table_resource = dynamodb_resource
        self.kinesis_client = kinesis_client

        # Identity and Processing/Dataclass lookup classes:
        self.lookup = lookup.DynamoDBLookupFactory.get_dynamodb_lookup(dynamodb_resource=dynamodb_resource, kinesis_client=kinesis_client, identity_table_name=identity_table_name, identity_nodes_table_name=identity_nodes_table_name, identity_edges_table_name=identity_edges_table_name, events_table_name=events_table_name, profile_table_name=profile_table_name, identity_notification_stream_name=identity_notification_stream_name)

    @property
    def request_params(
        self,
    ) -> ExperienceRestAPIRequestParams:
        return self._request_params

    def process(self) -> dict[str, typing.Any]:
        guest_atomic_id = self.lookup.atomic_id_lookup(domain=self.request_params.id_type, identifier=self.request_params.id)

        if not guest_atomic_id:
            return rest_api_response(
                status_code=204,
            )

        # Retrieve all experiences for this atomic id:
        # TODO - update to use date range params:
        experiences = self.lookup.get_events_from_profile(guest_atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 30))

        experiences_json = None
        if not experiences:
            return rest_api_response(
                status_code=204,
            )
        else:
            experiences_json = [experience.to_dict() for experience in experiences]

        return rest_api_response(body=experiences_json)
