"""
File containing code for the guest360 ingestion pipeline stack
"""
import logging
import sys

import aws_cdk
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ingestion.messaging_ingest import Guest360MessagingIngest
from app.guest360_constructs.app_config_base import Guest360AppConfigBase
from app.infrastructure.workstream_stack import WorkstreamStack

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Ingestion | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class IngestionMessaging(WorkstreamStack):
    """IngestionMessaging
    Stack dedicated to Message pattern ingestion. This is meant to create a stack for each messaging system.
    """

    @property
    def kinesis_streams(self) -> list[aws_cdk.aws_kinesis.Stream]:
        """Property to return kinesis streams"""
        return self.streams.kinesis_streams

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        config=dict,
        config_dictionary=dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        config_dictionary["resources"].update(
            {"data_pipe": config_dictionary["data_pipe"], "app_config_base": app_config_base}
        )

        self.streams = Guest360MessagingIngest(
            self, construct_id=config["stack_extension"], props=config_dictionary["resources"]
        )

        # Nags

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for BucketNotificationsHandler"},
            ],
        )
