"""Source Data Contract Template for WdwVirtualQueueMobileLeaveQueueEvent"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueWDWMobileLeaveQueueEventModel(BaseModel):
    """Payload class for VirtualQueueWDWMobileLeaveQueueEventModel"""

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
        key_path_value = "MobileLeaveQueueEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="MobileLeaveQueueEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    anonymous_party_leave_count: Optional[str] = Field(
        None,
        alias="anonymousPartyLeaveCount",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=118,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="{AAAAAAAA-E330-4444-8801-ABABABABABAB}",
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

    mobile_app: str = Field(
        ...,
        alias="mobileApp",
        name="",
        description="",
        example="MDX",
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
        example=1665775629145,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
