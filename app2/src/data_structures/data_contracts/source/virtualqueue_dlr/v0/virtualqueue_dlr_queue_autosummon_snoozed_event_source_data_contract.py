"""Source Data Contract for DLR VQ Queue Autosummon Snoozed Event"""
from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class VirtualQueueDLRQueueAutosummonSnoozedEventModel(BaseModel):
    """Payload class for VirtualQueueDLRQueueAutosummonSnoozedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Queue Autosummon Snoozed Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "QueueAutosummonSnoozedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="QueueAutosummonSnoozedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE002",
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

    snoozed_until: int = Field(
        ...,
        alias="snoozedUntil",
        name="",
        description="",
        example=1675197120000,
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
        example=1675196813970,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
