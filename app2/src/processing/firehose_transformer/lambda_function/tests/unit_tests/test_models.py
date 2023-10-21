""" Tests the kinesis models
"""
import json
import os
import pathlib

import pytest
from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import (
    KinesisFirehoseEvent,
    KinesisFirehoseRecord,
    KinesisFirehoseResponseRecord,
)


def test_models():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "firehose_event.json"), "r", encoding="UTF-8"
    ) as outfile:
        example_event = json.load(outfile)

    kinesis_firehose_event: KinesisFirehoseEvent = KinesisFirehoseEvent.parse_obj(example_event)

    assert KinesisFirehoseEvent.parse_obj(example_event).json(by_alias=True) == json.dumps(example_event)

    record: KinesisFirehoseRecord = kinesis_firehose_event.records[0]

    assert record.json(by_alias=True) == json.dumps(example_event["records"][0])

    record_dictionary = record.dict()

    with pytest.raises(Exception):
        KinesisFirehoseResponseRecord.parse_obj(record_dictionary)

    record_dictionary["result"] = "Ok"

    KinesisFirehoseResponseRecord.parse_obj(record_dictionary)
