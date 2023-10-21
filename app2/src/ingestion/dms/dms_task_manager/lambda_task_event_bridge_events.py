""" Lambda Function Code for DMS  Task Event Bridge Events
    Used to track two event bridge events: "REPLICATION_TASK_STARTED","REPLICATION_TASK_FAILED"

    For REPLICATION_TASK_FAILED  dms task events it will send a custom metric to CloudWatch but not restart the failed ones because DMS itself tries to restart failed tasks by default:
    https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ErrorHandling.html
    In case it is required that task manager restarts failed tasks,just  refactor function handle_dms_failed_task.

    For REPLICATION_TASK_STARTED it will validate REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS times if the dms task is running without error
    then clean the record on dynamoDB table and send the value of 0 to the custom metric.
"""
import os
import time
import json
import boto3
import botocore
from aws_lambda_powertools import Logger, Metrics

from app.src.ingestion.dms.dms_task_manager.task_manager_utils import (
    DMSReplicationTaskStatus,
    DMSReplicationTaskEventType,
)

# Make environment variables changes on DMSTaskManagerStack
TABLE_NAME = os.getenv("TABLE_NAME")
NAMESPACE = os.getenv("NAMESPACE", "DMSTaskFailed")
REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS = int(os.getenv("REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS", "15"))
REP_TASK_TIME_TO_WAIT_IN_SECONDS = int(os.getenv("REP_TASK_TIME_TO_WAIT_IN_SECONDS", "10"))
REP_TASK_FAILURE_METRIC = os.getenv("REP_TASK_FAILURE_METRIC", "CustomDMSTaskFailure")


logger = Logger(service=__name__, level="INFO")
metrics = Metrics(namespace=NAMESPACE)

dms_client = boto3.client("dms")
dynamodb_client = boto3.client("dynamodb")


def get_dynamodb_record(dms_task_arn, attribute) -> int:
    """Return the number of consecutive dms task operations failed in a dms task id
    if there is no record in dynamo returns 0
    """
    try:
        response = dynamodb_client.get_item(TableName=TABLE_NAME, Key={"dms_task_arn": {"S": dms_task_arn}})
        logger.info("get_dynamodb_record", response=response)
        return int(response.get("Item", {}).get(attribute, {}).get("N", 0))
    except (KeyError, json.JSONDecodeError, botocore.exceptions.ClientError, IndexError) as err:
        logger.error(err, error_type=type(err).__name__)
        raise err


def delete_dynamodb_record(dms_task_arn) -> str:
    """Delete Records history, this operation is idempotent for dynamodb operation"""
    try:
        dynamodb_client.delete_item(TableName=TABLE_NAME, Key={"dms_task_arn": {"S": dms_task_arn}})
        message = f"{dms_task_arn} is in a running state and had prior errors. Records in DynamoDB have been cleaned."
        logger.info(message)
        return message
    except (KeyError, json.JSONDecodeError, botocore.exceptions.ClientError, IndexError) as err:
        logger.error(err, error_type=type(err).__name__)
        raise err


def retrieve_dms_replication_task_response(dms_replication_task_arn: str) -> dict:
    """If the Event Bridge event corresponds to a DMS replication Task, return the API response"""
    try:
        task_filters = {"Name": "replication-task-arn", "Values": [dms_replication_task_arn]}
        describe_task = dms_client.describe_replication_tasks(Filters=[task_filters])
        dms_replication_task_response = describe_task["ReplicationTasks"][0]
        return dms_replication_task_response

    except (KeyError, json.JSONDecodeError, botocore.exceptions.ClientError, IndexError) as err:
        logger.error(err, error_type=type(err).__name__)
        raise err


def parse_dms_replication_task_metadata(replication_task_response: dict) -> tuple[str, str, str]:
    """Get arn,task id, rep instance arn and migration type from boto describe-replication-tasks response"""
    dms_task_status = replication_task_response["Status"]
    migration_type = replication_task_response["MigrationType"]  # ex: 'full-load'|'cdc'|'full-load-and-cdc'
    # Rep Instance ex: "arn:aws:dms:us-east-1: 220271737897:rep:NMYWE2V7WNL7XTI6RZHPNDDXBTRYQV3M3M3RBZY"
    dms_replication_instance_arn = replication_task_response["ReplicationInstanceArn"]
    logger.info("dms_migration_type: %s, task_status:%s", migration_type, dms_task_status)
    return (dms_task_status, migration_type, dms_replication_instance_arn)


