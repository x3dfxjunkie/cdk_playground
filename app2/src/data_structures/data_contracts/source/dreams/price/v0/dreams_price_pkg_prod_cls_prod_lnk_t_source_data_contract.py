"""Source Data Contract Template for DREAMS Price - Package Product Class Product Link"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - PKG_PROD_CLS_PROD_LNK_T Data"""

    pkg_prod_cls_id: int = Field(
        ...,
        alias="PKG_PROD_CLS_ID",
        name="",
        description="",
        example=758992,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-25T20:35:22.703832Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_id: int = Field(
        ...,
        alias="PROD_LNK_ID",
        name="",
        description="",
        example=1275656,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePkgProdClsProdLnkTModel(BaseModel):
    """Payload class for DREAMSPricePkgProdClsProdLnkTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Package Product Class Product Link"
        stream_name = ""
        description = """This table provides the IDs to associate the package to product classification and the product link table"""
        unique_identifier = ["data.PKG_PROD_CLS_ID", "data.PROD_LNK_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_PROD_CLS_PROD_LNK_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
