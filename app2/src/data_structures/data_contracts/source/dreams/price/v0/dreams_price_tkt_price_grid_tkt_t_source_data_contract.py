"""Source Data Contract for DREAMS Ticket Price Grid Ticket"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Ticket Price Grid Ticket Data"""

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

    tkt_id: int = Field(
        ...,
        alias="TKT_ID",
        name="",
        description="",
        example=857662,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_price_grid_id: int = Field(
        ...,
        alias="TKT_PRICE_GRID_ID",
        name="",
        description="",
        example=299558,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTktPriceGridTktTModel(BaseModel):
    """Payload class for DREAMSPriceTktPriceGridTktTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Ticket Price Grid Ticket"
        stream_name = ""
        description = "Ties ticket ID to the Price Grid ID"  # optional
        unique_identifier = ["data.TKT_ID", "data.TKT_PRICE_GRID_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "TKT_PRICE_GRID_TKT_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
