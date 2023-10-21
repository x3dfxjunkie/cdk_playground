"""Source Data Contract for CME DLR Reservation"""
from __future__ import annotations
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class Data"""

    age_group: Optional[str] = Field(
        None,
        alias="age_group",
        name="Age Group",
        description="Age Group Code specified for the ticket.  Some tickets, such as MEP Guest Passes and Certs, has 'ALL_AGES' when the ticket is not for a specific age group.",
        example="ADULT",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    guest_email_id: Optional[str] = Field(
        None,
        alias="guest_email_id",
        name="Guest Email Address",
        description="Primary guest email address for the reservation, not specific to the guest with the corresponding reservation",
        example="mickey.mouse@disney.com",
        guest_identifier=False,
        identifier_tag="Direct",
        transaction_identifier=False,
    )
    guest_first_name: str = Field(
        ...,
        alias="guest_first_name",
        name="Guest First Name",
        description="Guest first name for the reservation",
        example="Mickey",
        guest_identifier=False,
        identifier_tag="Direct",
        transaction_identifier=False,
    )
    guest_last_name: str = Field(
        ...,
        alias="guest_last_name",
        name="Guest Last Name",
        description="Guest last name for the reservation",
        example="Mouse",
        guest_identifier=False,
        identifier_tag="Direct",
        transaction_identifier=False,
    )
    auto_updated_dts: Optional[datetime] = Field(
        None,
        alias="auto_updated_dts",
        name="Auto Updated date timestamp",
        description="Date timestamp of the record when auto updated ",
        example="2023-04-20T13:33:15.231Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    conf_id: str = Field(
        ...,
        alias="conf_id",
        name="Confirmation ID",
        description="Confirmation ID from a successful Park Reservation",
        example="210860303607958528",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    created_dts: datetime = Field(
        ...,
        alias="created_dts",
        name="Create Date Timestamp",
        description="Record Created Date Timestamp",
        example="2023-04-10T18:33:15.231Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="Created User",
        description="User or Application that created the record",
        example="f-v-reservation",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    exp_date: date = Field(
        ...,
        alias="exp_date",
        name="Experience Date",
        description="Date of the Reservation",
        example="2022-11-16",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    exp_park: str = Field(
        ...,
        alias="exp_park",
        name="Experience Park ID",
        description="CME Park ID for the Reservation",
        example="WDW_MK",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    exp_slot: str = Field(
        ...,
        alias="exp_slot",
        name="Experience Time Slot",
        description="Time slot designated for the Reservation, ex: Daily (full day) or half",
        example="DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    external_res_id_alt: Optional[str] = Field(
        None,
        alias="external_res_id_alt",
        name="Alternate External Reservation Identifier",
        description="TBC",
        example="AAAA1111-AAAA-AAAA-AAAA-111111111111",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    id: int = Field(
        ...,
        alias="id",
        name="Record Identifier",
        description="Auto-Increment Record Identifier",
        example=12345678,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    inv_bucket_id: str = Field(
        ...,
        alias="inv_bucket_id",
        name="Inventory Bucket Identifier",
        description="Inventory Bucket which Reservation reserved from",
        example="WDW_EP_RESORT_DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    product_id: str = Field(
        ...,
        alias="product_id",
        name="Product Identifier",
        description="Product Identifier associated to the reservation",
        example="WDW_AP",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_id: str = Field(
        ...,
        alias="res_id",
        name="Reservation Identifier",
        description="Unique Reservation Identifier",
        example="10000001",
        guest_identifier=False,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    res_origin: str = Field(
        ...,
        alias="res_origin",
        name="Reservation Origin",
        description="Originating Application/System responsible for the Reservation",
        example="WEB-TICKET-PASSES",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_status: str = Field(
        ...,
        alias="res_status",
        name="Reservation Status",
        description="Reservation Status",
        example="REDEEMED",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_ticket_sku: Optional[str] = Field(
        None,
        alias="res_ticket_sku",
        name="Reservation Ticket SKU",
        description="Ticket Product Code in the Reservation",
        example="6KWPA",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    show_last_four: int = Field(
        ...,
        alias="show_last_four",
        name="Show Last Four",
        description="TBD",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    slot_start_dts: datetime = Field(
        ...,
        alias="slot_start_dts",
        name="Slot Start Date Timestamp",
        description="Reservation Slot Starting Date/Time",
        example="2022-05-26 00:00:00.000000",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    swid: str = Field(
        ...,
        alias="swid",
        name="Starwave ID",
        description="Registered Guest Starwave ID",
        example="{2490CA47-AAAA-BBBB-9397-84F343B7B726}",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    tkt_visual_id: Optional[str] = Field(
        None,
        alias="tkt_visual_id",
        name="Ticket Visual Identifier",
        description="Ticket Visual ID / TCOD associated with the reservation.  If the ticket is part of a room package, it is the Travel Component ID from Resort Reservation",
        example="15100012312312345",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    updated_dts: datetime = Field(
        ...,
        alias="updated_dts",
        name="Update Date Timestamp",
        description="Record updated Date Timestamp",
        example="2023-04-18T13:05:15.231Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    was_inv_override: int = Field(
        ...,
        alias="was_inv_override",
        name="Was Inventory Override",
        description="Specifies if the reservation was an override over specified inventory limits",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    updated_usr: Optional[str] = Field(
        None,
        alias="updated_usr",
        name="Updated User",
        description="Application/User who last updated the record",
        example="pending-job-processor",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    resort_res_id: Optional[str] = Field(
        None,
        alias="resort_res_id",
        name="Resort Reservation Identifier",
        description="Associated Resort Reservation",
        example="11111111",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=True,
    )
    redemption_dts: Optional[datetime] = Field(
        None,
        alias="redemption_dts",
        name="Redemption Date Timestamp",
        description="Reservation Redemption Date Timestamp",
        example="2023-04-17T10:45:25.231Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    or_classification: Optional[str] = Field(
        None,
        alias="or_classification",
        name="Override Classification",
        description="Reason for the inventory Override on the reservation",
        example="maxOverride",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    external_res_id: Optional[str] = Field(
        None,
        alias="external_res_id",
        name="External Reservation Identifier",
        description="Identifier from old park reservation system: GXP - only populated from migrated/historical records",
        example="1600000001",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    booking_category: Optional[str] = Field(
        None,
        alias="booking_category",
        name="Booking Category",
        description="Categorizes the booking group the reservation falls under.  For example: TICKET, AP, MEP, Bonus",
        example="GROUPS",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    pernr: Optional[str] = Field(
        None,
        alias="pernr",
        name="PERNR",
        description="Cast Member Personnel Number",
        example="",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    survey_sent: int = Field(
        ...,
        alias="survey_sent",
        name="Survey Sent",
        description="TBD",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRReservationModel(BaseModel):
    """CME DLR Reservation Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation"
        stream_name = ""  # info not available yet
        description = "Core table representing park reservations at DLR"  # optional
        unique_identifier = ["data.res_id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "reservation"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
