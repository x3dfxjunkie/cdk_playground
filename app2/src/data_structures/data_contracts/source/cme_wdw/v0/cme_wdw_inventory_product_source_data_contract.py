"""Source Data Contract for CME WDW Inventory Product"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)


class Data(BaseModel):
    """Class for CME Inventory Product Data"""

    id: str = Field(
        ...,
        alias="id",
        name="Inventory Product Identifier",
        description="Identifier that identifies a CME inventory product",
        example="WDW_MEPBONUS",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    name: str = Field(
        ...,
        alias="name",
        name="Inventory Product Name",
        description="Inventory Product Name",
        example="MEP Bonus Allocations",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    destination_id: str = Field(
        ...,
        alias="destination_id",
        name="Destination Identifier",
        description="Specifies destination for the corresponding inventory product",
        example="WDW",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    category_id: str = Field(
        ...,
        alias="category_id",
        name="Inventory Product Category Identifier",
        description="Specifies the category for the corresponding inventory product",
        example="MEPBONUS",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    percent_of_capacity_target: Optional[int] = Field(
        None,
        alias="percent_of_capacity_target",
        name="Percent of Capacity Target",
        description="TBD",
        example=1,
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
    created_usr: Optional[str] = Field(
        None,
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


class CMEWDWInventoryProductModel(BaseModel):
    """CME Inventory Product Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Product"
        stream_name = ""  # info not available yet
        description = "Inventory Products designated for Park Reservations"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "inventory_product"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
