"""test init rds"""
import logging
import sys

import boto3
import pytest
from moto import mock_secretsmanager

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

# pylint: disable=W0613, C0415, W0621


@pytest.fixture
def mock_os_environment(monkeypatch):
    # monkeypatch all environment variables necessary w/out affecting OS environment
    monkeypatch.setenv("ENDPOINT", "db-master-1.aaaaaaaaaa.us-east-1.rds.amazonaws.com")
    monkeypatch.setenv("PORT", "3306")
    monkeypatch.setenv("USER", "testing")
    monkeypatch.setenv("DBNAME", "testing")
    monkeypatch.setenv("REGION", "us-east-1")
    monkeypatch.setenv("SECRET_NAME", "secret")


@mock_secretsmanager
def test_get_secret_value(mock_os_environment):
    # must include package here due to global boto resource declarations
    from app.src.load_testing.lambdas.init_rds import lambda_function

    conn = boto3.client("secretsmanager", region_name="us-east-1")

    conn.create_secret(Name="secret", SecretString='{"password":"foosecret"}')  #'pragma: allowlist secret'
    result = lambda_function.get_secret_value("password")
    assert result == "foosecret"
