"""Source Data Contract for DREAMS Reporting Category"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Reporting Category Data"""

    rpt_ctgy_id: int = Field(
        ...,
        alias="RPT_CTGY_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_nm: str = Field(
        ...,
        alias="RPT_CTGY_NM",
        name="",
        description="",
        example="Z_Acma Florida Symposium",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_cd: str = Field(
        ...,
        alias="RPT_CTGY_CD",
        name="",
        description="",
        example="64",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_strt_dt: datetime = Field(
        ...,
        alias="RPT_CTGY_STRT_DT",
        name="",
        description="",
        example="2007-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_end_dt: datetime = Field(
        ...,
        alias="RPT_CTGY_END_DT",
        name="",
        description="",
        example="2009-12-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rpt_ctgy_dspl_seq_nb: int = Field(
        ...,
        alias="RPT_CTGY_DSPL_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILIOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-12-07T16:33:39.614Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingRptCtgyModel(BaseModel):
    """Payload class for DREAMSAccountingRptCtgyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reporting Category"
        stream_name = ""
        description = """Only one reporting category is still active this might be phased out"""
        unique_identifier = ["data.RPT_CTGY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "RPT_CTGY"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
