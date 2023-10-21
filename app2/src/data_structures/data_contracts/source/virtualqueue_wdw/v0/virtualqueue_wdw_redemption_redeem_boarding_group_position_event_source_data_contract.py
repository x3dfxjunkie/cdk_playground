"""Source Data Contract Template for WdwVirtualQueueRedemptionRedeemBoardingGroupPositionEvent"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class VirtualQueueWDWRedemptionRedeemBoardingGroupPositionEventModel(BaseModel):
    """Payload class for VirtualQueueWDWRedemptionRedeemBoardingGroupPositionEventModel"""

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
        key_path_value = "RedemptionRedeemBoardingGroupPositionEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="RedemptionRedeemBoardingGroupPositionEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=56,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="Unknown",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="virtualq-link-id:99eb2500-7cc3-4f67-b468-cb42b8385ecb",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    override_reason: Optional[str] = Field(
        None,
        alias="overrideReason",
        name="",
        description="",
        example="Override",
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

    queued_at: int = Field(
        ...,
        alias="queuedAt",
        name="",
        description="",
        example=1668686403050,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redeemed_at: int = Field(
        ...,
        alias="redeemedAt",
        name="",
        description="",
        example=1668707372197,
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

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="OK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    summoned_at: Optional[int] = Field(
        None,
        alias="summonedAt",
        name="",
        description="",
        example=1668701640000,
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
        example=1668707372197,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
