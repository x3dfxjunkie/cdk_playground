"""Source Data Contract Template for WdwVirtualQueueBoardingGroupCreatedEvent"""


from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class VirtualQueueWDWBoardingGroupCreatedEventModel(BaseModel):
    """Payload class forVirtualQueueWDWBoardingGroupCreatedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "BoardingGroupCreatedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="BoardingGroupCreatedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=179,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: str = Field(
        ...,
        alias="externalDefinitionId",
        name="",
        description="",
        example="411499845;entityType=Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="",
        example="90e81c93-b84c-48e0-a98d-121094fa842e",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_name: str = Field(
        ...,
        alias="siteName",
        name="",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    target_guests_per_group: int = Field(
        ...,
        alias="targetGuestsPerGroup",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    time_zone_offset_ms: int = Field(
        ...,
        alias="timeZoneOffsetMs",
        name="",
        description="",
        example=-14400000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1666202113479,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
