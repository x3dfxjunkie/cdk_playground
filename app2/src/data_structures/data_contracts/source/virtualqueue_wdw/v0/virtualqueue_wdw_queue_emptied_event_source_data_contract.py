"""Source Data Contract Template for WdwVirtualQueueQueueEmptiedEvent"""


from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class VirtualQueueWDWQueueEmptiedEventModel(BaseModel):
    """Payload class for VirtualQueueWDWQueueEmptiedEventModel"""

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
        key_path_value = "QueueEmptiedEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="QueueEmptiedEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    admin_id: str = Field(
        ...,
        alias="adminId",
        name="",
        description="",
        example="DDDDD000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="",
        example="716488b3-e407-4901-b3e5-5acd9ec6becc",
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

    time_zone_offset_ms: int = Field(
        ...,
        alias="timeZoneOffsetMs",
        name="",
        description="",
        example=-18000000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1674533368374,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
