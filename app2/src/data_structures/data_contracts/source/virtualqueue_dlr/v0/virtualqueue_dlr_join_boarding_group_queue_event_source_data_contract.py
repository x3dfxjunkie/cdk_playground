"""Source Data Contract for DLR VQ Join Boarding Group Queue Event"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueDLRJoinBoardingGroupQueueEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Join Boarding Group Queue Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "JoinBoardingGroupQueueEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="JoinBoardingGroupQueueEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    anonymous_party_size: Optional[int] = Field(
        None,
        alias="anonymousPartySize",
        name="",
        description="",
        example=1,
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

    boarding_group_type: str = Field(
        ...,
        alias="boardingGroupType",
        name="",
        description="",
        example="PRIMARY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cast_member_id: str = Field(
        ...,
        alias="castMemberId",
        name="",
        description="",
        example="MOUSE00W",
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

    current_geo_region_ids: Optional[str] = Field(
        None,
        alias="currentGeoRegionIds",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: str = Field(
        ...,
        alias="externalDefinitionId",
        name="",
        description="",
        example="401479;entityType=Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: Optional[str] = Field(
        None,
        alias="guestId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mobile_app: Optional[str] = Field(
        None,
        alias="mobileApp",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    party_guest_ids: List[str] = Field(
        ...,
        alias="partyGuestIds",
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
        example=1666057650907,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: Optional[int] = Field(
        None,
        alias="waitTime",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
