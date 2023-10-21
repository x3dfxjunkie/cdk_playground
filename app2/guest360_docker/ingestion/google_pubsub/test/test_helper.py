#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from base64 import b64encode
from boto3 import client
from moto import mock_secretsmanager
from unittest import mock
from unittest.mock import patch, MagicMock
from os import environ

from app.guest360_docker.ingestion.google_pubsub.environment_variables import (
    get_aws_secret,
    convert_dict_to_json_file,
    load_env_vars,
)


def test_dump():
    data_in = '{"a": 1, "b": "some_word"}'
    data_filename = "non_existent_file.json"
    with patch("builtins.open", mock.mock_open()) as m:
        convert_dict_to_json_file(data_in, data_filename)

    m.assert_called_once_with(data_filename, "w", encoding="utf-8")
    handle = m()
    handle.write.assert_called_once_with(data_in)


@mock_secretsmanager
def test_get_aws_secret_string():
    secret_name = "SOMESECRETNAME"  # pragma: allowlist secret
    secret_data = "MyImportanteData"  # pragma: allowlist secret

    conn = client("secretsmanager", region_name="us-west-2")
    conn.create_secret(Name=secret_name, SecretString=secret_data)
    result = conn.get_secret_value(SecretId=secret_name)
    assert result["SecretString"] == secret_data

    func_data = get_aws_secret(secret_name, "us-west-2")

    assert func_data == secret_data


@mock_secretsmanager
def test_get_aws_secret_base64():
    secret_name = "SOMESECRETNAME"  # pragma: allowlist secret
    secret_data = "MyImportanteData"  # pragma: allowlist secret

    data_encoded = b64encode(secret_data.encode("ascii"))

    conn = client("secretsmanager", region_name="us-west-2")
    conn.create_secret(Name=secret_name, SecretBinary=data_encoded)

    func_data = get_aws_secret(secret_name, "us-west-2")

    assert func_data.decode("ascii") == secret_data


new_vars = {"NEW_VAR_1": "something1", "SOME_OTHER_VAR": "something_else"}


@pytest.fixture(params=new_vars)
def env_vars_setup(monkeypatch):
    for k, v in new_vars.items():
        monkeypatch.setenv(k, v)


def test_load_env_vars(env_vars_setup):
    env_vars_dict = load_env_vars(new_vars.keys())
    final_dict = {k.lower(): v for k, v in new_vars.items()}

    assert final_dict == env_vars_dict


@pytest.fixture()
def gac_data(monkeypatch):
    monkeypatch.setenv("GOOGLE_APPLICATION_CREDENTIALS", "someultrasecretname")
    monkeypatch.setenv("REGION", "us-west-2")


@patch("app.guest360_docker.ingestion.google_pubsub.environment_variables.get_aws_secret")
@patch("app.guest360_docker.ingestion.google_pubsub.environment_variables.convert_dict_to_json_file")
@mock_secretsmanager
def test_load_env_gac(mock_convert, mock_secret, gac_data):
    filename = "gac_file.json"
    env_var = "GOOGLE_APPLICATION_CREDENTIALS"
    mock_secret.return_value = '{"key": "secret"}'
    mock_convert.return_value = MagicMock()

    assert environ.get(env_var) == "someultrasecretname"
    new_dict = load_env_vars([env_var])
    mock_convert.assert_called_with('{"key": "secret"}', filename)
    assert new_dict == {env_var.lower(): filename}
    assert environ.get(env_var) == filename
