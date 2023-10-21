"""Source Data Contract Template for DREAMS Price - Product Type data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_typ_t Data"""

    entrprs_prod_typ_id: int = Field(
        ...,
        alias="ENTRPRS_PROD_TYP_ID",
        name="",
        description="",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_typ_nm: str = Field(
        ...,
        alias="PROD_TYP_NM",
        name="",
        description="",
        example="ShowDiningProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdTypTModel(BaseModel):
    """Payload class for DREAMSPriceProdTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Identifies the subtype of the product.  For example, PACKAGE PRODUCT or COMPONENT PRODUCT. On the physical side, JDO numbers are used.  See examples below:"""
        unique_identifier = ["data.PROD_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
