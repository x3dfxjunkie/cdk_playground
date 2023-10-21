""" Tests the new line appender utility
"""
import base64
import json
import os
import pathlib

from app.src.processing.firehose_transformer.lambda_function.utils.newline_appender import append_new_line


def test_appender():
    with open(
        os.path.join(pathlib.Path(__file__).parent.resolve(), "firehose_event.json"), "r", encoding="UTF-8"
    ) as outfile:
        example_event = json.load(outfile)
    data: str = example_event["records"][0]["data"]
    assert base64.b64decode(append_new_line(data)).decode()[-1] == "\n"

    data: str = ""
    assert base64.b64decode(append_new_line(data)).decode()[-1] == "\n"
