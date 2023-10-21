"""Source Data Contract for DLR CME Park"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class data"""

    id: str = Field(
        ...,
        alias="id",
        name="Park Identifier",
        description="Identifiers park by a CME internal identifier",
        example="WDW_MK",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    name: str = Field(
        ...,
        alias="name",
        name="Park Name",
        description="Identifiers park by CME internal name",
        example="Magic Kingdom",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    destination_id: str = Field(
        ...,
        alias="destination_id",
        name="Destination Identifier",
        description="Identifiers destination by CME internal destination ID",
        example="WDW",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    max_capacity: int = Field(
        ...,
        alias="max_capacity",
        name="Maximum Capacity",
        description="Defines maximum capacity for the specific park",
        example=10000,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    percent_max_target: int = Field(
        ...,
        alias="percent_max_target",
        name="Percent Max Target",
        description="TBD",
        example=10,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
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
    update_usr: Optional[str] = Field(
        None,
        alias="update_usr",
        name="Update User",
        description="Application/User who last updated the record",
        example="pending-job-processor",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRParkModel(BaseModel):
    """CME Park Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Park"
        stream_name = ""  # info not available yet
        description = "Internal lookup table for Park ID/Name"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "park"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
