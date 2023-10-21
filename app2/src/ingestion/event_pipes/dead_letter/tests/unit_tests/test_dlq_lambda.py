"""Tests for DLQ Lambda Logic"""
# pylint: disable=C0415
# pylint: disable=W0621,W0613
import copy
import logging
import json
import os
import sys
from unittest import mock
import boto3
import pytest
import moto
import botocore.stub
import botocore.exceptions
from aws_lambda_context import LambdaContext
from aws_lambda_powertools import Logger

from app.src.ingestion.event_pipes.utils.app_config_utils import get_app_config_data
from app.src.ingestion.event_pipes.utils.process_data import HandledEventResponse


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
# set log levels for noisy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

MOCK_URL = "http://localhost:2772/applications/lst-teststack-use1-testappconfig-app/environments/lst-teststack-use1-testappconfig-env/configurations/lst-teststack-use1-testappconfig-profile"

SOURCE_KINESIS_TEST = "lst-use1-guest360-dlr-cme-kinesis-dmz-test"
TARGET_KINESIS_TEST = "lst-use1-guest360-dlr-cme-kinesis-test"
KINESIS_ARN_PREFIX = "arn:aws:kinesis:us-east-1:123456789012:stream/"
TEST_EVENT = [
    {
        "messageId": "0adcdb8d-7987-41a6-bde9-6bfde28d6d9d",
        "receiptHandle": "AQEB/nVoAudzes5Cfn7FRgA+/lvXm8IFKzAX+VZED3dfAg5z83Yyt9qwPNsexRCTw4v9ZeawrCHQSp25PAB9ExMtSTHZ81oqr63DHIWQ55h87vSP+MVWCdq6AS3tiwOwrRrZ6yv6w3H7UTPqb/jNlrtXbi4k9DYX4J3p2LtZHpaLg8ghiHlyUGZzOwdGFGwcg5UwgycZQRcy3NQqZenKXlqtgmCM5MiUoJXk0AEo483aKNVh65KacsVy4iL/hBri7oiKyLsUaGVgeKsS1pS9PMP357iaEU7dTP0WFh91MUE3+Hhe5+VTNoN0dD6juwIPmwgDUJ+hjP6id28/J0J//Me1VqfuR0/DDIFa1P6rwng+zvbaKpUmjJc91uhkVSrHIEm9gfFSjWKLsfnIl9+LWf/ANXzmaYXTo22la9q3BZKVm4A=",  # pragma: allowlist secret
        "body": '{"context":{"partnerResourceArn":"arn:aws:pipes:us-east-1:123456789012:pipe/lst-use1-guest360-dlr-cme-event-bridge-pipe-validation","condition":"RetryAttemptsExhausted"},"version":"1.0","timestamp":"2023-06-19T15:03:51.498Z","KinesisBatchInfo":{"shardId":"shardId-000000000000","startSequenceNumber":"1","endSequenceNumber":"1","approximateArrivalOfFirstRecord":"2023-06-19T15:03:46.620Z","approximateArrivalOfLastRecord":"2023-06-19T15:03:46.620Z","batchSize":1,"streamArn":"'
        + KINESIS_ARN_PREFIX
        + SOURCE_KINESIS_TEST
        + '"}}',
        "attributes": {
            "ApproximateReceiveCount": "1",
            "SentTimestamp": "1687187031624",
            "SenderId": "AROAX47OTYCKUZ6YRV5WU:poller-platform-customer-role-session",
            "ApproximateFirstReceiveTimestamp": "1687187031633",
        },
        "messageAttributes": {},
        "md5OfBody": "413b40fd3a42b71a3fc45a813d5304bf",  # pragma: allowlist secret
        "eventSource": "aws:sqs",
        "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:lst-use1-guest360-dlr-cme-sqs-dead-letter",
        "awsRegion": "us-east-1",
    }
]

