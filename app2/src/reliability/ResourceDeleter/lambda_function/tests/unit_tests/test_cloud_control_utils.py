""" Tests each cloud control util function with moto
"""
from unittest import TestCase, mock

import boto3
import pytest
from app.src.reliability.ResourceDeleter.lambda_function.utils import cloud_control_utils
from faker import Faker
from moto import mock_iam

from .utils import mock_make_api_call


@mock_iam
class CloudControlTests(TestCase):
    """
    Contains Tests for the cloud control API
    """

    client: boto3.client

    def setUp(self):
        self.client = boto3.client("iam", region_name="us-east-1")

    def test_get_resource(self):
        self.client.create_instance_profile(InstanceProfileName="my-profile", Path="my-path")
        self.client.create_role(RoleName="my-role", AssumeRolePolicyDocument="some policy", Path="/my-path/")
        self.client.add_role_to_instance_profile(InstanceProfileName="my-profile", RoleName="my-role")
        role = self.client.get_role(RoleName="my-role")["Role"]

        assert role["Path"] == "/my-path/"
        assert role["AssumeRolePolicyDocument"] == "some policy"
        profile = self.client.get_instance_profile(InstanceProfileName="my-profile")["InstanceProfile"]
        assert profile["Path"] == "my-path"

        assert len(profile["Roles"]) == 1
        role_from_profile = profile["Roles"][0]
        assert role_from_profile["RoleId"] == role["RoleId"]
        assert role_from_profile["RoleName"] == "my-role"

        assert self.client.list_roles()["Roles"][0]["RoleName"] == "my-role"

        cloud_control_client = boto3.client("cloudcontrol", region_name="us-east-1")

        with mock.patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
            resource = cloud_control_utils.get_resource("AWS::IAM", "my-role", cloud_control_client)

            assert resource.get("ResourceDescription").get("Identifier") == "my-role"

            with pytest.raises(Exception):
                resource = cloud_control_utils.get_resource("AWS::IAM", "non-existing-role", cloud_control_client)

    def test_get_resource_request_status(self):
        cloud_control_client = boto3.client("cloudcontrol", region_name="us-east-1")

        with mock.patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
            faker = Faker()
            Faker.seed(4321)
            request_token = faker.uuid4()
            request = cloud_control_utils.get_resource_request_status(request_token, cloud_control_client)

            assert request.get("ProgressEvent").get("RequestToken") == request_token

    def test_delete_resource(self):
        self.client.create_instance_profile(InstanceProfileName="my-profile", Path="my-path")
        self.client.create_role(RoleName="my-role", AssumeRolePolicyDocument="some policy", Path="/my-path/")

        cloud_control_client = boto3.client("cloudcontrol", region_name="us-east-1")

        with mock.patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
            cloud_control_utils.get_resource("AWS::IAM", "my-role", cloud_control_client)  # Ensures my-role exists
            request = cloud_control_utils.delete_resource("AWS::IAM", "my-role", cloud_control_client)

            assert request.get("ProgressEvent").get("Operation") == "DELETE"
            with pytest.raises(Exception):
                cloud_control_utils.get_resource(
                    "AWS::IAM", "my-role", cloud_control_client
                )  # Ensures my-role is deleted
