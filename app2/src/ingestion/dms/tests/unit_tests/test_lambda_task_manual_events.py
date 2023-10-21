"""
Test Lambda DMS task manual events
"""
import copy
from unittest.mock import patch
import pytest
import boto3
import botocore
from moto import mock_dms
from app.src.ingestion.dms.dms_task_manager.task_manager_utils import (
    ManualTask,
    MigrationType,
    StartReplicationTaskType,
    UnableToExecuteManualTaskError,
    UnknownManualTaskError,
    DMSReplicationTaskStatus,
)
from app.src.ingestion.dms.tests.unit_tests.constants_payloads import REPLICATION_TASK_PROPS, DESCRIBE_INSTANCE

original_botocore_api_call = botocore.client.BaseClient._make_api_call  # pylint: disable=W0212


# Mocked botocore _make_api_call function
def mock_make_api_call(self, operation_name, kwarg):
    # We need this because Describe Replication Instances is currently not supported by moto: https://docs.getmoto.org/en/4.1.11/docs/services/dms.html
    if operation_name == "DescribeReplicationInstances":
        return DESCRIBE_INSTANCE
    if operation_name == "DescribeReplicationTasks":
        response = original_botocore_api_call(self, operation_name, kwarg)
        if response["ReplicationTasks"][0]["Status"] == DMSReplicationTaskStatus.CREATING:
            # transition all `creating` tasks to `ready` for testing
            response["ReplicationTasks"][0]["Status"] = DMSReplicationTaskStatus.READY
        return response
    # If we don't want to patch the API call
    return original_botocore_api_call(self, operation_name, kwarg)


@pytest.fixture(autouse=True)
def mock_os_env(monkeypatch):
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")


@pytest.fixture
def delete_ingestion_modules_imported():
    # This fixture is needed to delete the app.src.ingestion.* modules we've already imported because otherwise, the global variables
    # declared at the top level of the module (such as Logger) can't be patched
    import sys

    ingestion_modules = {k: v for k, v in sys.modules.items() if "app.src.ingestion" in k}
    for k in ingestion_modules.keys():
        sys.modules.pop(k)  # delete the imports
    yield
    sys.modules = {**sys.modules, **ingestion_modules}  # re-add them to be a good potato and not wreak havoc


def test_error_with_invalid_params():
    from app.src.ingestion.dms.dms_task_manager import lambda_dms_manual_task

    with pytest.raises(UnableToExecuteManualTaskError):
        lambda_dms_manual_task.start_resume_or_reload_dms_task(None, None)


@mock_dms
def test_error_with_nonexistent_arn():
    # pylint: disable=C0415
    from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import (
        start_resume_or_reload_dms_task,
    )

    with pytest.raises(UnableToExecuteManualTaskError):
        start_resume_or_reload_dms_task("nonexistent_arn", StartReplicationTaskType.START_REPLICATION)


def test_invalid_manual_event():
    from app.src.ingestion.dms.dms_task_manager import lambda_dms_manual_task

    with pytest.raises(UnknownManualTaskError):
        event = {"task": "some_invalid_task", "dms_task_arn": "doesnt_matter"}
        lambda_dms_manual_task.handle_manual_event(event)


@mock_dms
def test_lambda_handler_manual():
    from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import lambda_handler

    client = boto3.client("dms")
    replication_task = client.create_replication_task(**REPLICATION_TASK_PROPS)
    task_arn = replication_task["ReplicationTask"]["ReplicationTaskArn"]
    manual_event = {"task": ManualTask.START, "dms_task_arn": task_arn}
    lambda_handler(manual_event, None)  # pylint: disable=E1128,W0612


@mock_dms
def test_lambda_handler_invalid_manual_request():
    from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import lambda_handler

    client = boto3.client("dms")
    replication_task = client.create_replication_task(**REPLICATION_TASK_PROPS)
    task_arn = replication_task["ReplicationTask"]["ReplicationTaskArn"]
    manual_event = {"task": ManualTask.STOP, "dms_task_arn": task_arn}
    # try to 'stop' an instance which isn't running (currently being created)
    with pytest.raises(UnableToExecuteManualTaskError):
        lambda_handler(manual_event, None)  # pylint: disable=E1128,W0612


@mock_dms
def test_lambda_handler_manual_cdc_start_position_invalid_type():
    from app.src.ingestion.dms.dms_task_manager import lambda_dms_manual_task

    client = boto3.client("dms")
    local_task_props = copy.deepcopy(REPLICATION_TASK_PROPS)
    local_task_props["MigrationType"] = MigrationType.FULL_LOAD
    replication_task = client.create_replication_task(**local_task_props)
    task_arn = replication_task["ReplicationTask"]["ReplicationTaskArn"]

    manual_event = {"task": ManualTask.START, "dms_task_arn": task_arn, "cdc_start_position": 123}
    with pytest.raises(lambda_dms_manual_task.UnableToExecuteManualTaskError):
        lambda_dms_manual_task.lambda_handler(manual_event, None)  # pylint: disable=E1128,W0612


