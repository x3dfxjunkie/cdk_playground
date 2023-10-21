"""Source Data Contract for CME WDW Inv Bucket"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)


class Data(BaseModel):
    """Class for CME Inv Bucket Data"""

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
    destination_id: str = Field(
        ...,
        alias="destination_id",
        name="Destination Identifier",
        description="Designates destination, such as WDW vs DLR, of the reservation ",
        example="",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    id: str = Field(
        ...,
        alias="id",
        name="Inventory Bucket Identifier",
        description="Identifies which inventory bucket the reservation belongs to",
        example="WDW_MK_AP_DAILY",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    inv_product_id: str = Field(
        ...,
        alias="inv_product_id",
        name="Inventory Product Identifier",
        description="Identifies the inventory Product that groups inventory buckets into specific categories",
        example="WDW_AP",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    is_active: int = Field(
        ...,
        alias="is_active",
        name="Is Active",
        description="is this inventory product active?",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    is_reservable: int = Field(
        ...,
        alias="is_reservable",
        name="Is Reservable",
        description="is this inventory product reservable?",
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
    park_id: str = Field(
        ...,
        alias="park_id",
        name="Park Identifier",
        description="Internal Park ID associated with the Reservation",
        example="WDW_EP",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    percent_of_daily_allocation: int = Field(
        ...,
        alias="percent_of_daily_allocation",
        name="Percent of Daily Allocation",
        description="TBD",
        example=100,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    slot: str = Field(
        ...,
        alias="slot",
        name="Slot Type",
        description="Reservation Slot Type, example: DAILY, HALF",
        example="HALF",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    slot_order: int = Field(
        ...,
        alias="slot_order",
        name="Slot Order",
        description="TBD",
        example=2,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    update_usr: str = Field(
        ...,
        alias="update_usr",
        name="Update User",
        description="Application/User who last updated the record",
        example="pending-job-processor",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    entry_window_start_time: Optional[str] = Field(
        None,
        alias="entry_window_start_time",
        name="Entry Window Start Time",
        description="Defines entry time for the reservation slot",
        example="15:00",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    entry_window_end_time: Optional[str] = Field(
        None,
        alias="entry_window_end_time",
        name="Entry Window End Time",
        description="Defines end time for the reservation slot",
        example="19:00",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEWDWInvBucketModel(BaseModel):
    """Payload class for CME WDW Inventory Bucket"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Bucket"
        stream_name = ""  # info not available yet
        description = "Inventory Bucket indicating reservation groups"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "inv_bucket"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
