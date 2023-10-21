"""Source Data Contract for DREAMS Payment Method Number Range"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Payment Method Number Range Data"""

    pmt_meth_nb_rnge_id: int = Field(
        ...,
        alias="PMT_METH_NB_RNGE_ID",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_id: int = Field(
        ...,
        alias="PMT_METH_ID",
        name="",
        description="",
        example=10001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_rnge_st_nb: str = Field(
        ...,
        alias="PMT_METH_RNGE_ST_NB",
        name="",
        description="",
        example="4200000000000000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_rnge_end_nb: str = Field(
        ...,
        alias="PMT_METH_RNGE_END_NB",
        name="",
        description="",
        example="4999999999999999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_nb_rnge_strt_dt: datetime = Field(
        ...,
        alias="PMT_METH_NB_RNGE_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_nb_rnge_end_dt: datetime = Field(
        ...,
        alias="PMT_METH_NB_RNGE_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
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
        example="2010-01-20T06:46:57.893Z",
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
        example="2010-01-20T06:46:57.893Z",
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


class DREAMSAccountingPmtMethNbRngeModel(BaseModel):
    """Payload class for DREAMSAccountingPmtMethNbRngeModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment Method Number Range"
        stream_name = ""
        description = """Payment Method tied to a starting number and ending number for a specific time frame"""
        unique_identifier = ["data.PMT_METH_NB_RNGE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT_METH_NB_RNGE"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
