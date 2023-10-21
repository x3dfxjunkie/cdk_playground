"""
Test Lambda Consolidate results
"""
import pytest
import boto3
from unittest.mock import MagicMock
from moto import mock_dynamodb
from botocore.exceptions import BotoCoreError

# pylint: disable=W0613, C0415, W0621


class TestConsolidateResults:
    """TestConsolidateResults"""

    mock_event = {
        "execution_name": "arn:aws:states:us-east-1:543276908693:execution:lst-pr-1790-guest360_execute_all_load_test_scenarios:ed8bfbb0-cb82-4743-be93-cc4eaa11c7da",
    }

    mock_ddb_item = {
        "execution_name": "arn:aws:states:us-east-1:543276908693:execution:lst-pr-1790-guest360_execute_all_load_test_scenarios:ed8bfbb0-cb82-4743-be93-cc4eaa11c7da",
        "test_case_record_name": "check_input_output_records",
        "scenario_name": "OrionEASystemTest",
        "system_test_case_metadata": "RecordsPublished == 200",
        "test_case_record_type": "condition",
        "test_case_status": True,
        "test_case_type": "system",
        "trace_id": "ed8bfbb0-cb82-4743-be93-cc4eaa11c7da",
    }

    @pytest.fixture
    def mock_os_environment(self, monkeypatch):
        monkeypatch.setenv("DDB_TABLE_RESULT", "lst-use1-guest360-guest360-load-testing-sfn-exec-eval")

    @mock_dynamodb
    def test_lambda_handler_with_dynamodb(self, mock_os_environment):
        # must include package here due to global boto resource declarations
        from app.src.load_testing.lambdas.consolidate_results import lambda_function

        dynamodb = boto3.resource("dynamodb", "us-east-1")
        table = dynamodb.create_table(
            TableName="lst-use1-guest360-guest360-load-testing-sfn-exec-eval",
            KeySchema=[
                {"AttributeName": "execution_name", "KeyType": "HASH"},
                {"AttributeName": "scenario_name", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "execution_name", "AttributeType": "S"},
                {"AttributeName": "scenario_name", "AttributeType": "S"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )

        table.put_item(Item=self.mock_ddb_item)

        event = {
            "execution_name": self.mock_ddb_item["execution_name"],
        }

        response = lambda_function.lambda_handler(event, None)

        assert len(response) > 0
        assert self.mock_ddb_item["execution_name"] in response
        assert self.mock_ddb_item["trace_id"] in response
        assert self.mock_ddb_item["test_case_type"] in response
        assert self.mock_ddb_item["test_case_record_type"] in response

        if self.mock_ddb_item["test_case_status"]:
            assert ":green_circle: Passed" in response
        else:
            assert ":red_circle: Failed" in response
        event = {
            "execution_name": "execution_name",
        }

        response = lambda_function.lambda_handler(event, None)
        assert response == "No results tests were found in the test results table with the provided execution name."

    @pytest.fixture
    def mock_boto3_resource(self, monkeypatch):
        monkeypatch.setenv("DDB_TABLE_RESULT", "lst-use1-guest360-guest360-load-testing-sfn-exec-eval")
        mock_dynamodb = MagicMock()
        mock_table = MagicMock()
        monkeypatch.setattr(
            "app.src.load_testing.lambdas.consolidate_results.lambda_function.boto3.resource",
            lambda *args, **kwargs: mock_dynamodb,
        )
        mock_dynamodb.Table.return_value = mock_table
        return mock_table

    def test_lambda_handler_boto_error(self, mock_boto3_resource):
        # must include package here due to global boto resource declarations
        from app.src.load_testing.lambdas.consolidate_results import lambda_function

        mock_boto3_resource.query.side_effect = BotoCoreError()
        result = lambda_function.lambda_handler(self.mock_event, None)
        assert result == "An error occurred while retrieving values from the DynamoDB."
