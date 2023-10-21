"""Source Data Contract Template for DREAMS Folio Travel Agency Commission Rate Specifics"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Travel Agency Commission Rate Specifics Data"""

    comm_rt_spec_id: int = Field(
        ...,
        alias="COMM_RT_SPEC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_id: int = Field(
        ...,
        alias="TRVL_AGCY_ID",
        name="",
        description="",
        example=72572,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rate_typ_nm: str = Field(
        ...,
        alias="RATE_TYP_NM",
        name="",
        description="",
        example="Percentage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ta_comm_rt_vl: int = Field(
        ...,
        alias="TA_COMM_RT_VL",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_spec_create_dt: datetime = Field(
        ...,
        alias="COMM_SPEC_CREATE_DT",
        name="",
        description="",
        example="2002-09-26T04:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_spec_strt_dt: datetime = Field(
        ...,
        alias="COMM_SPEC_STRT_DT",
        name="",
        description="",
        example="2002-09-26T04:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_spec_end_dt: Optional[datetime] = Field(
        None,
        alias="COMM_SPEC_END_DT",
        name="",
        description="",
        example="2099-12-31T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_comm_ds: Optional[str] = Field(
        None,
        alias="TRVL_AGCY_COMM_DS",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366850,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[str] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    all_rev_cls_in: str = Field(
        ...,
        alias="ALL_REV_CLS_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    all_pkg_in: str = Field(
        ...,
        alias="ALL_PKG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-10-13T09:50:09.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="IM775615",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-11-14T19:34:53.066Z",
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


class DREAMSFolioTaCommRtSpecModel(BaseModel):
    """Payload class for DREAMSFolioTaCommRtSpecModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Agency Commission Rate Specifics"
        stream_name = ""
        description = """This table provides the commission  rate information on select reservation components for Travel Agencies"""
        unique_identifier = ["data.COMM_RT_SPEC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TA_COMM_RT_SPEC"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
