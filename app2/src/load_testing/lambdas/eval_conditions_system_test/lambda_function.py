"""
Evaluator of Load and E2E tests
"""
import logging
import os

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import BotoCoreError, ClientError

# config names

CONFIG_EXECUTION_ID = "executionid"
CONFIG_TRACE_ID = "traceid"
CONFIG_OUTPUT = "output"
CONFIG_PARAMETER = "parameters"

CONFIG_TESTS = "tests"


CONFIG = "config"
CONFIG_SCENARIO_NAME = "name"
CONFIG_SYSTEM = "system_test"

dynamodb = boto3.resource("dynamodb", "us-east-1")
TABLE = dynamodb.Table(os.getenv("DDB_TABLE_RESULT"))

logger = logging.getLogger(__name__)


def lambda_handler(event, _context) -> None:
    """Lambda handler that read the values from DynamoDb
    and then evaluate the condition to the system test
    and push the result in a DynamoDB"""

    execution_name = event.get(CONFIG_EXECUTION_ID)
    trace_id = event.get(CONFIG_TRACE_ID)
    output_config = event.get(CONFIG).get(CONFIG_OUTPUT)
    tests_config = output_config.get(CONFIG_TESTS)
    scenario_name = event.get(CONFIG).get(CONFIG_SYSTEM).get(CONFIG_SCENARIO_NAME)
    parameters_names = output_config.get(CONFIG_PARAMETER)
    metrics_values = get_metrics_values_from_dynamodb(execution_name)
    results = evaluate_condition_tests(tests_config, metrics_values, parameters_names)
    save_results_to_dynamodb(execution_name, scenario_name, trace_id, results)


def evaluate_condition_tests(test_config, metrics_values, parameters) -> list[dict]:
    """
    Function that receive the test config and the metrics value,
    evaluate the condition of the system test and return the result
    Args:
        test_config (list(dict)): list with the configuration of the test example: name and condition
        metrics_values (list(dict)): list with the list of metrics values

    Returns:
        list(object): list with the list of result of the evaluation the conditions by the system test
    """
    tests_result = []
    for parameter in parameters:
        locals()[parameter.get("label")] = 0
    for metric_value in metrics_values:
        locals()[metric_value.get("test_case_record_name")] = metric_value.get("system_test_metric_value")

    for test in test_config:
        tests_result.append(
            {
                "name": test.get("name"),
                "condition": test.get("condition"),
                "status": eval(test.get("condition")),
            }
        )

    return tests_result


def get_metrics_values_from_dynamodb(execution_name) -> list[dict]:
    """
    Function that return the records of the dynamoDb by the key "execution_name"
    Args:
        execution_name (str): execution_name of the current execution of the system test

    Returns:
        list(dict): list of records with the metric values of the system test
    """
    items = None

    # DDB
    try:
        key_condition_expression = Key("execution_name").eq(execution_name)
        response = TABLE.query(KeyConditionExpression=key_condition_expression)
        if not response["Items"]:
            return "No results tests were found in the test results table with the provided execution name."
        items = response["Items"]
    except (BotoCoreError, ClientError) as e:
        logger.error("An error occurred while retrieving values from the DynamoDB: %s", str(e))
    return items


def save_results_to_dynamodb(execution_name, scenario_name, trace_id, results) -> None:
    """
    Function that save record in the dynamoDb

    Args:
        execution_name (str): execution_name of the test
        scenario_name (str): scenario_name of the test
        trace_id (str): trace_id of the test
        results (str): results results of the evaluation condition test
    """
    for result in results:
        item = {
            "execution_name": execution_name,
            "test_case_record_name": result["name"],
            "test_case_record_type": "condition",
            "test_case_type": "system",
            "scenario_name": scenario_name,
            "trace_id": trace_id,
            "system_test_case_metadata": result["condition"],
            "test_case_status": result["status"],
        }
        try:
            TABLE.put_item(Item=item)
        except ClientError as e:
            logger.error(
                "An error occurred while saving item to DynamoDB: %s",
                e.response["Error"]["Message"],
            )
