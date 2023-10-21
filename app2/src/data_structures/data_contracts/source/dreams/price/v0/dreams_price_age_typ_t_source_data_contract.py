"""Source Data Contract Template for DREAMS Price - AGE TYPE"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - AGE_TYP Data"""

    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="",
        description="",
        example="Infant",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceAgeTypTModel(BaseModel):
    """Payload class for DREAMSPriceAgeTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """An age bracket used for segmenting guests regardless of product chosen."""
        unique_identifier = ["data.AGE_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "AGE_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
