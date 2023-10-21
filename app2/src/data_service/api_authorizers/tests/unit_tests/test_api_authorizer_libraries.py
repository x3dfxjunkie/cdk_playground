import json
import logging
import os
import sys
from collections import namedtuple

import boto3
import moto
import pytest

import app.src.data_service.api_authorizers.api_authorizers.policy_generator as policy_generator
from app.src.data_service.api_authorizers.api_authorizers.scope_map_provider import \
    APIAuthorizerS3ScopeMapProvider

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

# create a stdout logger
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class TestApiAuthorizerLibrary:
    """
    data_* creates parameterized tests from data in tests/data/<parameter file name>.py
    """

    s3_bucket_name = "bucket_test"
    s3_bucket_object_key = "path/to/my/object_test"

    @pytest.fixture
    def mock_os_environment(self, monkeypatch):
        # monkeypatch all environment variables necessary w/out affecting OS environment
        monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
        monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
        monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
        monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    @pytest.fixture
    def mock_s3(self, mock_os_environment):
        s3_types = namedtuple("s3_types", ["client", "resource"])
        with moto.mock_s3():
            yield s3_types(
                boto3.client(
                    "s3", region_name=os.environ["AWS_DEFAULT_REGION"]),
                boto3.resource(
                    "s3", region_name=os.environ["AWS_DEFAULT_REGION"]),
            )

    @pytest.fixture
    def mock_s3_bucket(self, mock_os_environment, mock_s3):
        s3_bucket = mock_s3.resource.Bucket(self.s3_bucket_name)
        s3_bucket.create()
        s3_bucket.Versioning().enable()
        yield s3_bucket

    @pytest.fixture
    def mock_s3_scope_map_provider(self, mock_os_environment, mock_s3_bucket):
        s3_scope_map_provider = APIAuthorizerS3ScopeMapProvider(logger=logger,
                                                                environment={"VALIDATOR_SCOPE_MAP_S3_BUCKET": self.s3_bucket_name,
                                                                             "VALIDATOR_SCOPE_MAP_S3_OBJECT_KEY": self.s3_bucket_object_key, })
        yield s3_scope_map_provider

    @ pytest.fixture
    def mock_s3_scope_mapv1(self, mock_os_environment, mock_s3_bucket, data_scope_maps):
        # start mock_s3 context
        s3_object = mock_s3_bucket.put_object(
            Key=self.s3_bucket_object_key,
            Body=bytes(json.dumps(
                data_scope_maps.scopemap, indent=2), "utf-8"),
        )
        yield s3_object

    @ pytest.fixture
    def mock_s3_scope_mapv2(self, mock_os_environment, mock_s3_bucket, data_scope_maps):
        # start mock_s3 context
        s3_object = mock_s3_bucket.put_object(
            Key=self.s3_bucket_object_key, Body=bytes(
                json.dumps({}, indent=2), "utf-8")
        )
        s3_object = mock_s3_bucket.put_object(
            Key=self.s3_bucket_object_key,
            Body=bytes(json.dumps(
                data_scope_maps.scopemap, indent=2), "utf-8"),
        )
        yield s3_object

    @ pytest.fixture
    def mock_scope_map(self, monkeypatch, data_scope_maps):
        def monkeypatch_read_scope_map_object(*args, **kwargs):
            return data_scope_maps.scopemap

        monkeypatch.setattr(APIAuthorizerS3ScopeMapProvider, "read_scope_map_object",
                            monkeypatch_read_scope_map_object)

    def test_read_scope_map_object_patch(self, mock_scope_map, mock_s3_scope_map_provider, data_scope_maps):
        """
        Test monkey patch data for authorize.read_scope_map_object
        """
        assert mock_s3_scope_map_provider.read_scope_map_object() == data_scope_maps.scopemap

    def test_generate_policy(self, mock_scope_map, mock_s3_scope_map_provider, data_scope_maps):
        """
        test generating a policy utilizing data_scope_maps data
        """
        policy_out = policy_generator.generate_policy(
            scope_map=mock_s3_scope_map_provider.scope_map,
            principal="myfakeprincipal",
            account_id="myfakeaccountid",
            rest_api_id="myfakerestapiid",
            client_scopes=data_scope_maps.scopes,
        )
        logger.debug("policy=%s", json.dumps(policy_out, indent=2))
        assert policy_out == data_scope_maps.policy

    def test_read_scope_map_object_v1(self, mock_s3, mock_s3_scope_mapv1, mock_s3_scope_map_provider, data_scope_maps):
        """
        test reading v1 version of s3 object
        """
        versions = mock_s3.resource.Bucket(self.s3_bucket_name).object_versions.filter(
            Prefix=self.s3_bucket_object_key
        )
        for version in versions:
            obj = version.get()
            logger.debug(
                "Object: %s-%s-%s-%s-%s",
                self.s3_bucket_name,
                self.s3_bucket_object_key,
                obj.get("VersionId"),
                obj.get("ContentLength"),
                obj.get("LastModified"),
            )
        scope_map = mock_s3_scope_map_provider.read_scope_map_object(
            mock_s3_scope_mapv1)
        logger.debug("scope_map=%s", json.dumps(scope_map, indent=2))
        assert scope_map == data_scope_maps.scopemap

    def test_read_scope_map_object_v2(self, mock_s3, mock_s3_scope_mapv2, mock_s3_scope_map_provider, data_scope_maps):
        """
        Show all versions and validate v2
        """
        versions = mock_s3.resource.Bucket(self.s3_bucket_name).object_versions.filter(
            Prefix=self.s3_bucket_object_key
        )
        for version in versions:
            obj = version.get()
            logger.debug(
                "Object: %s-%s-%s-%s-%s",
                self.s3_bucket_name,
                self.s3_bucket_object_key,
                obj.get("VersionId"),
                obj.get("ContentLength"),
                obj.get("LastModified"),
            )

        scope_map = mock_s3_scope_map_provider.read_scope_map_object(
            mock_s3_scope_mapv2)
        logger.debug("scope_map=%s", json.dumps(scope_map, indent=2))
        assert scope_map == data_scope_maps.scopemap
