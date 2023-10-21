""" Tests the partition extractor
"""
import json
import os
import pathlib

from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import KinesisFirehoseEvent
from app.src.processing.firehose_transformer.lambda_function.utils.partition_extractor import extract_partition


def test_partition_extractor():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "firehose_event.json"), "r", encoding="UTF-8"
    ) as outfile:
        example_event = json.load(outfile)

    event: KinesisFirehoseEvent = KinesisFirehoseEvent.parse_obj(example_event)

    assert {"year": "2017", "month": "05", "day": "18", "hour": "02"} == extract_partition(event.records[0])
