"""Source Data Contract for DREAMS Ticket Feature"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Ticket Feature Data"""

    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=73634,
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

    tkt_id: int = Field(
        ...,
        alias="TKT_ID",
        name="",
        description="",
        example=8596,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTktFeatTModel(BaseModel):
    """Payload class for DREAMSPriceTktFeatTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Ticket Feature"
        stream_name = ""
        description = "Features of a Ticket"  # optional
        unique_identifier = ["data.TKT_ID", "data.FEAT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "TKT_FEAT_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
