"""
Evaluator of Load and E2E tests
"""
import boto3
import json
import os
import logging
from datetime import datetime, timezone
from botocore.exceptions import BotoCoreError
from botocore.client import ClientError
from dateutil.parser import ParserError

cloudwatch = boto3.client("cloudwatch")
dynamodb = boto3.resource("dynamodb")
stepfunctions = boto3.client("stepfunctions")
logger = logging.getLogger(__name__)


class Guest360LoadTestEvaluator:
    """
    A class for retrieving and evaluating CloudWatch metrics and test results using CloudWatch expressions.
    Attributes:
    - metrics (List[Dict]): A list of dictionaries containing information about the metrics to retrieve.
    - tests (List[Dict]): A list of dictionaries containing information about the tests to evaluate.
    - arn (str): The ARN of the CloudWatch metric target.
    - period (int): The period of the CloudWatch metrics to retrieve.
    - start_time (datetime): The start time of the CloudWatch metrics to retrieve.
    - end_time (datetime): The end time of the CloudWatch metrics to retrieve.
    """

    def __init__(self, metrics, tests, arn):
        self.metrics = metrics
        self.tests = tests
        self.arn = arn
        self.period = None
        self.start_time = None
        self.end_time = None

    def build_metric_data_queries(self):
        metric_data_queries = []

        for metric in self.metrics:
            query = {
                "Id": metric["label"],
                "MetricStat": {
                    "Metric": {
                        "Namespace": metric["namespace"],
                        "MetricName": metric["metric_name"],
                        "Dimensions": [
                            {"Name": dimension["name"], "Value": dimension["value"]}
                            for dimension in metric["dimensions"]
                        ],
                    },
                    "Period": int(metric.get("period", self.period)),
                    "Stat": metric["statistic"],
                },
                "ReturnData": True,
            }
            metric_data_queries.append(query)

        for test in self.tests:
            query = {
                "Id": test["name"],
                "Expression": test["condition"],
                "Label": test["condition"],
                "ReturnData": True,
            }
            metric_data_queries.append(query)
        return metric_data_queries

    def get_metric_data(self):
        try:
            metric_data_queries = self.build_metric_data_queries()
            response = cloudwatch.get_metric_data(
                MetricDataQueries=metric_data_queries,
                StartTime=self.start_time,
                EndTime=self.end_time,
            )
            return response["MetricDataResults"]
        except (BotoCoreError, ClientError) as e:
            logger.error("An error occurred while fetching metric data: %s", e)
            raise e

    def generate_table(self, metric_data_results):
        input_metrics_table = []
        test_results_table = []

        for metric in self.metrics:
            metric_result = next((result for result in metric_data_results if result["Id"] == metric["label"]), None)
            value = metric_result["Values"] if metric_result else None

            if value is not None:
                value = [str(val) for val in value]

            input_metrics_table.append(
                {
                    "label": metric["label"],
                    "namespace": metric["namespace"],
                    "metric_name": metric["metric_name"],
                    "statistic": metric["statistic"],
                    "value": value,
                }
            )

        for test in self.tests:
            test_result = next((result for result in metric_data_results if result["Id"] == test["name"]), None)

            status = "Unknown"
            if test_result:
                status_list = ["Pass" if value == 1.0 else "Failed" for value in test_result["Values"]]
                status = ", ".join(status_list)

            test_results_table.append(
                {
                    "name": test["name"],
                    "condition": test["condition"],
                    "status": status,
                }
            )

        return {
            "Input": {"Metrics": input_metrics_table},
            "Result": {"Tests": test_results_table},
        }

    def get_step_function_times(self):
        try:
            response = stepfunctions.describe_execution(executionArn=self.arn)
            start_time_str = response["startDate"]
            end_time_str = response.get("stopDate", datetime.now(timezone.utc))

            start_time = self._parse_datetime(start_time_str)
            end_time = self._parse_datetime(end_time_str)

            period = None
            if start_time and end_time:
                total_seconds = int((end_time - start_time).total_seconds())
                period = total_seconds - (total_seconds % 60)

            return start_time, end_time, period
        except ClientError as e:
            logger.error("An error occurred while processing the ARN '%s': %s", self.arn, e)
            return "None", "None", "0"

    @staticmethod
    def _parse_datetime(datetime_str):
        try:
            if isinstance(datetime_str, datetime):
                return datetime_str
            else:
                return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ParserError as e:
            logger.error("An error occurred while parsing datetime string '%s': %s", datetime_str, e)
            return None

    def evaluate_cw_metrics(self):
        try:
            self.start_time, self.end_time, self.period = self.get_step_function_times()
        except ValueError as e:
            logger.error("ValueError occurred while getting step function times: %s", e)
        logger.info("start_time: %s, end_time: %s, period: %s", self.start_time, self.end_time, self.period)
        get_metric_data = self.get_metric_data()
        generate_table = self.generate_table(get_metric_data)

        return generate_table


def lambda_handler(event, _):
    data = event["config"]
    arn = event["executionid"]
    execution_id = event["executionid"].split(":")[-1]
    scenario_name = data["scenario"]["name"]
    evaluation = data["evaluation"]
    metrics = evaluation["metrics"]
    tests = evaluation["tests"]

    guest360_load_test_evaluator = Guest360LoadTestEvaluator(metrics, tests, arn)
    cw_results = guest360_load_test_evaluator.evaluate_cw_metrics()
    cw_results["scenario_name"] = data["scenario"]["name"]
    save_to_dynamodb(execution_id, scenario_name, cw_results)
    logger.info("results: %s", cw_results)

    return {"statusCode": 200, "body": json.dumps(cw_results)}


def save_to_dynamodb(execution_id, scenario_name, results):
    table = dynamodb.Table(os.getenv("DDB_TABLE_RESULT"))
    try:
        table.put_item(
            Item={
                "execution_name": execution_id,
                "scenario_name": scenario_name,
                "results": results,
            }
        )
    except ClientError as e:
        logger.error(
            "An error occurred while saving item to DynamoDB: %s",
            e.response["Error"]["Message"],
        )
