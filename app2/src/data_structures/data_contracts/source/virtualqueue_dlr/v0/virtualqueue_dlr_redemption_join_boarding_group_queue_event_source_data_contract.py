"""Source Data Contract for DLR VQ Redemption Join Boarding Group Queue Event"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueDLRRedemptionJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class forVirtualQueueDLRRedemptionJoinBoardingGroupQueueEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Redemption Join Boarding Group Queue Event"
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "_type"
        key_path_value = "RedemptionJoinBoardingGroupQueueEvent"

    field_type: str = Field(
        ...,
        alias="_type",
        name="",
        description="",
        example="RedemptionJoinBoardingGroupQueueEvent",
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

    external_definition_id: str = Field(
        ...,
        alias="externalDefinitionId",
        name="",
        description="",
        example="IntegrationTest",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="Unknown",
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
        example=1597980328622,
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
