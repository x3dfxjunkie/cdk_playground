"""Source Data Contract for Dinetime Visits"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class CustomValue(BaseModel):
    """CustomValue Class"""

    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Name of application where visit was placed",
        example="requesterID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="Value",
        name="Value",
        description="Version of device where visit was placed ",
        example="WDW-iOS-7.21",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Loyalty(BaseModel):
    """Loyalty Class"""

    loyalty_card_id: str = Field(
        ...,
        alias="LoyaltyCardID",
        name="Loyalty Card Identifier",
        description="Loyalty card identifier of the guest.",
        example="{99999999-ED86-4A64-86FB-25ED86EA6449}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PhoneNumber(BaseModel):
    """PhoneNumber Class"""

    id: str = Field(
        ...,
        alias="ID",
        name="Phone Identifier",
        description="Unique identifier for the guest phone number.",
        example="99999999-83ef-4073-9606-146a4c414e7c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phone_number: str = Field(
        ...,
        alias="PhoneNumber",
        name="Phone Number",
        description="Guest phone number.",
        example="1234567890",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phone_number_string: str = Field(
        ...,
        alias="PhoneNumberString",
        name="Phone Number String",
        description="Phone number of the guest with LADA code.",
        example="+11234567890",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sort: int = Field(
        ...,
        alias="Sort",
        name="Sort",
        description="LADA code of guest phone number (?)",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Type",
        description="Type of the guest phone number.",
        example="Mobile",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guest(BaseModel):
    """Guest Class"""

    first_name: str = Field(
        ...,
        alias="FirstName",
        name="First Name",
        description="First name",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="ID",
        name="Identifier",
        description="A globally unique identifier for a guest record",
        example="99999999-83ef-4073-9606-146a4c414e7c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_anonymous: bool = Field(
        ...,
        alias="IsAnonymous",
        name="Is Anonymous Flag",
        description="Flag to indicates if guest data is anonymous.",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_subscribed_to_email_marketing: bool = Field(
        ...,
        alias="IsSubscribedToEmailMarketing",
        name="Is Subscribed to Email Marketing Flag",
        description="Flag to indicate whether guest subscribes to email marketing",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_subscribed_to_qsr_marketing: bool = Field(
        ...,
        alias="IsSubscribedToQsrMarketing",
        name="Is Subscribed To QSR Marketing",
        description="Flag to indicate whether guest subscribes to QSR's marketing",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_subscribed_to_sms_marketing: bool = Field(
        ...,
        alias="IsSubscribedToSmsMarketing",
        name="Is Subscribed to SMS Marketing",
        description="Flag to indicate whether guest subscribes to SMS marketing",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_name: str = Field(
        ...,
        alias="LastName",
        name="Last Name",
        description="Last name",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Las Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2020-07-09T17:11:47Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    loyalty: Loyalty = Field(..., alias="Loyalty", name="Loyalty", description="Guest loyalty info")
    notes: str = Field(
        ...,
        alias="Notes",
        name="Notes",
        description="Guest notes",
        example="The Hollywood Brown Derby Lunch\nAdults(3)\nChildren(1)\nInfants(1)\nhigh chairs(1)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Server Last Update",
        description="The date/time of the most recent change/update to the server.",
        example="2020-07-09T17:11:47Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phone_numbers: Optional[List[PhoneNumber]] = Field(
        None,
        alias="PhoneNumber",
        name="Phone Number",
        description="Collection of GuestPhoneNumber objects representing the guest phone number records",
    )
    food_allergies: Optional[str] = Field(
        None,
        alias="FoodAllergies",
        name="Food Allergies",
        description="Food allergies of the guest.",
        example="Shellfish, Fish, Milk",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Mixes(BaseModel):
    """Mixes Class"""

    count: int = Field(
        ...,
        alias="Count",
        name="Count",
        description="Mix count.",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Type",
        description="Mix type.",
        example="Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PartyMix(BaseModel):
    """PartyMix Class"""

    mixes: List[Mixes] = Field(
        ...,
        alias="Mixes",
        name="Mixes",
        description="Set of party mix details",
    )


class SeatedTable(BaseModel):
    """SeatedTable Class"""

    end_time: Optional[datetime] = Field(
        None,
        alias="EndTime",
        name="End Time",
        description="End time in ISO 8601 format",
        example="2023-02-28T13:59:54-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="Flag to indicate if table is active.",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_current: bool = Field(
        ...,
        alias="IsCurrent",
        name="Is Current Flag",
        description="Flag to indicate whether this record is current",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_time: datetime = Field(
        ...,
        alias="StartTime",
        name="Start Time",
        description="Start time in ISO 8601 format",
        example="2023-02-28T12:12:40-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_id: str = Field(
        ...,
        alias="TableID",
        name="Table Identifier",
        description="A globally unique identifier for a table record",
        example="157e126d-2d7a-41af-acd4-540564ff1700",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="TableName",
        name="Table Name",
        description="Name of the specified table",
        example="111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Quote(BaseModel):
    """Quote Class"""

    consumer_quote_string: str = Field(
        ...,
        alias="ConsumerQuoteString",
        name=" Consumer Quote String",
        description="Quote string presented to guest/consumer",
        example="55 minutes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote_high: int = Field(
        ...,
        alias="QuoteHigh",
        name="Quite High",
        description="Upper boundary of the Quote range",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote_low: int = Field(
        ...,
        alias="QuoteLow",
        name="Quote Low",
        description="Lower boundary of the Quote range",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site_quote_string: str = Field(
        ...,
        alias="SiteQuoteString",
        name="Site Quote String",
        description="Current quote information for employee viewing",
        example="55 minutes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PreassignedTable(BaseModel):
    """PreassignedTable Class"""

    end_time: Optional[datetime] = Field(
        None,
        alias="EndTime",
        name="End Time",
        description="End time in ISO 8601 format",
        example="2023-02-28T13:59:54-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="Flag to indicate table is active",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_current: bool = Field(
        ...,
        alias="IsCurrent",
        name="Is Current Flag",
        description="Flag to indicate whether this record is current",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_time: datetime = Field(
        ...,
        alias="StartTime",
        name="Start Time",
        description="Start time in ISO 8601 format",
        example="2023-02-28T12:12:40-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_id: str = Field(
        ...,
        alias="TableID",
        name="Table Identifier",
        description="A globally unique identifier for a table record",
        example="99999999-2d7a-41af-acd4-540564ff1700",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="TableName",
        name="Table Name",
        description="Name of the specified table",
        example="111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Visits(BaseModel):
    """Visits Class"""

    arrival_time: Optional[datetime] = Field(
        None,
        alias="ArrivalTime",
        name="Arrival Time",
        description="Time in which the guest arrives to the venue",
        example="2023-02-28T12:08:04-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    completed_time: Optional[datetime] = Field(
        None,
        alias="CompletedTime",
        name="Completed Time",
        description="Completed time in ISO 8601 format",
        example="2023-02-28T13:59:54-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    confirmation_number: Optional[str] = Field(
        None,
        alias="ConfirmationNumber",
        name="Confirmation Number",
        description="Confirmation number of the visit",
        example="123ABC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    confirmation_number_id: int = Field(
        ...,
        alias="ConfirmationNumberId",
        name="Confirmation Number Identifier",
        description="Confirmation number identifier of the visit",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    creation_time: datetime = Field(
        ...,
        alias="CreationTime",
        name="Creation Time",
        description="Creation time in ISO 8601 format",
        example="2023-02-28T05:32:12-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    custom_values: Optional[List[CustomValue]] = Field(
        None, alias="CustomValue", name="Custom Value", description="Custom value of the visit record"
    )
    estimated_arrival_time: Optional[datetime] = Field(
        None,
        alias="EstimatedArrivalTime",
        name="Estimated Arrival Time",
        description="Estimated arrival time in ISO 8601 format",
        example="2023-02-28T12:25:00-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    external_id: Optional[str] = Field(
        None,
        alias="ExternalID",
        name="External Identifier",
        description="External identifier of the visit record from a 3rd party",
        example="999999999999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest: Guest = Field(..., alias="Guest", name="Guest", description="Guest details")
    guest_id: str = Field(
        ...,
        alias="GuestID",
        name="Guest Identifier",
        description="A globally unique identifier for the guest record tied to the current visit record.",
        example="99999999-83ef-4073-9606-146a4c414e7c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="ID",
        name="Identifier",
        description="Globally unique identifier for the related visit record",
        example="99999999-83ef-4073-9606-146a4c414e7c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    iid: int = Field(
        ...,
        alias="IID",
        name="Integer Identifier",
        description="An integer type identifier for a QSR visit record",
        example=9999999999,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Las Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2023-02-28T05:32:12-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notes: str = Field(
        ...,
        alias="Notes",
        name="Notes",
        description="Notes of the visit",
        example="The Hollywood Brown Derby Lunch\nAdults(3)\nChildren(1)\nInfants(1)\nhigh chairs(1)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notification_type: str = Field(
        ...,
        alias="NotificationType",
        name="Notification Type",
        description="Notification type of the visit.",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    paged_time: Optional[datetime] = Field(
        None,
        alias="PagedTime",
        name="Paged Time",
        description="Paged time in ISO 8601 format",
        example="2023-02-28T12:11:07-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    party_mix: PartyMix = Field(
        ...,
        alias="PartyMix",
        name="Party Mix",
        description="Party mix details",
    )
    seated_tables: Optional[List[SeatedTable]] = Field(
        None,
        alias="SeatedTable",
        name="Seated Table",
        description="Seated table details",
    )
    seated_time: Optional[datetime] = Field(
        None,
        alias="SeatedTime",
        name="Seated Time",
        description="Seated time in ISO 8601 format",
        example="2023-02-28T12:12:40-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Sever Last Update",
        description="Server last update timestamp of the event, in ISO 8601 format",
        example="2023-02-28T05:32:12-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    size: int = Field(
        ...,
        alias="Size",
        name="Visit size",
        description="Visit cover count size.",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="Status",
        name="Visit Status",
        description="Status of current visit record.",
        example="Completed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Visit Type",
        description="Type of current visit record.",
        example="Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visit_source: str = Field(
        ...,
        alias="VisitSource",
        name="Visit Source",
        description="Visit record source.",
        example="DineTimeAPI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    canceled_time: Optional[datetime] = Field(
        None,
        alias="CanceledTime",
        name="Canceled Time",
        description="Canceled time in ISO 8601 format",
        example="2023-02-28T14:13:35-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote: Optional[Quote] = Field(None, alias="Quote", name="Quote", description="Quote-related information")
    seating_area_name: Optional[str] = Field(
        None,
        alias="SeatingAreaName",
        name="Seating Area Name",
        description="Seating area's name",
        example="Restaurant",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preassigned_tables: Optional[List[PreassignedTable]] = Field(
        None,
        alias="PreassignedTable",
        name="Preassigned Table",
        description="Collection of VisitPreassignedTable objects representing preassigned tables with the visit",
    )


class DineTimeVisitsModel(BaseModel):
    """DineTimeVisitsModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Visits Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Visits Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    more_data: bool = Field(
        ...,
        alias="MoreData",
        name="More Data Flag",
        description="Flag to indicate if record has more data with same site id",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Visit site identifier",
        example="99999999-c5b7-4424-b953-f8aaecaa2aa0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    timestamp_cutoff: datetime = Field(
        ...,
        alias="TimestampCutoff",
        name="Timestamp Cutoff",
        description="Cutoff timestamp of the visit, in ISO 8601 format",
        example="2023-02-28T19:33:05.904+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visits: List[Visits] = Field(..., alias="Visits", name="Visits", description="Collection of visit details")
