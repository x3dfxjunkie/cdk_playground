""" Tests the entire lambda function with a mock input
"""

import json
import os
import pathlib

from app.src.processing.firehose_transformer.lambda_function.lambda_function import lambda_handler
from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import KinesisFirehoseRecord
from app.src.processing.firehose_transformer.lambda_function.utils.newline_appender import append_new_line
from app.src.processing.firehose_transformer.lambda_function.utils.partition_extractor import extract_partition


def test_lambda_function():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "firehose_event.json"), "r", encoding="UTF-8"
    ) as outfile:
        example_event = json.load(outfile)
    response = lambda_handler(example_event, None)
    partitions = extract_partition(KinesisFirehoseRecord.parse_obj(example_event["records"][0]))

    assert response == {
        "records": [
            {
                "recordId": example_event["records"][0]["recordId"],
                "approximateArrivalTimestamp": example_event["records"][0]["approximateArrivalTimestamp"],
                "data": append_new_line(example_event["records"][0]["data"]),
                "result": "Ok",
                "metadata": {"partitionKeys": partitions},
            }
        ]
    }

    example_event.pop("invocationId")

    print(example_event)

    response = lambda_handler(example_event, None)

    assert response == {
        "records": [
            {
                "recordId": example_event["records"][0]["recordId"],
                "approximateArrivalTimestamp": example_event["records"][0]["approximateArrivalTimestamp"],
                "data": append_new_line(example_event["records"][0]["data"]),
                "result": "Ok",
                "metadata": {"partitionKeys": partitions},
            }
        ]
    }
