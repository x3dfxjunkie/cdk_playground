"""Source Data Contract for GAM WDW Dine"""
from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class NativeGuestIdItem(BaseModel):
    """Data class that represents various Guest Identifier types and values"""

    type: str = Field(
        ...,
        alias="type",
        name="Dining Guest ID Type",
        description="The Guest ID type for the dining party",
        example="transactional-guest-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Dining Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the dining party",
        example="750854738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class PartyMix(BaseModel):
    """Data class that represents the Guest party mix"""

    adult: str = Field(
        ...,
        alias="adult",
        name="Adult",
        description="Number of adults in the party mix",
        example="2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    child: str = Field(
        ...,
        alias="child",
        name="Child",
        description="Number of children in the party mix",
        example="2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    infant: str = Field(
        ...,
        alias="infant",
        name="Infant",
        description="Number of infants in the party mix",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    unknown: str = Field(
        ...,
        alias="unknown",
        name="Unknown",
        description="Unknown party mix type",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PrepaidAmountItem(BaseModel):
    """Data class that represents details of prepaid amounts"""

    age_type: str = Field(
        ...,
        alias="ageType",
        name="Age Type",
        description="Age group of Guests - Adult, Child, Infant",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_count: str = Field(
        ...,
        alias="ageCount",
        name="Age Count",
        description="Number of Guests by age group",
        example="2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    amount: str = Field(
        ...,
        alias="amount",
        name="Amount",
        description="Amount prepaid for each Guest in the age group, with tax",
        example="55.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sub_total: str = Field(
        ...,
        alias="subTotal",
        name="Sub Total",
        description="Sub total for each Guest in the age group, prior to tax",
        example="49.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TotalPrepaidAmount(BaseModel):
    """Data class that represents total prepaid amounts"""

    amount: str = Field(
        ...,
        alias="amount",
        name="Amount",
        description="Total amount prepaid for all Guests in the dining party",
        example="110.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax: str = Field(
        ...,
        alias="tax",
        name="Tax",
        description="Total tax prepaid for all Guests in the dining party",
        example="10.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gratuity: str = Field(
        ...,
        alias="gratuity",
        name="Gratuity",
        description="Total gratuity prepaid for all Guests in the dining party",
        example="20.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sub_total: str = Field(
        ...,
        alias="subTotal",
        name="Sub Total",
        description="Sub total for all Guests in the dining party, prior to tax",
        example="49.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prepaid_amount: List[PrepaidAmountItem] = Field(
        ...,
        alias="prepaidAmount",
        name="Prepaid Amount",
        description="Prepaid amounts for Guest by each age group",
    )


class EventDining(BaseModel):
    """Data class that represents details related to reservation of an event dining"""

    product_type: str = Field(
        ...,
        alias="productType",
        name="Product Type",
        description="Dining event product type",
        example="ShowPackage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: Optional[str] = Field(
        None,
        alias="productId",
        name="Product ID",
        description="Dining event product ID",
        example="159470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product: str = Field(
        ...,
        alias="enterpriseProduct",
        name="Enterprise Product",
        description="Dining event enterprise product ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: datetime = Field(
        ...,
        alias="startDateTime",
        name="Start Datetime",
        description="Start datetime of the dining reservation",
        example="2023-06-25T16:45:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    service_period: str = Field(
        ...,
        alias="servicePeriod",
        name="Service Period",
        description="Dining event service period ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_service_period: str = Field(
        ...,
        alias="wdproServicePeriod",
        name="WDPRO Service Period",
        description="WDPRO service period ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    party_mix: Optional[PartyMix] = Field(
        None,
        alias="partyMix",
        name="Party Mix",
        description="Number of Adult, Child, Infant in the party mix",
    )
    total_prepaid_amount: Optional[TotalPrepaidAmount] = Field(
        None,
        alias="totalPrepaidAmount",
        name="Total Prepaid Amount",
        description="Total prepaid amount for the entire dining party",
    )


class ShowDining(BaseModel):
    """Data class that represents details related to reservation of a dinner show"""

    product_type: str = Field(
        ...,
        alias="productType",
        name="Product Type",
        description="Dining show product type",
        example="ShowDiningProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: Optional[str] = Field(
        None,
        alias="productId",
        name="Product ID",
        description="Dining show product ID",
        example="159470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product: str = Field(
        ...,
        alias="enterpriseProduct",
        name="Enterprise Product",
        description="Dining show enterprise product ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: datetime = Field(
        ...,
        alias="startDateTime",
        name="Start Datetime",
        description="Start datetime of the dining reservation",
        example="2023-06-25T16:45:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    service_period: str = Field(
        ...,
        alias="servicePeriod",
        name="Service Period",
        description="Dining show service period ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_service_period: str = Field(
        ...,
        alias="wdproServicePeriod",
        name="WDPRO Service Period",
        description="WDPRO service period ID",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    party_mix: Optional[PartyMix] = Field(
        None,
        alias="PartyMix",
        name="Party Mix",
        description="Number of Adult, Child, Infant in the party mix",
    )
    total_prepaid_amount: Optional[TotalPrepaidAmount] = Field(
        None,
        alias="totalPrepaidAmount",
        name="Total Prepaid Amount",
        description="Total prepaid amount for the entire dining party",
    )
    printed_table_number: Optional[str] = Field(
        None,
        alias="printedTableNumber",
        name="Printed Table Number",
        description="Assigned table number for the dining party",
        example="73",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_pickup_indicator: Optional[str] = Field(
        None,
        alias="TicketPickupIndicator",
        name="Ticket Pickup Indicator",
        description="Indicates whether the ticket was already picked up",
        example="false",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AllergyItem(BaseModel):
    """Data class that represents food allergies notified for the dining party"""

    allergy: Optional[str] = Field(
        None,
        alias="allergy",
        name="Allergy",
        description="List of food allergies to be accommodated for the dining party ",
        example="No Wheat or Gluten",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AddOnComponentItem(BaseModel):
    """Data class that represents other add on components in a dining reservation"""

    quantity: Optional[str] = Field(
        None,
        alias="quantity",
        name="Quantity",
        description="The quantity of the product added",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product_id: Optional[str] = Field(
        None,
        alias="enterpriseProductId",
        name="Enterprise Product ID",
        description="Enterprise ID of the product added",
        example="19313501",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: Optional[str] = Field(
        None,
        alias="productId",
        name="Product ID",
        description="ID of the product added",
        example="5429398",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PartyMemberItem(BaseModel):
    """Data class that represents roles and relationships of Guests in the reservation"""

    role: str = Field(
        ...,
        alias="role",
        name="Role",
        description="Role of the Guest - Owner or Guest",
        example="Guest",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_group: str = Field(
        ...,
        alias="ageGroup",
        name="Age Group",
        description="Age group of the Guest - ADULT, CHILD, INFANT etc.",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    relationship: List[str] = Field(
        ...,
        alias="relationship",
        name="Relationship",
        description="Relationship of the Guest to the Dining Party - OWNER and/or PARTICIPANT",
        example=["PARTICIPANT"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Id(BaseModel):
    """Data class that represents the Guest ID type/value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Dining Guest ID Type",
        description="The Guest transaction ID type assigned by the dining reservation system; this field however carries the ID value",
        example="750854738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Dining Guest ID Value",
        description="The Guest transaction ID value assigned by the dining reservation system at the individual Guest level",
        example="750854738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class PrimaryTransactionalGuest(BaseModel):
    """Data class that represents the primary Guest ID"""

    id: Id = Field(
        ...,
        alias="id",
        name="Guest Transaction ID",
        description="Guest ID type/value pair for the primary Guest",
    )


class SpecialRequestItem(BaseModel):
    """Data class that represents specially requested items in a dining reservation"""

    code: str = Field(
        ...,
        alias="code",
        name="Code",
        description="Code for the special request",
        example="SNWA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="name",
        name="Name",
        description="Name for the special request",
        example="Wheelchair accessibility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of the special request",
        example="SE_SPECIAL_NEED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DiningReservationItem(BaseModel):
    """Data class that represents the dining reservation details in a CREATE, MODIFY or DELETE event"""

    dining_reservation_number: str = Field(
        ...,
        alias="diningReservationNumber",
        name="Dining Reservation Number",
        description="Dining reservation number",
        example="353116564535",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    reservation_source: Optional[str] = Field(
        None,
        alias="reservationSource",
        name="Reservation Source",
        description="Source, most likely the originating system of the dining reservation, but often seen as NONE",
        example="NONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    owner_participant: Optional[bool] = Field(
        None,
        alias="ownerParticipant",
        name="Owner Participant",
        description="Indicates if the booking Guest is also a participant",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Dining Status",
        description="Status of the dining reservation - Booked etc.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vip_level: Optional[str] = Field(
        None,
        alias="vipLevel",
        name="VIP Level",
        description="Indicates if the booking Guest is a VIP",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    booking_date_time: Optional[datetime] = Field(
        None,
        alias="bookingDateTime",
        name="Booking Datetime",
        description="Dining reservation booking datetime",
        example="2023-04-26T07:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    contact_number: Optional[str] = Field(
        None,
        alias="contactNumber",
        name="Contact Number",
        description="Contact phone number for the dining reservation",
        example="14046614693",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    event_dining: Optional[EventDining] = Field(
        None,
        alias="eventDining",
        name="Event Dining",
        description="Event dining details, if applicable",
    )
    show_dining: Optional[ShowDining] = Field(
        None,
        alias="showDining",
        name="Show Dining",
        description="Show dining details, if applicable",
    )
    allergies: Optional[List[AllergyItem]] = Field(
        None,
        alias="allergies",
        name="Allergies",
        description="Food allergies, if any, for dining party",
    )
    add_on_components: Optional[List[AddOnComponentItem]] = Field(
        None,
        alias="addOnComponents",
        name="Add On Components",
        description="Additional components added to the dining reservation",
    )
    party_members: Optional[List[PartyMemberItem]] = Field(
        None,
        alias="partyMembers",
        name="Party Members",
        description="Details, roles, contacts etc. of the dining party",
    )
    primary_transactional_guest: Optional[PrimaryTransactionalGuest] = Field(
        None,
        alias="primaryTransactionalGuest",
        name="Primary Transactional Guest",
        description="Additional details of the primary Guest of the dining reservation",
    )
    special_requests: Optional[List[SpecialRequestItem]] = Field(
        None,
        alias="specialRequests",
        name="Special Requests",
        description="Special requests added to the dining reservation",
    )
    cancellation_date_time: Optional[datetime] = Field(
        None,
        alias="cancellationDateTime",
        name="Cancellation Datetime",
        description="Dining reservation cancellation datetime",
        example="2023-04-26T07:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GAMWDWDineModel(BaseModel):
    """Payload class for GAMWDWDineModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Dine"
        stream_name = "gam-kinesis-gam-dining-guest360-wdw"
        description = """WDW Guest dining reservations as shared from the reservation source system"""
        unique_identifier = ["diningReservation.diningReservationNumber"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "Dining Reservation"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - Dining Reservation",
        example="Dining Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the dining reservation was created, modified or deleted",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Dining party Guest identifiers from the source system",
    )
    timestamp: Optional[datetime] = Field(
        None,
        alias="timestamp",
        name="Event timestamp",
        description="Timestamp of the event generated by GAM",
        example="2023-03-29T12:57:49Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dining_reservation: Optional[DiningReservationItem] = Field(
        None,
        alias="diningReservation",
        Name="Dining Reservation",
        description="Dining reservation details for CREATE, MODIFY and DELETE actions",
    )
