"""Source Data Contract Template for DREAMS Price - Feature Frequency Data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - feat_frq_t Data"""

    feat_frq_nm: str = Field(
        ...,
        alias="FEAT_FRQ_NM",
        name="",
        description="",
        example="Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeatFrqTModel(BaseModel):
    """Payload class for DREAMSPriceFeatFrqTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """How often a Feature may be enjoyed by the guest."""
        unique_identifier = ["data.FEAT_FRQ_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FEAT_FRQ_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
