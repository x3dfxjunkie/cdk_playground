import json
import logging
import os
import sys
from collections import namedtuple

import boto3
import moto
import pytest

# from collections import namedtuple

# set log levels for nozy boto calls to info
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

# create a stdout logger
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class TestLambdaAuthorizer:
    """
    data_* creates parameterized tests from data in tests/data/<parameter file name>.py
    """

    authz_validate_url = "https://stg.authorization.go.com/validate/"
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
        monkeypatch.setenv("AUTHZ_VALIDATE_URL", self.authz_validate_url)
        monkeypatch.setenv("VALIDATOR_SCOPE_MAP_S3_BUCKET",
                           self.s3_bucket_name)
        monkeypatch.setenv("VALIDATOR_SCOPE_MAP_S3_OBJECT_KEY",
                           self.s3_bucket_object_key)

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
    def mock_s3_scope_mapv1(self, mock_os_environment, mock_s3_bucket, data_scope_maps):
        # start mock_s3 context
        s3_object = mock_s3_bucket.put_object(
            Key=self.s3_bucket_object_key,
            Body=bytes(json.dumps(data_scope_maps.scopemap, indent=2), "utf-8"),
        )
        yield s3_object

    def test_validate_input_with_expected_inputs(
        self,
        mock_s3,
    ):
        event = {
            "headers": {
                "Authorization": "Bearer foobar",
            },
            "requestContext": {"accountId": "123456789012", "apiId": "myapiid"},
        }
        # must include package here due to global boto resource declarations
        from app.src.data_service.api_authorizers.api_authorizers import \
            lambda_function

        config = lambda_function.validate_input(event=event)

        config_expected = {
            "validate_url": self.authz_validate_url,
            "auth_token": "foobar",
            "account_id": "123456789012",
            "api_id": "myapiid",
        }
        assert config.keys() == config_expected.keys()
        assert config.items() == config_expected.items()

    def test_validate_input_with_missing_data(
        self,
        mock_s3,
    ):
        from app.src.data_service.api_authorizers.api_authorizers import \
            lambda_function

        event = {
            "headers": {
                "Authorization": "Bearer foobar",
            },
            "requestContext": {"accountId": "123456789012", "apiId": "myapiid"},
        }
        del event["headers"]
        # must include package here due to global boto resource declarations
        with pytest.raises(KeyError) as error:
            config = lambda_function.validate_input(event=event)
        assert error.typename == "KeyError"