def handle_dms_started_task(dms_task_arn) -> str:
    """Handle behavior for DMS_TASK_STARTED"""
    number_failed_operations = get_dynamodb_record(dms_task_arn, "task_errors_qty")
    if number_failed_operations == 0:
        message = f"No action taken.{dms_task_arn} started event and no previous errors."
        logger.info(message)
        return message

    logger.info(
        f"{number_failed_operations} previous error(s) for {dms_task_arn} started event, validate current status {REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS} times. It will clean the record if all of them are not failed"
    )
    # Validate the status of the task a maximum of  REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS times.
    # If it doesn't fail at any point, clean the records in DynamoDB and send a CloudWatch metric with a value of 0 to clear the alarm
    for execution in range(REP_TASK_MAX_RETRIES_FOR_FAILED_STATUS):
        time.sleep(REP_TASK_TIME_TO_WAIT_IN_SECONDS)
        task_current_status = retrieve_dms_replication_task_response(dms_task_arn)["Status"]
        logger.info(f"Execution:{execution}, Task status:{task_current_status}, {dms_task_arn}")
        if task_current_status == DMSReplicationTaskStatus.FAILED:
            message = f"No action taken.Task {dms_task_arn} received started event and has previous errors but has failed in the evaluation time."
            logger.info(message)
            return message
    if task_current_status == DMSReplicationTaskStatus.RUNNING:
        # This value is 0  to transition the alarm state from  IN ALARM to OK
        metrics.add_metric(name=REP_TASK_FAILURE_METRIC, unit="Count", value=0)
        return delete_dynamodb_record(dms_task_arn)


def dms_update_failed_records(dms_task_arn: str, attribute: str) -> int:
    """Update quantity of: task_errors_qty, JiraTickets"""
    try:
        # Update record, response has no useful information
        response = dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={"dms_task_arn": {"S": dms_task_arn}},
            UpdateExpression=f"SET {attribute} = if_not_exists({attribute}, :init) + :incr",
            ExpressionAttributeValues={":init": {"N": "0"}, ":incr": {"N": "1"}},
            ReturnValues="UPDATED_NEW",
        )
        # Extract and return the updated value
        updated_value = int(response["Attributes"][attribute]["N"])
        logger.info("Updated record to %s:%s ,task: %s", attribute, updated_value, dms_task_arn)
        return updated_value
    except (KeyError, json.JSONDecodeError, botocore.exceptions.ClientError, IndexError) as err:
        logger.error(err, error_type=type(err).__name__)
        raise err


def handle_dms_failed_task(dms_task_arn) -> str:
    """Handle dms task failed event,it creates/increases the failed record in dynamodb and sends it to CW Metric
    No autostarting failed task because DMS itself tries to restart failed tasks in the default config:
    https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ErrorHandling.html
    """
    metrics.add_metric(name=REP_TASK_FAILURE_METRIC, unit="Count", value=1)
    # Update que task_errors_quantity attribute in dynamodb table
    dms_update_failed_records(dms_task_arn, "task_errors_qty")

    message = f"No action taken for {dms_task_arn}, simply log it as a CloudWatch metric."
    logger.info(message)
    return message


def handle_eventbridge_event(event: dict) -> str:
    """Handle eventbridge events: dms task started, dms task failed"""
    dms_task_arn = event["resource"]
    event_type = event["eventType"]
    rep_task_response = retrieve_dms_replication_task_response(dms_task_arn)
    dms_instance_arn = parse_dms_replication_task_metadata(rep_task_response)[2]
    # Set default dimensions:
    metrics.set_default_dimensions(ReplicationTaskArn=dms_task_arn, ReplicationInstanceArn=dms_instance_arn)
    # Match event type
    match event_type:
        case DMSReplicationTaskEventType.TASK_STARTED:
            return handle_dms_started_task(dms_task_arn)
        case DMSReplicationTaskEventType.TASK_FAILED:  # add record in dynamodb or create jira ticket
            return handle_dms_failed_task(dms_task_arn)
        case _:
            response = f"Event category:{event_type} for task {dms_task_arn}, no action taken"
            logger.info(response)
            return response


@metrics.log_metrics()
def lambda_handler(event, _):  # pylint: disable=W0613
    """It handles manually triggered events(start, restart,resume, stop and matching)
    and Event Bridge/StepFunctions Events to start/restart new and failed dms tasks
    """
    logger.info("##### DMS Task Manager Event Bridge Payload ######", payload=event)
    return handle_eventbridge_event(event)
