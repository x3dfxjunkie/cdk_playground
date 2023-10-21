"""
Test Lambda for list app config
"""
import pytest
import json
import os
import io
from unittest.mock import patch
from botocore.response import StreamingBody
from app.src.load_testing.lambdas.get_list_app_config.lambda_function import lambda_handler


@pytest.fixture
def mock_appconfig_client():
    with patch("boto3.client") as mock_client:
        yield mock_client("appconfig")


sample_appconfig_response = {"Items": [{"Name": "prefix-app", "Id": "app-id"}], "NextToken": ""}

sample_profile_response = {"Items": [{"Id": "profile1-id"}]}

sample_json_content = b'{"data_contracts":["test_data"]}'
content_length = len(sample_json_content)

sample_version_response = {"Items": [{"VersionNumber": "1"}]}

hosted_config_response = {"Content": StreamingBody(io.BytesIO(sample_json_content), content_length=content_length)}


def test_lambda_handler(mock_appconfig_client):
    def side_effect_list(*args, **kwargs):
        if mock_appconfig_client.list_applications.call_count == 1:
            return {"Items": [{"Name": "prefix-app1", "Id": "app1-id"}], "NextToken": "0000"}
        else:
            return {"Items": [{"Name": "prefix-app2", "Id": "app2-id"}], "NextToken": None}

    mock_appconfig_client.list_applications.return_value = sample_appconfig_response
    mock_appconfig_client.list_applications.side_effect = side_effect_list
    mock_appconfig_client.list_configuration_profiles.return_value = sample_profile_response
    mock_appconfig_client.list_hosted_configuration_versions.return_value = sample_version_response

    # Set the environment variable
    os.environ["prefix"] = "prefix"
    event = {}
    handler = {}
    # Invoke the Lambda function
    result = lambda_handler(event, handler)

    # Assertions
    assert len(result) == 2
    if len(result) == 2:
        json_result = json.loads(result[0])
        assert json_result["name"] == "prefix-app1"
        assert json_result["data"]["application_id"] == "app1-id"
