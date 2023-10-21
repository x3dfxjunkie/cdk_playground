"""Source Data Contract Template for DREAMS Price - Season and Price Sheet Element data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - SEAS_PRICE_SHEET_ELMNT_T Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2017-05-15T14:25:58Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_id: int = Field(
        ...,
        alias="PRICE_SHEET_ELMNT_ID",
        name="",
        description="",
        example=83725828,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seas_id: int = Field(
        ...,
        alias="SEAS_ID",
        name="",
        description="",
        example=17347,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2017-05-15T14:25:58Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSeasPriceSheetElmntTModel(BaseModel):
    """Payload class for DREAMSPriceSeasPriceSheetElmntTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """This is an association table for Season and Price Sheet Element."""
        unique_identifier = ["data.SEAS_ID", "data.PRICE_SHEET_ELMNT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SEAS_PRICE_SHEET_ELMNT_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
