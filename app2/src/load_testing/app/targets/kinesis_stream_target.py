"""
Kinesis stream target
"""
import json
import logging
import uuid
from typing import Any, Dict, List

import boto3  # AWS boto3 library.

from app.src.load_testing.app.targets.exceptions import LoadTestTargetException
from app.src.load_testing.app.targets.target import Target  # Abstract class


class KinesisStreamTarget(Target):
    """
    Subclass of DataSink. Implements a generic Kinesis writer.
    locust "users" will need to instatiate this to write events
    to a kinesis datastream for related load tests
    """

    def __init__(self, stream_name: str, region: str = "us-east-1"):
        self._target_type = "Kinesis Data Stream"
        self._client = boto3.client("kinesis", region)
        self.stream_name = stream_name  # Setting the stream name
        self.region = region  # Setting the AWS Region
        self.send_count = 0

    @property
    def target_type(self) -> str:
        return self._target_type

    def send_data(self, data: Dict[str, Any]) -> None:
        """write a record to Kinesis datastream

        Args:
            data (Dict[str, Any]): A single record
        """
        try:
            self._client.put_record(
                StreamName=self.stream_name,
                Data=json.dumps(data),
                PartitionKey=f"{uuid.uuid4()}",
            )
            self.send_count += 1
        except (
            self._client.exceptions.InternalFailureException,
            self._client.exceptions.LimitExceededException,
            self._client.exceptions.ProvisionedThroughputExceededException,
            self._client.exceptions.ResourceInUseException,
        ) as e:
            raise LoadTestTargetException from e

    def send_batch(self, batch: List[Dict[str, Any]]) -> None:
        raise NotImplementedError

    def __del__(self):
        # pylint: disable=W1203
        logging.info(f"destroying KinesisStreamTarget; total send count {self.send_count}")
