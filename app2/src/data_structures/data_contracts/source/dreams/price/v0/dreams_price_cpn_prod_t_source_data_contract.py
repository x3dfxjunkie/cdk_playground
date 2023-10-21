"""Source Data Contract Template for DREAMS Price - Coupon Product"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - CPN_PROD_T Data"""

    cpn_cd: str = Field(
        ...,
        alias="CPN_CD",
        name="",
        description="",
        example="TS",
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

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=4585,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceCpnProdTModel(BaseModel):
    """Payload class for DREAMSPriceCpnProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PROD_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_PROD_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
