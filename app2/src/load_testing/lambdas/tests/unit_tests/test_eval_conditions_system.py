"""
Test Lambda Evaluator conditions system tests
"""
import boto3
import pytest
from moto import mock_dynamodb


# pylint: disable=W0613, C0415, W0621
class TestValConditionSystemTest:
    """TestValConditionSystemTest"""

    EXECUTION_NAME = "arn:aws:states:us-east-1:543276908693:execution:lst-guest360-guest360_execute_all_load_test_scenarios:575dc5a3-3905-45fb-863b-d808c8e16565"

    mock_ddb_items = [
        {
            "execution_name": EXECUTION_NAME,
            "test_case_record_name": "locust_records_sent",
            "scenario_name": "OrionEASystemTest",
            "system_test_metric_metadata": {
                "endpoint": {
                    "dimensions": [
                        {"Name": "Source", "Value": "Orion_EA"},
                        {"Name": "Target", "Value": "Kinesis"},
                        {"Name": "request_type", "Value": "send_event"},
                        {"Name": "target", "Value": "Kinesis Data Stream"},
                        {
                            "Name": "Execution_Id",
                            "Value": EXECUTION_NAME,
                        },
                    ],
                    "metric_name": "events_success",
                    "namespace": "locust-load-tests",
                    "statistic": "Sum",
                    "type": "cloudwatch",
                },
                "label": "locust_records_sent",
            },
            "system_test_metric_value": 105,
            "test_case_record_type": "metric",
            "test_case_type": "system",
            "trace_id": EXECUTION_NAME,
        },
        {
            "execution_name": EXECUTION_NAME,
            "test_case_record_name": "put_records_s3_glue",
            "scenario_name": "system_tests/latest/orion_ea_system_testing.yaml",
            "system_test_metric_metadata": {"test": "data"},
            "system_test_metric_value": 100,
            "test_case_record_type": "metric",
            "test_case_type": "system",
            "trace_id": EXECUTION_NAME,
        },
        {
            "execution_name": EXECUTION_NAME,
            "test_case_record_name": "scenario_config_limit_records",
            "scenario_name": "OrionEASystemTest",
            "system_test_metric_metadata": {
                "endpoint": {"type": "static", "value": 100},
                "label": "scenario_config_limit_records",
            },
            "system_test_metric_value": 100,
            "test_case_record_type": "metric",
            "test_case_type": "system",
            "trace_id": EXECUTION_NAME,
        },
    ]

    @pytest.fixture
    def mock_os_environment(self, monkeypatch):
        monkeypatch.setenv("DDB_TABLE_RESULT", "lst-use1-guest360-guest360-load-testing-sfn-exec-eval")

    @mock_dynamodb
    def test_lambda_handler_with_dynamodb(self, mock_os_environment):
        # must include package here due to global boto resource declarations
        from app.src.load_testing.lambdas.eval_conditions_system_test import lambda_function

        dynamodb = boto3.resource("dynamodb", "us-east-1")
        table = dynamodb.create_table(
            TableName="lst-use1-guest360-guest360-load-testing-sfn-exec-eval",
            KeySchema=[
                {"AttributeName": "execution_name", "KeyType": "HASH"},
                {"AttributeName": "test_case_record_name", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "execution_name", "AttributeType": "S"},
                {"AttributeName": "test_case_record_name", "AttributeType": "S"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )
        for item in self.mock_ddb_items:
            table.put_item(Item=item)

        event = {
            "prefix": "lst-use1-guest360",
            "traceid": self.EXECUTION_NAME,
            "executionid": self.EXECUTION_NAME,
            "config": {
                "system_test": {"name": "OrionEASystemTest", "description": "OrionEA System test"},
                "output": {
                    "parameters": [{"label": "locust_records_sent"}],
                    "tests": [
                        {"name": "check_locust_send_records", "condition": "locust_records_sent >= 100"},
                        {
                            "name": "check_input_output_records",
                            "condition": "(locust_records_sent - scenario_config_limit_records)/scenario_config_limit_records * 100 < 10",
                        },
                    ],
                },
            },
        }

        lambda_function.lambda_handler(event, None)
        results = lambda_function.get_metrics_values_from_dynamodb(self.EXECUTION_NAME)

        assert len(results) == 5
