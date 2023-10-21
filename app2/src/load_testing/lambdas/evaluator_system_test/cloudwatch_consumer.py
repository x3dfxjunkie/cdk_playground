"""CloudWatchConsumer"""
import logging
from datetime import datetime, timezone

import boto3
from app.src.load_testing.lambdas.evaluator_system_test.endpoint_consumer import EndPointConsumer
from botocore.client import ClientError
from botocore.exceptions import BotoCoreError

logger = logging.getLogger(__name__)


class CloudWatchConsumer(EndPointConsumer):
    """CloudWatchConsumer"""

    def __init__(self, label, namespace, metric_name, statistic, dimensions, start_time, period, execution_id):
        self.label = label
        self.namespace = namespace
        self.metric_name = metric_name
        self.statistic = statistic
        self.dimensions = dimensions
        self.start_time_str = start_time
        self.period = period
        self.dimensions.append({"Name": "Execution_Id", "Value": execution_id})
        self.cw_client = boto3.client("cloudwatch", "us-east-1")
        self.get_metric_times()

    def validate_parameter(self):
        return self.get_metric_value()

    def get_metric_value(self):
        try:
            list_data_results = []
            query = {
                "Id": self.label,
                "MetricStat": {
                    "Metric": {
                        "Namespace": self.namespace,
                        "MetricName": self.metric_name,
                        "Dimensions": [
                            {"Name": dimension["Name"], "Value": dimension["Value"]} for dimension in self.dimensions
                        ],
                    },
                    "Period": self.period,
                    "Stat": self.statistic,
                },
                "ReturnData": True,
            }
            metric_data_queries = [query]
            default_kwargs = {
                "MetricDataQueries": metric_data_queries,
                "StartTime": self.start_time,
                "EndTime": self.end_time,
            }
            next_token = ""

            while next_token is not None:
                updated_kwargs = default_kwargs.copy()

                if next_token != "":
                    updated_kwargs["NextToken"] = next_token

                response = self.cw_client.get_metric_data(**default_kwargs)
                next_token = response.get("NextToken")
                list_data_results.extend(response["MetricDataResults"])

            return self.get_total_values(list_data_results)
        except (BotoCoreError, ClientError) as e:
            logger.error("An error occurred while fetching metric data: %s", e)
            raise e

    def get_total_values(self, data_results):
        total = 0
        for result in data_results:
            for value in result["Values"]:
                total = total + value

        return total

    def _parse_datetime(self, datetime_str):
        try:
            if isinstance(datetime_str, datetime):
                return datetime_str
            else:
                return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        except ValueError as e:
            logger.error("An error occurred while parsing datetime string '%s': %s", datetime_str, e)
            return None

    def get_metric_times(self):
        end_time_str = datetime.now(timezone.utc)

        self.start_time = self._parse_datetime(self.start_time_str)
        self.end_time = self._parse_datetime(end_time_str)

        if self.period is None and self.start_time and self.end_time:
            total_seconds = int((self.end_time - self.start_time).total_seconds())
            self.period = total_seconds - (total_seconds % 60)
