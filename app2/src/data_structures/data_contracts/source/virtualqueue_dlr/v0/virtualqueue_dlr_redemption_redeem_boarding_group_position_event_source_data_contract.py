"""Source Data Contract for DLR VQ Redemption Redeem Boarding Group Position Event"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRRedemptionRedeemBoardingGroupPositionEventModel(BaseModel):
    """Payload class for VirtualQueueDLRRedemptionRedeemBoardingGroupPositionEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Redemption Redeem Boarding Group Position Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
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
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="ticket-visual-id:1066497692092656499107",
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
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queued_at: int = Field(
        ...,
        alias="queuedAt",
        name="",
        description="",
        example=1666053232597,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redeemed_at: int = Field(
        ...,
        alias="redeemedAt",
        name="",
        description="",
        example=1666064767238,
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
        example=1666060935304,
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
        example=1666064767238,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
