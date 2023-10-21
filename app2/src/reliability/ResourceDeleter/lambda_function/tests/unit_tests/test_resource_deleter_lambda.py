"""
    This tests the Resource Deleter Lambda from a mock event (APPCONFIG, DMS, DYNAMODB, EC2, IAM)
"""
# pylint: disable=C0415
import boto3
import importlib
import mock
import os
import pytest
from typing import Union

from moto import mock_appconfig, mock_dms, mock_dynamodb, mock_ec2, mock_iam, mock_kinesis
from .utils import mock_make_api_call

from app.src.reliability.ResourceDeleter.lambda_function.lambda_function import (
    lambda_handler,
    InvalidAppConfigResourceError,
    InvalidDMSResourceError,
    InvalidEC2ResourceError,
    InvalidTypeNameError,
)

# Environment Variable. Did this to appease sonarqube.
mock_string = "botocore.client.BaseClient._make_api_call"

REPLICATION_TASK_PROPS = {
    "ReplicationTaskIdentifier": "dmsreplicationtask01",
    "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:source-endpoint",
    "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:target-endpoint",
    "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:ABCDE12345ABCDE12",
    "MigrationType": "full-load-and-cdc",
    "TableMappings": '{"TableMappings": [{"Type": "Include", "SourceSchema": "schema1", "SourceTable": "table1", "TargetTable": "table1"}, {"Type": "Exclude", "SourceSchema": "schema2", "SourceTable": "table2"}]}',
    "ReplicationTaskSettings": '{"TargetMetadata": {"TargetSchema": "target_schema"}}',
}


@mock_appconfig
class TestAppConfigLambda:
    """Test Class to Test AppConfig Resource Deletion: Application and Config Profile"""

    def create_resources(self, monkeypatch):
        """Creating App and config profile for testing"""

        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

        # Instantiate dms client
        appconfig_client = boto3.client("appconfig", region_name="us-east-1")

        app_payload = appconfig_client.create_application(
            Name="TestApp", Description="TestApp to delete for testing resource deleter", Tags={"tag": "tag_value"}
        )

        app_identifier = app_payload["Id"]

        config_payload = appconfig_client.create_configuration_profile(
            ApplicationId=app_identifier,
            Name="TestConfigProfile",
            Description="Test to delete profiles",
            LocationUri="hosted",
        )

        config_identifier = config_payload["Id"]

        return config_identifier, app_identifier, appconfig_client

    def test_delete_config(self, monkeypatch):
        """FXN to test deleting configuration profile"""

        config_identifier, app_identifier, appconfig_client = self.create_resources(monkeypatch)

        with mock.patch(mock_string, new=mock_make_api_call):
            response = lambda_handler(
                {
                    "TypeName": "AWS::AppConfig::ConfigurationProfile",
                    "Identifier": {
                        "ApplicationId": app_identifier,
                        "ConfigurationProfileId": config_identifier,
                    },
                },
                None,
            )
            assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

            with pytest.raises(Exception):
                appconfig_client.get_configuration_profile(
                    ApplicationId=app_identifier, ConfigurationProfileId=config_identifier
                )

    def test_delete_app(self, monkeypatch):
        """FXN to test deleting application"""

        _, app_identifier, appconfig_client = self.create_resources(monkeypatch)

        with mock.patch(mock_string, new=mock_make_api_call):
            response = lambda_handler(
                {"TypeName": "AWS::AppConfig::Application", "Identifier": app_identifier},
                None,
            )
            assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

            # Test to make sure application was deleted
            with pytest.raises(Exception):
                appconfig_client.get_application(ApplicationId=app_identifier)
                print("If application not deleted, this will not raise exception and will fail test")


