"""Source Data Contract for DLR VQ Boarding Group Created Event"""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRBoardingGroupCreatedEventModel(BaseModel):
    """Payload class for VirtualQueueDLRBoardingGroupCreatedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Boarding Group Created Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
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
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: Optional[str] = Field(
        None,
        alias="externalDefinitionId",
        name="",
        description="",
        example="401479;entityType=Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="",
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_name: str = Field(
        ...,
        alias="siteName",
        name="",
        description="",
        example="DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    target_guests_per_group: int = Field(
        ...,
        alias="targetGuestsPerGroup",
        name="",
        description="",
        example=2400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    time_zone_offset_ms: int = Field(
        ...,
        alias="timeZoneOffsetMs",
        name="",
        description="",
        example=-25200000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1667709612730,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
