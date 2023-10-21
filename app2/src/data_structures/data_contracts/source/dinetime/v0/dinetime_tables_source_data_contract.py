"""Source Data Contract for Dinetime Tables"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


class TableItem(BaseModel):
    """TableItem Class"""

    id: str = Field(
        ...,
        alias="ID",
        name="Table Identifier",
        description="Globally unique identifier of the table",
        example="99999999-8138-4b91-a596-6aa96ebde09f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: bool = Field(
        ...,
        alias="IsActive",
        name="Is Table Active",
        description="Indicates if table stills active.",
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
        example="2022-03-16T17:12:24.951+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    maximum_seat_count: int = Field(
        ...,
        alias="MaximumSeatCount",
        name="Maximum Seat Count",
        description="The maximum number of guests that may be seated at table",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    minimum_seat_count: int = Field(
        ...,
        alias="MinimumSeatCount",
        name="Minimum Seat Count",
        description="The minimum number of guests that may be seated at table",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Table Name",
        description="The table name.",
        example="121",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    seat_count: int = Field(
        ...,
        alias="SeatCount",
        name="Seat Count",
        description="The number of guests seated at the table",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeTablesModel(BaseModel):
    """DineTimeTablesModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Tables Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Tables Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Site Identifier",
        description="Globally unique identifier of the site",
        example="99999999-c5b7-4424-b953-f8aaecaa2aa0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table: List[TableItem] = Field(..., alias="Table", name="Table", description="Table details")