TEST_DATA = {
    "data": {
        "id": 00000,
        "inv_bucket_id": "DP_TICKET-TEST",
        "res_status": "NEW",
        "res_date": "2023-06-18",
        "activity_date": "2023-06-15",
        "last_updated": "2023-06-15T11:00:00Z",
        "facility_id": "DP_TEST",
        "slot": "DAILY",
        "num_reservations": 5,
        "num_guests": 5,
    },
    "metadata": {
        "timestamp": "2023-06-15T18:13:12.086617Z",
        "record-type": "data",
        "operation": "update",
        "partition-key-type": "schema-table",
        "schema-name": "awakening",
        "table-name": "test_stats",
        "transaction-id": 0000000000000000,
    },
}

TEST_DATA_2 = {
    "data": {"id": "WDW", "name": "Walt Disney World Resort", "time_zone": "America/New_York"},
    "metadata": {
        "timestamp": "2023-06-22T15:23:53.223530Z",
        "record-type": "data",
        "operation": "load",
        "partition-key-type": "primary-key",
        "schema-name": "awakening",
        "table-name": "destination",
    },
}


TEST_PARTITION_KEY = "awakening.test_stats"
METADATA_TABLE_NAME = "metadata.table-name"
DATA_PIPE_INFO = {
    "default_router_database": "DEFAULT_ROUTER_TEST_LANDING",
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "schema_path": "metadata.schema-name",
    "table_path": "metadata.table-name",
    "data_mapper_type": "nested",
    "data_contracts": [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_wdw.v0.cme_wdw_res_guest_links_source_data_contract",
            "class_name": "CMEWDWResGuestLinksModel",
            "data_contract_version": "0.0.1",
            "key_path": [{"name": METADATA_TABLE_NAME, "value": "res_guest_links"}],
            "router_database": "LATEST_LANDING",
            "router_schema": "LND__CME_WDW",
            "router_table": "RES_GUEST_LINKS",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_reservation_source_data_contract",
            "class_name": "CMEDLRReservationModel",
            "data_contract_version": "0.0.1",
            "key_path": [{"name": METADATA_TABLE_NAME, "value": "reservation"}],
            "router_database": "LATEST_LANDING",
            "router_schema": "LND__CME_DLR",
            "router_table": "RESERVATION",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_wdw.v0.cme_wdw_destination_source_data_contract",
            "class_name": "CMEWDWDestinationModel",
            "data_contract_version": "0.0.1",
            "key_path": [{"name": METADATA_TABLE_NAME, "value": "destination"}],
            "router_database": "LATEST_LANDING",
            "router_schema": "LND__CME_WDW",
            "router_table": "INVENTORY_PRODUCT",
        },
    ],
}


@pytest.fixture(scope="module")
def monkeypatch_module():
    mpatch = pytest.MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="module", autouse=True)
def mock_os_environment(monkeypatch_module):  # pylint: disable=W0621
    # monkeypatch all environment variables necessary w/out affecting OS environment
    monkeypatch_module.setenv("APPCONFIG_URL_PATH", "")
    monkeypatch_module.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch_module.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch_module.setenv("AWS_LAMBDA_FUNCTION_NAME", "testing")
    monkeypatch_module.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch_module.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch_module.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch_module.setenv("eventSourceARN", "arn:aws:kinesis:region:0000000000000:stream/stream-name")
    monkeypatch_module.setenv("KINESIS_STREAM_NAME", "lst-use1-guest360-dlr-cme-kinesis-test")
    monkeypatch_module.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch_module.setenv("OTEL_NAMESPACE", "testing_namespace")


@pytest.fixture(scope="module", autouse=True)
def mock_requests():
    """Needed for patch querying AWS AppConfig"""
    with mock.patch("requests.get") as mock_request:
        mock_response = mock.Mock()
        mock_response.content.decode.return_value = json.dumps(DATA_PIPE_INFO).encode("utf-8")
        mock_request.return_value = mock_response
        yield mock_request


@pytest.fixture(scope="module")
def mock_kinesis(mock_os_environment):  # pylint: disable=W0613,W0621
    with moto.mock_kinesis():
        yield boto3.client("kinesis")


@pytest.fixture(scope="function")
def mock_stream_source(mock_os_environment, mock_kinesis):  # pylint: disable=W0621
    shard_count = 1
    stream_name = SOURCE_KINESIS_TEST

    # Create the Kinesis data stream
    mock_kinesis.create_stream(StreamName=stream_name, ShardCount=shard_count)

    yield stream_name

    # Delete the Kinesis data stream after every test
    mock_kinesis.delete_stream(StreamName=stream_name)


