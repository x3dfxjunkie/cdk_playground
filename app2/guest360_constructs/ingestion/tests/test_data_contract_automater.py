""" Test Data Contract Automater Construct to ensure resources are being provisioned"""
import pytest
from aws_cdk import App, Stack, assertions, Environment, aws_ec2
from app.guest360_constructs.ingestion.data_contract_automater import DataContractAutomater
import os
from pathlib import Path

TEST_CONTEXT = {
    "environment": "local",
    "stack_name": "testStack",
    "prefix": "test-prefix-use1",
    "region": "us-east-1",
}


@pytest.fixture
def app_stack():
    test_app = App(context=TEST_CONTEXT)
    test_stack = Stack(test_app, "TestStack", env=Environment(account="123456789", region="us-east-1"))
    stack_path = str(Path(os.getcwd()).parents[0])

    lambda_path = f"{stack_path}/bazel-bin/app/src/data_structures/utilities/ui/"
    lambda_file = f"{lambda_path}lambda_archive.zip"

    if not os.path.exists(lambda_path):
        os.makedirs(lambda_path)

    empty_zip_data = b"PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    if not os.path.isfile(lambda_file):
        with open(lambda_file, "wb") as zip_file:
            zip_file.write(empty_zip_data)

    vpc_endpoint = aws_ec2.InterfaceVpcEndpoint.from_interface_vpc_endpoint_attributes(
        test_stack, "vpc_endpoint", port=8888, vpc_endpoint_id="test"
    )

    DataContractAutomater(test_stack, "data_contract_automater", {"vpc_endpoints": [vpc_endpoint]})

    yield test_stack


def test_role(app_stack):  # pylint: disable=redefined-outer-name
    template = assertions.Template.from_stack(app_stack)
    template.has_resource("AWS::IAM::Role", {})


def test_lambda_function_provisioned(app_stack):  # pylint: disable=redefined-outer-name
    template = assertions.Template.from_stack(app_stack)
    template.has_resource("AWS::Lambda::Function", {})


def test_api_gateway(app_stack):  # pylint: disable=redefined-outer-name
    # Ensure API Gateway is Created
    # Ensure that it is using a VPC Endpoint
    template = assertions.Template.from_stack(app_stack)
    print(template.to_json())

    template.has_resource_properties(
        "AWS::ApiGateway::RestApi", {"EndpointConfiguration": {"Types": ["PRIVATE"], "VpcEndpointIds": ["test"]}}
    )
