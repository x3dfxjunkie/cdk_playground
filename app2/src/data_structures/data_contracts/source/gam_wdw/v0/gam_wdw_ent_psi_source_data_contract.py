"""Source Data Contract for GAM WDW Personal Scheduled Items"""
from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class EnterpriseContent(BaseModel):
    """Data class that represents the entreprise ID details of the entertainment"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of the entertainment",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Enterprise ID of the entertainment",
        example="7E11A1170AD5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ParticipantGuestIdentifierItem(BaseModel):
    """Data class that represents the Participant Guest ID type/value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Guest ID Type",
        description="The Guest ID type for the participant",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the participant",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class PrimaryGuestIdentifier(BaseModel):
    """Data class that represents the Primary Guest ID type/value pair"""

    type: str = Field(
        ...,
        alias="type",
        name="Guest ID Type",
        description="The Guest ID type for the primary Guest",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the primary Guest",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class GAMWDWEntPsiModel(BaseModel):
    """Payload class for GAMWDWEntPsiModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Ent PSI"
        stream_name = "gam-kinesis-ent-psi-guest360-wdw"
        description = """Notes and non-bookable personal scheduled items of WDW Guests through MDX"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "PSI"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always PSI",
        example="PSI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: str = Field(
        ...,
        alias="source",
        name="Source",
        description="Source system for the personal scheduled event",
        example="MDX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Action",
        description="Describes whether the Personal Scheduled Item was created new or modified or deleted",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_id: str = Field(
        ...,
        alias="nativeId",
        name="Native ID",
        description="Native ID of the personal scheduled event",
        example="1900051793",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    name: Optional[str] = Field(
        None,
        alias="name",
        name="Name",
        description="Name of the personal scheduled event",
        example="Nap time",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    description: Optional[str] = Field(
        None,
        alias="description",
        name="Description",
        description="Description of the personal scheduled event",
        example="tommy's naptime",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: Optional[datetime] = Field(
        None,
        alias="startDateTime",
        name="Start Date Time",
        description="Start date time of the personal scheduled event",
        example="2017-09-22T08:25:42Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time: Optional[datetime] = Field(
        None,
        alias="endDateTime",
        name="End Date Time",
        description="End date time of the personal scheduled event",
        example="2017-09-22T08:25:42Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary_guest_identifier: Optional[PrimaryGuestIdentifier] = Field(
        None,
        alias="primaryGuestIdentifier",
        name="Primary Guest Identifier",
        description="Primary guest identifier of the personal scheduled event",
    )
    participant_guest_identifiers: Optional[List[ParticipantGuestIdentifierItem]] = Field(
        None,
        alias="participantGuestIdentifiers",
        name="Participant Guest Identifiers",
        description="Participant guest identifiers of the personal scheduled event",
    )
    location: Optional[str] = Field(
        None,
        alias="location",
        name="Location",
        description="Location of the personal scheduled event",
        example="Resort room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_content: Optional[EnterpriseContent] = Field(
        None,
        alias="enterpriseContent",
        name="Enterprise Content",
        description="Enterprise content of the personal scheduled event",
    )
    timestamp: Optional[datetime] = Field(
        None,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-04-26T15:04:54Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
