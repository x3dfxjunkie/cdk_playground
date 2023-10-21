"""Source Data Contract Template for WdwVirtualQueueLeaveBoardingGroupQueueEvent"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueWDWLeaveBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueWDWLeaveBoardingGroupQueueEventModel"""

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
        key_path_value = "LeaveBoardingGroupQueueEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="LeaveBoardingGroupQueueEvent",
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
        example=0,
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

    client: str = Field(
        ...,
        alias="client",
        name="",
        description="",
        example="REDEMPTION_APP",
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
        example=1666967322177,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
