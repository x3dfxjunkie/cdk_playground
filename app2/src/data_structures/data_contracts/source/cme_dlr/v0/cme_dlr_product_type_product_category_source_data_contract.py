"""Source Data Contract Template for CME DLR Product Category and Product Type"""


from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for CME Product Category and Product Type data"""

    product_type_id: str = Field(
        ...,
        alias="product_type_id",
        name="",
        description="",
        example="ap",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_category_id: str = Field(
        ...,
        alias="product_category_id",
        name="",
        description="",
        example="AP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: int = Field(
        ...,
        alias="is_active",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_comp_ticket: int = Field(
        ...,
        alias="is_comp_ticket",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_park_hopper: int = Field(
        ...,
        alias="is_park_hopper",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    has_blockout: int = Field(
        ...,
        alias="has_blockout",
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
        example="2020-06-05T12:38:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    update_usr: Optional[str] = Field(
        None,
        alias="update_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_usr: Optional[str] = Field(
        None,
        alias="created_usr",
        name="",
        description="",
        example="MOUSM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_on: Optional[datetime] = Field(
        None,
        alias="created_on",
        name="",
        description="",
        example="2021-07-07T15:11:57Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRProductTypeProductCategoryModel(BaseModel):
    """Payload class for CMEDLRProductTypeProductCategoryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Product Type Product Category"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.product_type_id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "product_type_product_category"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