@pytest.fixture(scope="function")
def mock_stream_target(mock_os_environment, mock_kinesis):  # pylint: disable=W0621
    shard_count = 1
    stream_name = TARGET_KINESIS_TEST

    # Create the Kinesis data stream
    mock_kinesis.create_stream(StreamName=stream_name, ShardCount=shard_count)

    #  # Send test message to the stream, needed to work properly the function get_records
    #  mock_kinesis.put_record(
    #  StreamName=stream_name,
    #  Data=json.dumps(TEST_DATA),
    #  PartitionKey=TEST_PARTITION_KEY,
    #  )
    yield stream_name

    # Delete the Kinesis data stream after every test
    mock_kinesis.delete_stream(StreamName=stream_name)


@pytest.fixture(scope="module", autouse=True)
def mock_lambda_context():
    lambda_context = LambdaContext()
    lambda_context.function_name = "function_name"
    lambda_context.function_version = "function_version"
    lambda_context.invoked_function_arn = "invoked_function_arn"
    lambda_context.memory_limit_in_mb = "memory_limit_in_mb"
    lambda_context.aws_request_id = "aws_request_id"
    yield lambda_context


"""
AppConfig Test
"""


def test_get_app_config_data(mock_requests):
    result = get_app_config_data(url_path=MOCK_URL, timeout=30)

    assert result == DATA_PIPE_INFO
    mock_requests.assert_called_once_with(MOCK_URL, timeout=30)


"""
get_records tests section
"""


def test_get_records_from_stream(mock_kinesis, mock_stream_source):
    kinesis_data = json.loads(copy.copy(TEST_EVENT[0]["body"]))
    kinesis_batch_info = kinesis_data["KinesisBatchInfo"]
    push_to_dmz_kinesis(mock_kinesis, kinesis_data)

    from app.src.ingestion.event_pipes.dead_letter.runner import get_records

    logger.debug(f"{kinesis_data=}")
    logger.debug(f"{kinesis_batch_info=}")
    response = get_records(kinesis_batch_info)
    logger.debug("kinnesis batch get_records: %s", response)
    assert len(response) == 1
    assert response[0]["Data"] == json.dumps(kinesis_data).encode()


def test_get_records_empty(mock_stream_source):
    kinesis_data = json.loads(copy.copy(TEST_EVENT[0]["body"]))
    kinesis_batch_info = kinesis_data["KinesisBatchInfo"]

    from app.src.ingestion.event_pipes.dead_letter.runner import get_records

    logger.debug(f"{kinesis_data=}")
    logger.debug(f"{kinesis_batch_info=}")
    response = get_records(kinesis_batch_info)
    logger.debug("kinnesis batch get_records: %s", response)
    assert len(response) == 0


def test_get_records_error_exception():
    from app.src.ingestion.event_pipes.dead_letter.runner import get_records

    kinesis_data = json.loads(copy.copy(TEST_EVENT)[0]["body"])
    kinesis_batch_info = kinesis_data["KinesisBatchInfo"]
    kinesis_batch_info["streamArn"] = None
    with pytest.raises(AttributeError):
        get_records(kinesis_batch_info)


def test_get_records_throughput_exception():
    from app.src.ingestion.event_pipes.dead_letter.runner import get_records, kinesis_client

    kinesis_data = json.loads(copy.copy(TEST_EVENT)[0]["body"])
    kinesis_batch_info = kinesis_data["KinesisBatchInfo"]
    stubber = botocore.stub.Stubber(kinesis_client)

    # Append many responses as retries
    for _ in range(1, 6):
        stubber.add_client_error(  # Adds a ClientError to the response queue
            method="get_shard_iterator",
            service_error_code="ProvisionedThroughputExceededException",
            service_message="Provisioned throughput exceeded for shard",
        )

    stubber.activate()
    with pytest.raises(botocore.exceptions.ClientError) as err:
        get_records(kinesis_batch_info)
    assert err.value.response["Error"]["Code"] == "ProvisionedThroughputExceededException"
    stubber.deactivate()


