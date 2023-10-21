"""Source Data Contract Template for DREAMS Price - Tax Table Details data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_TBL_DTL_T Data"""

    tax_end_amt: float = Field(
        ...,
        alias="TAX_END_AMT",
        name="",
        description="",
        example=1834.92,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_rt_fee_am: float = Field(
        ...,
        alias="TAX_RT_FEE_AM",
        name="",
        description="",
        example=171.66,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_strt_amt: float = Field(
        ...,
        alias="TAX_STRT_AMT",
        name="",
        description="",
        example=2640.85,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_tbl_id: int = Field(
        ...,
        alias="TAX_TBL_ID",
        name="",
        description="",
        example=1000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxTblDtlTModel(BaseModel):
    """Payload class for DREAMSPriceTaxTblDtlTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The actual tax ranges as they would be on a tax card supplied by the tax jurisdiction."""
        unique_identifier = ["data.TAX_TBL_ID", "data.TAX_STRT_AMT"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_TBL_DTL_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
