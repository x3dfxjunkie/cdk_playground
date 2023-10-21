"""
Test Lambda for app config
"""
import pytest
import json
import os
import io
from unittest.mock import patch
from botocore.response import StreamingBody
from app.src.load_testing.lambdas.get_app_config.lambda_function import lambda_handler


@pytest.fixture
def mock_appconfig_client():
    with patch("boto3.client") as mock_client:
        yield mock_client("appconfig")


sample_json_content = b'{"data_contracts":["test_data"]}'
content_length = len(sample_json_content)

hosted_config_response = {"Content": StreamingBody(io.BytesIO(sample_json_content), content_length=content_length)}


def test_lambda_handler(mock_appconfig_client):
    def side_effect_hosted(*args, **kwargs):
        return {"Content": StreamingBody(io.BytesIO(sample_json_content), content_length=content_length)}

    mock_appconfig_client.get_hosted_configuration_version.return_value = hosted_config_response
    mock_appconfig_client.get_hosted_configuration_version.side_effect = side_effect_hosted
    # Set the environment variable
    os.environ["prefix"] = "prefix"
    event = {
        "app_config": {
            "name": "lst-use1-pr-4268-dlr-lightning-lane-app",
            "stack_extension": "dlr-lightning-lane",
            "data": {"application_id": "agn1s57", "configuration_profile_id": "sb1odfs", "version_number": 1},
        }
    }
    handler = {}
    # Invoke the Lambda function
    result = lambda_handler(event, handler)

    # Assertions
    assert len(result) == 1
    if len(result) == 1:
        json_result = json.loads(result[0])
        assert json_result["name"] == "lst-use1-pr-4268-dlr-lightning-lane-app"
        assert json_result["stack_extension"] == "dlr-lightning-lane"
