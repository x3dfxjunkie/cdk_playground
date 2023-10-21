"""Source Data Contract Template for DREAMS Price - Tax Group data"""


from __future__ import annotations

# from typing import List
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_GRP_T Data"""

    tax_grp_ds: Optional[str] = Field(
        None,
        alias="TAX_GRP_DS",
        name="",
        description="",
        example="For use with accommodations in Hawaii",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_grp_id: int = Field(
        ...,
        alias="TAX_GRP_ID",
        name="",
        description="",
        example=364826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_grp_nm: str = Field(
        ...,
        alias="TAX_GRP_NM",
        name="",
        description="",
        example="Hawaii Resorts Accommodations Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxGrpTModel(BaseModel):
    """Payload class for DREAMSPriceTaxGrpTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A collection of tax types that can be reused for products."""
        unique_identifier = ["data.TAX_GRP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_GRP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
