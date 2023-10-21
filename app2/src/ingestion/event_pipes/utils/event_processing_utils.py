"""Module for all event processing functions used by our lambdas"""
from operator import itemgetter
from aws_lambda_powertools import Logger


def get_event_items(event: dict, logger: Logger) -> tuple:
    event_keys = ("data", "sequenceNumber", "eventID", "partitionKey")
    try:
        items = itemgetter(*event_keys)(event)
    except KeyError:
        logger.exception("Failed to unpack keys for event dictionary")
        raise

    if not isinstance(items, tuple) or len(items) != 4:
        raise ValueError("Could not unpack event_items")
    items = list(items)
    items[2] = get_shard_seq(items[2])

    return tuple(items)


def get_shard_seq(event_id: str) -> str:
    """
    >>> get_shard_seq("shardId-000000000000: 49640450530655783448641595467156077838773832572853026818")
    '000000000000-49640450530655783448641595467156077838773832572853026818'

    given a valid aws kinesis eventID, return shardidnumber-sequencenumber

    Args:
        event_id: string of eventid from kinesis
    Returns:
        string: decoded eventid
    Raises:
        ValueError: error if invalid eventid
    """
    try:
        shardid, sequence = event_id.split(":", maxsplit=1)
    except ValueError as exc:
        raise ValueError(f"{event_id=} Not a valid aws eventID") from exc
    shardid = "".join(filter(str.isdigit, shardid))
    sequence = "".join(filter(str.isdigit, sequence))
    return f"{shardid}-{sequence}"
