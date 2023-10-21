"""
    This class contains test utility functions
"""
import json
import random
from datetime import datetime

import boto3
import botocore
from faker import Faker

# Original botocore _make_api_call function
# pylint: disable-next=protected-access
orig = botocore.client.BaseClient._make_api_call


def mock_make_api_call(self, operation_name, kwarg):
    print("OPERATION_NAME: ", operation_name)
    print("KWARGS_: ", kwarg)

    if operation_name == "GetResource":
        # Under the hood, GetResources calls the api for the type
        # E.g. if TypeName is AWS:IAM, it calls AWS::IAM resource calls
        type_name = kwarg.get("TypeName")

        identifier = kwarg.get("Identifier")

        if type_name == "AWS::IAM":
            client = boto3.client("iam", region_name="us-east-1")
            response = client.get_role(RoleName=identifier)
            properties = json.dumps(response["Role"], default=str)
            return {"TypeName": type_name, "ResourceDescription": {"Identifier": identifier, "Properties": properties}}
        if type_name == "AWS::DynamoDB":
            client = boto3.client("dynamodb", region_name="us-east-1")
            response = client.describe_table(TableName=identifier)
            properties = json.dumps(response["Table"], default=str)
            return {"TypeName": type_name, "ResourceDescription": {"Identifier": identifier, "Properties": properties}}

    if operation_name == "GetResourceRequestStatus":
        request_token = kwarg.get("RequestToken")
        return {
            "ProgressEvent": {
                "TypeName": "Some Resource",
                "Identifier": "Some Identifier",
                "RequestToken": request_token,
                "Operation": "DELETE",
                "OperationStatus": random.choice(["IN_PROGRESS", "SUCCESS"]),
                "EventTime": datetime(2015, 1, 1),
                "ResourceModel": "Some Model",
                "StatusMessage": "Some Message",
            }
        }

    if operation_name == "DeleteResource":
        type_name = kwarg.get("TypeName")
        identifier = kwarg.get("Identifier")

        faker = Faker()
        Faker.seed(321)
        request_token = faker.uuid4()

        if type_name == "AWS::IAM":
            client = boto3.client("iam", region_name="us-east-1")
            client.delete_role(RoleName=identifier)
            return {
                "ProgressEvent": {
                    "TypeName": type_name,
                    "Identifier": identifier,
                    "RequestToken": request_token,
                    "Operation": "DELETE",
                    "OperationStatus": "IN_PROGRESS",
                    "EventTime": datetime(2015, 1, 1),
                    "ResourceModel": "Some Model",
                    "StatusMessage": "Some Message",
                }
            }
        return {
            "ProgressEvent": {
                "TypeName": "Some Resource",
                "Identifier": "Some Identifier",
                "RequestToken": request_token,
                "Operation": "DELETE",
                "OperationStatus": "IN_PROGRESS",
                "EventTime": datetime(2015, 1, 1),
                "ResourceModel": "Some Model",
                "StatusMessage": "Some Message",
            }
        }

    return orig(self, operation_name, kwarg)
