"""Source Data Contract Template for DREAMS Pricing Tax Type"""


from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_TYP_T Data"""

    tax_juris_id: int = Field(
        ...,
        alias="TAX_JURIS_ID",
        name="",
        description="",
        example=80000443,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_tbl_max_amt: Optional[int] = Field(
        None,
        alias="TAX_TBL_MAX_AMT",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_tbl_min_amt: Optional[int] = Field(
        None,
        alias="TAX_TBL_MIN_AMT",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_tbl_pc: Optional[int] = Field(
        None,
        alias="TAX_TBL_PC",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_typ_ds: Optional[str] = Field(
        None,
        alias="TAX_TYP_DS",
        name="",
        description="",
        example="Tax Tables for Indian River County Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_typ_id: int = Field(
        ...,
        alias="TAX_TYP_ID",
        name="",
        description="",
        example=77618,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_typ_nm: str = Field(
        ...,
        alias="TAX_TYP_NM",
        name="",
        description="",
        example="Indian River County Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    use_tax_tbl_in: int = Field(
        ...,
        alias="USE_TAX_TBL_IN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_by_prod_loc_in: int = Field(
        ...,
        alias="VAR_BY_PROD_LOC_IN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxTypTModel(BaseModel):
    """Payload class for DREAMSPriceTaxTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Tax Type"
        stream_name = ""
        description = """A classification of taxes for certain jurisdictions. A jurisdiction may have more than one tax type defined for it."""
        unique_identifier = ["data.TAX_TYP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
