"""Source Data Contract Template for WdwVirtualQueueJoinBoardingGroupQueueEvent"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueWDWJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueWDWJoinBoardingGroupQueueEventModel"""

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

    anonymous_party_size: Optional[str] = Field(
        None,
        alias="anonymousPartySize",
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
        example=114,
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
        example="411499845;entityType=Attraction",
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
        example=1668805727439,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: int = Field(
        ...,
        alias="waitTime",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
