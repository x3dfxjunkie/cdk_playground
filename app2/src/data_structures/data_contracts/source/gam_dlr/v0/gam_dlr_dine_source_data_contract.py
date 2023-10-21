"""Source Data Contract for GAM DLR Dine"""
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

    adult: Optional[str] = Field(
        None,
        alias="adult",
        name="Adult",
        description="Number of adults in the party mix",
        example="2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    child: Optional[str] = Field(
        None,
        alias="child",
        name="Child",
        description="Number of children in the party mix",
        example="2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    infant: Optional[str] = Field(
        None,
        alias="infant",
        name="Infant",
        description="Number of infants in the party mix",
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
        description="Amount prepaid for each Guest in the age group",
        example="55.00",
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
    prepaid_amount: List[PrepaidAmountItem] = Field(
        ...,
        alias="prepaidAmount",
        name="Prepaid Amount",
        description="Prepaid amounts by each Guest by each age group",
    )


class EventDining(BaseModel):
    """Data class that represents details related to reservation of an event dining"""

    product_type: str = Field(
        ...,
        alias="productType",
        name="Product Type",
        description="",
        example="ShowPackage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: Optional[str] = Field(
        None,
        alias="productId",
        name="Product ID",
        description="",
        example="159470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product: str = Field(
        ...,
        alias="enterpriseProduct",
        name="Enterprise Product",
        description="",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_enterprise_product: str = Field(
        ...,
        alias="wdproEnterpriseProduct",
        name="WDPRO Enterprise Product",
        description="",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_dining_facility: str = Field(
        ...,
        alias="enterpriseDiningFacility",
        name="Enterprise Dining Facility",
        description="",
        example="354261",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_enterprise_dining_facility: str = Field(
        ...,
        alias="wdproEnterpriseDiningFacility",
        name="WDPRO Enterprise Dining Facility",
        description="",
        example="354261",
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
        description="",
        example="369069",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_service_period: str = Field(
        ...,
        alias="wdproServicePeriod",
        name="WDPRO Service Period",
        description="",
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
    dining_policy: str = Field(
        ...,
        alias="diningPolicy",
        name="Dining Policy",
        description="",
        example="354261",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_dining_policy: str = Field(
        ...,
        alias="wdproDiningPolicy",
        name="WDPRO Dining Policy",
        description="",
        example="354261",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    total_prepaid_amount: Optional[TotalPrepaidAmount] = Field(
        None,
        alias="totalPrepaidAmount",
        name="Total Prepaid Amount",
        description="Total prepaid amount for the entire dining party",
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

    quantity: str = Field(
        ...,
        alias="quantity",
        name="Quantity",
        description="The quantity of the product added",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product_id: str = Field(
        ...,
        alias="enterpriseProductId",
        name="Enterprise Product ID",
        description="Enterprise ID of the product added",
        example="19313501",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: str = Field(
        ...,
        alias="productId",
        name="Product ID",
        description="ID of the product added",
        example="5429398",
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
        description="The Guest transaction ID type assigned by the dining reservation system at the Guest level",
        example="transactional-guest-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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


class Name(BaseModel):
    """Data class that represents the Guest name components"""

    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="First Name",
        description="Dining Guest first name",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: str = Field(
        ...,
        alias="lastName",
        name="Last Name",
        description="Dining Guest last name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="middleName",
        name="Middle Name",
        description="Dining Guest middle name",
        example="M",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    title: Optional[str] = Field(
        None,
        alias="title",
        name="Name Title",
        description="Dining Guest name title",
        example="Mr.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    suffix: Optional[str] = Field(
        None,
        alias="suffix",
        name="Name Suffix",
        description="Dining Guest name suffix",
        example="Sr.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class AddressListItem(BaseModel):
    """Data class that represents the Guest addresses"""

    address_line1: Optional[str] = Field(
        None,
        alias="addressLine1",
        name="Address",
        description="Dining Guest address line1",
        example="123 Main St",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    city: Optional[str] = Field(
        None,
        alias="city",
        name="Address City",
        description="City name from the dining Guest address",
        example="Orlando",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    country: Optional[str] = Field(
        None,
        alias="country",
        name="Address Country",
        description="Country code from the dining Guest address",
        example="USA",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    postal_code: Optional[str] = Field(
        None,
        alias="postalCode",
        name="Address Postal Code",
        description="Postal code from the dining Guest address",
        example="06520",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    state: Optional[str] = Field(
        None,
        alias="state",
        name="Address State",
        description="State name from the dining Guest address",
        example="FL",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Address Type",
        description="Type of the dining Guest address",
        example="HOME",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EmailListItem(BaseModel):
    """Data class that represents the Guest email addresses"""

    email: Optional[str] = Field(
        None,
        alias="email",
        name="Email Address",
        description="Dining Guest email address",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class PhoneListItem(BaseModel):
    """Data class that represents the Guest phone numbers"""

    number: Optional[str] = Field(
        None,
        alias="number",
        name="Phone Number",
        description="Phone number of the dining Guest",
        example="19493383116",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Phone Type",
        description="Type of the dining Guest phone",
        example="PERSONAL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ExternalGuestReferenceItem(BaseModel):
    """Data class that represents the Guest ID type/value from external source systems"""

    type: str = Field(
        ...,
        alias="type",
        name="External Reference ID Type",
        description="External source system ID type of the dining Guest, often found to be SWID",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="External Reference ID Value",
        description="External source system ID value corresponding to the ID type of the dining Guest",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class TransactionalGuest(BaseModel):
    """Data class that represents the individual Guest contact details"""

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="Guest Transaction ID",
        description="Transaction ID assigned by the dining reservation system at the individual Guest level",
        example="750853769",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    role: Optional[str] = Field(
        None,
        alias="role",
        name="Role",
        description="Role of the Guest - specified for the owner and optional for the rest",
        example="OWNER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: Name = Field(
        ...,
        alias="name",
        name="Guest Name",
        description="Name details of the dining Guests, often marked as Guest 1, Guest 2 etc. for non-primary Guests",
    )
    address_list: List[AddressListItem] = Field(
        ...,
        alias="addressList",
        name="Address List",
        description="Address details of the dining Guest, mainly applicable to the primary Guest",
    )
    phone_list: List[PhoneListItem] = Field(
        ...,
        alias="phoneList",
        name="Phone List",
        description="Phone number details of the dining Guest, mainly applicable to the primary Guest",
    )
    email_list: List[EmailListItem] = Field(
        ...,
        alias="emailList",
        name="Email List",
        description="Email addres details of the dining Guest, mainly applicable to the primary Guest",
    )
    external_guest_references: Optional[List[ExternalGuestReferenceItem]] = Field(
        None,
        alias="externalGuestReferences",
        name="External Guest References",
        description="External source system ID type/value, mainly applicable to the primary Guest",
    )


class PartyMemberItem(BaseModel):
    """Data class that represents the individual Guest roles, age groups etc."""

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="Guest ID",
        description="Unique Guest ID, although always found to be 0",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
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
    age_group: Optional[str] = Field(
        None,
        alias="ageGroup",
        name="Age Group",
        description="Age group of the Guest - ADULT, CHILD, INFANT etc.; often not present for the OWNER",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: Id = Field(
        ...,
        alias="id",
        name="Guest Transaction ID",
        description="Guest ID type/value pair for the dining Guest",
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
    transactional_guest: TransactionalGuest = Field(
        ...,
        alias="transactionalGuest",
        name="Transactional Guest",
        description="Details, contacts etc. of the dining party",
    )


class PrimaryTransactionalGuest(BaseModel):
    """Data class that represents the primary Guest ID"""

    id: Id = Field(
        ...,
        alias="id",
        name="Guest Transaction ID",
        description="Guest ID type/value pair for the primary Guest",
    )
    last_name: str = Field(
        ...,
        alias="lastName",
        name="Guest Last Name",
        description="Primary Guest last name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    swid: str = Field(
        ...,
        alias="swid",
        name="Starwave Guest Identifier",
        description="Unique identifier for the Guest's online account",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    guest_id: str = Field(
        ...,
        alias="guestId",
        name="Guest Transaction ID",
        description="Transaction ID assigned by the dining reservation system at the individual Guest level",
        example="750853769",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
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
    claimable: Optional[bool] = Field(
        None,
        alias="claimable",
        name="Claimable",
        description="Indicates if the dining reservation is claimable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_dining: Optional[EventDining] = Field(
        None,
        alias="eventDining",
        name="Event Dining",
        description="Event dining details, if applicable",
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
        alias="PrimaryTransactionalGuest",
        name="Primary Transactional Guest",
        description="Additional details of the primary Guest of the dining reservation",
    )


class GAMDLRDineModel(BaseModel):
    """Payload class for GAMDLRDineModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM DLR Dine"
        stream_name = "gam-kinesis-dreams-dine-guest360-dlr"
        description = """DLR Guest dining reservations as shared from the reservation source system"""
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
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Details of Guest IDs from source systems for the dining party",
    )
    dining_reservation: DiningReservationItem = Field(
        ...,
        alias="diningReservation",
        Name="Dining Reservation",
        description="Dining reservation details for CREATE, MODIFY and DELETE actions",
    )
