"""Source Data Contract for DLR VQ Boarding Group Released Event"""
from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class VirtualQueueDLRBoardingGroupReleasedEventModel(BaseModel):
    """Payload class for VirtualQueueDLRBoardingGroupReleasedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Boarding Group Released Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "BoardingGroupReleasedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="BoardingGroupReleasedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=175,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group_type: str = Field(
        ...,
        alias="boardingGroupType",
        name="",
        description="",
        example="PRIMARY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE053",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_ids: List[str] = Field(
        ...,
        alias="guestIds",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    message_campaign_id: str = Field(
        ...,
        alias="messageCampaignId",
        name="",
        description="",
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
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

    recovery_type: str = Field(
        ...,
        alias="recoveryType",
        name="",
        description="",
        example="NO_RECOVERY",
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

    time_zone_offset_ms: int = Field(
        ...,
        alias="timeZoneOffsetMs",
        name="",
        description="",
        example=-28800000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1674876880671,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