"""
get_pydantic_validation tests section
"""


def test_get_pydantic_validation():
    from app.src.ingestion.event_pipes.utils.data_contract_utils import (
        validate_record_conforms_to_data_contract,
    )

    mock_logger = mock.Mock(spec=Logger)

    response = validate_record_conforms_to_data_contract(DATA_PIPE_INFO["data_contracts"][2], TEST_DATA_2, mock_logger)
    assert response.startswith("app.")


def test_get_pydantic_validation_error():
    from app.src.ingestion.event_pipes.utils.data_contract_utils import (
        validate_record_conforms_to_data_contract,
        DataValidationError,
    )

    mock_logger = mock.Mock(spec=Logger)
    with pytest.raises(DataValidationError):
        validate_record_conforms_to_data_contract(DATA_PIPE_INFO["data_contracts"][0], TEST_DATA, mock_logger)


"""
send_to_kinesis_validated tests section
"""


def test_send_to_kinesis_validated(mock_stream_target):
    import app.src.ingestion.event_pipes.dead_letter.runner as runner

    # Need json.dumps() or will raise ParameterValidation Error valid types: <class 'bytes'>, <class 'bytearray'>
    records_list = [{"Data": json.dumps(copy.copy(TEST_DATA)), "PartitionKey": TEST_PARTITION_KEY}]
    runner.validate_inputs(None)
    response = runner.send_to_kinesis_validated(records_list)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


def test_send_to_kinesis_validated_parameter_exception():
    import app.src.ingestion.event_pipes.dead_letter.runner as runner

    records_list = [{"Data": copy.copy(TEST_DATA), "PartitionKey": TEST_PARTITION_KEY}]
    with pytest.raises(botocore.exceptions.ParamValidationError):
        runner.validate_inputs(None)
        runner.send_to_kinesis_validated(records_list)


"""
lambda_handler tests section
"""


def test_lambda_handler_one_record(mock_stream_source, mock_stream_target, mock_kinesis):
    import app.src.ingestion.event_pipes.dead_letter.runner as runner

    # push event onto kinesis stream
    kinesis_data = copy.copy(TEST_DATA)
    push_to_dmz_kinesis(mock_kinesis, kinesis_data)

    response = runner.lambda_handler(copy.copy(TEST_EVENT), mock_lambda_context)

    # At mocking time we are using just one shard and writing one record in kinesis stream
    get_shard_iterator = mock_kinesis.get_shard_iterator(
        StreamName=mock_stream_target, ShardId="shardId-000000000000", ShardIteratorType="TRIM_HORIZON"
    )
    request = mock_kinesis.get_records(ShardIterator=get_shard_iterator["ShardIterator"], Limit=100)
    logger.debug("mock_kinesis_target records=%s", request)

    assert len(request["Records"]) == 1
    for response in request["Records"]:
        target_response = json.loads(response["Data"].decode())
        assert target_response["router_database"] == "DEFAULT_ROUTER_TEST_LANDING"
        assert target_response["router_schema"] == "awakening"
        assert target_response["router_table"] == "test_stats"
        assert target_response["stream"] == SOURCE_KINESIS_TEST
        # Cloud Event
        assert target_response["type"] == "exception"
        assert target_response["source"] == f"{KINESIS_ARN_PREFIX}{SOURCE_KINESIS_TEST}"
        assert target_response["id"] == "shardId-000000000000-1"
        assert target_response["partition_key"] == TEST_PARTITION_KEY
        assert target_response["validated"] is False


def test_lambda_handler_healing_exception():
    import app.src.ingestion.event_pipes.dead_letter.runner as runner

    exception_event = copy.deepcopy(TEST_EVENT)
    exception_event[0].pop("body")

    with pytest.raises((runner.HealingError, botocore.exceptions.ParamValidationError)):
        runner.lambda_handler(exception_event, mock_lambda_context)


