"""Source Data Contract for DREAMS Product Price Grid"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Price Grid Data"""

    cmpnt_prod_id: int = Field(
        ...,
        alias="CMPNT_PROD_ID",
        name="",
        description="",
        example=106239,
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

    price_grid_id: int = Field(
        ...,
        alias="PRICE_GRID_ID",
        name="",
        description="",
        example=9247501,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdPriceGridTModel(BaseModel):
    """Payload class for DREAMSPriceProdPriceGridTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product Price Grid"
        stream_name = ""
        description = "Ties price grid IDs to component product IDs"  # optional
        unique_identifier = ["data.PRICE_GRID_ID", "data.CMPNT_PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_PRICE_GRID_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
