"""test cloudwatch consumer"""
import logging
import sys

import boto3
import pytest
from app.src.load_testing.lambdas.evaluator_system_test.cloudwatch_consumer import CloudWatchConsumer
from botocore.exceptions import NoCredentialsError
from moto import mock_cloudwatch

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


class TestCloudWatchConsumer:
    """class test cloudwatch consumer"""

    @pytest.fixture(scope="module")
    def constants_values(self):
        values = {
            "timestamp": "2023-06-01T16:12:10.192Z",
            "metric_name": "request_count",
            "namespace": "locust-load-tests",
            "dimensions": [
                {"Name": "Source", "Value": "Orion_EA"},
                {"Name": "Execution_Id", "Value": "123445"},
                {"Name": "Target", "Value": "Kinesis"},
            ],
        }

        return values

    @mock_cloudwatch
    def test_cloudwtach_consumer(self, constants_values):
        # Prepare Cloudwatch metrics dummy
        cwclient = boto3.client("cloudwatch", "us-east-1")
        metric_records = []
        for _ in range(10):
            metric_record = {
                "MetricName": constants_values["metric_name"],
                "Dimensions": constants_values["dimensions"],
                "Timestamp": constants_values["timestamp"],
                "Value": 1,
                "Unit": "Count",
            }
            metric_records.append(metric_record)

        cwclient.put_metric_data(Namespace=constants_values["namespace"], MetricData=metric_records)
        # create instance CloudWatchConsumer
        cloudwtach_consumer = CloudWatchConsumer(
            "LabelTest",
            namespace=constants_values["namespace"],
            metric_name=constants_values["metric_name"],
            statistic="Sum",
            dimensions=[
                {"Name": "Source", "Value": "Orion_EA"},
                {"Name": "Target", "Value": "Kinesis"},
            ],
            start_time=constants_values["timestamp"],
            period=None,
            execution_id="123445",
        )
        assert cloudwtach_consumer.validate_parameter() == 10

    def test_raise_format_exception(self, constants_values):
        cloudwtach_consumer = CloudWatchConsumer(
            "LabelTest",
            namespace=constants_values["namespace"],
            metric_name=constants_values["metric_name"],
            statistic="Sum",
            dimensions=[
                {"Name": "Source", "Value": "Orion_EA"},
                {"Name": "Target", "Value": "Kinesis"},
            ],
            start_time=constants_values["timestamp"],
            period=None,
            execution_id="123445",
        )
        # pylint: disable=W0212
        assert cloudwtach_consumer._parse_datetime("2023-JUN-01T16:12:10.192Z") is None

    def test_error_boto_core(self, constants_values):
        cloudwtach_consumer = CloudWatchConsumer(
            "LabelTest",
            namespace=constants_values["namespace"],
            metric_name=constants_values["metric_name"],
            statistic="Sum",
            dimensions=[
                {"Name": "Source", "Value": "Orion_EA"},
                {"Name": "Target", "Value": "Kinesis"},
            ],
            start_time=constants_values["timestamp"],
            period=None,
            execution_id="123445",
        )
        with pytest.raises(NoCredentialsError):
            cloudwtach_consumer.validate_parameter()
