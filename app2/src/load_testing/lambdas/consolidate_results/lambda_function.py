"""
This AWS Lambda function is designed to retrieve and process data from a DynamoDB table and generate a markdown string.
The lambda function is triggered by the pipeline. It processes each item by extracting metrics and test results and
transforms them into a Markdown format using a Jinja2 template based on the result of the Load/System test.
"""
import os
import boto3
import logging
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, TemplateError
from boto3.dynamodb.conditions import Key
from botocore.exceptions import BotoCoreError, ClientError
from collections import defaultdict

# Constants
TEMPLATES_DIRECTORY = "app/src/load_testing/lambdas/consolidate_results/"
TABLE_NAME = os.getenv("DDB_TABLE_RESULT")
DYNAMODB = boto3.resource("dynamodb", "us-east-1")
TABLE = DYNAMODB.Table(TABLE_NAME)
logger = logging.getLogger(__name__)


def lambda_handler(event, _):
    execution_name = event["execution_name"]
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
        return "An error occurred while retrieving values from the DynamoDB."

    # MD
    markdown_str = ""
    try:
        file_loader = FileSystemLoader(TEMPLATES_DIRECTORY)
        env = Environment(loader=file_loader)
        template = env.get_template("system_test_template.j2")
    except TemplateNotFound as e:
        logger.error("An error occurred while locating the template: %s", str(e))
        return "An error occurred while locating the template."

    grouped_items = defaultdict(lambda: defaultdict(list))

    for item in items:
        scenario_name = item["scenario_name"]
        record_type = item["test_case_record_type"]
        test_case_type = item["test_case_type"]
        execution_name = item["execution_name"]
        trace_id = item["trace_id"]

        grouped_items[scenario_name][record_type].append(item)
        grouped_items[scenario_name]["test_case_type"] = test_case_type
        grouped_items[scenario_name]["execution_name"] = execution_name
        grouped_items[scenario_name]["trace_id"] = trace_id

    try:
        for scenario_name, scenario_items in grouped_items.items():
            metrics = scenario_items.get("metric", [])
            conditions = scenario_items.get("condition", [])
            test_case_type = scenario_items.get("test_case_type", "")
            execution_name = scenario_items.get("execution_name", "")
            trace_id = scenario_items.get("trace_id", "")
            rendered_item = template.render(
                scenario_name=scenario_name,
                metrics=metrics,
                conditions=conditions,
                test_case_type=test_case_type,
                execution_name=execution_name,
                trace_id=trace_id,
            )
            markdown_str += rendered_item
    except TemplateError as e:
        logger.error("An error occurred while rendering the template: %s", str(e))
        return "An error occurred while rendering the template."

    return markdown_str
