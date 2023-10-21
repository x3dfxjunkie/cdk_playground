"""Source Data Contract for dinetime-tables-events"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Statistics(BaseModel):
    """Statistics Class"""

    opened_time: datetime = Field(
        ...,
        alias="OpenedTime",
        name="Opened Time",
        description="The open timestamp of the table status in ISO 8601 format",
        example="2023-05-17T16:06:36.34645+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    closed_time: Optional[datetime] = Field(
        None,
        alias="ClosedTime",
        name="Closed time",
        description="The close timestamp of the table record in ISO8601 format",
        example="2023-05-17T14:18:46.4620163+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_available_time: datetime = Field(
        ...,
        alias="LastAvailableTime",
        name="Last Available Time",
        description="Last time the table was available in ISO 8601 format",
        example="2023-05-17T17:39:13.6103246+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Table(BaseModel):
    """Table Class"""

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique identifier of the event",
        example="99999999-0464-408f-ade8-18c10655913a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Table Name",
        description="The table name",
        example="34",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    seat_count: int = Field(
        ...,
        alias="SeatCount",
        name="Seat Count",
        description="The number of guests seated at the table",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    min_seat_count: int = Field(
        ...,
        alias="MinSeatCount",
        name="Minimum Seat Count",
        description="The minimum number of guests that may be seated at table",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_seat_count: int = Field(
        ...,
        alias="MaxSeatCount",
        name="Maximum Seat Count",
        description="The maximum number of guests that may be seated at table",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_seats: bool = Field(
        ...,
        alias="EndSeats",
        name="End Seats Flag",
        description="Flag to indicate whether table has endseat. 'True' means active.",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    qsr_table_shape_id: int = Field(
        ...,
        alias="QsrTableShapeID",
        name="QSR Table Shape Identifier",
        description="QSR-defined integer ID representing the shape of the table",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    statistics: Statistics = Field(..., alias="Statistics", name="Statistics", description="Statistics of the table")


class Station(BaseModel):
    """Station Class"""

    uid: Optional[str] = Field(
        None,
        alias="UID",
        name="Unique Identifier",
        description="Unique Identifier of the station",
        example="99999999-f932-4347-a583-3bb9ae2860e1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: Optional[str] = Field(
        None,
        alias="Name",
        name="Name",
        description="Name of the station",
        example="2 - Minnie",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    key: Optional[str] = Field(
        None,
        alias="Key",
        name="Key",
        description="Key of the station. Commonly same as UID",
        example="99999999-f932-4347-a583-3bb9ae2860e1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class FloorPlan(BaseModel):
    """FloorPlan Class"""

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique identifier of the floor plan record",
        example="99999999-0464-408f-ade8-18c10655913a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Floor Plan Name",
        description="Name of the floorplan.",
        example="34",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    key: str = Field(
        ...,
        alias="Key",
        name="Floor Plan Key",
        description="Globally unique identifier of the floor plan",
        example="99999999-f932-4347-a583-3bb9ae2860e1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Shift(BaseModel):
    """Shift Class"""

    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique identifier of the shift record",
        example="99999999-0464-408f-ade8-18c10655913a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Shift Name",
        description="Shift name",
        example="34",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    key: str = Field(
        ...,
        alias="Key",
        name="Shift Key",
        description="Key of the shift",
        example="99999999-f932-4347-a583-3bb9ae2860e1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Content(BaseModel):
    """Content Class"""

    table: Table = Field(..., alias="Table", name="Table", description="Table of the event")
    station: Station = Field(..., alias="Station", name="Station", description="Station of the event")
    floor_plan: FloorPlan = Field(..., alias="FloorPlan", name="FloorPlan", description="FloorPlan of the event")
    shift: Shift = Field(..., alias="Shift", name="Shift", description="Shift of the event")


class Event(BaseModel):
    """Event Class"""

    category: str = Field(
        ...,
        alias="Category",
        name="Event Category",
        description="Category of the event",
        example="TableEvent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    content: Content = Field(..., alias="Content", name="Content", description="Content of the event")
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Last Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2023-05-17T10:39:21.9281179-07:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    server_last_update: datetime = Field(
        ...,
        alias="ServerLastUpdate",
        name="Server Last Update",
        description="Server last update timestamp of the event, in ISO 8601 format",
        example="2023-05-17T17:39:44.623+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sync_source: str = Field(
        ...,
        alias="SyncSource",
        name="Synchronization source",
        description="Sync source of the event",
        example="Backoffice",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="Type",
        name="Event Type",
        description="Type of TableEvent.",
        example="TableClosed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    uid: str = Field(
        ...,
        alias="UID",
        name="Unique Identifier",
        description="Globally unique identifier of the event",
        example="99999999-0464-408f-ade8-18c10655913a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    version: int = Field(
        ...,
        alias="Version",
        name="Event Version",
        description="Version of the event.",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeTablesEventsModel(BaseModel):
    """DineTimeTablesEventsModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Tables Events Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Tables Events Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    events: List[Event] = Field(..., alias="Events", name="Events", description="Set of events.")
    more_data: bool = Field(
        ...,
        alias="MoreData",
        name="More Data Flag",
        description="Indicates if event has more data with same site identifier.",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    download_cutoff: datetime = Field(
        ...,
        alias="DownloadCutoff",
        name="Download Cutoff",
        description="Download cutoff timestamp of the event, in ISO 8601 format",
        example="2023-05-17T18:19:48.186+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Globally unique identifier of the site",
        example="99999999-5d47-4bad-bee8-3143dcc1f7c9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
