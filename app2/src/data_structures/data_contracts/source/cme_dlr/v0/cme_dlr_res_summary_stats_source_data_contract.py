"""Source Data Contract for CME DLR Res Summary Stats"""
from __future__ import annotations
from datetime import datetime
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
        description="Identifies a specific Reservation Summary Statistic Record",
        example="22201111",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    when_reported: datetime = Field(
        ...,
        alias="when_reported",
        name="When Reported",
        description="Date Timestamp of the reservation summary record was reported",
        example="2023-04-21T11:35:13Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    report_period_minutes: int = Field(
        ...,
        alias="report_period_minutes",
        name="Report Period Minutes",
        description="Interval/duration between summary statistics are reported",
        example=5,
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
    facility_id: str = Field(
        ...,
        alias="facility_id",
        name="Facility Identifier",
        description="Internal facility identifier to designate a location used within CME.  Does not equate to Facility Enteprise ID",
        example="WDW_AK",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    slot: str = Field(
        ...,
        alias="slot",
        name="Experience Time Slot",
        description="Time slot representing reservations summary statitics.  Ex: Daily (full day) or half",
        example="DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_res_bookings: int = Field(
        ...,
        alias="num_res_bookings",
        name="Number of Reservation Bookings",
        description="Number of reservations per inventory bucket within the reporting interval/duration",
        example=15,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_confirmations: int = Field(
        ...,
        alias="num_confirmations",
        name="Number of Confirmations",
        description="TBD - Number of confirmations per inventory bucket within the reporting interval/duration",
        example=12,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_res_redemptions: int = Field(
        ...,
        alias="num_res_redemptions",
        name="Number of Reservation Redemptions",
        description="Number of redemptions per inventory bucket within the reporting interval/duration",
        example=35,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_res_cancellations: int = Field(
        ...,
        alias="num_res_cancellations",
        name="Number of Reservation Cancellations",
        description="Number of cancellations per inventory bucket within the reporting interval/duration",
        example=15,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    num_guests: int = Field(
        ...,
        alias="num_guests",
        name="Number of Guests",
        description="Number of guests in reservation per inventory bucket within the reporting interval/duration",
        example=15,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRResSummaryStatsModel(BaseModel):
    """CME Reservation Summary Statistics Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Summary Statistics"
        stream_name = ""  # info not available yet
        description = "Reservation summary counts for a specific inventory bucket/facility"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_summary_stats"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
