"""
This Function is the handler function for the resource deleter.
Resource Deleter can delete IAM Roles, DynamoDB Tables, and DMS Tasks
Make sure to provide proper identifier
APPCONFIG: See code below for resource requirements
DMS TASK: Task ARN, Endpoint ARN, Instance ARN
DYNAMODB Table: Table Name
IAM Role: Role Name
EC2 KEYPAIRS: Key Pair Name

For more information see: /workspace/docs/runbooks/orphaned_resources.md
"""
import boto3
import json
from enum import Enum
from app.src.reliability.ResourceDeleter.lambda_function.utils.cloud_control_utils import (
    get_dms_operation_status,
    delete_resource,
    get_resource,
)

# CUSTOM EXCEPTIONS


class InvalidAppConfigResourceError(Exception):
    """Custom exception for invalid AppConfig Resource"""


class InvalidDMSResourceError(Exception):
    """Custom exception for invalid DMS Resource"""


class InvalidEC2ResourceError(Exception):
    """Custom exception for invalid EC2 Resource"""


class InvalidTypeNameError(Exception):
    """Custom exception for Invalid Type Names"""


# ENUMS FOR PROPER TYPE NAMES AND RESOURCES


class ValidAppConfigResource(str, Enum):
    """Valid AppConfig resources allowed for resource deleter"""

    APP: str = "AWS::AppConfig::Application"
    CONFIGPROFILE: str = "AWS::AppConfig::ConfigurationProfile"
    CONFIGVERSION: str = "AWS::AppConfig::HostedConfigurationVersion"


class ValidDMSResource(str, Enum):
    """Valid DMS resources allowed for resource deleter"""

    ENDPOINT: str = "AWS::DMS::Endpoint"
    INSTANCE: str = "AWS::DMS::ReplicationInstance"
    TASK: str = "AWS::DMS::ReplicationTask"


class ValidEC2Resource(str, Enum):
    """Valid EC2 resources allowed for resource deleter
    Only need KeyPair compatibility for now
    """

    KEYPAIR: str = "AWS::EC2::KeyPair"
    SG: str = "AWS::EC2::SecurityGroup"


class ValidTypeName(str, Enum):
    """Valid Type Names allowed for resource deleter"""

    APPCONFIG: str = "AWS::AppConfig"
    DMS: str = "AWS::DMS"
    DYNAMODB: str = "AWS::DynamoDB"
    EC2: str = "AWS::EC2"
    IAM: str = "AWS::IAM"


# MAIN LAMBDA FXN CODE


def lambda_handler(event: dict, _):
    """Entry point - will delegate proper aws resource client per typename and resource"""
    # Will throw a resource not found exception and better for DX

    # Get type name (ie. AWS::DMS::RESOURCE) and prefix (AWS::DMS)
    type_name = event.get("TypeName")
    type_name_prefix = "::".join(type_name.split("::")[0:2])  # Returns AWS::<ResourceType>

    identifier = event.get("Identifier")

    # Ensure type name matches respective client, and then calls fxn to delete resource
    match type_name_prefix:
        case ValidTypeName.APPCONFIG:
            client = boto3.client("appconfig")
            response = appconfig_handler(type_name=type_name, identifier=identifier, client=client)

        case ValidTypeName.DMS:
            client = boto3.client("dms")
            # Currently, this lambda supports DMS instances, endpoints, and tasks
            response = dms_handler(type_name=type_name, identifier=identifier, client=client)

        case ValidTypeName.EC2:
            client = boto3.client("ec2")
            response = ec2_handler(type_name=type_name, identifier=identifier, client=client)

        case ValidTypeName.IAM | ValidTypeName.DYNAMODB:
            client = boto3.client("cloudcontrol")
            response = cloudcontrol_handler(type_name=type_name, identifier=identifier, client=client)

        case _:
            raise InvalidTypeNameError(
                f"""
                  Invalid TypeName '{type_name_prefix}'
                  Valid TypeNames are: {[e.value for e in ValidTypeName]}"""
            )

    return json.loads(json.dumps(response, default=str))


# HANDLER FXNS FOR ALL AWS TYPE NAMES


def appconfig_handler(type_name, identifier, client):
    """Handles boto3 calls for AppConfig Resources: Application, ConfigurationProfile, HostedConfigurationVersion"""

    match type_name:
        case ValidAppConfigResource.APP:
            response = client.delete_application(ApplicationId=identifier)

        case ValidAppConfigResource.CONFIGPROFILE:
            # Turn payload into dictionary for required params for delete api call
            try:
                response = client.delete_configuration_profile(
                    ApplicationId=identifier["ApplicationId"],
                    ConfigurationProfileId=identifier["ConfigurationProfileId"],
                )
            except ValueError as exc:
                raise ValueError(
                    'Identifier for configuration profiles must be formatted as "Identifier : {"ApplicationId": "xxx","ConfigurationProfileId": "xxxx"}"'
                ) from exc

        case ValidAppConfigResource.CONFIGVERSION:
            try:
                response = client.delete_hosted_configuration_version(
                    ApplicationId=identifier["ApplicationId"],
                    ConfigurationProfileId=identifier["ConfigurationProfileId"],
                    VersionNumber=identifier["VersionNumber"],
                )
            except ValueError as exc:
                raise ValueError(
                    'Identifier for configuration profiles must be formatted as "Identifier : {"ApplicationId": "xxx","ConfigurationProfileId": "xxxx", "VersionNumber": "x"}"'
                ) from exc
        case _:
            raise InvalidAppConfigResourceError(
                f"""
                  Invalid ResourceType '{type_name}'
                  Valid TypeNames are: {[e.value for e in ValidAppConfigResource]}"""
            )

    return response


def cloudcontrol_handler(type_name, identifier, client):
    """Handles IAM resources among various others - use caution with undocumented resources"""
    get_resource(type_name, identifier, client=client)
    response = delete_resource(type_name, identifier, client=client)

    return response


def dms_handler(type_name, identifier, client):
    """Handles boto3 calls for DMS Resources - ENDPOINTS, INSTANCES, TASKS"""

    match type_name:
        case ValidDMSResource.ENDPOINT:
            response = client.delete_endpoint(EndpointArn=identifier)
            get_dms_operation_status(response["Endpoint"]["Status"])

        case ValidDMSResource.INSTANCE:
            response = client.delete_replication_instance(ReplicationInstanceArn=identifier)
            get_dms_operation_status(response["ReplicationInstance"]["ReplicationInstanceStatus"])

        case ValidDMSResource.TASK:
            response = client.delete_replication_task(ReplicationTaskArn=identifier)
            get_dms_operation_status(response["ReplicationTask"]["Status"])

        case _:
            raise InvalidDMSResourceError(
                f"""
                  Invalid ResourceType '{type_name}'
                  Valid TypeNames are: {[e.value for e in ValidDMSResource]}"""
            )

    return response


def ec2_handler(type_name, identifier, client):
    """Handles boto3 calls for EC2 Resources
    type_name: KeyPair | SecurityGroup
    identifier: KeyPair name | Security Group Name
    client: boto3 call to ec2 for resource
    """

    match type_name:
        case ValidEC2Resource.KEYPAIR:
            response = client.delete_key_pair(KeyName=identifier, DryRun=False)

        case ValidEC2Resource.SG:
            response = client.delete_security_group(GroupName=identifier)

        case _:
            raise InvalidEC2ResourceError(
                f"""
                  Invalid ResourceType '{type_name}'
                  Valid TypeNames are: {[e.value for e in ValidEC2Resource]}"""
            )

    return response
