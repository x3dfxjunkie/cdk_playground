"""Main entry point for lambda execution.
"""
import base64
import json
import os

from app.src.processing.realtime.module.domains.gam.identity_processor import IdentityProcessor
from app.src.processing.realtime.module.domains.lightning_lane.event_generator import LightningLaneEventGenerator
from app.src.processing.realtime.module.domains.stream_processor import StreamProcessor
from app.src.processing.realtime.module.utils import dynamodb_client
from aws_lambda_powertools import Logger
from opentelemetry import trace

logging = Logger(service=__name__)
trace.get_tracer_provider()
tracer = trace.get_tracer(__name__)

# Maps the arn name of the stream to the function to be called to process that stream
# TODO: determine if this is the approach we should use long term. This might be just a temporary solution for clean development
# TODO: if this becomes the long-term approach, we should evaluate lazy initialization of each module


def set_module_mapping() -> dict:
    """Returns the module needed to handle a particular type of message.

    Returns:
        dict: A dictionary of modules mapped to event types.
    """
    endpoint_url = os.environ.get("ENDPOINT_URL")
    event_table_name = os.environ.get("EXPERIENCE_EVENT_TABLE_NAME")
    identity_table_name = os.environ.get("IDENTITY_TABLE_NAME")
    identity_nodes_table_name = os.environ.get("IDENTITY_NODES_TABLE_NAME")
    identity_edges_table_name = os.environ.get("IDENTITY_EDGES_TABLE_NAME")
    profile_table_name = os.environ.get("PROFILE_TABLENAME")
    identity_notification_stream_name = os.environ.get("IDENTITY_NOTIFICATION_STREAM_NAME")
    source_ll_kinesis_stream_name = os.environ.get("RAW_LL_STREAM_NAME", "guest360-ea-test")
    source_gam_kinesis_stream_name = os.environ.get("RAW_GAM_STREAM_NAME", "gam")

    module_mapping = {
        source_ll_kinesis_stream_name: LightningLaneEventGenerator(
            dynamodb_client.get_dynamodb_resource(endpoint_url=endpoint_url),
            dynamodb_client.get_kinesis_client(endpoint_url=endpoint_url),
            event_table_name=event_table_name,
            identity_table_name=identity_table_name,
            identity_nodes_table_name=identity_nodes_table_name,
            identity_edges_table_name=identity_edges_table_name,
            profile_table_name=profile_table_name,
            identity_notification_stream_name=identity_notification_stream_name,
        ),
        source_gam_kinesis_stream_name: IdentityProcessor(
            dynamodb_client.get_dynamodb_resource(endpoint_url=endpoint_url),
            dynamodb_client.get_kinesis_client(endpoint_url=endpoint_url),
            event_table_name=event_table_name,
            identity_table_name=identity_table_name,
            identity_nodes_table_name=identity_nodes_table_name,
            identity_edges_table_name=identity_edges_table_name,
            profile_table_name=profile_table_name,
            identity_notification_stream_name=identity_notification_stream_name,
        ),
    }
    return module_mapping


def handler(event: dict, context):
    """
    Lambda handler for processing events from the Kinesis stream
    """
    logging.debug(event)
    # This will be a reference to the function to be called to process the stream, depending on the source stream
    # It's being initialized so we can use memoization and using it as a flag that we don't need to re-evaluate what module to use for each record on Kinesis
    processing_module: StreamProcessor | None = None
    module_mapping = set_module_mapping()

    # We need to always assume that a kinesis event will contain a batch (not just a single records)
    # We will loop through each records and base64 decode, and the put in this list before passing to the processing module
    parsed_records = []

    # Get the record from the event
    try:
        processing_module = process_records(event, processing_module, module_mapping, parsed_records)
    except Exception as e:
        logging.warning(
            "Exception caught while batch processing records, sending to dead letter queue. \nException: %s", e
        )
        send_to_dead_letter_table(event)

    # Sends the list of data to the processing module
    if processing_module is not None:
        with tracer.start_as_current_span("process_records_batch"):
            processing_module.process_records_batch(parsed_records)


def process_records(event, processing_module, module_mapping, parsed_records):
    """Process and base64 decode records given a batched event.

    Args:
        event (str): Event name
        processing_module (StreamProcessor): The actual processor for the event
        module_mapping (Dict): A collection of stream processors
        parsed_records (List): A collection of events.

    Returns:
        The processing module based on the parsed ARN
    """
    for record in event["Records"]:
        try:
            with tracer.start_as_current_span("base64_decode_message"):
                processing_module = base64_decode_message(
                    event, processing_module, module_mapping, parsed_records, record
                )
        except Exception as e:
            logging.warning("Error attempting to base64 decode payload for message: %s \nException: %s", record, e)
            send_to_dead_letter_table(record)
    return processing_module


def base64_decode_message(event, processing_module, module_mapping, parsed_records, record):
    """Return the processing module and parsed records based on the base64 encoded message

    Args:
        event (str): Base64 encoded string

    Returns:
        Processing module.
    """
    if processing_module is None:
        processing_module = get_processing_module(event, record, module_mapping)

    # Decodes the data from the record and adds to the parsed_records list so it can be sent to the processing module
    base64_decode = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
    parsed_records.append(json.loads(base64_decode))
    return processing_module


def get_processing_module(event, record, module_mapping):
    """Get the processing module from the eventSourceARN

    Args:
        event (str): Event Type
        record (Dict): Dictionary representation of the kinesis event
        module_mapping (StreamProcessor): Mapping of modules to stream processors.

    Raises:
        Exception: Raises an exception if there it no way to process an event seen by the lambda.

    Returns:
        StreamProcessor: The processor for this event.
    """
    source_stream_name = record["eventSourceARN"].split("/")[-1]

    # Log info the number of records using lazy formatting
    logging.debug("Processing %i records from %s", len(event["Records"]), source_stream_name)

    # Throw an error if there's no processing module for the stream
    if source_stream_name not in module_mapping:
        raise Exception(
            f'Tried to find a processing module for the stream, but no module was found for "{source_stream_name}". Check the module_mapping has a module associated with the stream name.'
        )

        # Set the processing module to the module associated with the stream name
    processing_module = module_mapping[source_stream_name]
    return processing_module


def send_to_dead_letter_table(record):
    """Send the record to the dead letter table if it can't be processed. This is to avoid hanging lambdas.
    This is not implemented yet.

    Args:
        record (Dict): The record that cannot be processed.
    """
    logging.warning("Found a bad message. Throwing away until dead letter table is implemented. \nEvent: %s", record)
