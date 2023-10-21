"""
File containing code for the guest360 ingestion pipeline stack
"""
import logging
import sys
from aws_cdk import Stack
from app.guest360_constructs.app_config_base import Guest360AppConfigBase

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ingestion.kinesis_event_pipe import Kinesis
from app.infrastructure.workstream_stack import WorkstreamStack


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Ingestion | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class IngestionKinesis(WorkstreamStack):
    """IngestionMessaging
    Stack dedicated to Message pattern ingestion. This is meant to create a stack for each messaging system.
    """

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        config: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)

        self.kinesis_streams = []

        # log the current stack_extension for potential debugging...
        logger.debug(
            "Passing configuration to pipeline stack: TYPE %s NAME %s",
            config["ingest_pattern"],
            config["stack_extension"],
        )
        app_config_base_props = {
            "deployment_strategy": {
                "deployment_duration_in_minutes": 0,
                "growth_factor": 100,
                "replicate_to": "NONE",
            },
        }
        app_config_base = Guest360AppConfigBase(
            self, construct_id=config["stack_extension"], props=app_config_base_props
        )

        for config_dictionary in config["pattern_instances"]:
            config_dictionary["resources"].update(
                {
                    "static_buckets": config["static_buckets"],
                    "data_pipe": config_dictionary["data_pipe"],
                    "app_config_base": app_config_base,
                }
            )
            stream = Kinesis(self, construct_id=config["stack_extension"], props=config_dictionary["resources"])
            self.kinesis_streams.append(
                {
                    "stream_name": stream.kinesis_stream_name,
                    "stream": stream.kinesis_stream,
                    "firehose_name": stream.firehose_name,
                }
            )
