"""Source Data Contract for DLR VQ Queue Is Auto Summon Enabled Updated Event"""
from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class VirtualQueueDLRQueueIsAutosummonEnabledUpdatedEventModel(BaseModel):
    """Payload class for VirtualQueueDLRQueueIsAutosummonEnabledUpdatedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Queue Is Autosummon Enabled Updated Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "QueueIsAutosummonEnabledUpdatedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="QueueIsAutosummonEnabledUpdatedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    autosummon_enabled: bool = Field(
        ...,
        alias="autosummonEnabled",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE020",
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
        example=1620348298742,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
