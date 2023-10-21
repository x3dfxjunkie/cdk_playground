"""Source Data Contract for DREAMS Price Grid Product Channel"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Grid Product Channel Data"""

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=1000004,
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
        example=1111661,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_prod_chan_end_dt: datetime = Field(
        ...,
        alias="PRICE_GRID_PROD_CHAN_END_DT",
        name="",
        description="",
        example="2035-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_grid_prod_chan_strt_dt: datetime = Field(
        ...,
        alias="PRICE_GRID_PROD_CHAN_STRT_DT",
        name="",
        description="",
        example="2023-08-25T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_id: int = Field(
        ...,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=133615,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceGridProdChanTModel(BaseModel):
    """Payload class for DREAMSPricePriceGridProdChanTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Price Grid Product Channel"
        stream_name = ""
        description = "This table ties together the the product channel ID and the Policy ID"  # optional
        unique_identifier = ["data.PRICE_GRID_ID", "data.PROD_CHAN_ID", "data.PLCY_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PRICE_GRID_PROD_CHAN_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
