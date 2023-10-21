"""Source Data Contract for GAM WDW Celebrations"""

from __future__ import annotations
from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class NativeGuestIdItem(BaseModel):
    """Data class that represents various Guest Identifier types and values"""

    type: str = Field(
        ...,
        alias="type",
        name="Celebrating Guest ID Type",
        description="The Guest ID type for the celebrating party.",
        example="celebration_link_id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Celebrating Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the celebrating party",
        example="6051418",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class ExternalReferenceItem(BaseModel):
    """Data class that represents external source system ID types and values"""

    type: str = Field(
        ...,
        alias="type",
        name="External Reference ID Type",
        description="External source system ID type that the celebration is tied to. E.g. Travel Party Segment ID",
        example="travel-plan-segment-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="External Reference ID Value",
        description="External source system ID value corresponding to the ID type that the celebration is tied to",
        example="153116351221",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )


class GuestIdentifier(BaseModel):
    """Data class that represents the Guest ID type/value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Celebrating Guest ID Type",
        description="The Guest ID type for the celebration party",
        example="celebration_link_id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Celebrating Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the celebrating party",
        example="6051419",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class CelebrationGuestItem(BaseModel):
    """Data class that represents roles and IDs of celebrant Guests"""

    celebration_role: str = Field(
        ...,
        alias="celebrationRole",
        name="Celebration Role",
        description="Role of the Guest in the celebrating party - CELEBRANT, OWNER, PARTICIPANT etc.",
        example="CELEBRANT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_identifier: GuestIdentifier = Field(
        ...,
        alias="guestIdentifier",
        name="Guest Identifier",
        description="Unique Guest identifiers for the celebrating party",
    )


class Celebration(BaseModel):
    """Data class that represents the celebration details of the Guests"""

    celebration_id: str = Field(
        ...,
        alias="celebrationId",
        name="Celebration ID",
        description="Unique ID created for each celebration registered by Guest",
        example="50895207",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    celebration_name: str = Field(
        ...,
        alias="celebrationName",
        name="Celebration Name",
        description="Celebration name, as chosen by the Guest",
        example="Jane's Birthday Celebration",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    celebration_type: str = Field(
        ...,
        alias="celebrationType",
        name="Celebration Type",
        description="System ID for What the Guest is celebrating - Birthday, Anniversary, Reunion etc.",
        example="411753226",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    celebration_type_name: str = Field(
        ...,
        alias="celebrationTypeName",
        name="Celebration Type Name",
        description="What the Guest is celebrating - Birthday, Anniversary, First Visit etc.",
        example="Birthday",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Celebration Status",
        description="Status of the celebration - Active, Inactive etc.",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    surprise: bool = Field(
        ...,
        alias="surprise",
        name="Surprise",
        description="Flag set to indicate if the celebration is a surprise for the celebrant",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    celebration_date: Optional[date] = Field(
        None,
        alias="celebrationDate",
        name="Celebration Date",
        description="Celebration Date, if the celebration is specific to a date, E.g. Birthdate, Anniversary date etc.",
        example="2023-06-28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    milestone: Optional[int] = Field(
        None,
        alias="milestone",
        name="Celebration Milestone",
        description="Celebration milestone in number of years, if applicable",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: datetime = Field(
        ...,
        alias="startDateTime",
        name="Start Datetime",
        description="Start datetime for the duration that the celebration is valid",
        example="2023-09-13T04:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time: datetime = Field(
        ...,
        alias="endDateTime",
        name="End Datetime",
        description="End datetime for the duration that the celebration is valid",
        example="2023-09-18T03:59:59Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    external_references: List[ExternalReferenceItem] = Field(
        ...,
        alias="externalReferences",
        name="External References",
        description="External source system IDs that the celebration is tied to. E.g. Travel Party Segment ID",
    )
    guests: List[CelebrationGuestItem] = Field(
        ...,
        alias="guests",
        name="Guests",
        description="Unique IDs of the Guests in the context of the celebration",
    )


class ReservationGuestItem(BaseModel):
    """Data class that represents the individual Guest details in the context of the resort reservation"""

    first_name: str = Field(
        ...,
        alias="firstName",
        name="Guest First Name",
        description="Guest first name",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: str = Field(
        ...,
        alias="lastName",
        name="Guest Last Name",
        description="Guest last name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    guest_identifier: GuestIdentifier = Field(
        ...,
        alias="guestIdentifier",
        name="Guest Identifier",
        description="Unique Guest identifiers for the celebrating party in the context of the resort reservation",
    )
    role: str = Field(
        ...,
        alias="role",
        name="Role",
        description="Role of the Guest in the celebrating party - CELEBRANT, PARTICIPANT etc.",
        example="CELEBRANT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ResortReservationItem(BaseModel):
    """Data class that represents the resort reservation details of celebrant Guests"""

    entitlement_id_type: str = Field(
        ...,
        alias="entitlementIdType",
        name="Entitlement ID Type",
        description="Entitlement ID type that the celebration is tied to. E.g. Travel Party Segment ID, Dining Res Nbr etc.",
        example="travel-plan-segment-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement_id_value: str = Field(
        ...,
        alias="entitlementIdValue",
        name="Entitlement ID Value",
        description="Entitlement ID value corresponding to the ID type that the celebration is tied to",
        example="153116351221",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    guests: List[ReservationGuestItem] = Field(
        ...,
        alias="guests",
        name="Guests",
        description="Unique IDs of the Guests in the context of the resort reservation",
    )


class GAMWDWCelebrationsModel(BaseModel):
    """Payload class for GAMWDWCelebrationsModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Celebrations"
        stream_name = "gam-kinesis-gam-celebrations-guest360"
        description = "WDW Guest celebrations that are attached to reservations"
        unique_identifier = ["celebration.celebrationId"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "CELEBRATION"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always CELEBRATION",
        example="CELEBRATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the Guest celebration was created new, modified or deleted",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-04-26T15:04:54Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Details of Guest IDs from source systems for the celebrating party",
    )
    celebration: Celebration = Field(
        ...,
        alias="celebration",
        name="Celebration",
        description="Details of the Guest celebration as tied to the visit",
    )
    resort_reservations: List[ResortReservationItem] = Field(
        ...,
        alias="resortReservations",
        name="Resort Reservations",
        description="Details of the resort reservation that the Guest celebration is tied to",
    )
