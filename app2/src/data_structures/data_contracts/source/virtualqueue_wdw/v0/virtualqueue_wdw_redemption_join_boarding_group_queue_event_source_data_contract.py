"""Source Data Contract Template for WdwVirtualQueueRedemptionJoinBoardingGroupQueueEvent"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class VirtualQueueWDWRedemptionJoinBoardingGroupQueueEventModel(BaseModel):
    """Payload class for VirtualQueueWDWRedemptionJoinBoardingGroupQueueEventModel"""

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
        example="f74c2b9f-1a4c-40cb-898e-9915a1ab2cef",
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
        example=1666668521595,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: Optional[int] = Field(
        None,
        alias="waitTime",
        name="",
        description="",
        example=25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
