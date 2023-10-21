""" Lambda Function for Manual Tasks
    Used to manual Start/Restart/Resume/stop DMS rep Tasks
    Valid payloads include:
    - {"dms_task_arn": "arn:aws:dms:us-east-1:543276908693:task:XXXX" , "task": "start" }
    - {"dms_task_name_filter": "*-low" , "task": "start" } # to start all dms replication tasks ending with "-low"
    - {"dms_task_arn": "arn:aws:dms:us-east-1:543276908693:task:XXXX" , "task": "start", "cdc_start_position": "XYZ" }
"""
import fnmatch
from typing import List, Optional
from aws_lambda_powertools import Logger
import boto3
import botocore
from app.src.ingestion.dms.dms_task_manager.task_manager_utils import (
    ManualTask,
    StartReplicationTaskType,
    UnableToExecuteManualTaskError,
    UnknownManualTaskError,
)

logger = Logger(service=__name__, level="INFO")

dms_client = boto3.client("dms")


def stop_dms_task(dms_task_arn: str) -> str:
    """Stop a DMS replication Task"""
    try:
        logger.info("## Trying to stop task_arn:%s", dms_task_arn)
        dms_task_stop = dms_client.stop_replication_task(ReplicationTaskArn=dms_task_arn)
        logger.info("task_response:%s, task_arn:%s", dms_task_stop["ReplicationTask"]["Status"], dms_task_arn)
        return f"No errors when trying to stop dms task {dms_task_arn}"
    except (botocore.exceptions.ClientError, botocore.exceptions.ParamValidationError) as err:
        logger.error("### Error while trying to stop the task: %s", err)
        raise UnableToExecuteManualTaskError(f"Unable to stop DMS Task {dms_task_arn}") from err


def start_resume_or_reload_dms_task(
    dms_task_arn: str,
    rerun_type: StartReplicationTaskType,
    cdc_start_position: Optional[str] = None,
) -> str:
    """Try to restart the failed dms task, use rerun type based in migration type
    Args:
        dms_task_arn_ (str): Failed DMS Task name , ex:
        arn:aws:dms:us-east-1:220271737897:task:E2FDDWUKQJV7UCIKU3GCEWAXX6HYE5OKAILG7AA
        rerun_type (str)
    Returns:
        str
    """
    try:
        # Allowed values for StartReplicationTaskType='start-replication'|'resume-processing'|'reload-target',
        logger.info("## Trying to %s task_arn:%s", rerun_type, dms_task_arn)
        kwargs = {"CdcStartPosition": cdc_start_position} if cdc_start_position else {}
        dms_task_restart = dms_client.start_replication_task(
            ReplicationTaskArn=dms_task_arn, StartReplicationTaskType=rerun_type, **kwargs
        )
        logger.info(
            "task_response:%s, task_arn:%s, rerun_type:%s, kwargs:%s",
            dms_task_restart["ReplicationTask"]["Status"],
            dms_task_arn,
            rerun_type,
            kwargs,
        )
        # Update last_start_restart_date in dynamodb record
        return f"No errors when trying to start/resume/reload dms task {dms_task_arn}"

    except (botocore.exceptions.ClientError, botocore.exceptions.ParamValidationError) as err:
        logger.error("### Error while trying to %s the task: %s", rerun_type, err)
        raise UnableToExecuteManualTaskError(
            f"Unable to start replication task {dms_task_arn} with {rerun_type}"
        ) from err


def handle_manual_event(event: dict) -> List[str] | str:
    """Send manual Start/Stop/Resume/Reload for DMS task
    and filters: get dms task arns that matches a pattern and make operations on them
    """
    if dms_task_filter_criteria := event.get("dms_task_name_filter"):
        return apply_to_matching_dms_tasks(event, dms_task_filter_criteria)
    task = event.pop("task")
    match task:
        case ManualTask.STOP:
            return stop_dms_task(event["dms_task_arn"])
        case ManualTask.START:
            event["rerun_type"] = StartReplicationTaskType.START_REPLICATION
            return start_resume_or_reload_dms_task(**event)
        case ManualTask.RESUME:
            event["rerun_type"] = StartReplicationTaskType.RESUME_PROCESSING
            return start_resume_or_reload_dms_task(**event)
        case ManualTask.RELOAD:
            event["rerun_type"] = StartReplicationTaskType.RELOAD_TARGET
            return start_resume_or_reload_dms_task(**event)
        case _:
            raise UnknownManualTaskError(
                f"Unknown manual task supplied: {task}. Valid values are: {[e.value for e in ManualTask]}"
            )


def apply_to_matching_dms_tasks(event: dict, dms_task_filter_criteria: str) -> List[str]:
    """Filter tasks that matches dms_task_filter_criteria(it uses dms task Identifier), allowed to use wildcards.
    Make the required operations for all the dms tasks that matches the criteria.
    ex: event1: {"dms_task_name_filter": "dmsreplicationtask*","task": "resume"}
    """
    all_dms_tasks = retrieve_all_dms_tasks()
    all_dms_tasks_matching_filter = filter(
        lambda dms_task: fnmatch.fnmatch(dms_task["ReplicationTaskIdentifier"], dms_task_filter_criteria),
        all_dms_tasks,
    )
    dms_task_arns = map(lambda dms_task: dms_task["ReplicationTaskArn"], all_dms_tasks_matching_filter)

    task = event["task"]
    response = [handle_manual_event({"dms_task_arn": dms_task, "task": task}) for dms_task in dms_task_arns]
    return response


def retrieve_all_dms_tasks():
    dms_tasks_description = dms_client.describe_replication_tasks()
    all_dms_tasks = dms_tasks_description["ReplicationTasks"]
    while marker := dms_tasks_description.get("Marker"):
        dms_tasks_description = dms_client.describe_replication_tasks(Marker=marker)
        all_dms_tasks += dms_tasks_description["ReplicationTasks"]
    return all_dms_tasks


def lambda_handler(event, _):  # pylint: disable=W0613
    """It handles Event Bridge/StepFunctions Events and router to corresponding action"""
    logger.info("##### Lambda Task Manual Event Payload ######", payload=event)
    return handle_manual_event(event)
