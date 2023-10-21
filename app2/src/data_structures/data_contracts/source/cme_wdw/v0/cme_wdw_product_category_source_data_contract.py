"""Source Data Contract Template for CME WDW Product Category"""


from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)

from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for CME Product Category data"""

    created_on: Optional[datetime] = Field(
        None,
        alias="created_on",
        name="",
        description="",
        example="2021-05-06T17:10:11Z",
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
    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="AP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    # last_updated: datetime = Field(
    #     ...,
    #     alias="last_updated",
    #     name="",
    #     description="",
    #     example="2021-05-06T17:10:11Z",
    #     guest_identifier=False,
    #     transaction_identifier=False,
    #     identifier_tag="",
    # )
    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Annual Pass",
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


class CMEWDWProductCategoryModel(BaseModel):
    """Payload class for CMEWDWProductCategoryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Product Category"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "product_category"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
