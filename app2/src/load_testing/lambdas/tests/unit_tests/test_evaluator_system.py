"""
TestSystemTest
"""
import logging
import sys
from datetime import datetime

import boto3
from app.src.load_testing.lambdas.evaluator_system_test.evaluator_system import EvaluatorSystemTest
from moto import mock_cloudwatch, mock_dynamodb, mock_s3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


class TestSystemTest:
    """
    TestSystemTest
    """

    @mock_s3
    @mock_cloudwatch
    @mock_dynamodb
    def test_lambda_handler(self, monkeypatch, freezer):
        freezer.move_to("2023-09-21")
        monkeypatch.setenv("DDB_TABLE_RESULT", "lst-use1-guest360-guest360-load-testing-sfn-exec-eval")
        # pylint: disable=C0415
        from app.src.load_testing.lambdas.evaluator_system_test import lambda_function

        """test_lambda_handler"""
        sample_data = """
            TestSystemTest
            """
        # Prepare bucket dummy
        bucket_name = "lst-use1-guest360-ingestion-raw"
        bucket_path = "/snowpipe/database=LATEST_LANDING/schema=LND__EA/table=WDW_LIGHTNING_LANE/stream=wdw-lightning-lane/2023/05/22/16/"  # pragma: allowlist secret

        client = boto3.client("s3")
        client.create_bucket(Bucket=bucket_name)
        for i in range(10):
            client.put_object(
                Bucket=bucket_name, Body=bytes(sample_data, encoding="utf-8"), Key=f"{bucket_path}/test_file_{i}.txt"
            )

        # Prepare Cloudwatch metrics dummy
        cwclient = boto3.client("cloudwatch", "us-east-1")
        timestamp = datetime.utcnow()
        metric_records = []
        for _ in range(9):
            metric_record = {
                "MetricName": "request_count",
                "Dimensions": [
                    {"Name": "Source", "Value": "Orion_EA"},
                    {"Name": "Execution_Id", "Value": "123445"},
                    {"Name": "Target", "Value": "Kinesis"},
                ],
                "Timestamp": timestamp,
                "Value": 1,
                "Unit": "Count",
            }
            metric_records.append(metric_record)

        cwclient.put_metric_data(Namespace="locust-load-tests", MetricData=metric_records)

        dynamo_client = boto3.client("dynamodb", "us-east-1")

        dynamo_client.create_table(
            AttributeDefinitions=[
                {"AttributeName": "execution_name", "AttributeType": "S"},
                {"AttributeName": "scenario_name", "AttributeType": "S"},
            ],
            KeySchema=[
                {
                    "AttributeName": "execution_name",
                    "KeyType": "HASH",
                },
                {
                    "AttributeName": "scenario_name",
                    "KeyType": "RANGE",
                },
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
            TableName="lst-use1-guest360-guest360-load-testing-sfn-exec-eval",
        )

        # Test lambda
        event = {
            "executionid": "123445",
            "traceid": "123445",
            "start_time": "2023-07-05T16:12:10.192Z",
            "prefix": "lst-use1-guest360",
            "scenario_name": "OrionEASystemTest",
            "config": {
                "label": "DataMockerRecordsCW",
                "endpoint": {
                    "type": "cloudwatch",
                    "namespace": "locust-load-tests",
                    "metric_name": "request_count",
                    "statistic": "Sum",
                    "dimensions": [
                        {"Name": "Source", "Value": "Orion_EA"},
                        {"Name": "Target", "Value": "Kinesis"},
                    ],
                },
            },
        }

        trace_id = event.get("traceid")
        start_time = event.get("start_time")
        prefix = event.get("prefix")

        parameter_config = event.get("config")

        evaluator = EvaluatorSystemTest(start_time, prefix, trace_id)
        parameter_value = evaluator.get_parameter_value(parameter_config)

        assert parameter_value.get("value") == 0

        lambda_function.lambda_handler(event, None)
