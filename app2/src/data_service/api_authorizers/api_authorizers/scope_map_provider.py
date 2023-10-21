""" Package that get the scope map from different locations (DynamoDB, S3 or Local File) """
import io
import json
import logging
import typing
from abc import ABC, abstractmethod
from enum import Enum

import boto3
import botocore
from aws_lambda_powertools import Logger

from app.src.data_service.api_authorizers.api_authorizers.lambda_environment import (
    APIAuthorizerS3ScopeMapProviderEnvironment,
)


class APIAuthorizerScopeMapProviderStoreType(Enum):
    """Enumeration of possible provider storage locations for scope map (i.e. where scope map document is stored)."""

    S3 = "S3"
    LOCAL_FILE = "LOCAL_FILE"
    DYNAMODB = "DYNAMODB"


class APIAuthorizerScopeMapProvider(ABC):
    """Interface for scope map provider classes.  Allows type of provider to be passed generally, and implementation handled by subclass."""

    @property
    @abstractmethod
    def store_type(self) -> APIAuthorizerScopeMapProviderStoreType:
        pass

    @property
    @abstractmethod
    def lambda_environment(self) -> dict:
        pass

    @property
    @abstractmethod
    def scope_map(self) -> dict:
        pass


class APIAuthorizerS3ScopeMapProvider(APIAuthorizerScopeMapProvider):
    """
    Encapsulates logic to get API validator scope map document from an S3 bucket.
    The scope map document simply maps AuthZ scopes to URLs to determine what scopes
    have access to what URLs/method combinations.
    """

    def __init__(
        self,
        environment: APIAuthorizerS3ScopeMapProviderEnvironment,
        logger: typing.Optional[logging.Logger] = Logger(service=__name__),
        s3_client=boto3.resource("s3"),
    ):
        self.s3_client = s3_client
        self.environment = environment
        self.scope_map_bucket_name = environment.get("VALIDATOR_SCOPE_MAP_S3_BUCKET")
        self.scope_map_object_key = environment.get("VALIDATOR_SCOPE_MAP_S3_OBJECT_KEY")
        self.logger = logger

    @property
    def lambda_environment(self) -> dict:
        """
        Returns environment variables associated with this scope map provider type, generally to be used in lambda environment.
        For example, contains the name of the S3 bucket and key so that the lambda can access the map through boto.
        """
        return dict(self.environment)

    @property
    def store_type(self) -> APIAuthorizerScopeMapProviderStoreType:
        return APIAuthorizerScopeMapProviderStoreType.S3

    def read_scope_map_object(
        self,
        s3_object,
    ) -> dict:
        """
        Read boto3 s3 object and return json dictionary
        """
        # read scope_map json
        try:
            # ensure object is accessible
            s3_object.load()

            with io.BytesIO() as file:
                s3_object.download_fileobj(file)
                file.seek(0)
                scope_map = json.loads(file.read().decode("utf-8"))
        except botocore.exceptions.ClientError as error:
            self.logger.exception("boto ClientError caught while reading scope_map, error=%s", error)
            raise error
        except (io.UnsupportedOperation, io.BlockingIOError) as error:
            self.logger.exception("Failed reading file due to IO, error=%s", error)
            raise error
        return scope_map

    @property
    def scope_map(self) -> dict:
        """Retuns the associated scope map json (as dict)."""
        try:
            s3_object = self.s3_client.Object(
                self.scope_map_bucket_name,
                self.scope_map_object_key,
            )
            return self.read_scope_map_object(s3_object)
        except botocore.exceptions.ClientError as error:
            self.logger.exception(error)
            raise error


class APIAuthorizerLocalFileScopeMapProvider(APIAuthorizerScopeMapProvider):
    """
    Encapsulates logic to get API validator scope map document from a local file in the lambda runtime.
    """

    # TODO - this should eventually be a yaml file instead of py dict.

    def __init__(self, scope_map_dict: dict = None) -> None:
        self._scope_map = scope_map_dict

    @property
    def store_type(self) -> APIAuthorizerScopeMapProviderStoreType:
        return APIAuthorizerScopeMapProviderStoreType.LOCAL_FILE

    @property
    def lambda_environment(self) -> dict:
        pass

    @property
    def scope_map(self) -> dict:
        return self._scope_map


class APIAuthorizerDynamoDBScopeMapProvider(APIAuthorizerScopeMapProvider):
    """
    Encapsulates logic to get API validator scope map document from a DynamoDB Table.
    The scope map document simply maps AuthZ scopes to URLs to determine what scopes
    have access to what URLs/method combinations.
    """

    def __init__(
        self,
        logger: typing.Optional[logging.Logger] = Logger(service=__name__),
        dynamodb_client=boto3.resource("dynamodb", region_name="us-east-1"),
        scope_map_table_name: str = "scope_map_table",
    ):
        self.dynamodb_client = dynamodb_client
        self.table = dynamodb_client.Table(scope_map_table_name)  # TODO - Name of the table
        self.logger = logger
        self._scope_map = None

    @property
    def lambda_environment(self) -> dict:
        """
        Returns environment variables associated with this scope map provider type
        """
        return dict(self.environment)

    @property
    def store_type(self) -> APIAuthorizerScopeMapProviderStoreType:
        return APIAuthorizerScopeMapProviderStoreType.DYNAMODB

    def read_scope_map_object(self) -> dict:
        """
        Read boto3 dynamodb object and return json dictionary
        """
        # read scope_map json
        try:
            # ensure object is accessible
            response = self.table.scan()
        except botocore.exceptions.ClientError as error:
            self.logger.exception("boto ClientError caught while reading scope_map, error=%s", error)
            raise error
        except (io.UnsupportedOperation, io.BlockingIOError) as error:
            self.logger.exception("Failed reading file due to IO, error=%s", error)
            raise error
        return response["Items"]

    @property
    def scope_map(self) -> dict:
        """Retuns the associated scope map json (as dict)."""
        try:
            # return self._scope_map
            return self.read_scope_map_object()
        except botocore.exceptions.ClientError as error:
            self.logger.exception(error)
            raise error
