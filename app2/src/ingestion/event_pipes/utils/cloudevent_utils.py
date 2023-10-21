"""Module for functions related to cloudevents"""
from typing import Optional
from cloudevents.pydantic import CloudEvent
import cloudevents
from aws_lambda_powertools import Logger
from app.src.utils.otel.otel import otel_helpers


def get_cloudevent(data: dict, logger: Logger) -> Optional[CloudEvent]:
    cloudevent = None
    required_fields = {k for k, v in CloudEvent.__fields__.items() if v.required} | {"data"}
    if required_fields - data.keys():
        # set differencing - if there's any leftover, it means our payload doesn't have a required field
        return cloudevent
    try:
        cloudevent = cloudevents.pydantic.from_dict(data)
    except ValueError:
        logger.debug("CloudEvent not found in data")
    return cloudevent


def parse_cloudevent_metadata_if_necessary(data: dict, logger: Logger):
    received_cloudevent = get_cloudevent(data, logger)  # values: CloudEvent object or  None
    cloudevent_attributes = {}
    otel_parent_context = None
    logger.debug("data=%s", data)
    if received_cloudevent:
        # get the parent context if available
        otel_parent_context = otel_helpers.otel_context_from_cloudevent(received_cloudevent)
        cloudevent_attributes = dict(received_cloudevent.get_attributes())
        # since the data is a cloudevent get the data and override data
        assert received_cloudevent.data is not None
        data = dict(received_cloudevent.data)
    return data, cloudevent_attributes, otel_parent_context
