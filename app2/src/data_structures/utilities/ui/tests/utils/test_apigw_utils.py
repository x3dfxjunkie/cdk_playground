"""This file tests out apigw_utils"""
import os
import pathlib
import json
from app.src.data_structures.utilities.ui.dataclass_generator.utils.apigw_utils import (
    generate_api_gateway_url,
    ApiGatewayRequestContext,
    add_prefix_to_path,
)


def test_obtain_url():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "api_gateway_event.json"), mode="r", encoding="utf8"
    ) as file:
        test_event = json.load(file)

    request_context: ApiGatewayRequestContext = ApiGatewayRequestContext.parse_obj(test_event["requestContext"])

    assert (
        generate_api_gateway_url(request_context)
        == "elw68tqwyl-vpce-0081be8a6c5e738e3.execute-api.us-east-1.amazonaws.com/latest/"
    )


def test_add_prefix():
    expected_url = "https://elw68tqwyl-vpce-0081be8a6c5e738e3.execute-api.us-east-1.amazonaws.com/latest/static/img/Data-Contract-Auto-Mater.png"
    current_url = "https://elw68tqwyl-vpce-0081be8a6c5e738e3.execute-api.us-east-1.amazonaws.com/static/img/Data-Contract-Auto-Mater.png"
    assert add_prefix_to_path(current_url, "latest") == expected_url

    # Case when latest is already in prefix
    expected_url = "https://elw68tqwyl-vpce-0081be8a6c5e738e3.execute-api.us-east-1.amazonaws.com/latest/static/img/Data-Contract-Auto-Mater.png"
    current_url = "https://elw68tqwyl-vpce-0081be8a6c5e738e3.execute-api.us-east-1.amazonaws.com/latest/static/img/Data-Contract-Auto-Mater.png"
    assert add_prefix_to_path(current_url, "latest") == expected_url
