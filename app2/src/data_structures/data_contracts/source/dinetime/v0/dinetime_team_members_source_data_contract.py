"""Source Data Class for Dinetime Team Members"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class TeamMemberItem(BaseModel):
    """TeamMemberItem Class"""

    creation_time: datetime = Field(
        ...,
        alias="CreationTime",
        name="Creation Time",
        description="Creation time in ISO 8601 format",
        example="2021-11-04T21:01:01+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_name: str = Field(
        ...,
        alias="FirstName",
        name="First Name",
        description="First name of the team member",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="True flag indicates record is active",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_name: str = Field(
        ...,
        alias="LastName",
        name="Last Name",
        description="Last name of the team member",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Last Update",
        description="The date/time of the most recent change/update to the resource data point",
        example="2022-02-21T21:04:21.882+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    server_id: int = Field(
        ...,
        alias="ServerID",
        name="Server Identifier",
        description="Integer ID of the TeamMember record",
        example=123456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Uniquer Identifier",
        description="Globally unique identifier of the team member",
        example="99999999-1e64-4546-a057-b74d00eadac5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    notes: Optional[str] = Field(
        None,
        alias="Notes",
        name="Notes",
        description="Notes of the team member record",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    email: Optional[str] = Field(
        None,
        alias="Email",
        name="Email",
        description="Email of the team member",
        example="qwerty@myemail.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    home_phone: Optional[str] = Field(
        None,
        alias="HomePhone",
        name="Home Phone",
        description="Home phone of the team member",
        example="1234567890",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mobile_phone: Optional[str] = Field(
        None,
        alias="MobilePhone",
        name="Mobile Phone",
        description="MobilePhone of the Team Member record",
        example="1234567890",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_id: Optional[str] = Field(
        None,
        alias="CardId",
        name="Card Identifier",
        description="Card ID of the Team Member record",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_id: Optional[str] = Field(
        None,
        alias="ExternalId",
        name="External Identifier",
        description="External ID of the Team Member record",
        example="123456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeTeamMembersModel(BaseModel):
    """DineTimeTeamMembersModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Team Members Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Team Members Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Globally unique identifier of the site",
        example="99999999-16d1-4a0b-82e9-a98e05be39db",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    team_member: List[TeamMemberItem] = Field(
        ...,
        alias="TeamMember",
        name="Team Member",
        description="Team Member details",
    )
