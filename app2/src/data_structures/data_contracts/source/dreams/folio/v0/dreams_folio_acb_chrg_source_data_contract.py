"""Source Data Contract Template for ACB_CHRG.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for ACB_CHRG"""

    acb_chrg_id: int = Field(
        ...,
        alias="ACB_CHRG_ID",
        name="",
        description="",
        example=3409068428,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_ctgy_id: int = Field(
        ...,
        alias="CHRG_BACK_CTGY_ID",
        name="",
        description="",
        example=18,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_rsn_id: int = Field(
        ...,
        alias="CHRG_BACK_RSN_ID",
        name="",
        description="",
        example=533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_loc_nm: str = Field(
        ...,
        alias="CHRG_BACK_LOC_NM",
        name="",
        description="",
        example="ALC The Edison",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WILLV108",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-12T16:34:10.004000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioAcbChrgModel(BaseModel):
    """Payload class for DREAMSFolioAcbChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Auto Charge Back Charge"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.ACB_CHRG_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACB_CHRG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
