"""
Test Data Contract Event Pipes Validation
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures

import json
import logging
import sys
from importlib import reload
from unittest import mock

import pytest
from app.src.ingestion.event_pipes.utils.app_config_utils import get_app_config_data
from app.src.ingestion.event_pipes.utils.data_contract_utils import DataContractNotFoundException
from app.src.ingestion.event_pipes.validation.tests.unit_tests.sample_payloads_and_events import (
    DATA_PIPE_INFO,
    DATA_PIPE_INFO_GALAXY,
    DATA_PIPE_INFO_GAM,
    DATA_PIPE_INFO_DINETIME,
    DATA_PIPE_INFO_PLAYAPP,
    DATA_PIPE_INFO_SNAPP,
    DATA_PIPE_INFO_SHOPDISNEY,
    DINETIME_EVENT,
    EVENT_CME_DOUBLE,
    EVENT_CME_INVBUCKETDATETIME,
    EVENT_CME_INVBUCKETDATETIME_TRANSACTION_ID,
    EVENT_CME_RESERVATION,
    EVENT_CME_RESERVATION_CLOUDEVENT,
    EVENT_CME_RESERVATION_OPERATION_LOAD,
    EVENT_CME_VALIDATION_ERROR,
    EVENT_DOES_NOT_MATCH_DATACONTRACT,
    GALAXY_EVENT,
    GAM_DLR_EVENT,
    GAM_DLR_BROKEN_EVENT,
    PLAYAPP_EVENT,
    SHOPDISNEY_EVENT,
    SNAPP_EVENT,
)
from aws_lambda_powertools import Logger, Metrics
from aws_lambda_powertools.metrics import metrics as metrics_global
from cloudevents.pydantic import CloudEvent
from pydantic import error_wrappers
from typing import Dict

MOCK_URL = "http://localhost:2772/applications/lst-teststack-use1-testappconfig-app/environments/lst-teststack-use1-testappconfig-env/configurations/lst-teststack-use1-testappconfig-profile"


# set log levels for noisy calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class LambdaContext:
    """
    Sample Lambda Context that only include required fields
    """

    function_name: str

    def __init__(self, function_name: str) -> None:
        self.function_name = function_name


CONTEXT = LambdaContext("validator_lambda")


@pytest.fixture(scope="module")
def monkeypatch_module():
    mpatch = pytest.MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="module", autouse=True)
def mock_os_env(monkeypatch_module):  # pylint: disable=redefined-outer-name
    monkeypatch_module.setenv("APPCONFIG_URL_PATH", "")
    monkeypatch_module.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch_module.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch_module.setenv("AWS_LAMBDA_FUNCTION_NAME", "testing")
    monkeypatch_module.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch_module.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch_module.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch_module.setenv("eventSourceARN", "arn:aws:kinesis:region:0000000000000:stream/stream-name")
    monkeypatch_module.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch_module.setenv("OTEL_NAMESPACE", "testing_namespace")


@pytest.fixture(scope="function", autouse=True)
def reset_metric_set():
    # Clear out every metric data prior to every test
    metrics = Metrics()
    metrics.clear_metrics()
    metrics_global.is_cold_start = True  # ensure each test has cold start
    metrics.clear_default_dimensions()  # remove persisted default dimensions, if any
    yield


def test_get_app_config_data(mock_requests):
    result = get_app_config_data(url_path=MOCK_URL, timeout=30)
    assert result == DATA_PIPE_INFO
    mock_requests.assert_called_once_with(MOCK_URL, timeout=30)


@pytest.fixture(scope="module", autouse=True)
def mock_requests():
    mock_response = mock.Mock()
    mock_response.content.decode.return_value = json.dumps(DATA_PIPE_INFO).encode("utf-8")
    with mock.patch("requests.get") as mock_requests:
        mock_requests.return_value = mock_response
        yield mock_requests


# Ensure datacontract validation does not fail for transaction_id optional field
def test_cme_invbucketdatetime_transaction_id_optional():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_INVBUCKETDATETIME_TRANSACTION_ID, CONTEXT)
    assert response[0]["data"]["metadata"]["table-name"] == "inv_bucket_date_time"


def test_cme_reservation_source_data_contract():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_RESERVATION, CONTEXT)
    logger.debug(f"{response=}")
    assert len(response) == 1


def test_cme_reservation_cloudevent_data():
    check_keys = {
        "source",
        "id",
        "type",
        "subject",
        "specversion",
        "time",
        "datacontenttype",
        "tracestate",
        "traceparent",
    }
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_RESERVATION_CLOUDEVENT, CONTEXT)
    logger.debug(f"{response=}")
    assert len(response) == 1
    # ensure response has all check_keys by diffing sets and checking to ensure empty
    assert not (check_keys - response[0].keys())


def test_cme_reservation_otel_propagation_in_response():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_RESERVATION, CONTEXT)
    logger.debug(f"{response=}")
    assert len(response) == 1
    assert response[0].get("traceparent")
    assert response[0].get("tracestate")


# Ensure datacontract validation does not fail for metadata operation load new enum
def test_cme_reservation_operation_load():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_RESERVATION_OPERATION_LOAD, CONTEXT)
    assert response[0]["data"]["metadata"]["table-name"] == "reservation"


def test_cme_double_object():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_DOUBLE, CONTEXT)
    assert len(response) == 2


@pytest.mark.skip(reason="should be implemented for following sprints to 7")
def test_cme_not_match_data_contractv1():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    with pytest.raises((runner.DataValidationError, DataContractNotFoundException)) as err:
        runner.lambda_handler(EVENT_DOES_NOT_MATCH_DATACONTRACT, CONTEXT)
    assert isinstance(err.value, (runner.DataValidationError, DataContractNotFoundException))


def test_cme_not_match_data_contractv2():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_DOES_NOT_MATCH_DATACONTRACT, CONTEXT)
    assert response[0]["exception_error"].startswith("DataContractNotFoundException:")


@pytest.mark.skip(reason="should be implemented for following sprints to 7")
def test_cme_invbucketdatetime_pydantic_validation_errorv1():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    with pytest.raises(runner.DataValidationError):
        runner.lambda_handler(EVENT_CME_VALIDATION_ERROR, CONTEXT)


def test_cme_invbucketdatetime_pydantic_validation_errorv2():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    response = runner.lambda_handler(EVENT_CME_VALIDATION_ERROR, CONTEXT)
    assert response[0]["exception_error"].startswith("ValidationError:")


@pytest.mark.skip(reason="should be implemented for following sprints to 6")
def test_cme_invbucketdatetime_pydantic_validation_error2():
    from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

    with pytest.raises(error_wrappers.ValidationError):
        runner.lambda_handler(EVENT_CME_VALIDATION_ERROR, CONTEXT)


def test_event_keys_success():
    expected_tuple = (
        "eyJkYXRhIjogeyJpZCI6IDc0MDA3NDUzLCJyZXNfaWQiOiAiNDUwNjA2NDA3NzE0NjUzMTg0IiwiY29uZl9pZCI6ICI0NTA2MDY0MDc2OTc4NzU5NjgiLCJzd2lkIjogInsyNDkwQ0E0Ny1BQUFBLUJCQkItOTM5Ny04NEYzNDNCN0I3MjZ9Iiwid2FzX2ludl9vdmVycmlkZSI6IDAsImd1ZXN0X2ZpcnN0X25hbWUiOiAiR3Vlc3QiLCJndWVzdF9sYXN0X25hbWUiOiAiVGhyZWVTaXh0eSIsImd1ZXN0X2VtYWlsX2lkIjogIm5vdHJlYWxAeW9wbWFpbC5jb20iLCJpbnZfYnVja2V0X2lkIjogIldEV19NS19BUF9EQUlMWSIsImV4cF9kYXRlIjogIjIwMjMtMDQtMjEiLCJleHBfc2xvdCI6ICJEQUlMWSIsImV4cF9wYXJrIjogIldEV19NSyIsInByb2R1Y3RfaWQiOiAiV0RXX0FQIiwic2xvdF9zdGFydF9kdHMiOiAiMjAyMy0wNC0yMVQwMzowMDowMFoiLCJyZXNfc3RhdHVzIjogIkFMTE9DQVRFRCIsInRrdF92aXN1YWxfaWQiOiAiMjQxMzI5MDUwODIyMDAwMzIiLCJyZXNfdGlja2V0X3NrdSI6ICJOMUZDMyIsInJlc19vcmlnaW4iOiAiV0VCLVRJQ0tFVFMtUEFTU0VTIiwiY3JlYXRlZF91c3IiOiAiZi1jbWUtcmVzZXJ2YXRpb24iLCJjcmVhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJ1cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJhZ2VfZ3JvdXAiOiAiQURVTFQiLCJzaG93X2xhc3RfZm91ciI6IDAsInN1cnZleV9zZW50IjogMCwiYXV0b191cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMFoifSwibWV0YWRhdGEiOiB7InRpbWVzdGFtcCI6ICIyMDIzLTA0LTE3VDE3OjMzOjE3LjM4MTM4MloiLCJyZWNvcmQtdHlwZSI6ICJkYXRhIiwib3BlcmF0aW9uIjogImluc2VydCIsInBhcnRpdGlvbi1rZXktdHlwZSI6ICJzY2hlbWEtdGFibGUiLCJzY2hlbWEtbmFtZSI6ICJhd2FrZW5pbmciLCJ0YWJsZS1uYW1lIjogInJlc2VydmF0aW9uIiwidHJhbnNhY3Rpb24taWQiOiA4MDY3NDk0ODEyOTM1MTJ9fQ==",  # pragma: allowlist secret
        "49640450530655783448641595467156077838773832572853026818",
        "000000000000-49640450530655783448641595467156077838773832572853026818",
        "test2",
    )
    from app.src.ingestion.event_pipes.utils.event_processing_utils import get_event_items  # pylint: disable=C0415

    mock_logger = mock.Mock(spec=Logger)
    return_tuple = get_event_items(EVENT_CME_RESERVATION[0], mock_logger)
    logger.info(f"{return_tuple=}")
    assert isinstance(return_tuple, tuple)
    assert return_tuple == expected_tuple


def test_event_keys_key_error():
    event = EVENT_CME_RESERVATION[0]
    from app.src.ingestion.event_pipes.utils.event_processing_utils import get_event_items  # pylint: disable=C0415

    mock_logger = mock.Mock(spec=Logger)

    # force missing partitionkey
    event.pop("partitionKey", None)
    with pytest.raises(KeyError) as exception_info:
        get_event_items(event, mock_logger)
    assert str(exception_info.value) == "'partitionKey'"


def test_get_event_data():
    event_data = EVENT_CME_INVBUCKETDATETIME[0]["data"]
    from app.src.ingestion.event_pipes.data_mapper.data_mapper import IngestionDataMapper

    mock_logger = mock.Mock(spec=Logger)
    data_mapper = IngestionDataMapper.get_data_mapper("nested")({})
    return_dict = data_mapper.parse_payload(event_data, mock_logger)
    logger.debug(f"{return_dict=}")
    assert isinstance(return_dict, dict)


def test_get_event_data_bad_base64():
    event_data = EVENT_CME_INVBUCKETDATETIME[0]["data"]
    event_data = event_data + "myBadData"
    from app.src.ingestion.event_pipes.data_mapper.data_mapper import IngestionDataMapper

    mock_logger = mock.Mock(spec=Logger)
    data_mapper = IngestionDataMapper.get_data_mapper("nested")({})

    with pytest.raises(ValueError) as exception_info:
        data_mapper.parse_payload(event_data, mock_logger)
    logger.debug(f"{exception_info=}")


def test_get_cloudevent_success():
    event_data = {
        "data": b"\x00\x00\x11Hello World",
        "datacontenttype": "application/octet-stream",
        "dataschema": None,
        "id": "11775cb2-fd00-4487-a18b-30c3600eaa5f",
        "source": "dummy:source",
        "specversion": "1.0",
        "subject": None,
        "time": "2022-07-16 12:03:20.519216+00:00",
        "type": "dummy.type",
    }
    from app.src.ingestion.event_pipes.utils.cloudevent_utils import get_cloudevent

    mock_logger = mock.Mock(spec=Logger)

    cloudevent = get_cloudevent(event_data, mock_logger)
    assert isinstance(cloudevent, CloudEvent)


def test_get_cloudevent_unsuccessful():
    event_data = {"foo": "bar"}
    from app.src.ingestion.event_pipes.utils.cloudevent_utils import get_cloudevent

    mock_logger = mock.Mock(spec=Logger)

    cloudevent = get_cloudevent(event_data, mock_logger)
    assert cloudevent is None


def test_get_shard_seq_successful():
    expected = "000000000000-49640450530655783448641595467156077838773832572853026818"
    event_id = EVENT_CME_RESERVATION[0]["eventID"]
    from app.src.ingestion.event_pipes.utils.event_processing_utils import get_shard_seq  # pylint: disable=C0415

    assert get_shard_seq(event_id) == expected


@pytest.mark.skip(reason="should be implemented for following sprints to 7")
def test_get_shard_seq_unsuccessfulv1():
    event_id = "notme"
    from app.src.ingestion.event_pipes.validation import runner

    with pytest.raises((runner.DataValidationError, error_wrappers.ValidationError)) as err:
        runner.lambda_handler(EVENT_CME_VALIDATION_ERROR, CONTEXT)
    assert isinstance(err.value, (runner.DataValidationError, error_wrappers.ValidationError))


def test_get_shard_seq_unsuccessfulv2():
    event_id = "notme"
    from app.src.ingestion.event_pipes.utils.event_processing_utils import get_shard_seq  # pylint: disable=C0415

    with pytest.raises(ValueError):
        get_shard_seq(event_id)


@pytest.fixture
def delete_ingestion_modules_imported():
    # This fixture is needed to delete the app.src.ingestion.* modules we've already imported because otherwise, the variables
    # which read from the os environment variables in the lambda code have already been assigned and won't change

    ingestion_modules = {k: v for k, v in sys.modules.items() if "app.src" in k}
    for k in ingestion_modules.keys():
        sys.modules.pop(k)  # delete the imports
    yield
    sys.modules = {**sys.modules, **ingestion_modules}  # re-add them to be a good potato and not wreak havoc


def patch_requests_get(data: dict):
    mock_response = mock.Mock()
    mock_response.content.decode.return_value = json.dumps(data).encode("utf-8")

    return mock.patch("requests.get", return_value=mock_response)


def test_gam_events():
    with patch_requests_get(DATA_PIPE_INFO_GAM):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(GAM_DLR_EVENT, CONTEXT)
        assert len(results) == 2
        assert {result["type"] for result in results} == {
            "app.src.data_structures.data_contracts.source.gam_dlr.v0.gam_dlr_tickets_source_data_contract.GAMDLRTicketsModel",
            "app.src.data_structures.data_contracts.source.gam_dlr.v0.gam_dlr_registered_guest_source_data_contract.GAMDLRRegisteredGuestModel",
        }


def test_cloud_event_attributes():
    with patch_requests_get(DATA_PIPE_INFO_GAM):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        results = runner.lambda_handler([*GAM_DLR_EVENT, *EVENT_CME_VALIDATION_ERROR], CONTEXT)
        for result in results:
            assert all(
                key in result
                for key in ("id", "type", "source", "subject", "stream", "partition_key", "check_sum", "validated")
            )


def test_metrics_counts():
    with patch_requests_get(DATA_PIPE_INFO_GAM):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        from aws_lambda_powertools.metrics import MetricUnit, MetricResolution

        old_add_metric = runner.powertool_metrics.add_metric

        add_metric_counts: Dict[str, float] = {
            "rows_failed": 0.0,
            "rows_warning": 0.0,
            "rows_success": 0.0,
            "rows_started": 0.0,
        }

        def monkey_patched_add_metric(
            name: str, unit: MetricUnit | str, value: float, resolution: MetricResolution | int = 60
        ) -> None:
            nonlocal add_metric_counts
            if name not in add_metric_counts:
                add_metric_counts[name] = value
            else:
                add_metric_counts[name] += value
            old_add_metric(name, unit, value, resolution)

        runner.powertool_metrics.add_metric = monkey_patched_add_metric

        runner.lambda_handler([*GAM_DLR_EVENT, *EVENT_CME_VALIDATION_ERROR], CONTEXT)

        # We should expect 1 failed 2 success
        print(add_metric_counts)

        assert round(add_metric_counts["rows_failed"]) == 1
        assert round(add_metric_counts["rows_warning"]) == 0
        assert round(add_metric_counts["rows_success"]) == 2
        assert round(add_metric_counts["rows_started"]) == 3


def test_gam_entitlement_events():
    # NOTE: with cloudevent wrapping, this fails
    with patch_requests_get(DATA_PIPE_INFO_GAM):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        results = runner.lambda_handler(GAM_DLR_BROKEN_EVENT, CONTEXT)
        assert len(results) == 1


def test_playapp_quest_events():
    only_contract = DATA_PIPE_INFO_PLAYAPP["data_contracts"][0]  # for singleton, we only have one contract
    with patch_requests_get(DATA_PIPE_INFO_PLAYAPP):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(PLAYAPP_EVENT, CONTEXT)
        assert len(results) == 1
        assert f"{only_contract['data_contract']}.{only_contract['class_name']}" == results[0]["type"]


def test_galaxy_events():
    with patch_requests_get(DATA_PIPE_INFO_GALAXY):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(GALAXY_EVENT, CONTEXT)
        assert len(results) == 1
        assert results[0]["router_table"] == "GTS.Galaxy.Pass.Created"


def test_dinetime_cloudevent_events():
    with patch_requests_get(DATA_PIPE_INFO_DINETIME):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(DINETIME_EVENT, CONTEXT)
        assert len(results) == 1
        assert results[0]["router_table"] == "DINING_RESERVATION"


def test_dinetime_cloudevent_event_no_parse_key():
    from app.src.ingestion.event_pipes.data_mapper.data_mapper import PayloadParsingError

    DATA_PIPE_INFO_DINETIME["key_to_load"] = "some-nonexistent-key"
    with pytest.raises(PayloadParsingError), patch_requests_get(DATA_PIPE_INFO_DINETIME):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        runner.lambda_handler(DINETIME_EVENT, CONTEXT)


def test_snapp_events():
    with patch_requests_get(DATA_PIPE_INFO_SNAPP):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(SNAPP_EVENT, CONTEXT)
        assert len(results) == 1
        assert results[0]["validated"]


def test_nested_xml_events():
    with patch_requests_get(DATA_PIPE_INFO_SHOPDISNEY):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        runner = reload(runner)
        results = runner.lambda_handler(SHOPDISNEY_EVENT, CONTEXT)
        assert len(results) == 1


def test_no_data_contracts_in_mappings(monkeypatch, delete_ingestion_modules_imported):
    data_pipe_info_no_contracts = {k: v for k, v in DATA_PIPE_INFO.items() if k != "data_contracts"}

    with patch_requests_get(data_pipe_info_no_contracts):
        from app.src.ingestion.event_pipes.validation import runner  # pylint: disable=C0415

        response = runner.lambda_handler(EVENT_CME_RESERVATION_OPERATION_LOAD, CONTEXT)
        assert response[0]["exception_error"].startswith("DataContractNotFoundException:")
