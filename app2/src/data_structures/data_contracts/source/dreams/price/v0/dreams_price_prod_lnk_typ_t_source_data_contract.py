"""Source Data Contract Template for DREAMS Price - Product Link Type data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_lnk_typ_t Data"""

    entrprs_prod_lnk_typ_id: int = Field(
        ...,
        alias="ENTRPRS_PROD_LNK_TYP_ID",
        name="",
        description="",
        example=80000361,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_typ_nm: str = Field(
        ...,
        alias="PROD_LNK_TYP_NM",
        name="",
        description="",
        example="Add On",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdLnkTypTModel(BaseModel):
    """Payload class for DREAMSPriceProdLnkTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The purpose of the association of one SKU to another as in the case of Associating a discontinued SKU with the SKU or SKUs that it replaces."""
        unique_identifier = ["data.PROD_LNK_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_LNK_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
