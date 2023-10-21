"""Source Data Contract for DREAMS Post Account"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Post Account Data"""

    pst_acct_id: int = Field(
        ...,
        alias="PST_ACCT_ID",
        name="",
        description="",
        example=20001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_acct_typ_nm: str = Field(
        ...,
        alias="PST_ACCT_TYP_NM",
        name="",
        description="",
        example="Posting Item",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_acct_nm: str = Field(
        ...,
        alias="PST_ACCT_NM",
        name="",
        description="",
        example="Accounts Receivable Whsl Pkg Adjustment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ui_dspl_seq_nb: int = Field(
        ...,
        alias="UI_DSPL_SEQ_NB",
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
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T05:52:22.552Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5a_S1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-04-30T18:13:21.427Z",
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


class DREAMSAccountingPstAcctModel(BaseModel):
    """Payload class for DREAMSAccountingPstAcctModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Post Account"
        stream_name = ""
        description = """The post account type associated to the post account name
Posting Item
Payment Method"""
        unique_identifier = ["data.PST_ACCT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PST_ACCT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
