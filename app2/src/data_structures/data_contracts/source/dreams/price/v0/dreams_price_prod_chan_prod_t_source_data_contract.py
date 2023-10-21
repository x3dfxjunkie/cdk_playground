"""Source Data Contract for DREAMS Product Channel Product"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Channel Product Data"""

    prod_chan_id: int = Field(
        ...,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=40908,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_prod_end_dt: Optional[datetime] = Field(
        None,
        alias="PROD_CHAN_PROD_END_DT",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_prod_strt_dt: Optional[datetime] = Field(
        None,
        alias="PROD_CHAN_PROD_STRT_DT",
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
        example=54482,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdChanProdTModel(BaseModel):
    """Payload class for DREAMSPriceProdChanProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product Channel Product"
        stream_name = ""
        description = "Ties the Product to the Product Channel"  # optional
        unique_identifier = ["data.PROD_CHAN_ID", "data.PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_CHAN_PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
