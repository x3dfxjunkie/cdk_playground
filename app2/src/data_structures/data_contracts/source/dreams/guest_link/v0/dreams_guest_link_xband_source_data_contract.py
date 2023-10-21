"""Source Data Contract for Dreams Guest Link Magic Band"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Guest Link Magic Band"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-02T13:37:21.278744Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_media_id: int = Field(
        ...,
        alias="EXPRNC_MEDIA_ID",
        name="",
        description="",
        example=111111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hf_secur_xband_id: Optional[str] = Field(
        None,
        alias="HF_SECUR_XBAND_ID",
        name="",
        description="",
        example="1111111111111111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mfr_uid: str = Field(
        ...,
        alias="MFR_UID",
        name="",
        description="",
        example="36129626925941252",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-02T13:37:21.278744Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    xband_sec_sts_nm: Optional[str] = Field(
        None,
        alias="XBAND_SEC_STS_NM",
        name="",
        description="",
        example="ORIGINAL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    xband_sts_nm: str = Field(
        ...,
        alias="XBAND_STS_NM",
        name="",
        description="",
        example="ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestLinkXbandModel(BaseModel):

    """Payload Class for Dreams Guest Link Magic Band"""

    class Config:
        """Payload Level Metadata"""

        title = "Magic Band"
        stream_name = ""
        description = """This table ties the following attributes and or IDs to the Experience Media ID: XBAND_STS_NM
ACTIVE
INACTIVE
VOID
XBAND_SEC_STS_NM
BUSINESS_NEED
BUSINESS_NEEDS_CHECKED_OUT
DAMAGED
etc., manufacturer User ID, Experience Card ID, or HF_SECURE_XBAND_ID"""
        unique_identifier = ["data.EXPRNC_MEDIA_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "xband"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