@mock_dms
def test_dms_lambda_function(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    # Instantiate dms client
    dms_client = boto3.client("dms", region_name="us-east-1")

    # Create and start two DMS tasks
    replication_task_1 = {**REPLICATION_TASK_PROPS, "ReplicationTaskIdentifier": "prd-use1-g360-dreams-dine-cdc3"}
    response_task_1 = dms_client.create_replication_task(**replication_task_1)

    # Get ARNS
    dms_replication_task_1_arn = response_task_1["ReplicationTask"]["ReplicationTaskArn"]

    with mock.patch(mock_string, new=mock_make_api_call):
        response = lambda_handler(
            {"TypeName": "AWS::DMS::ReplicationTask", "Identifier": dms_replication_task_1_arn},
            None,
        )

        assert response["ReplicationTask"]["Status"] == "deleting"


@mock_ec2
def test_ec2_lambda_function(monkeypatch):
    """Test deleting keypairs on ec2"""
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    ec2_client = boto3.client("ec2", region_name="us-east-1")
    identifier = "TestKeyPair"
    ec2_client.create_key_pair(KeyName=identifier, DryRun=False)
    ec2_client.create_security_group(Description=identifier, GroupName=identifier, DryRun=False)
    # DELETE KEY PAIR
    with mock.patch(mock_string, new=mock_make_api_call):
        response = lambda_handler({"TypeName": "AWS::EC2::KeyPair", "Identifier": identifier}, None)
        assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

    # DELETE KEY PAIR
    with mock.patch(mock_string, new=mock_make_api_call):
        response = lambda_handler({"TypeName": "AWS::EC2::SecurityGroup", "Identifier": identifier}, None)
        assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


@mock_dynamodb
@mock_kinesis
def test_dynamo_lambda_function(monkeypatch):
    from app.src.data_structures.tests.utils.setup_dynamodb import setup_dynamodb

    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    table_name = "TEST_TABLE"
    setup_dynamodb(
        table_name, "identity_nodes", "identity_edges", "profile", "events", "identity_notification_stream", True
    )

    with mock.patch(mock_string, new=mock_make_api_call):
        response = lambda_handler({"TypeName": "AWS::DynamoDB", "Identifier": table_name}, None)
        assert isinstance(response.get("ProgressEvent").get("EventTime"), str)

        assert (
            response.get("ProgressEvent").get("Operation") == "DELETE"
            and response.get("ProgressEvent").get("OperationStatus") == "SUCCESS"
        )


@mock_iam
def test_iam_lambda_function(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    iam_client = boto3.client("iam", region_name="us-east-1")
    iam_client.create_instance_profile(InstanceProfileName="my-profile", Path="my-path")
    iam_client.create_role(RoleName="my-role", AssumeRolePolicyDocument="some policy", Path="/my-path/")

    with mock.patch(mock_string, new=mock_make_api_call):
        response = lambda_handler({"TypeName": "AWS::IAM", "Identifier": "my-role"}, None)
        assert isinstance(response.get("ProgressEvent").get("EventTime"), str)

        assert (
            response.get("ProgressEvent").get("Operation") == "DELETE"
            and response.get("ProgressEvent").get("OperationStatus") == "SUCCESS"
        )

        with pytest.raises(Exception):
            # Should be deleted
            lambda_handler({"TypeName": "AWS::IAM", "Identifier": "my-role"}, None)


class TestCustomExceptions:
    """Test Class to Test Custom Exceptions"""

    def test_invalid_appconfig_resource_error(self, monkeypatch):
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

        with pytest.raises(InvalidAppConfigResourceError) as excinfo:
            lambda_handler(
                {"TypeName": "AWS::AppConfig::Invalid", "Identifier": "TASK_TEST_ARN"},
                None,
            )
        error = "".join(str(excinfo.value).split())
        assert (
            error
            == """InvalidResourceType'AWS::AppConfig::Invalid'ValidTypeNamesare:['AWS::AppConfig::Application','AWS::AppConfig::ConfigurationProfile','AWS::AppConfig::HostedConfigurationVersion']"""
        )

    def test_invalid_dms_resource_error(self, monkeypatch):
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

        with pytest.raises(InvalidDMSResourceError) as excinfo:
            lambda_handler(
                {"TypeName": "AWS::DMS::Replication", "Identifier": "TASK_TEST_ARN"},
                None,
            )
        error = "".join(str(excinfo.value).split())
        assert (
            error
            == """InvalidResourceType'AWS::DMS::Replication'ValidTypeNamesare:['AWS::DMS::Endpoint','AWS::DMS::ReplicationInstance','AWS::DMS::ReplicationTask']"""
        )

    def test_invalid_ec2_resource_error(self, monkeypatch):
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

        with pytest.raises(InvalidEC2ResourceError) as excinfo:
            lambda_handler(
                {"TypeName": "AWS::EC2::Invalid", "Identifier": "TASK_TEST_ARN"},
                None,
            )
        error = "".join(str(excinfo.value).split())
        assert (
            error
            == """InvalidResourceType'AWS::EC2::Invalid'ValidTypeNamesare:['AWS::EC2::KeyPair','AWS::EC2::SecurityGroup']"""
        )

    def test_invalid_type_name_error(self, monkeypatch):
        monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

        with pytest.raises(InvalidTypeNameError) as excinfo:
            lambda_handler(
                {"TypeName": "AWS::WRONG::ReplicationTask", "Identifier": "TASK_TEST_ARN"},
                None,
            )
        error = "".join(str(excinfo.value).split())
        print(error)
        assert (
            error
            == """InvalidTypeName'AWS::WRONG'ValidTypeNamesare:['AWS::AppConfig','AWS::DMS','AWS::DynamoDB','AWS::EC2','AWS::IAM']"""
        )
