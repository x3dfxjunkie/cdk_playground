"""dms_replication_task construct tests
"""
import logging
import sys
import json
import pytest
import yaml
from aws_cdk import App, Environment, Stack
from aws_cdk.assertions import Template

from app.guest360_constructs.ingestion.dms.dms_replication_task import Guest360DMSReplicationTask

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

STACK_ID = "TestStack"
DMS_TASK_ID = "TestTask"

SHORT_ENV = {
    "ephemeral": "lst",
    "latest": "lst",
    "stage": "stg",
    "load": "lod",
    "prod": "prd",
}

DMS_REP_INSTANCE_ARN = "arn:aws:dms:us-east-1:123456789012:rep:abc123def456ghi789"
DMS_SOURCE_ENDPOINT_ARN = "arn:aws:rds:us-east-1:123456789012:db:my-db-instance"
DMS_TARGET_ENDPOINT_ARN = "arn:aws:kinesis:us-east-1:123456789012:stream/my-stream"
DMS_MIGRATION_TYPE = "full-load-and-cdc"

TABLE_MAPPINGS = {
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {"schema-name": "my_database", "table-name": "my_table1"},
            "rule-action": "include",
            "filters": [],
        },
        {
            "rule-type": "selection",
            "rule-id": "2",
            "rule-name": "2",
            "object-locator": {"schema-name": "my_database", "table-name": "my_table2"},
            "rule-action": "include",
            "filters": [],
        },
    ]
}

# Data extracted from app/infrastructure/reliability/configs/alarm_defaults.yaml for p3
SNS_TOPICS_CI_SERVICE_NOW = {
    "local": {"topic": "wdpr-guest360-dev-snow-pri4", "snow_config_item": "WDPR Guest360 - AWS Latest"},
    "latest": {"topic": "wdpr-guest360-dev-snow-pri4", "snow_config_item": "WDPR Guest360 - AWS Latest"},
    "load": {"topic": "wdpr-guest360-tst-snow-pri4", "snow_config_item": "WDPR Guest360 - AWS Load Test"},
    "stage": {"topic": "wdpr-guest360-tst-snow-pri4", "snow_config_item": "WDPR Guest360 - AWS Staging"},
    "prod": {"topic": "wdpr-guest360-prd-snow-pri4", "snow_config_item": "WDPR Guest360 - AWS Production"},
}


@pytest.fixture
def setup_environment(environment):
    short_env = SHORT_ENV[environment]
    test_context = {
        "environment": environment,
        "prefix": f"{short_env}-use1-guest360",
    }
    snow_topic = SNS_TOPICS_CI_SERVICE_NOW[environment]["topic"]
    snow_ci = SNS_TOPICS_CI_SERVICE_NOW[environment]["snow_config_item"]
    test_app = App(context=test_context)
    test_stack = Stack(test_app, STACK_ID, env=Environment(account="123456789", region="us-east-1"))

    dms_task_props = {
        "replication_task_identifier": DMS_TASK_ID,
        "source_endpoint_arn": DMS_SOURCE_ENDPOINT_ARN,
        "target_endpoint_arn": DMS_TARGET_ENDPOINT_ARN,
        "replication_instance_arn": DMS_REP_INSTANCE_ARN,
        "migration_type": DMS_MIGRATION_TYPE,
        "table_mappings": TABLE_MAPPINGS,
    }

    task = Guest360DMSReplicationTask(test_stack, DMS_TASK_ID, props=dms_task_props)

    # render template.
    template = Template.from_stack(test_stack)
    logger.debug(yaml.dump(template.to_json()))

    return (short_env, snow_topic, snow_ci, template, task)


# Deploy dms Replication Task (test all environments)
@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["latest", "load", "stage", "prod"])
def test_rds_mysql_to_kinesis_rep_task(setup_environment):
    short_env, _, _, template, task = setup_environment

    assert task.dms_replication_name == f"{short_env}-use1-g360-testtask"

    template.has_resource_properties(
        "AWS::DMS::ReplicationTask",
        {
            "MigrationType": DMS_MIGRATION_TYPE,
            "TableMappings": json.dumps(TABLE_MAPPINGS),
            "ReplicationInstanceArn": DMS_REP_INSTANCE_ARN,
            "SourceEndpointArn": DMS_SOURCE_ENDPOINT_ARN,
            "TargetEndpointArn": DMS_TARGET_ENDPOINT_ARN,
            "ReplicationTaskIdentifier": f"{short_env}-use1-g360-testtask",
        },
    )


# Test Enabled servicenow ticket creation (p3 alarm) on {environment}-infra-feature-flags.yaml
@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["latest", "load", "stage"])
def test_p3_alarm_service_now_tickets(setup_environment):
    _, snow_topic, snow_ci, template, _ = setup_environment
    template.has_resource_properties(
        "AWS::CloudWatch::Alarm",
        {
            "ActionsEnabled": True,
            "AlarmActions": [f"arn:aws:sns:us-east-1:123456789:{snow_topic}"],
            "AlarmDescription": f"[SNOWAG:app-global-Guest360][SNOWCI:{snow_ci}][SNOWDESC:Guest360DMSReplicationTask2990c failed on CustomDMSTaskFailure ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 3]Guest360DMSReplicationTask2990c failed on CustomDMSTaskFailure ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD 3",
            "MetricName": "CustomDMSTaskFailure",
            "Namespace": "DMSTaskFailed",
        },
    )


# Disabled servicenow  ticket creation (use default alarm) on {environment}-infra-feature-flags.yaml
# Focus on validating the default sns topic
@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["prod"])
def test_default_alarm_static_env(setup_environment):
    short_env, _, _, template, _ = setup_environment
    # Validate it creates the Alarm for DMS task in static environment
    template.has_resource_properties(
        "AWS::CloudWatch::Alarm",
        {
            "ActionsEnabled": True,
            "AlarmActions": [f"arn:aws:sns:us-east-1:123456789:{short_env}-use1-guest360-alarm-notifications"],
        },
    )
