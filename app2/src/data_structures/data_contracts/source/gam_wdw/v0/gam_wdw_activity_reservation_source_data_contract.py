"""Source Data Contract for GAM WDW Activity Reservation"""

from __future__ import annotations
from datetime import datetime
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


class InventoryDetails(BaseModel):
    """Data class that represents the inventory details related to the activity booked"""

    reservable_resource_id: List[str] = Field(
        ...,
        alias="reservableResourceId",
        name="Reservable Resource ID",
        description="Reservable resource identifier for the activity inventory",
        example=["A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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


class Activity(BaseModel):
    """Data class that represents the details related to the activity that is booked"""

    enterprise_product: int = Field(
        ...,
        alias="enterpriseProduct",
        name="Enterprise Product",
        description="Enterprise product ID for the activity",
        example=16854268,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_facility: int = Field(
        ...,
        alias="enterpriseFacility",
        name="Enterprise Facility",
        description="Enterprise facility ID for the activity",
        example=353586,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_enterprise_product: int = Field(
        ...,
        alias="wdproEnterpriseProduct",
        name="WDPRO Enterprise Product",
        description="WDPRO Enterprise product ID for the activity",
        example=16854268,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wdpro_facility: int = Field(
        ...,
        alias="wdproFacility",
        name="WDPRO Facility",
        description="WDPRO facility ID for the activity",
        example=16854268,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_type: str = Field(
        ...,
        alias="productType",
        name="Product Type",
        description="Activity product type",
        example="ChildActivityProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    service_start_date: datetime = Field(
        ...,
        alias="serviceStartDate",
        name="Service Start Datetime",
        description="Start datetime of the activity",
        example="2023-06-25T16:45:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    duration: int = Field(
        ...,
        alias="duration",
        name="Duration",
        description="Duration of the activity (often in hours)",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    freeze_elapsed_time: int = Field(
        ...,
        alias="freezeElapsedTime",
        name="Freeze Elapsed Time",
        description="Freeze elapsed time",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    freeze_time_to_live: int = Field(
        ...,
        alias="freezeTimeToLive",
        name="Freeze Time To Live",
        description="Freeze time to live",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    inventory_details: InventoryDetails = Field(
        ...,
        alias="inventoryDetails",
        name="Inventory Details",
        description="Details of the inventory associated with the activity",
    )
    party_mix: PartyMix = Field(
        ...,
        alias="partyMix",
        name="Party Mix",
        description="Number of Adult, Child, Infant in the party mix",
    )


class Id(BaseModel):
    """Data class that represents the Guest ID type/value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Guest ID Type",
        description="The Guest transaction ID type assigned by the reservation system",
        example="transactional-guest-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Guest ID Value",
        description="The Guest transaction ID value assigned by the reservation system",
        example="750854738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="indirect",
    )


class PrimaryGuest(BaseModel):
    """Data class that represents the primary Guest ID"""

    id: Id = Field(
        ...,
        alias="id",
        name="Guest Transaction ID",
        description="Guest ID type/value pair for the primary Guest",
    )


class TransactionalGuestItem(BaseModel):
    """Data class that represents roles and relationships of Guests in the reservation"""

    id: Id = Field(
        ...,
        alias="id",
        name="Guest Transaction ID",
        description="Guest ID type/value pair for the reservation Guest",
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
    relationship: List[str] = Field(
        ...,
        alias="relationship",
        name="Relationship",
        description="Relationship of the Guest to the reservation Party - OWNER and/or PARTICIPANT",
        example=["PARTICIPANT"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ActivityReservation(BaseModel):
    """Data class that represents the activity reservation details in a CREATE, MODIFY or DELETE event"""

    contact_name: Optional[str] = Field(
        None,
        alias="contactName",
        name="Contact Name",
        description="Contact person full name for the activity reservation",
        example="Mickey, Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="direct",
    )
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Status",
        description="Status of the Activity reservation - Booked etc.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_number: Optional[str] = Field(
        None,
        alias="reservationNumber",
        name="Reservation Number",
        description="Activity reservation number",
        example="502971245457",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="indirect",
    )
    travel_plan_id: Optional[int] = Field(
        None,
        alias="travelPlanId",
        name="Travel Plan ID",
        description="Travel Plan ID which encompasses all reservations for the visit or travel plan",
        example=953118278452,
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="indirect",
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
    booking_date: Optional[datetime] = Field(
        None,
        alias="bookingDate",
        name="Booking Date",
        description="Activity reservation booking datetime",
        example="2023-04-26T07:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    extra_care_required: Optional[bool] = Field(
        None,
        alias="extraCareRequired",
        name="Extra Care Required",
        description="Indicates whether extra care is required for the activity",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activity: Optional[Activity] = Field(
        None,
        alias="activity",
        name="Activity",
        description="Details of the activity reserved",
    )
    primary_guest: Optional[PrimaryGuest] = Field(
        None,
        alias="primaryGuest",
        name="Primary Guest",
        description="Additional details of the primary Guest of the reservation; this Guest may not be a participant",
    )
    transactional_guests: Optional[List[TransactionalGuestItem]] = Field(
        None,
        alias="transactionalGuests",
        name="Transactional Guests",
        description="Additional details and roles of individual Guests in the reservation; this may not be available for all Guests on the reservation",
    )
    service_period_id: Optional[int] = Field(
        None,
        alias="servicePeriodId",
        name="Service Period ID",
        description="Service period identifier for the activity",
        example=19278773,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    unit_measure_count: Optional[int] = Field(
        None,
        alias="unitMeasureCount",
        name="Unit Measure Count",
        description="Unit measure count of the activity",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    inventory_overide_reason_id: Optional[int] = Field(
        None,
        alias="inventoryOverideReasonId",
        name="Inventory Overide Reason ID",
        description="Inventory override reason ID; found to be 0 if not applicable",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activity_reservation_number: Optional[str] = Field(
        None,
        alias="activityReservationNumber",
        name="Activity Reservation Number",
        description="Activity reservation number; duplicate of reservation_number",
        example="502971245457",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="indirect",
    )


class GAMWDWActivityReservationModel(BaseModel):
    """Payload class for GAMWDWActivityReservationModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Activity Reservation"
        stream_name = "gam-kinesis-gam-activityreservation-guest360-wdw"
        description = """WDW Guest activity reservations as shared by the reservation source system"""
        unique_identifier = ["activityReservation.activityReservationNumber"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "Activity Reservation"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - Activity Reservation",
        example="Activity Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the activity reservation was created, modified or deleted",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Reservation party Guest identifiers from the reservation system",
    )
    activity_reservation: Optional[ActivityReservation] = Field(
        None,
        alias="activityReservation",
        Name="Activity Reservation",
        description="Activity reservation details for CREATE, MODIFY and DELETE actions",
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
