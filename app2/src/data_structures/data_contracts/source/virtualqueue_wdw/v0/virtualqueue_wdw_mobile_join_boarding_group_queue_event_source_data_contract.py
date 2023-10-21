"""Source Data Contract Template for WdwVirtualQueueMobileJoinBoardingGroupQueueEvent"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class VirtualQueueWDWMobileJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueWDWMobileJoinBoardingGroupQueueEventModel"""

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
        key_path_value = "MobileJoinBoardingGroupQueueEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="MobileJoinBoardingGroupQueueEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=37,
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

    current_geo_region_ids: Optional[List[str]] = Field(
        None,
        alias="currentGeoRegionIds",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: str = Field(
        ...,
        alias="externalDefinitionId",
        name="",
        description="",
        example="10460;entityType=entertainment-venue",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="{AAAAAAAA-ABCD-ABCD-1234-BBBBBBBBBBBB}",
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
        example="603dd3be-d1ec-4f6b-aeea-f7e4c1d072b0",
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
        example=1668706577704,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: int = Field(
        ...,
        alias="waitTime",
        name="",
        description="",
        example=200,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
