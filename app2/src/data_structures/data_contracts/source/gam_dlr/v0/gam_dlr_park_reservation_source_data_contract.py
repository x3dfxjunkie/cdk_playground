"""Source Data Contract for GAM DLR Park Reservation"""

from __future__ import annotations
from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class NativeGuestIdItem(BaseModel):
    """Data class that represents various Guest Identifier types and values"""

    type: str = Field(
        ...,
        alias="type",
        name="Guest ID Type",
        description="Guest ID type for the reservation party",
        example="transactional-guest-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Guest ID Value",
        description="Guest ID value corresponding to the Guest ID type for the reservation party",
        example="750834738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Entitlement(BaseModel):
    """Data class that represents the details of the entitlement and the primary contact"""

    res_id: str = Field(
        ...,
        alias="resId",
        name="Reservation ID",
        description="Reservation ID - unique for each party-entry booking",
        example="2746232133626135552",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    conf_id: str = Field(
        ...,
        alias="confId",
        name="Confirmation ID",
        description="Confirmation ID provided to the Guest, common for the whole party that is booked together",
        example="274623211613552640",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    swid: str = Field(
        ...,
        alias="swid",
        name="Starwave Guest Identifier",
        description="Unique identifier for the booking Guest's online account",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="First Name",
        description="First name of Guest for whom party entry entitlement was booked",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="lastName",
        name="Last Name",
        description="Last name of Guest for whom party entry entitlement was booked",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    email: Optional[str] = Field(
        None,
        alias="email",
        name="Email Address",
        description="Email address of booking Guest",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    exp_date: date = Field(
        ...,
        alias="expDate",
        name="Experience Date",
        description="Experience date for the booking",
        example="2023-05-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exp_slot: str = Field(
        ...,
        alias="expSlot",
        name="Experience Slot",
        description="Slot booked, often the whole day of the booked day",
        example="DAILY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exp_park: Optional[str] = Field(
        None,
        alias="ExpPark",
        name="Experience Park",
        description="Park booked for entry",
        example="DLR_DP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    slot_start_date_time: datetime = Field(
        ...,
        alias="slotStartDateTime",
        name="Slot Start Datetime",
        description="Reservation slot start datetime - often seen to be at 0hrs on the booked day",
        example="2023-05-06T00:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_status: str = Field(
        ...,
        alias="reservationStatus",
        name="Reservation Status",
        description="Status of the park reservation - NEW when created, CANCELED when deleted",
        example="NEW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_group: Optional[str] = Field(
        None,
        alias="ageGroup",
        name="Age Group",
        description="Age group of the Guest - ADULT, CHILD, ALL_AGES etc.",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_visual_id: str = Field(
        ...,
        alias="ticketVisualId",
        name="Ticket Visual ID",
        description="Visual ID of the ticket for which park reservation was booked",
        example="705310557062042399040",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    sku: str = Field(
        ...,
        alias="sku",
        name="Stock Keeping Unit",
        description="Sku number for the reservation",
        example="70532PAH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_origin: str = Field(
        ...,
        alias="reservationOrigin",
        name="Reservation Origin",
        description="Reservation origin indicating the channel through which reservation was made",
        example="WEB-TICKETS-PASSES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: str = Field(
        ...,
        alias="productId",
        name="Product ID",
        description="Park reservation product ID",
        example="DLR_RESORT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GAMDLRParkReservationModel(BaseModel):
    """Payload class for GAMDLRParkReservationModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM DLR Park Reservation"
        stream_name = "gam-kinesis-gam-parkreservation-guest360-dlr"
        description = "DLR Guest part reservations as shared by the park reservation source system"
        unique_identifier = ["entitlement.resId"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "CmeParkReservation"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - CmeParkReservation",
        example="CmeParkReservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the park reservation was created or deleted",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Guest identifiers, often SWIDs, for the booking Guest and the party",
    )
    entitlement: Entitlement = Field(
        ...,
        alias="entitlement",
        name="Entitlement",
        description="Details of the booked entitlement and the primary contact",
    )
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-04-28T19:35:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
