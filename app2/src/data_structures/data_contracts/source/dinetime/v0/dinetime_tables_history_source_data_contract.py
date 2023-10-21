"""Source Data Contract for Dinetime Tables History"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Mix(BaseModel):
    """Mix Class"""

    count: int = Field(
        ...,
        alias="Count",
        name="Mix Count",
        description="Count of the party mix type",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Mix Type",
        description="Type of the party mix. The following are considered acceptable values: Adult, Child, Infant, Senior.",
        example="Infant",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PartyMix(BaseModel):
    """PartyMix Class"""

    mixes: List[Mix] = Field(..., alias="Mixes", name="Mixes", description="Party mix details")


class PreassignedTable(BaseModel):
    """PreassignedTable Class"""

    end_time: Optional[str] = Field(
        None,
        alias="EndTime",
        name="End Time",
        description="End time in ISO 8601 format",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="True flag to indicate preassigned table is active",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_current: bool = Field(
        ...,
        alias="IsCurrent",
        name="Is Record Current Flag",
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
        example="2023-02-07T11:29:05-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_id: str = Field(
        ...,
        alias="TableID",
        name="Table Identifier",
        description="A globally unique identifier for a preassigned table record",
        example="99999999-ae1f-4725-b761-1076d6c8d541",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="TableName",
        name="Table Name",
        description="Name of the specified table",
        example="304A-7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SeatedTable(BaseModel):
    """SeatedTable Class"""

    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="True flag indicates table is active",
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
        example="2023-02-07T11:29:05-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_id: str = Field(
        ...,
        alias="TableID",
        name="Table Identifier",
        description="A globally unique identifier for a table record",
        example="99999999-ae1f-4725-b761-1076d6c8d541",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="TableName",
        name="Table Name",
        description="Name of the specified table",
        example="304A-7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_time: Optional[datetime] = Field(
        None,
        alias="EndTime",
        name="End Time",
        description="End time in ISO 8601 format",
        example="2023-02-07T17:33:49-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CustomValue(BaseModel):
    """CustomValue Class"""

    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="The table name",
        example="304A-5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="Value",
        name="Value",
        description="Collection of VisitCustomValue objects representing the visit custom value",
        example="MOBILE-APP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Quote(BaseModel):
    """Quote Class"""

    consumer_quote_string: str = Field(
        ...,
        alias="ConsumerQuoteString",
        name="Consumer Quote String",
        description="Quote string presented to guest/consumer",
        example="60 minutes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote_high: int = Field(
        ...,
        alias="QuoteHigh",
        name="Quote High",
        description="Upper boundary of the Quote range",
        example=60,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote_low: int = Field(
        ...,
        alias="QuoteLow",
        name="Quote Low",
        description="Lower boundary of the Quote range",
        example=56,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site_quote_string: str = Field(
        ...,
        alias="SiteQuoteString",
        name="Site Quote String",
        description="Current quote information for employee viewing",
        example="60 minutes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Visit(BaseModel):
    """Visit Class"""

    arrival_time: datetime = Field(
        ...,
        alias="ArrivalTime",
        name="Arrival Time",
        description="Arrival time in ISO 8601 format.",
        example="2023-02-07T11:29:09-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    confirmation_number: Optional[str] = Field(
        None,
        alias="ConfirmationNumber",
        name="Confirmation Number",
        description="Confirmation number",
        example="9ABCDE",
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
        example="2023-02-07T05:34:01-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    estimated_arrival_time: Optional[datetime] = Field(
        None,
        alias="estimated_arrival_time",
        name="",
        description="",
        example="2023-02-07T17:30:00-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    external_id: Optional[str] = Field(
        None,
        alias="ExternalID",
        name="External Identifier",
        description="Estimated arrival time in ISO 8601 format",
        example="999999999999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id: str = Field(
        ...,
        alias="GuestID",
        name="Guest Identifier",
        description="A globally unique identifier for the guest record tied to the current visit record.",
        example="99999999-9999-9999-94de-809612acadf6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="ID",
        name="Identifier",
        description="Globally identifier for a visit record, which could be a WebAhead, reservation, or walk-in",
        example="99999999-9999-9999-b98a-dfacd4ab7166",
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
        name="Last Update",
        description="Last update timestamp of the event, in ISO 8601 format",
        example="2023-02-08T08:00:59.623+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notes: str = Field(
        ...,
        alias="Notes",
        name="Notes",
        description="Visit notes",
        example="Crown of Corellia Dining Room Captain's Table\r\n\r\n Celebrations:Birthday,Barb Schultz",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notification_type: str = Field(
        ...,
        alias="NotificationType",
        name="Notification Type",
        description="Visit notification type",
        example="SMS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    paged_time: Optional[datetime] = Field(
        None,
        alias="PagedTime",
        name="Paged Time",
        description="Paged time in ISO 8601 format",
        example="2023-02-07T17:33:49-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    party_mix: PartyMix = Field(
        ...,
        alias="PartyMix",
        name="Party Mix",
        description="Guests indicated details for reservation",
    )
    preassigned_tables: Optional[List[PreassignedTable]] = Field(
        None,
        alias="PreassignedTables",
        name="Preassigned Tables",
        description="Collection of VisitPreassignedTable objects representing preassigned tables with the visit",
    )
    seated_tables: List[SeatedTable] = Field(
        ...,
        alias="SeatedTables",
        name="Seated Tables",
        description="Seated tables details on the visit",
    )
    seated_time: Optional[datetime] = Field(
        None,
        alias="SeatedTime",
        name="Seated Time",
        description="Seated time in ISO 8601 format",
        example="2023-02-07T17:33:49-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Server Last Update",
        description="Server last update timestamp of the event, in ISO 8601 format",
        example="2023-02-08T08:19:41.103+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    size: int = Field(
        ...,
        alias="Size",
        name="Size",
        description="Cover count size",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="Status",
        name="Status",
        description="Status of current visit record. The following are considered acceptable values: NotYetArrived, PartiallyArrived, Waiting, NoShow, WalkAway, Notified, PartiallySeated, Seated, AlmostFinished, Payment, Completed, CheckStarted, Canceled",
        example="Seated",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Type",
        description="Type of current visit record. The following are considered acceptable values: WalkIn, CallAhead, Reservation, Carryout.",
        example="Infant",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visit_source: str = Field(
        ...,
        alias="VisitSource",
        name="Visit Source",
        description="Visit data source",
        example="DineTimeAPI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    completed_time: Optional[datetime] = Field(
        None,
        alias="CompletedTime",
        name="Completed Time",
        description="Completed time in ISO 8601 format",
        example="2023-02-20T21:26:37-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    custom_values: Optional[List[CustomValue]] = Field(
        None,
        alias="CustomValues",
        name="Custom Values",
        description="Collection of VisitCustomValue objects representing the visit custom value",
    )
    seating_area_name: Optional[str] = Field(
        None,
        alias="seating_area_name",
        name="",
        description="Identifier of the related seating area for the table",
        example="Restaurant",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quote: Optional[Quote] = Field(None, alias="Quote", name="Quote", description="Quote-related information")


class HistoryItem(BaseModel):
    """HistoryItem Class"""

    created_date: datetime = Field(
        ...,
        alias="CreatedDate",
        name="Created Date",
        description="Creation time of the table, in ISO 8601 format",
        example="2013-01-01T00:00:00+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    floor_plan_name: str = Field(
        ...,
        alias="FloorPlanName",
        name="Floor Plan Name",
        description="Name of the related floor plan for the table history record",
        example="Main",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="ID",
        name="Identifier",
        description="A globally unique identifier for a table record",
        example="99999999-a351-4324-b98a-dfacd4ab7166",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Active Flag",
        description="True flag indicates table is active",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Last Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2023-02-08T08:00:59.623+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    maximum_seat_count: int = Field(
        ...,
        alias="MaximumSeatCount",
        name="Maximum Seat Count",
        description="Maximum seats for reservation",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    minimum_seat_count: int = Field(
        ...,
        alias="MinimumSeatCount",
        name="Minimum Seat Count",
        description="Minimum seats for reservation",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Table Name",
        description="The table name",
        example="304A-5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    operating_period_name: str = Field(
        ...,
        alias="OperatingPeriodName",
        name="Operating Period Name",
        description="Operation Period Name",
        example="Dinner",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    seat_count: int = Field(
        ...,
        alias="SeatCount",
        name="Seat Count",
        description="The number of guests seated at the table",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Server Last Update",
        description="Server last update timestamp of the event, in ISO 8601 format",
        example="2023-02-08T08:19:41.103+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    shift_name: str = Field(
        ...,
        alias="ShiftName",
        name="Shift Name",
        description="Name of the related shift for the table history record ",
        example="16 Floor Plan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    station_name: str = Field(
        ...,
        alias="StationName",
        name="Station Name",
        description="Name of the related station for the table history record",
        example="Section 1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    team_member_uid: str = Field(
        ...,
        alias="TeamMemberUID",
        name="Team Member Unique Identifier",
        description="Globally unique identifier of the team member",
        example="99999999-7b14-4df0-90cc-3ef029ce1281",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visit: Visit = Field(
        ...,
        alias="Visit",
        name="Visit",
        description="Visit details",
    )
    visit_uid: str = Field(
        ...,
        alias="VisitUID",
        name="Visit Uinique Identifier",
        description="Globally unique identifier for the related visit record",
        example="99999999-3ad0-46f9-bd37-a4a1379cafc8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cleaned_time: Optional[datetime] = Field(
        None,
        alias="CleanedTime",
        name="Cleaned Time",
        description="Cleaned time of the table in ISO 8601 format",
        example="2023-02-21T09:52:29+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dirtied_time: Optional[datetime] = Field(
        None,
        alias="DirtiedTime",
        name="Dirtied Time",
        description="Dirty time of the table in ISO 8601 format",
        example="2023-02-21T09:48:33+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeTablesHistoryModel(BaseModel):
    """DineTimeTablesHistoryModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Tables History Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Tables History Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    cut_off_date: datetime = Field(
        ...,
        alias="CutOffDate",
        name="Cutoff Date",
        description="Cutoff time of the table in ISO 8601 format",
        example="2023-02-08T08:19:41.103+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    has_more_data: bool = Field(
        ...,
        alias="HasMoreData",
        name="Has More Data Flag",
        description="Flag to indicate if record has more data with same site id",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    history: List[HistoryItem] = Field(..., alias="History", name="History", description="History details")
    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Site identifier.",
        example="99999999-16d1-4a0b-82e9-a98e05be39db",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
