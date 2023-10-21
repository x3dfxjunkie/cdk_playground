"""Source Data Contract Template for ADM_PROD"""


from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - ADM_PROD Data"""

    adm_prod_id: int = Field(
        ...,
        alias="ADM_PROD_ID",
        name="",
        description="",
        example=59863,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    adm_dy_vld_cn: int = Field(
        ...,
        alias="ADM_DY_VLD_CN",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    adm_exp_dy_cn: Optional[int] = Field(
        None,
        alias="ADM_EXP_DY_CN",
        name="",
        description="",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    adm_addtnl_ds: Optional[str] = Field(
        None,
        alias="ADM_ADDTNL_DS",
        name="",
        description="",
        example="NOT VALID FOR WATER PARK HOPPING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceAdmProdTModel(BaseModel):
    """Payload class for DREAMSPriceAdmProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Admission Product"
        stream_name = ""
        description = "Provides additional product information for Admission products ie: The number of days the guest tickets is valid for 1,4,3,5,6,2,365,7,9,10,421,450,12,11,0,8,13"  # optional
        unique_identifier = ["data.ADM_PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "ADM_PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
