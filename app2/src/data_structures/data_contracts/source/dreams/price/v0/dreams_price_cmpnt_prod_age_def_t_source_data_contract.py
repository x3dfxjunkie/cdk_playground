"""Source Data Contract Template for CMPNT_PROD_AGE_DEF"""


from __future__ import annotations
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - CMPNT_PROD_AGE_DEF Data"""

    age_def_id: int = Field(
        ...,
        alias="AGE_DEF_ID",
        name="",
        description="",
        example=15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=162498,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceCmpntProdAgeDefTModel(BaseModel):
    """Payload class for DREAMSPriceCmpntProdAgeDefTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Component Product Age Definition"
        stream_name = ""
        description = "Ties the age definition ID to the product ID"  # optional
        unique_identifier = ["data.AGE_DEF_ID", "data.PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CMPNT_PROD_AGE_DEF_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
