"""
Evaluator of Load and E2E tests
"""
import logging
import os

import boto3
from app.src.load_testing.lambdas.evaluator_system_test.evaluator_system import EvaluatorSystemTest
from botocore.client import ClientError

# config names
CONFIG_PARAMETERS = "parameters"
CONFIG_EXECUTION_ID = "executionid"
CONFIG_TRACE_ID = "traceid"
CONFIG_OUTPUT = "output"


CONFIG_START_TIME = "start_time"
CONFIG_PREFIX = "prefix"
CONFIG = "config"
CONFIG_SCENARIO_NAME = "scenario_name"
CONFIG_SYSTEM = "system_test"

dynamodb = boto3.resource("dynamodb", "us-east-1")

logger = logging.getLogger(__name__)


# pylint: disable=W0612, W0621
def lambda_handler(event, _):
    execution_id = event.get(CONFIG_EXECUTION_ID)
    trace_id = event.get(CONFIG_TRACE_ID)
    start_time = event.get(CONFIG_START_TIME)
    prefix = event.get(CONFIG_PREFIX)

    parameter_config = event.get(CONFIG)

    scenario_name = event.get(CONFIG_SCENARIO_NAME)
    evaluator = EvaluatorSystemTest(start_time, prefix, trace_id)
    system_test_metric = evaluator.get_parameter_value(parameter_config)

    save_metrics_to_dynamodb(execution_id, scenario_name, trace_id, system_test_metric)


def save_metrics_to_dynamodb(execution_id, scenario_name, trace_id, system_test_metric):
    table = dynamodb.Table(os.getenv("DDB_TABLE_RESULT"))

    item = {
        "execution_name": execution_id,
        "test_case_record_name": system_test_metric["name"],
        "test_case_record_type": "metric",
        "test_case_type": "system",
        "scenario_name": scenario_name,
        "trace_id": trace_id,
        # TODO: Tech Debt: This will not always be INT
        "system_test_metric_value": int(system_test_metric["value"]),
        "system_test_metric_metadata": system_test_metric["metadata"],
    }

    try:
        table.put_item(Item=item)
    except ClientError as e:
        logger.error(
            "An error occurred while saving item to DynamoDB: %s",
            e.response["Error"]["Message"],
        )
