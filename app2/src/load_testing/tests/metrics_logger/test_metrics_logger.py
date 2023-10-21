"""Unit Test for Guest360CloudwatchMetricsLogger"""
import datetime
import logging
import os
import sys

import boto3
from moto import mock_cloudwatch

from app.src.load_testing.app.metrics_logger.cw_metrics_logger import Guest360CloudwatchMetricsLogger

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


@mock_cloudwatch
def test_cloudwatch_metric_logger() -> None:
    """
    This unit test
    1. uses Guest360CloudwatchMetricsLogger class to buffer and puts metrics to cloudwatch
    2. uses get_metric_data to verify if the metrics were published
    3. checks if incomplete buffers are put to cw when the metric logger object is destroyed
    """
    logger.info("Unit test for Guest360CloudwatchMetricsLogger")

    start_time = datetime.datetime.utcnow()

    namespace = "guest360_load_test_metrics"
    dimensions = [{"Name": "dimension_name", "Value": "test_dimension"}]
    os.environ["AWS_REGION"] = "us-east-1"
    cwclient = boto3.client("cloudwatch", "us-east-1")

    metrics_logger = Guest360CloudwatchMetricsLogger(namespace=namespace, dimensions=dimensions)
    test_value = 0
    num_requests = 1000
    for _ in range(num_requests):
        metrics_logger.publish(metric_name="test_metric", metric_value=100, metric_unit="Count")
        test_value += 100
    logger.info("Published test metrics")

    end_time = datetime.datetime.utcnow()
    del metrics_logger

    response = cwclient.get_metric_data(
        MetricDataQueries=[
            {
                "Id": "test",
                "MetricStat": {
                    "Metric": {"Namespace": namespace, "MetricName": "test_metric", "Dimensions": dimensions},
                    "Period": 60,
                    "Stat": "Sum",
                },
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
    )
    logger.info(response)

    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert response["MetricDataResults"][0]["Values"][0] == test_value


def test_singleton():
    dimensions = [{"Name": "dimension_name", "Value": "test_dimension"}]
    namespace = "guest360_load_test_metrics"
    metrics_logger = Guest360CloudwatchMetricsLogger(namespace=namespace, dimensions=dimensions)

    metrics_logger_1 = Guest360CloudwatchMetricsLogger(namespace=namespace, dimensions=dimensions)
    assert metrics_logger is metrics_logger_1
