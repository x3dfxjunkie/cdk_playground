""" Function that simply transform base64 data and appends a new line
"""
import datetime
from typing import Dict

from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import KinesisFirehoseRecord


def extract_partition(record: KinesisFirehoseRecord) -> Dict[str, str]:
    approximate_arrival_timestamp = datetime.datetime.fromtimestamp(record.approximate_arrival_timestamp * 1e-3)

    partition_keys: Dict[str, str] = {
        "year": approximate_arrival_timestamp.strftime("%Y"),
        "month": approximate_arrival_timestamp.strftime("%m"),
        "day": approximate_arrival_timestamp.strftime("%d"),
        "hour": approximate_arrival_timestamp.strftime("%H"),
    }
    return partition_keys
