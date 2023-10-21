"""Source Data Contract for GAM DLR Planning Party"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Manager(BaseModel):
    """Data class that represents the manager of the planning party"""

    type: str = Field(
        ...,
        alias="type",
        name="Manager Guest ID Type",
        description="The Guest ID type for the manager of the planning party. Could be any ID type which locates a Guest uniquely.",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Manager Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the manager",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Identifier(BaseModel):
    """Data class that represents the Guest ID type/value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Member Guest ID Type",
        description="The Guest ID type for the member. Could be any ID type which locates a Guest uniquely.",
        example="ticket-visual-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Member Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the member",
        example="705940557025160139296",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class MemberItem(BaseModel):
    """Data class that represents the member details"""

    identifier: Identifier = Field(
        ...,
        alias="identifier",
        name="Identifier",
        description="Unique identifiers for the member",
    )


class RemovedGuestIdentifierItem(BaseModel):
    """Data class that represents the members that were removed from the planning party"""

    type: str = Field(
        ...,
        alias="type",
        name="Member Guest ID Type",
        description="The Guest ID type for the member that has been removed",
        example="guid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Member Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the removed member",
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class PlanningParty(BaseModel):
    """Data class that represents the manager and member details"""

    id: str = Field(
        ...,
        alias="id",
        name="Planning Party ID",
        description="Planning Party ID, not found to be unique and comes as '0' for some CREATEs",
        example="6190016",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Planning Party Type",
        description="Planning party type based on the Guests - Default, Quest, Story Guests etc.",
        example="DEFAULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location: str = Field(
        ...,
        alias="location",
        name="Planning Party Location",
        description="Facility ID for the planning party",
        example="336894",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: datetime = Field(
        ...,
        alias="startDateTime",
        name="Start DateTime",
        description="Start datetime of the planning party",
        example="2023-04-05T15:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time: datetime = Field(
        ...,
        alias="endDateTime",
        name="End DateTime",
        description="End datetime of the planning party",
        example="2023-04-06T05:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    manager: Manager = Field(
        ...,
        alias="manager",
        name="Manager",
        description="Identifier for the manager of the planning party",
    )
    members: List[MemberItem] = Field(
        ...,
        alias="members",
        name="Members",
        description="Identifier(s) for the member(s) of the planning party",
    )
    removed_guest_identifiers: Optional[List[RemovedGuestIdentifierItem]] = Field(
        None,
        alias="removedGuestIdentifiers",
        name="Removed Guest Identifiers",
        description="Identifier(s) for the removed member(s) of the planning party when modified",
    )


class GAMDLRPlanningPartyModel(BaseModel):
    """Payload class for GAMDLRPlanningPartyModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM DLR Planning Party"
        stream_name = "gam-kinesis-gam-planningparty-guest360-dlr"
        description = """DLR Guests that are tied under planning parties via MDX"""
        unique_identifier = ["planningParty.id", "planningParty.type"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "PlanningParty"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always PlanningParty",
        example="PlanningParty",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the planning party was created new, modified or deleted",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    planning_party: PlanningParty = Field(
        ...,
        alias="planningParty",
        name="Planning Party",
        description="Planning Party details",
    )
    timestamp: Optional[datetime] = Field(
        None,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-04-03T20:27:29.776652604Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
