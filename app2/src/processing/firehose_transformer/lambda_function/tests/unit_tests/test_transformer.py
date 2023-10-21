""" This function tests the transformer """
import json
import os
import pathlib

from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import (
    KinesisFirehoseRecord,
    KinesisFirehoseResponseRecord,
)
from app.src.processing.firehose_transformer.lambda_function.utils.transformer import transformer


def test_transformer():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "firehose_event.json"), "r", encoding="UTF-8"
    ) as outfile:
        example_event = json.load(outfile)

    record: KinesisFirehoseRecord = KinesisFirehoseRecord.parse_obj(example_event["records"][0])

    assert isinstance(transformer(record), KinesisFirehoseResponseRecord)
