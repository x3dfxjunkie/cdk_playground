"""Source Data Contract for CME DLR Audit Inventory Bucket By Date Time"""


from __future__ import annotations

from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class for CME Audit Inventory Bucket by Date Time data"""

    audit_action: str = Field(
        ...,
        alias="audit_action",
        name="",
        description="",
        example="UPDATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_on: Optional[datetime] = Field(
        None,
        alias="created_on",
        name="",
        description="",
        example="2022-01-10T14:28:12Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_usr: Optional[str] = Field(
        None,
        alias="created_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    curr_inventory: Optional[int] = Field(
        None,
        alias="curr_inventory",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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
    has_override: Optional[int] = Field(
        None,
        alias="has_override",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=56424,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    inv_bucket_id: str = Field(
        ...,
        alias="inv_bucket_id",
        name="",
        description="",
        example="DLR_CA_B_VISTA_19_00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    inv_date: date = Field(
        ...,
        alias="inv_date",
        name="",
        description="",
        example="2023-07-21",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: Optional[int] = Field(
        None,
        alias="is_active",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_reservable: Optional[int] = Field(
        None,
        alias="is_reservable",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="",
        description="",
        example="2022-03-01T08:12:04Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_inventory: Optional[int] = Field(
        None,
        alias="max_inventory",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    record_id: int = Field(
        ...,
        alias="record_id",
        name="",
        description="",
        example=14577,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    soft_inventory_limit: Optional[int] = Field(
        None,
        alias="soft_inventory_limit",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    time_zone: Optional[str] = Field(
        None,
        alias="time_zone",
        name="",
        description="",
        example="America/Los_Angeles",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    update_usr: str = Field(
        ...,
        alias="update_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRAuditInvBucketDateTimeModel(BaseModel):
    """Payload class for CMEWDWAuditInvBucketDateTimeModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Audit Inventory Bucket by Date Time"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "audit_inv_bucket_date_time"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
