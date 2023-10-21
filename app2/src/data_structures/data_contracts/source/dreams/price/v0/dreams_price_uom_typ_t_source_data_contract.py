"""Source Data Contract Template for DREAMS Price - Unit of Measurement Type data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - UOM_TYP_T Data"""

    uom_typ_nm: str = Field(
        ...,
        alias="UOM_TYP_NM",
        name="",
        description="",
        example="Hour",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceUomTypTModel(BaseModel):
    """Payload class for DREAMSPriceUomTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = (
            """Documents the specific unit values.  For example, second, minute, hour, day, week, month, year."""
        )
        unique_identifier = ["data.UOM_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "UOM_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