@mock_dms
@pytest.mark.parametrize(
    "task_name_filter,status",
    [("*cdc*", "stopped"), ("*full*", "running")],
)
def test_stop_all_tasks_filter_match(
    task_name_filter: str,
    status: str,
    delete_ingestion_modules_imported,  # pylint: disable=unused-argument,redefined-outer-name
):
    # 3 Scenarios
    # 1. Given the filter *cdc*, which matches all dms tasks running, and 'stop', but in dry run mode. Therefore, no tasks should be stopped and we should see the task arns in the logs
    # 2. Given the filter *cdc*, which matches all dms tasks running, and 'stop'. Therefore, all tasks should be stopped
    # 3. Given the filter *full* which matches no dms tasks running, and 'stop'. Therefore, no tasks should be stopped

    replication_task_1 = {**REPLICATION_TASK_PROPS, "ReplicationTaskIdentifier": "prd-use1-g360-dreams-dine-cdc3"}
    replication_task_2 = {**REPLICATION_TASK_PROPS, "ReplicationTaskIdentifier": "prd-use1-g360-dreams-rmful-cdc4"}
    client = boto3.client("dms")

    # Create and start two DMS tasks
    response_task_1 = client.create_replication_task(**replication_task_1)
    response_task_2 = client.create_replication_task(**replication_task_2)

    dms_replication_task_1_arn = response_task_1["ReplicationTask"]["ReplicationTaskArn"]
    dms_replication_task_2_arn = response_task_2["ReplicationTask"]["ReplicationTaskArn"]
    with patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
        from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import (
            lambda_handler,
        )  # pylint: disable=C0415

        manual_event = {"task": ManualTask.STOP, "dms_task_name_filter": task_name_filter}

        client.start_replication_task(
            ReplicationTaskArn=dms_replication_task_1_arn,
            StartReplicationTaskType=StartReplicationTaskType.START_REPLICATION,
        )
        client.start_replication_task(
            ReplicationTaskArn=dms_replication_task_2_arn,
            StartReplicationTaskType=StartReplicationTaskType.START_REPLICATION,
        )

        # the replication task is running, so we shouldn't take any action
        lambda_handler(manual_event, None)
    task_filters = {"Name": "replication-task-arn", "Values": [dms_replication_task_1_arn, dms_replication_task_2_arn]}
    describe_task = client.describe_replication_tasks(Filters=[task_filters])
    assert all(dms_task["Status"] == status for dms_task in describe_task["ReplicationTasks"])


@mock_dms
def test_retrieve_all_dms_tasks():
    client = boto3.client("dms")

    # create a bunch of DMS replication tasks
    number_of_dms_tasks_created = 150
    for i in range(number_of_dms_tasks_created):
        payload = {**REPLICATION_TASK_PROPS, "ReplicationTaskIdentifier": f"dummy-{i}"}
        client.create_replication_task(**payload)

    from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import retrieve_all_dms_tasks

    all_dms_tasks = retrieve_all_dms_tasks()

    assert len(all_dms_tasks) == number_of_dms_tasks_created


@mock_dms
def test_reload_full_dms_task():
    """TODO: moto doesn't currently verify validity of `StartReplicationTaskType`, so there are no exceptions when running `reload` on a `cdc` task
    when that gets addressed, revisit these tests and add another failure example
    """
    replication_task = {
        **REPLICATION_TASK_PROPS,
        "ReplicationTaskIdentifier": "test",
        "MigrationType": MigrationType.FULL_LOAD,
    }
    client = boto3.client("dms")

    # Create and start two DMS tasks
    response = client.create_replication_task(**replication_task)

    dms_replication_task_arn = response["ReplicationTask"]["ReplicationTaskArn"]

    with patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
        from app.src.ingestion.dms.dms_task_manager.lambda_dms_manual_task import (
            lambda_handler,
        )  # pylint: disable=C0415

        manual_event_stop = {"task": ManualTask.STOP, "dms_task_arn": dms_replication_task_arn}

        client.start_replication_task(
            ReplicationTaskArn=dms_replication_task_arn,
            StartReplicationTaskType=StartReplicationTaskType.START_REPLICATION,
        )

        # stop the dms task
        lambda_handler(manual_event_stop, None)

        manual_event_reload = {"task": ManualTask.RELOAD, "dms_task_arn": dms_replication_task_arn}

        lambda_handler(manual_event_reload, None)

        task_filters = {"Name": "replication-task-arn", "Values": [dms_replication_task_arn]}
        describe_task = client.describe_replication_tasks(Filters=[task_filters])
        assert describe_task["ReplicationTasks"][0]["Status"] == "running"
