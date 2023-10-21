"""Source Data Contract for Dreams Guest Link EXPRNC_MEDIA"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Guest Link EXPRNC_MEDIA Data"""

    exprnc_media_id: int = Field(
        ...,
        alias="exprnc_media_id",
        name="",
        description="",
        example=1234567890,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gst_lnk_id: int = Field(
        ...,
        alias="GST_LNK_ID",
        name="",
        description="",
        example=1234567890,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_media_typ_nm: str = Field(
        ...,
        alias="EXPRNC_MEDIA_TYP_NM",
        name="",
        description="",
        example="XBAND",
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-15T04:00:54.673-05:00",
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
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-15T04:00:54.673-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestLinkExprncMediaModel(BaseModel):
    """Payload class for DREAMSGuestLinkExprncMediaModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Media"
        stream_name = ""
        description = """This table associates the experience media ID with the guest link ID by Media Type: EXPRNC_MEDIA_TYP_NM
        XBAND
        MAG_PLUS_RFID_CARD
        RFID_ONLY_CARD"""
        unique_identifier = ["data.exprnc_media_id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_media"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
