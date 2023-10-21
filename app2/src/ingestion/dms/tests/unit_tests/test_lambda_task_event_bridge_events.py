"""
Test Lambda DMS Event Bridge events
"""
import pytest
import botocore
import boto3
from moto import mock_dms, mock_dynamodb
from app.src.ingestion.dms.tests.unit_tests.constants_payloads import (
    EVENT_TASK_FAILED,
    EVENT_TASK_STARTED,
    EVENT_TASK_STOPPED,
    TASK_ARN,
    REPLICATION_TASK_PROPS,
)

from app.src.ingestion.dms.dms_task_manager.task_manager_utils import (
    DMSReplicationTaskEventType,
    StartReplicationTaskType,
)

TABLE_NAME = "test_table"
TABLE_ATTRIBUTES_DEFINITION = [{"AttributeName": "dms_task_arn", "AttributeType": "S"}]
TABLE_KEY_SCHEMA = [{"AttributeName": "dms_task_arn", "KeyType": "HASH"}]


@pytest.fixture(autouse=True)
def mock_os_env(monkeypatch):
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch.setenv("TABLE_NAME", TABLE_NAME)
    monkeypatch.setenv(
        "REP_TASK_TIME_TO_WAIT_IN_SECONDS", "0"
    )  # so any tests involving changing the instance state don't wait forever


@pytest.fixture()
def mock_dynamo_db(mock_os_env):  # Using mock_os_env because it needs to set a region for dynamodb
    with mock_dynamodb():
        yield boto3.client("dynamodb")


@pytest.fixture()
def mock_dynamodb_table(mock_dynamo_db):
    mock_dynamo_db.create_table(
        TableName=TABLE_NAME,
        AttributeDefinitions=TABLE_ATTRIBUTES_DEFINITION,
        KeySchema=TABLE_KEY_SCHEMA,
        BillingMode="PAY_PER_REQUEST",
    )
    yield
    mock_dynamo_db.delete_table(TableName=TABLE_NAME)


@pytest.fixture()
def mock_dms_client(mock_os_env):  # Using mock_os_env because it needs to set a region for dynamodb
    with mock_dms():
        yield boto3.client("dms")


@pytest.fixture()
def mock_dms_task(mock_dms_client):
    response = mock_dms_client.create_replication_task(**REPLICATION_TASK_PROPS)
    dms_task_arn = response["ReplicationTask"]["ReplicationTaskArn"]
    mock_dms_client.start_replication_task(
        ReplicationTaskArn=dms_task_arn,
        StartReplicationTaskType=StartReplicationTaskType.START_REPLICATION,
    )  # now dms task is running

    yield
    mock_dms_client.stop_replication_task(ReplicationTaskArn=dms_task_arn)
    mock_dms_client.delete_replication_task(ReplicationTaskArn=dms_task_arn)


def test_not_ready_or_failed_task(mock_dms_task, mock_dynamodb_table):
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import (
        handle_eventbridge_event,
    )  # pylint: disable=C0415

    # the replication task is running, so we shouldn't take any action
    result = handle_eventbridge_event(EVENT_TASK_STARTED)

    assert result == f"No action taken.{TASK_ARN} started event and no previous errors."


def test_edge_case_handle_eventbridge_event(mock_dms_task):
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import lambda_handler

    result = lambda_handler(EVENT_TASK_STOPPED, "test_context")
    assert (
        result
        == f"Event category:{DMSReplicationTaskEventType.TASK_STOPPED.value} for task {TASK_ARN}, no action taken"
    )


def test_handle_eventbridge_event_failed(mock_dms_task, mock_dynamodb_table):  # pylint: disable=W0613,W0621
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import handle_eventbridge_event

    result = handle_eventbridge_event(EVENT_TASK_FAILED)
    assert result == f"No action taken for {TASK_ARN}, simply log it as a CloudWatch metric."


def test_get_dynamodb_record_exception():
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import get_dynamodb_record

    with pytest.raises(botocore.exceptions.ClientError):
        get_dynamodb_record(TASK_ARN, "ERROR_ATTRIBUTE")


def test_delete_dynamodb_record(mock_dynamodb_table):  # pylint: disable=W0613,W0621
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import delete_dynamodb_record

    response = delete_dynamodb_record(TASK_ARN)
    assert response == f"{TASK_ARN} is in a running state and had prior errors. Records in DynamoDB have been cleaned."


def test_delete_dynamodb_record_error():  # pylint: disable=W0613,W0621
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import delete_dynamodb_record

    with pytest.raises(botocore.exceptions.ClientError):
        delete_dynamodb_record(TASK_ARN)


def test_retrieve_dms_replication_task_response_error():
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import (
        retrieve_dms_replication_task_response,
    )

    with pytest.raises(botocore.exceptions.ClientError):
        retrieve_dms_replication_task_response("BAD_ARN")  # It fails because not mocked DMS in the test


def test_dms_update_failed_records(mock_dynamodb_table):
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import dms_update_failed_records

    dms_update_failed_records(TASK_ARN, "task_errors_qty")
    failed_operations_qty = dms_update_failed_records(TASK_ARN, "task_errors_qty")
    jira_tickets_qty = dms_update_failed_records(TASK_ARN, "jira_ticket_qty")
    assert failed_operations_qty == 2 and jira_tickets_qty == 1


def test_dms_update_failed_records_error():
    from app.src.ingestion.dms.dms_task_manager.lambda_task_event_bridge_events import dms_update_failed_records

    with pytest.raises(botocore.exceptions.ClientError):
        dms_update_failed_records(TASK_ARN, attribute="test")
