"""Source Data Class for Dinetime Team Member Events"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class FloorPlan(BaseModel):
    """FloorPlan Class"""

    key: str = Field(
        ...,
        alias="Key",
        name="Key",
        description="Key of the floor plan. Commonly same as UID",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Name of the floor plan.",
        example="Blue Bayou",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Unique identifier of the floor plan",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Shift(BaseModel):
    """Shift Class"""

    key: str = Field(
        ...,
        alias="Key",
        name="Key",
        description="Key of the shift. Commonly same as UID.",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Name of the Shift",
        example="Blue Bayou",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Unique identifier of the shift",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Station(BaseModel):
    """Station Class"""

    key: str = Field(
        ...,
        alias="Key",
        name="Key",
        description="Key of the station. Commonly same as UID.",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Name of the station.",
        example="Blue Bayou",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Unique identifier of the station",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TeamMember(BaseModel):
    """TeamMember Class"""

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

    id: int = Field(
        ...,
        alias="Id",
        name="Identifier",
        description="Identifier of the team member.",
        example=0,
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

    notes: str = Field(
        ...,
        alias="Notes",
        name="Notes",
        description="Notes on team member's record",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_id: int = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Integer identifier of the site",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique identifier of the shift record",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_id: Optional[str] = Field(
        None,
        alias="ExternalId",
        name="External Identifier",
        description="External ID of the TeamMember record",
        example="123456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Content(BaseModel):
    """Content Class"""

    floor_plan: FloorPlan = Field(
        ...,
        alias="FloorPlan",
        name="Floor Plan",
        description="Floor plan details in the content of the team member",
    )

    shift: Shift = Field(
        ...,
        alias="Shift",
        name="Shift",
        description="Shift details in the content of the team member",
    )

    stations: List[Station] = Field(
        ...,
        alias="Stations",
        name="",
        description="Station details in the content of the team member",
    )

    team_member: TeamMember = Field(
        ...,
        alias="TeamMember",
        name="Team Member",
        description="Team member details",
    )


class Event(BaseModel):
    """Event Class"""

    category: str = Field(
        ...,
        alias="Category",
        name="Category",
        description="Category of the event",
        example="TeamMemberEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content: Content = Field(
        ...,
        alias="Content",
        name="Content",
        description="Content details of the team member",
    )

    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Last Update",
        description="Last update timestamp of the event, in ISO 8601 format",
        example="2023-02-24T19:20:53.4503407-08:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Server Last Update",
        description="Server last update timestamp of the event, in ISO 8601 format",
        example="2023-02-25T03:25:37.343+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sync_source: str = Field(
        ...,
        alias="SyncSource",
        name="Sync Source",
        description="Sync source of the event.",
        example="Backoffice",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="Type",
        name="Type",
        description="Type of the event",
        example="TeamMemberStationAssigned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique Identifier of the event",
        example="99999999-389e-41b3-8e03-87a2e940a400",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    version: int = Field(
        ...,
        alias="Version",
        name="Version",
        description="Version of the event record",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeTeamMemberEventsModel(BaseModel):
    """DineTimeTeamMemberEventsModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Team Member Events Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Team Member Events Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    download_cutoff: datetime = Field(
        ...,
        alias="DownloadCutoff",
        name="Download Cutoff",
        description="Download cutoff timestamp of the event, in ISO 8601 format",
        example="2023-02-25T04:10:37.916+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    events: List[Event] = Field(
        ...,
        alias="Events",
        name="Events",
        description="Set of events",
    )

    more_data: bool = Field(
        ...,
        alias="MoreData",
        name="More Data Flag",
        description="Flag that indicates if record has more data with same site identifier.",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Globally unique identifier of the site",
        example="99999999-e3c9-42de-ad8d-39a2da747dd9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
