"This module serves to make lambda_function.py more declarative and easier to unit test."
import time

import boto3


def get_dms_operation_status(operation_status):
    if operation_status in ("failed", "stopped", "stopping"):
        raise SystemError("Error deleting dms resource. If Instance, make sure to delete all associated tasks first")


def get_resource(type_name: str, identifier: str, client: boto3.client = None):
    if not client:
        client = boto3.client("cloudcontrol")

    return client.get_resource(TypeName=type_name, Identifier=identifier)


def get_resource_request_status(request_token: str, client: boto3.client = None):
    if not client:
        client = boto3.client("cloudcontrol")

    return client.get_resource_request_status(RequestToken=request_token)


def delete_resource(type_name: str, identifier: str, client: boto3.client = None):
    if not client:
        client = boto3.client("cloudcontrol")

    response = client.delete_resource(TypeName=type_name, Identifier=identifier)
    progress_event = response.get("ProgressEvent")
    request_token = progress_event.get("RequestToken")
    operation_status = progress_event.get("OperationStatus")

    while operation_status != "SUCCESS":
        time.sleep(1)
        response = get_resource_request_status(request_token, client)
        progress_event = response.get("ProgressEvent")
        request_token = progress_event.get("RequestToken")
        operation_status = progress_event.get("OperationStatus")
        if operation_status in ("FAILED", "CANCEL_IN_PROGRESS", "CANCEL_COMPLETE"):
            raise SystemError(
                progress_event.get(
                    "ErrorCode", progress_event.get("StatusMessage", "There was an error processing your request.")
                )
            )

    return response
