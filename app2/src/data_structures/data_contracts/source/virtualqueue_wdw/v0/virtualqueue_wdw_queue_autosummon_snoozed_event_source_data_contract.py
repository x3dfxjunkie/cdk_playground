"""Source Data Contract Template for WdwVirtualQueueAutosummonSnoozedEvent"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class VirtualQueueWDWQueueAutosummonSnoozedEventModel(BaseModel):
    """Payload class forVirtualQueueWDWQueueAutosummonSnoozedEventModel"""

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
        example="ABCDE002",
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

    snoozed_until: int = Field(
        ...,
        alias="snoozedUntil",
        name="",
        description="",
        example=1667512800000,
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
        example=1667512491016,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
