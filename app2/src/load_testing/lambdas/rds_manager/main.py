""" Lambda Function Code for Managing RDS instances for chaos testing
    Used to: Simulate patching, starts, stops, updates to RDS instances

    Valid payloads include:
    - {"action": "start" }
    - {"action": "stop" }
    - {"action": "modify", "ApplyImmediately": true, "EngineVersion": "10.6.15"}
    - {"action": "modify", "ApplyImmediately": true, "CACertificateIdentifier": "rds-ca-rsa2048-g1", "CertificateRotationRestart": true}
    - {"action": "modify_dms_inst", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:543276908693:rep:XXXX", "ApplyImmediately": true, "EngineVersion": "3.5.1", "AllowMajorVersionUpgrade": true}
    - {"action": "reboot_dms_inst", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:543276908693:rep:XXXX"}

"""
import os
import boto3
import botocore
from enum import Enum
from aws_lambda_powertools import Logger, Metrics

NAMESPACE = os.getenv("NAMESPACE", "RDSActionFailed")
RDS_FAILURE_METRIC = os.getenv("RDS_FAILURE_METRIC", "RDSActionFailure")
region = os.getenv("REGION")
db_inst_identifier = os.getenv("DBInstanceIdentifier")

logger = Logger(service=__name__)
metrics = Metrics(namespace=NAMESPACE)

rds_client = boto3.client("rds", region_name=region)

dms_client = boto3.client("dms", region_name=region)


class UnknownActionError(Exception):
    """Custom exception for unknown manual rds action"""


class RDSAction(str, Enum):
    START: str = "start"
    STOP: str = "stop"
    REBOOT: str = "reboot"
    MODIFY: str = "modify"
    MODIFY_DMS: str = "modify_dms_inst"
    REBOOT_DMS: str = "reboot_dms_inst"


def handle_rds_event(event: dict) -> None:
    """handles payload to start/stop/reboot/modify dms or rds instances"""
    match event.pop("action"):
        case RDSAction.STOP:
            stop_rds(db_inst_identifier)
        case RDSAction.START:
            start_rds(db_inst_identifier)
        case RDSAction.REBOOT:
            reboot_rds(db_inst_identifier)
        case RDSAction.MODIFY:
            kwargs = event
            modify_rds(db_inst_identifier, **kwargs)
        case RDSAction.MODIFY_DMS:
            kwargs = event
            modify_dms_instance(**kwargs)
        case RDSAction.REBOOT_DMS:
            kwargs = event
            reboot_dms_instance(**kwargs)
        case _:
            raise UnknownActionError(f"Unknown action supplied: Valid values are: {[e.value for e in RDSAction]}")


def stop_rds(db_inst_identifier: str) -> None:
    """Stop a RDS db instance"""
    try:
        response = rds_client.stop_db_instance(DBInstanceIdentifier=db_inst_identifier)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error("### Error while trying to stop the rds instance: %s", err, error_type=type(err).__name__)
        raise err


def start_rds(db_inst_identifier: str) -> None:
    """start a RDS db instance"""
    try:
        response = rds_client.start_db_instance(DBInstanceIdentifier=db_inst_identifier)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error("### Error while trying to start the rds instance: %s", err, error_type=type(err).__name__)
        raise err


def reboot_rds(db_inst_identifier: str) -> None:
    """reboot a RDS db instance"""
    try:
        response = rds_client.reboot_db_instance(DBInstanceIdentifier=db_inst_identifier)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error("### Error while trying to reboot the rds instance: %s", err, error_type=type(err).__name__)
        raise err


def modify_rds(db_inst_identifier: str, **kwargs) -> None:
    """modify a RDS db instance per docs https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_instance.html"""
    try:
        response = rds_client.modify_db_instance(DBInstanceIdentifier=db_inst_identifier, **kwargs)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error("### Error while trying to modify the rds instance: %s", err, error_type=type(err).__name__)
        raise err


def modify_dms_instance(**kwargs) -> None:
    """modify a dms replication instance instance per docs https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_replication_instance.html"""
    try:
        response = dms_client.modify_replication_instance(**kwargs)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error(
            "### Error while trying to modify the dms replication instance: %s", err, error_type=type(err).__name__
        )
        raise err


def reboot_dms_instance(**kwargs) -> None:
    """reboot a DMS replication instance"""
    try:
        response = dms_client.reboot_replication_instance(**kwargs)
        logger.info(response)
    except (botocore.exceptions.ClientError,) as err:
        logger.error(
            "### Error while trying to modify the dms replication instance: %s", err, error_type=type(err).__name__
        )
        raise err


@metrics.log_metrics()
def lambda_handler(event, _):  # pylint: disable=W0613
    """handles payload to start/stop/reboot/modify dms or rds instances"""
    handle_rds_event(event)
