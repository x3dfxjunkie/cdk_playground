"""Source Data Contract Template for DREAMS Price - Tax Table data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_TBL_T Data"""

    ds: str = Field(
        ...,
        alias="DS",
        name="",
        description="",
        example="Osceola County 7.0% Tax Table for 2003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_tbl_id: int = Field(
        ...,
        alias="TAX_TBL_ID",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxTblTModel(BaseModel):
    """Payload class for DREAMSPriceTaxTblTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A set of taxes as they would appear on a tax card."""
        unique_identifier = ["data.TAX_TBL_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_TBL_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
