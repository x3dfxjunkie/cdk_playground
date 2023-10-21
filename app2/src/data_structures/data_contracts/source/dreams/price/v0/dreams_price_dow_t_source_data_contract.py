"""Source Data Contract Template for DREAMS Price - DOW"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - DOW Data"""

    dow_cd: str = Field(
        ...,
        alias="DOW_CD",
        name="",
        description="",
        example="Wed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dow_nm: str = Field(
        ...,
        alias="DOW_NM",
        name="",
        description="",
        example="Wednesday",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceDowTModel(BaseModel):
    """Payload class for DREAMSPriceDowTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The time dimension for a day of the week."""
        unique_identifier = ["data.DOW_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "DOW_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
