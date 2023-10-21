"""Source Data Contract Template for DREAMS Price - Tax Group/Type data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_GRP_TAX_TYP_T Data"""

    tax_grp_id: int = Field(
        ...,
        alias="TAX_GRP_ID",
        name="",
        description="",
        example=80007254,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_grp_tax_typ_pc: float = Field(
        ...,
        alias="TAX_GRP_TAX_TYP_PC",
        name="",
        description="",
        example=0.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_typ_id: int = Field(
        ...,
        alias="TAX_TYP_ID",
        name="",
        description="",
        example=80007067,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxGrpTaxTypTModel(BaseModel):
    """Payload class for DREAMSPriceTaxGrpTaxTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The Tax Types associated with a Tax Group and percentage."""
        unique_identifier = ["data.TAX_GRP_ID", "data.TAX_TYP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_GRP_TAX_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
