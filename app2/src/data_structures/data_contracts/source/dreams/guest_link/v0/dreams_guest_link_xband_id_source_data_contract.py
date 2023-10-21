"""Source Data Contract for Dreams Guest Link XBAND_ID"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Guest Link Magic Band Data"""

    xband_id_typ_nm: str = Field(
        ...,
        alias="XBAND_ID_TYP_NM",
        name="",
        description="",
        example="XBMS_XBAND_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_media_id: int = Field(
        ...,
        alias="EXPRNC_MEDIA_ID",
        name="",
        description="",
        example=1234567890,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    xband_id_vl: str = Field(
        ...,
        alias="XBAND_ID_VL",
        name="",
        description="",
        example="A1111222-AAAA-BBBB-CCCC-456DDD1111FD",
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
        example="2023-06-22T09:57:39.850-05:00",
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
        example="2023-06-22T09:57:39.850-05:00",
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


class DREAMSGuestLinkXbandIdModel(BaseModel):
    """Payload class for DREAMSGuestLinkXbandIdModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Magic Band ID"
        stream_name = ""
        description = """This table ties together the experience media ID and the Magic Band ID value: XBAND_ID_TYP_NM
        PUBLIC_LONG_RANGE_ID
        PUBLIC_SHORT_RANGE_ID
        XBMS_XBAND_ID
        VISUAL_ID"""
        unique_identifier = ["data.XBAND_ID_TYP_NM", "data.EXPRNC_MEDIA_ID", "data.XBAND_ID_VL"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "xband_id"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
