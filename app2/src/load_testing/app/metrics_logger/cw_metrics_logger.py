"""Guest360CloudwatchMetricsLogger: Implementation of Guest360MetricsLogger for AWS Cloudwatch"""
import datetime
import logging
import os
import threading
from typing import Any, List

import boto3
import botocore.exceptions

from app.src.load_testing.app.metrics_logger.metrics_logger import Guest360MetricsLogger


class Guest360CloudwatchMetricsLogger(Guest360MetricsLogger):
    """
    Implements  Guest360MetricsLogger for AWS Cloudwatch
    """

    _instance = None
    _lock = threading.Lock()

    # pylint: disable=W0613, E1120
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Guest360CloudwatchMetricsLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, namespace: str, dimensions: List, buffer_size: int = 1000):
        aws_region = os.getenv("AWS_REGION", "us-east-1")
        self.cwclient = boto3.client("cloudwatch", aws_region)
        self.metric_records = []
        self.namespace = namespace
        self.dimensions = dimensions
        self.buffer_size = min(1000, buffer_size)  # CW accepts a max of 1000 records
        logging.info("Creating Guest360 Metrics Logger")

    def publish(self, metric_name: str, metric_value: Any, metric_unit: str) -> None:
        """
        Buffers metric records and puts the metrics on cloudwatch
        Caution: using this to send high resolution metrics will increase cost
        To Do: Implement a StatisticsLogger to aggrgeate and send statistics only

        Args:
            metric_name (str): name of the metric
            metric_value (Any): value of the metric
            metric_unit (str): unit of measurement
        """
        timestamp = datetime.datetime.utcnow()
        metric_record = {
            "MetricName": metric_name,
            "Dimensions": self.dimensions,
            "Timestamp": timestamp,
            "Value": metric_value,
            "Unit": metric_unit,
        }
        self.metric_records.append(metric_record)

        if len(self.metric_records) == self.buffer_size:
            try:
                self.cwclient.put_metric_data(Namespace=self.namespace, MetricData=self.metric_records)

            except botocore.exceptions.ClientError as e:
                # retry
                logging.warning(str(e))
                if e.response["Error"]["Code"] == "LimitExceededException":
                    logging.warning("API call limit exceeded; retrying...")
                    self.cwclient.put_metric_data(Namespace=self.namespace, MetricData=self.metric_records)
                else:
                    logging.warning("encountered exception when putting metrics; dumping ...")
                    logging.exception(e)
            self.metric_records.clear()

    def __del__(self):
        """
        Put any incomplete buffers on cloudwatch before destroying the object
        """
        if len(self.metric_records) > 0:
            self.cwclient.put_metric_data(Namespace=self.namespace, MetricData=self.metric_records)
        logging.info("Detroying Guest360 Metrics Logger for namespace")
