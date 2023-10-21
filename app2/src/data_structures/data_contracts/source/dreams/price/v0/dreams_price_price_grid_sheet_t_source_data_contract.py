"""Source Data Contract for DREAMS Price Grid Sheet"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Grid Sheet Data"""

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

    price_grid_id: int = Field(
        ...,
        alias="PRICE_GRID_ID",
        name="",
        description="",
        example=1111484,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_id: int = Field(
        ...,
        alias="PRICE_SHEET_ID",
        name="",
        description="",
        example=11112247,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceGridSheetTModel(BaseModel):
    """Payload class for DREAMSPricePriceGridSheetTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Price Grid Sheet"
        stream_name = ""
        description = "This table ties the Price Grid ID to the Price Sheet ID"  # optional
        unique_identifier = ["data.PRICE_GRID_ID", "data.PRICE_SHEET_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PRICE_GRID_SHEET_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
