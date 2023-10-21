"""Guest360CloudwatchMetricsLogger: Implementation of Guest360MetricsLogger for AWS Cloudwatch"""
import datetime
import json
import logging
from typing import Any, Dict, List

import gevent.monkey
from app.src.load_testing.app.metrics_logger.metrics_logger import Guest360MetricsLogger

# Gevent is being used to monkey patch the native socket implementation, as it provides a more efficient implementation
# Since this logger requires sending high volume of events and is deployyed as a side car, gevent helps keep cpu utilization lower
from gevent import socket

gevent.monkey.patch_socket()


class Guest360CloudwatchEmfMetricsLogger(Guest360MetricsLogger):
    """
    Implements a Singleton CW EMF metrics logger
    This logger sends messages through UDP to a sidecar deployed close to the locust container application using Cloudwatch Embedded Metric Format
    """

    # pylint: disable=W0613, W1201, E1120
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Guest360CloudwatchEmfMetricsLogger, cls).__new__(cls)
        return cls.instance

    def __init__(self, cwagent_ip: str, cwagent_port: int, namespace: str, log_group_name: str):
        # initialize a CW EMF Metrics Logger
        # The CW EMF Metrics Logger requires IP and Port of a cloudwatch-agent
        # The CW EMF Metrics Logger send log entires to cloudwatch-agent over UDP port
        self.cwagent_ip = cwagent_ip
        self.cwagent_port = cwagent_port
        self.namespace = namespace
        self.log_group_name = log_group_name
        # create a UDP socket
        self.sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)

        logging.info(
            "Creating Guest360CloudwatchEmfMetricsLogger for %s namespace and %s log group",
            self.namespace,
            self.log_group_name,
        )

    def publish(self, metrics: List[Dict[str, Any]], dimensions: List[Dict[str, Any]]) -> None:
        """
        This methods prepares a log entry in EMF format with the provided metric and dimension values
        and sends the log entry to a cloudwatch agent over UDP
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html
        Args:
            metrics (List): List of Dicts containing 4 elements - name, value, unit and storage_resolution
            dimensions (List): List of Dicts containing 2 elements - name and value
        """

        # prepare log entry in EMF format
        #
        metrics_data = {
            "_aws": {
                "Timestamp": int(datetime.datetime.now().timestamp() * 1000),
                "LogGroupName": self.log_group_name,
                "CloudWatchMetrics": [
                    {
                        "Namespace": self.namespace,
                        "Dimensions": [[dimension["name"] for dimension in dimensions]],
                        "Metrics": [
                            {
                                "Name": metric["name"],
                                "Unit": metric["unit"],
                                "StorageResolution": metric["storage_resolution"],
                            }
                            for metric in metrics
                        ],
                    }
                ],
            },
        }

        for dimension in dimensions:
            metrics_data[dimension["name"]] = dimension["value"]

        for metric in metrics:
            metrics_data[metric["name"]] = metric["value"]

        # send log entry to cloudwatch
        message = json.dumps(metrics_data)
        self.sock.sendto(bytes(message, "utf-8"), (self.cwagent_ip, self.cwagent_port))

    def __del__(self):
        """
        destroy the Guest360CloudwatchEmfMetricsLogger object
        """
        self.sock.close()
        logging.info(
            "Destroying Guest360CloudwatchEmfMetricsLogger for %s namespace and %s log group",
            self.namespace,
            self.log_group_name,
        )
