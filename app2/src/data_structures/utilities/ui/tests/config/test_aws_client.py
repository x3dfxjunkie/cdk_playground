import os
import json
import pytest
from unittest.mock import patch
from app.src.data_structures.utilities.ui.dataclass_generator.config.aws_client import AWSClient
from app.src.data_structures.utilities.ui.tests.conftest import (
    PATCH_DATACLASS_GEN_DIR,
    AWS_SESSION_DATA,
    AWS_SECRET_MANAGER,
)


def test__init__():
    aws = AWSClient()
    assert aws.user_role_arn is None


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.aws_client.boto3.Session")
def test_aws_auth(boto3_session):
    boto3_session.return_value.client.return_value.assume_role.return_value = AWS_SESSION_DATA
    aws = AWSClient()
    response = aws.aws_auth()
    assert response
    assert response["Credentials"] == AWS_SESSION_DATA["Credentials"]


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.aws_client.boto3.Session")
def test_get_secrets_client(boto3_session):
    boto3_session.return_value.client.return_value.get_secret_value.return_value = AWS_SECRET_MANAGER
    secrets_dict = AWSClient().get_secrets_client("test/secrets/path")
    assert secrets_dict
    assert secrets_dict == json.loads(AWS_SECRET_MANAGER["SecretString"])
