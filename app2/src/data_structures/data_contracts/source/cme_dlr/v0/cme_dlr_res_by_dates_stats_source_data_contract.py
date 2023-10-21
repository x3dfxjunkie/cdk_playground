"""Source Data Contract for CME DLR Res by Dates Stats"""
from __future__ import annotations
from datetime import date, datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class data"""

    id: str = Field(
        ...,
        alias="id",
        name="Record Identifier",
        description="Identifies a specific Reservation by Dates Statistic Record",
        example="22201111",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    inv_bucket_id: str = Field(
        ...,
        alias="inv_bucket_id",
        name="Inventory Bucket Identifier",
        description="Identifier to a specific reservation inventory bucket ",
        example="WDW_MK_AP_DAILY",
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
    res_date: date = Field(
        ...,
        alias="res_date",
        name="Reservation Date",
        description="Date which the reservation was made",
        example="2022-11-24",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    activity_date: date = Field(
        ...,
        alias="activity_date",
        name="Activity Date",
        description="Date which the reservation is valid for",
        example="2022-11-24",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="Last Updated",
        description="Date/time which the reservation statistics record was last updated",
        example="2023-04-21T11:35:13Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    facility_id: str = Field(
        ...,
        alias="facility_id",
        name="Facility Identifier",
        description="Internal facility identifier to designate a location used within CME.  Does not equate to Facility Enterprise ID",
        example="WDW_AK",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    slot: str = Field(
        ...,
        alias="slot",
        name="Experience Time Slot",
        description="Time slot representing reservations by date statistics.  Ex: Daily (full day) or half",
        example="DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_reservations: int = Field(
        ...,
        alias="num_reservations",
        name="Number of Reservations",
        description="Number of reservations per inventory bucket on a specific activity and reservation date to a specific time slot and reservation status",
        example=15,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_guests: int = Field(
        ...,
        alias="num_guests",
        name="Number of Guests",
        description="Number of guests per inventory bucket on a specific activity and reservation date to a specific time slot and reservation status",
        example=15,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRResByDatesStatsModel(BaseModel):
    """CME Reservation By Dates Statistics Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation By Dates Statistics"
        stream_name = ""  # info not available yet
        description = "Reservation By Dates Statistics providing aggregated reservation counts by a specific date for a given slot/location"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_by_dates_stats"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
