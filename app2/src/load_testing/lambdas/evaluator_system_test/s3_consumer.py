"""
    Consumer S3
"""
import gzip
import logging
import os
import tempfile
from datetime import datetime
from typing import Any, List

import boto3
import pytz
from app.src.load_testing.lambdas.evaluator_system_test.endpoint_consumer import EndPointConsumer
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
temp_dir = tempfile.gettempdir()
TEMP_LOCAL_FILE = f"{temp_dir}/temp_s3_object.gz"


class S3Consumer(EndPointConsumer):
    """
    Gets count of objects or records from S3
    """

    def __init__(self, bucket_name: str, prefix: str, start_time: str, statistic: str, trace_id=None) -> None:
        self.s3_client = boto3.client("s3")
        self.statistic = statistic
        self.bucket_name = bucket_name  # Setting the bucket name
        self.prefix = f"{prefix}{self.format_time_to_path(start_time)}"  # Setting the bucket path
        self.window_start = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%f%z").replace(
            minute=0, second=0, microsecond=0
        )
        self.window_end = pytz.utc.localize(datetime.utcnow())
        self.trace_id = trace_id

    def format_time_to_path(self, start_time: str):
        return start_time[0:13].replace("-", "/").replace("T", "/")

    def count_records_s3(self, s3_objects):
        count_of_records = 0
        for s3_object in s3_objects:
            try:  # download s3_object
                self.s3_client.download_file(self.bucket_name, s3_object, TEMP_LOCAL_FILE)
            except ClientError as error:
                logger.error("An error occurred downloading s3 object '%s': %s", s3_object, str(error))
                continue

            try:  # counting the records
                with gzip.open(TEMP_LOCAL_FILE, "rt") as local_file:
                    for line in local_file:
                        if self.trace_id:
                            # no newlines in the file
                            count_of_records += line.count(self.trace_id)
            except (OSError, ValueError) as error:
                logger.error("An error occurred reading s3 object '%s': %s", s3_object, str(error))

            try:  # remove the local copy
                os.remove(TEMP_LOCAL_FILE)
            except OSError:
                continue
        return count_of_records

    def validate_parameter(self) -> Any:
        list_objects = self.get_file_names()
        if self.statistic == "CountOfObjects":
            return len(list_objects)
        if self.statistic == "CountOfRecords":
            return self.count_records_s3(list_objects)

    def get_file_names(self) -> List:
        file_names = []

        default_kwargs = {"Bucket": self.bucket_name, "Prefix": self.prefix}
        next_token = ""

        while next_token is not None:
            updated_kwargs = default_kwargs.copy()

            if next_token != "":
                updated_kwargs["ContinuationToken"] = next_token

            response = self.s3_client.list_objects_v2(**updated_kwargs)
            contents = response.get("Contents")
            if contents is not None and len(contents) > 0:
                for result in contents:
                    key = result.get("Key")
                    # include files that were likely created during the test.
                    last_modified = result.get("LastModified")
                    if key[-1] != "/" and (self.window_start < last_modified < self.window_end):
                        file_names.append(key)

            next_token = response.get("NextContinuationToken")

        return file_names