def test_lambda_handler_two_records_one_exception(mock_stream_source, mock_stream_target, mock_kinesis):
    """Send two events, the first ok and the second  with error. It will raise an error
    in execution time but at last will put in kinesis the good one.
    """
    import app.src.ingestion.event_pipes.dead_letter.runner as runner

    # push event onto kinesis stream
    kinesis_data = copy.copy(TEST_DATA)
    push_to_dmz_kinesis(mock_kinesis, kinesis_data)
    # This variable will be a list of a good and incomplete event

    exception_event = copy.deepcopy(TEST_EVENT)
    exception_event[0].pop("body")
    custom_event = [copy.copy(TEST_EVENT[0]), exception_event[0]]
    with pytest.raises((runner.HealingError, botocore.exceptions.ParamValidationError)):
        response = runner.lambda_handler(custom_event, mock_lambda_context)

    # At mocking time we are using just one shard and writing one record in kinesis stream
    get_shard_iterator = mock_kinesis.get_shard_iterator(
        StreamName=mock_stream_target, ShardId="shardId-000000000000", ShardIteratorType="TRIM_HORIZON"
    )
    request = mock_kinesis.get_records(ShardIterator=get_shard_iterator["ShardIterator"], Limit=100)
    logger.debug("mock_kinesis_target records=%s", request)
    assert len(request["Records"]) == 1


def push_to_dmz_kinesis(mock_kinesis_client, data) -> None:
    #  # Send test message to the stream, needed to work properly the function get_records
    response = mock_kinesis_client.put_record(
        StreamName=SOURCE_KINESIS_TEST,
        Data=json.dumps(data),
        PartitionKey=TEST_PARTITION_KEY,
    )
    logger.debug(f"push_to_dmz_kinesis: {response=}")


"""
put_records, example response from moto:
{
    "FailedRecordCount": 0,
    "Records": [
        {
            "SequenceNumber": "2",
            "ShardId": "shardId-000000000000"
        }
    ],
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "server": "amazon.com",
            "date": "Thu, 10 Aug 2023 21:30:20 GMT"
        },
        "RetryAttempts": 0
    }
}

get_records:
{
    "Records": [
        {
            "SequenceNumber": "1",
            "ApproximateArrivalTimestamp": datetime.datetime(2023,8,14,23,18,26,418486, tzinfo=tzlocal()),
            "Data": b"{"data": {"id": 0, "inv_bucket_id": "DP_TICKET-TEST", "res_status": "NEW", "res_date": "2023-06-18", "activity_date": "2023-06-15", "last_updated": "2023-06-15T11: 00: 00Z", "facility_id": "DP_TEST", "slot": "DAILY", "num_reservations": 5, "num_guests": 5}, "metadata": {"timestamp": "2023-06-15T18: 13: 12.086617Z", "record-type": "data", "operation": "update", "partition-key-type": "schema-table", "schema-name": "awakening", "table-name": "test_stats", "transaction-id": 0}}",
            "PartitionKey": "awakening.test_stats"
        },
        {
            "SequenceNumber": "2",
            "ApproximateArrivalTimestamp": datetime.datetime(2023,..),
            "Data": b"{"...",
            "PartitionKey": "awakening.test_stats"
        }
    ],
    "NextShardIterator": "alphanumericvalues==\n",
    "MillisBehindLatest": 0,
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "server": "amazon.com",
            "date": "Mon, 14 Aug 2023 23:18:26 GMT"
        },
        "RetryAttempts": 0
    }
}

describe_stream: example response from moto:
{
    "StreamDescription": {
        "StreamName": "lst-use1-guest360-dlr-cme-kinesis-test",
        "StreamARN": "arn:aws:kinesis:us-east-1: 123456789012:stream/lst-use1-guest360-dlr-cme-kinesis-test",
        "StreamStatus": "ACTIVE",
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "StartingHashKey": "0",
                    "EndingHashKey": "340282366920938463463374607431768211456"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber": "1"
                }
            }
        ],
        "HasMoreShards": False,
        "RetentionPeriodHours": 24,
        "StreamCreationTimestamp": datetime.datetime(2023,8,14,22,53,43,318114),
        "EnhancedMonitoring": [
            {
                "ShardLevelMetrics": []
            }
        ],
        "EncryptionType": "NONE"
    },
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "server": "amazon.com",
            "date": "Mon,14 Aug 2023 22: 53: 59 GMT"
        },
        "RetryAttempts": 0
    }
}
"""
