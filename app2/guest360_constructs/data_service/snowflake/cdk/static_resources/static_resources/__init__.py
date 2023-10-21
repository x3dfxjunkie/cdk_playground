"""Aws Snowpipe Construct
Creates roles, policies, sqs queue and policies for snowpipe
"""
# pylint: disable=logging-fstring-interpolation lazy processing not needed in cdk

import logging
from typing import TypedDict
from strongtyping.strong_typing import match_class_typing

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.data_service.snowflake.cdk.external_stage.external_stage import ExternalStage
from app.guest360_constructs.data_service.snowflake.cdk.notification_integration.notification_integration import (
    NotificationIntegration,
)

logger = logging.getLogger(__name__)


@match_class_typing
class StaticResourcesProps(TypedDict):
    """aws snowpipe properties from config file"""

    external_stage: dict
    notification_integration: dict


class StaticResources(Construct360):
    """l3 construct for combining ExternalStage and NotificationIntegration"""

    @property
    def external_stage(self) -> ExternalStage:
        return self._external_stage

    @property
    def notification_integration(self) -> NotificationIntegration:
        return self._notification_integration

    def __init__(self, scope: Construct360, construct_id: str, props: StaticResourcesProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # runtime check of types
        StaticResourcesProps(props)

        self._external_stage = ExternalStage(self, self.pass_id, props["external_stage"])
        self._notification_integration = NotificationIntegration(self, self.pass_id, props["notification_integration"])
