"""Source Data Contract Template for ACM_PROD"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - ACM_PROD Data"""

    acm_prod_id: int = Field(
        ...,
        alias="ACM_PROD_ID",
        name="",
        description="",
        example=56602,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rm_typ_cd: str = Field(
        ...,
        alias="RM_TYP_CD",
        name="",
        description="",
        example="5A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_prod_addl_chg_thrshld_nb: int = Field(
        ...,
        alias="ACM_PROD_ADDL_CHG_THRSHLD_NB",
        name="",
        description="",
        example=5,
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


class DREAMSPriceAcmProdTModel(BaseModel):
    """Payload class for DREAMSPriceAcmProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Product"
        stream_name = ""
        description = "This provides the Accommodation (hotel room, villa, campsite) room type code as well as the threshold for that room when the Accommodation is a double occupancy, the extra guests pay an additional charge per night"  # optional
        unique_identifier = ["data.ACM_PROD_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "ACM_PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
