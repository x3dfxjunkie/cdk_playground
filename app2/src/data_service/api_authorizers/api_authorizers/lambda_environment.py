"""
Module that get variables from the environment.
"""
from typing import TypedDict


class APIAuthorizerS3ScopeMapProviderEnvironment(TypedDict):
    """Typed dictionary of Lambda environment variables expected for S3 scope map provider."""

    VALIDATOR_SCOPE_MAP_S3_BUCKET: str
    VALIDATOR_SCOPE_MAP_S3_OBJECT_KEY: str
    AUTHZ_VALIDATE_URL: str


class APIAuthorizerDynamoDBScopeMapProviderEnvironment(TypedDict):
    """Typed dictionary of Lambda environment variables expected for S3 scope map provider."""

    VALIDATOR_SCOPE_MAP_DYNAMODB_TABLE: str
    AUTHZ_VALIDATE_URL: str
