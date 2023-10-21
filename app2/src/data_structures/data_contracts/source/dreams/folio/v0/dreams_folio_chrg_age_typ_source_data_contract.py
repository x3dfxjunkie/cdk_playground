"""Source Data Contract Template for CHRG_AGE_TYP.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_AGE_TYP"""

    chrg_age_typ_id: int = Field(
        ...,
        alias="CHRG_AGE_TYP_ID",
        name="",
        description="",
        example=1366654952,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="",
        description="",
        example="Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_id: int = Field(
        ...,
        alias="CHRG_ID",
        name="",
        description="",
        example=3406863669,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_age_typ_cn: int = Field(
        ...,
        alias="CHRG_AGE_TYP_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ROGEB054",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-04T10:06:57.257000Z",
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


class DREAMSFolioChrgAgeTypModel(BaseModel):
    """Payload class for DREAMSFolioChrgAgeTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Age Type"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_AGE_TYP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_AGE_TYP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
