"""Source Data Contract for DLR VQ Mobile Join Boarding Group Queue Event"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRMobileJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueDLRMobileJoinBoardingGroupQueueEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Mobile Join Boarding Group Queue Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
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
        example=2,
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
        example="18492231;entityType=Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mobile_app: str = Field(
        ...,
        alias="mobileApp",
        name="",
        description="",
        example="DISNEYLAND",
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
        example="A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1",
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
        example=-28800000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1668889721181,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: int = Field(
        ...,
        alias="waitTime",
        name="",
        description="",
        example=555,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
