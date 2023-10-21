""" Code of the Lambda Function for the Lambda Authorizer """
import os
import json
import requests

from urllib.error import HTTPError
from aws_lambda_powertools import Logger
from app.src.data_service.api_authorizers.api_authorizers import policy_generator
from app.src.data_service.api_authorizers.api_authorizers.scope_map_provider import (
    APIAuthorizerDynamoDBScopeMapProvider,
)

logger = Logger(service=__name__)


def validate_input(event: dict) -> dict:
    """
    validate the input of the request
    """
    validated_config = {
        "validate_url": os.environ["AUTHZ_VALIDATE_URL"],
        "auth_token": event["headers"]["Authorization"].split(" ")[1],
        "account_id": event["requestContext"]["accountId"],
        "api_id": event["requestContext"]["apiId"],
    }

    return validated_config


def validate_token(url: str):
    """
    perform request for token validation url
    """
    try:
        response = requests.get(url, timeout=10)
        logger.debug("validate response %s", response.text)
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        logger.exception("API authorizer response = %s error = %s", response.text, http_err)
        raise http_err


# pylint: disable=unused-argument
def lambda_handler(
    event: dict,
    context,
):
    """
    Initial function for the lambda
    """
    logger.info("accessing lambda auth functions")

    scope_map_provider = APIAuthorizerDynamoDBScopeMapProvider(
        logger=logger,
        scope_map_table_name=os.environ["SCOPE_MAP_TABLE_NAME"],
    )

    config = validate_input(event)
    url = f"{config['validate_url']}/{config['auth_token']}"
    response = validate_token(url)
    scope_map = {}

    response_body = response.json()
    principal_id = response_body["client_id"]
    client_scopes = response_body.get("scope")

    if client_scopes:
        client_scopes = client_scopes.split(" ")
    scope_map["authorization"] = json.loads(json.dumps(scope_map_provider.scope_map, default=str))

    policy = policy_generator.generate_policy(
        scope_map=scope_map,
        principal=principal_id,
        account_id=config["account_id"],
        rest_api_id=config["api_id"],
        client_scopes=client_scopes,
    )

    logger.debug("Policy build document %s", policy)

    return policy
