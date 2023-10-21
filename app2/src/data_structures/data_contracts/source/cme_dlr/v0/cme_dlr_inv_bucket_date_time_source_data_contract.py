"""Source Data Contract for CME DLR Inventory Bucket by Date Time"""
from __future__ import annotations
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class for CME Inventory Bucket by Date Time Data"""

    created_on: datetime = Field(
        ...,
        alias="created_on",
        name="Create On",
        description="Record created date timestamp",
        example="2023-01-12 09:06:41.000000",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="Created User",
        description="User or Application that created the record",
        example="MOUSM001",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    curr_inventory: int = Field(
        ...,
        alias="curr_inventory",
        name="Current Inventory",
        description="Current Inventory/Reservation Count for the designated inventory bucket and date",
        example=50,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    entry_window_end_time: Optional[str] = Field(
        None,
        alias="entry_window_end_time",
        name="Entry Window End Time",
        description="Defines end time for the inventory bucket and date",
        example="19:00",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    entry_window_start_time: Optional[str] = Field(
        None,
        alias="entry_window_start_time",
        name="Entry Window Start Time",
        description="Defines entry time for the inventory bucket and date",
        example="15:00",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    id: int = Field(
        ...,
        alias="id",
        name="Inventory Bucket Date Time Identifier",
        description="Unique Identifier to a Inventory bucket on a specific Date",
        example=32258,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    inv_bucket_id: str = Field(
        ...,
        alias="inv_bucket_id",
        name="Inventory Bucket Identifier",
        description="Identifier to a specific Inventory bucket",
        example="WDW_MK_AP_DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    inv_date: date = Field(
        ...,
        alias="inv_date",
        name="Inventory Date",
        description="Designates the date for the specific inventory",
        example="2024-01-05",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    is_active: int = Field(
        ...,
        alias="is_active",
        name="Is Active",
        description="TBD",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    is_reservable: int = Field(
        ...,
        alias="is_reservable",
        name="Is Reservable",
        description="TBD",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="Last Updated",
        description="Record updated Date Timestamp",
        example="2022-12-12 12:09:39.960000",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    max_inventory: int = Field(
        ...,
        alias="max_inventory",
        name="Max Inventory",
        description="Maximum inventory count allowed for a specific inventory bucket and date",
        example=500,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reported_inventory: Optional[int] = Field(
        None,
        alias="reported_inventory",
        name="Reported Inventory",
        description="TBD",
        example=300,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    soft_inventory_limit: int = Field(
        ...,
        alias="soft_inventory_limit",
        name="Soft Inventory Limit",
        description="Soft inventory limit",
        example=450,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    time_zone: str = Field(
        ...,
        alias="time_zone",
        name="Time Zone",
        description="Time zone where the inventory is set",
        example="America/New_York",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    update_usr: str = Field(
        ...,
        alias="update_usr",
        name="Update User",
        description="Application/User who last updated the record",
        example="MOUSM001",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRInvBucketDateTimeModel(BaseModel):
    """CME DLR Inventory Bucket by Date Time Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Bucket by Date Time"
        stream_name = ""  # info not available yet
        description = "Inventory Bucket by Date Time specifying inventory availability per bucket within the specified date/time"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "inv_bucket_date_time"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
