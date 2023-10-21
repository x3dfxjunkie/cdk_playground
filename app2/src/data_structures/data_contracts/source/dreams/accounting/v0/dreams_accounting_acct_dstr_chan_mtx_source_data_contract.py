"""Source Data Contract for DREAMS Account Distribution Channel Matrix"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Account Distribution Channel Matrix Data"""

    acct_dstr_chan_mtrx_id: int = Field(
        ...,
        alias="ACCT_DSTR_CHAN_MTRX_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_dstr_chan_nm: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_NM",
        name="",
        description="",
        example="Group Sales",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_chan_nm: str = Field(
        ...,
        alias="SLS_CHAN_NM",
        name="",
        description="",
        example="Groups and Conventions",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comnctn_chan_nm: str = Field(
        ...,
        alias="COMNCTN_CHAN_NM",
        name="",
        description="",
        example="Contact Center",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dstr_chan_mtrx_strt_dt: datetime = Field(
        ...,
        alias="ACCT_DSTR_CHAN_MTRX_STRT_DT",
        name="",
        description="",
        example="1980-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dstr_chan_mtrx_end_dt: datetime = Field(
        ...,
        alias="ACCT_DSTR_CHAN_MTRX_END_DT",
        name="",
        description="",
        example="2020-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dstr_chan_mtrx_actv_in: str = Field(
        ...,
        alias="ACCT_DSTR_CHAN_MTRX_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T19:46:52.470Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T19:46:52.470Z",
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


class DREAMSAccountingAcctDstrChanMtxModel(BaseModel):
    """Payload class for DREAMSAccountingAcctDstrChanMtxModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Distribution Channel Matrix"
        stream_name = ""
        description = """This field maps reservation sales and communication channels to a SAP channel"""
        unique_identifier = ["data.ACCT_DSTR_CHAN_MTRX_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_DSTR_CHAN_MTX"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
