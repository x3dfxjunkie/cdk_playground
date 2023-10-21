"""test init rds"""
import logging
import sys
import os
import botocore

import boto3
import pytest
from unittest.mock import patch, Mock
from moto import mock_rds

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

RDS_PROPS = {
    "DBName": "testdb",
    "DBInstanceIdentifier": "testdb",
    "AllocatedStorage": 123,
    "DBInstanceClass": "db.m5.large",
    "Engine": "mariadb",
    "MasterUsername": "testuser",  # pragma: allowlist secret
}

test_rep_inst_arn = "arn:aws:dms:us-east-1:123456789012:rep:dmsreplicationinstance01"

REPLICATION_INSTANCE = {
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "string",
        "ReplicationInstanceClass": "string",
        "ReplicationInstanceStatus": "string",
        "AllocatedStorage": 123,
        "MultiAZ": True,
        "EngineVersion": "3.4.7",
        "KmsKeyId": "12345677890",
        "ReplicationInstanceArn": test_rep_inst_arn,
    }
}


def mock_make_api_call(self, operation_name, kwarg):
    # We need this because Create Replication Instance is currently not supported by moto: https://docs.getmoto.org/en/4.1.11/docs/services/dms.html
    if operation_name == "CreateReplicationInstance":
        return REPLICATION_INSTANCE


@pytest.fixture
def mock_os_environment(monkeypatch):
    # monkeypatch all environment variables necessary w/out affecting OS environment
    monkeypatch.setenv("ENDPOINT", "db-master-1.aaaaaaaaaa.us-east-1.rds.amazonaws.com")
    monkeypatch.setenv("PORT", "3306")
    monkeypatch.setenv("USER", "testuser")
    monkeypatch.setenv("DBNAME", "testdb")
    monkeypatch.setenv("REGION", "us-east-1")
    monkeypatch.setenv("DBInstanceIdentifier", "testdb")


@mock_rds
def test_reboot_rds(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    event = {"action": RDSAction.REBOOT}
    lambda_handler(event, None)  # pylint: disable=E1128,W0612


@mock_rds
def test_start_rds(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    db_inst_identifier = os.getenv("DBInstanceIdentifier")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    rds_client.stop_db_instance(DBInstanceIdentifier=db_inst_identifier)
    event = {"action": RDSAction.START}
    lambda_handler(event, None)  # pylint: disable=E1128,W0612


@mock_rds
def test_stop_rds(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    event = {"action": RDSAction.STOP}
    lambda_handler(event, None)  # pylint: disable=E1128,W0612


@mock_rds
def test_modify_rds(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    event = {"action": RDSAction.MODIFY, "ApplyImmediately": True, "EngineVersion": "10.6.15"}
    lambda_handler(event, None)  # pylint: disable=E1128,W0612


def test_lambda_handler_invalid_reboot(mock_os_environment):
    # no rds to reboot
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    event = {"action": RDSAction.REBOOT}
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "DBInstanceNotFoundFault"


@mock_rds
def test_lambda_handler_invalid_start(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    event = {"action": RDSAction.START}
    # try to 'start' an instance which is already running
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "InvalidDBInstanceStateFault"


@mock_rds
def test_lambda_handler_invalid_stop(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    db_inst_identifier = os.getenv("DBInstanceIdentifier")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    rds_client.stop_db_instance(DBInstanceIdentifier=db_inst_identifier)
    event = {"action": RDSAction.STOP}
    # try to 'stop' an instance which is already stopped
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "InvalidDBInstanceStateFault"


@mock_rds
def test_lambda_handler_invalid_modify(mock_os_environment):
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    region = os.getenv("REGION")
    rds_client = boto3.client("rds", region)

    rds_client.create_db_instance(**RDS_PROPS)
    event = {"action": RDSAction.MODIFY, "invalidKey": "something"}
    with pytest.raises(botocore.exceptions.ParamValidationError):
        lambda_handler(event, None)  # pylint: disable=E1128,W0612


def test_lambda_handler_invalid_client_modify(mock_os_environment):
    # no rds to modify
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    event = {"action": RDSAction.MODIFY, "ApplyImmediately": True, "EngineVersion": "10.6.15"}
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "DBInstanceNotFoundFault"


def test_lambda_handler_modify_dms(mock_os_environment):
    with patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
        from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

        event = {
            "action": RDSAction.MODIFY_DMS,
            "ReplicationInstanceArn": test_rep_inst_arn,
            "ApplyImmediately": True,
            "EngineVersion": "3.5.1",
            "AllowMajorVersionUpgrade": True,
        }
        lambda_handler(event, None)  # pylint: disable=E1128,W0612


def test_lambda_handler_reboot_dms(mock_os_environment):
    with patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call):
        from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

        event = {
            "action": RDSAction.REBOOT_DMS,
            "ReplicationInstanceArn": test_rep_inst_arn,
        }
        lambda_handler(event, None)  # pylint: disable=E1128,W0612


def test_lambda_handler_invalid_modify_dms(mock_os_environment):
    # no dms to modify
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    event = {
        "action": RDSAction.MODIFY_DMS,
        "ReplicationInstanceArn": test_rep_inst_arn,
        "ApplyImmediately": True,
        "EngineVersion": "3.5.1",
        "AllowMajorVersionUpgrade": True,
    }
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "ResourceNotFoundFault"


def test_lambda_handler_invalid_reboot_dms(mock_os_environment):
    # no dms to reboot
    from app.src.load_testing.lambdas.rds_manager.main import lambda_handler, RDSAction

    event = {
        "action": RDSAction.REBOOT_DMS,
        "ReplicationInstanceArn": test_rep_inst_arn,
    }
    with pytest.raises(botocore.exceptions.ClientError) as exc:
        lambda_handler(event, None)  # pylint: disable=E1128,W0612
        err = exc.value.response["Error"]
        assert err["Message"] == "ResourceNotFoundFault"
