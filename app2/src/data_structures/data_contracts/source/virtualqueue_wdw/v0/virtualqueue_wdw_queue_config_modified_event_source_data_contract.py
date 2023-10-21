"""Source Data Contract Template for WdwVirtualQueueQueueConfigModifiedEvent"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class VirtualQueueWDWQueueConfigModifiedEventModel(BaseModel):
    """Payload class for VirtualQueueWDWQueueConfigModifiedEventModel"""

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
        example="AAAAA000",
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

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Guardians of the Galaxy: Cosmic Rewind",
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

    symbolic_identifier: Optional[str] = Field(
        None,
        alias="symbolicIdentifier",
        name="",
        description="",
        example="gotg",
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
        example=1666200343558,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
