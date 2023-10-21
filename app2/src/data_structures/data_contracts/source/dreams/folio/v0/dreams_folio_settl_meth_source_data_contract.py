"""Source Data Contract for Dreams Folio Settlement Method"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Dreams Folio Settlement Method Data"""

    chg_priv_in: str = Field(
        ...,
        alias="CHG_PRIV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-24T11:21:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    incdntl_in: str = Field(
        ...,
        alias="INCDNTL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_cls_nm: str = Field(
        ...,
        alias="JDO_CLS_NM",
        name="",
        description="",
        example="SettlementMethod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_id: Optional[str] = Field(
        None,
        alias="PMT_ID",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_nm: str = Field(
        ...,
        alias="PMT_METH_NM",
        name="",
        description="",
        example="Cash",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_typ_nm: str = Field(
        ...,
        alias="PMT_METH_TYP_NM",
        name="",
        description="",
        example="Cash",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_actv_in: str = Field(
        ...,
        alias="SETTL_METH_ACTV_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_create_dt: datetime = Field(
        ...,
        alias="SETTL_METH_CREATE_DT",
        name="",
        description="",
        example="2023-08-24T11:21:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_end_dt: Optional[datetime] = Field(
        None,
        alias="SETTL_METH_END_DT",
        name="",
        description="",
        example="0028-02-29T13:10:31Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_id: int = Field(
        ...,
        alias="SETTL_METH_ID",
        name="",
        description="",
        example=435034849,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_inactv_dts: Optional[datetime] = Field(
        None,
        alias="SETTL_METH_INACTV_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_strt_dt: Optional[str] = Field(
        None,
        alias="SETTL_METH_STRT_DT",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-24T11:21:24.093000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSettlMethModel(BaseModel):
    """Payload class for DREAMSFolioSettlMethModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Settlement Method"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.SETTL_METH_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SETTL_METH"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
