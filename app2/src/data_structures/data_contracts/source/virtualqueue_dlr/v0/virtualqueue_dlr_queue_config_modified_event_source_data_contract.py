"""Source Data Contract for DLR VQ Queue Config Modified Event"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRQueueConfigModifiedEventModel(BaseModel):
    """Payload class for VirtualQueueDLRQueueConfigModifiedEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Queue Config Modified Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "QueueConfigModifiedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="QueueConfigModifiedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    action: str = Field(
        ...,
        alias="action",
        name="",
        description="",
        example="UPDATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: Optional[str] = Field(
        None,
        alias="externalDefinitionId",
        name="",
        description="",
        example="18492231;entityType=Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="World of Color - Season of Light",
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

    symbolic_identifier: Optional[str] = Field(
        None,
        alias="symbolicIdentifier",
        name="",
        description="",
        example="world-of-color",
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
        example=1670431426328,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
