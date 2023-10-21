"""
deserialize data from dynamodb event stream into dataclass
"""
import builtins
import json
import logging

from app.src.utils.base64_decode import base64_decode
from app.src.data_structures.object_lookup import lookup
from app.src.data_structures.events.base_event import BaseEvent

logger = logging.getLogger(__name__)


def deserialize(data, dynamodb_actions: list = None) -> BaseEvent:
    """deserialize data from dynamodb stream to guest360 event obj

    Args:
        data (str): data to deserialize into guest360 event obj
        dynamodb_actions (list, optional): _description_. Defaults to None.

    Raises:
        builtins.ValueError: unable to decode data or deserialize event

    Returns:
        event: BaseEvent
    """
    dynamodb_actions = [] if dynamodb_actions is None else dynamodb_actions

    # decode base64 data
    try:
        data_str = base64_decode.b64decode(data)
        dynamodb_data = json.loads(data_str)
    except (json.JSONDecodeError,) as error:
        raise builtins.ValueError(f"DynamoDB stream='{data_str}' could not be deserialized into dataclass") from error

    if dynamodb_data["eventName"] not in dynamodb_actions:
        raise builtins.ValueError(f'DynamoDB eventName {dynamodb_data["eventName"]} not found')

    # now try and deserialize into dataclass
    try:
        event = lookup.EventDeserializer.get_event_from_dynamo(dynamodb_data["dynamodb"]["NewImage"])
    except (builtins.KeyError, builtins.TypeError) as error:
        raise builtins.ValueError(f"DynamoDB NewImage not able to be deserialized in {error=}") from error
    return event
