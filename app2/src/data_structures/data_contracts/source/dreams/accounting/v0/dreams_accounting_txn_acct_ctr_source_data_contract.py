"""Source Data Contract Dreams Transaction Account Center"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Source Data Contract Dreams Transaction Account Center"""

    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=1412,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chg_acct_enbl_in: str = Field(
        ...,
        alias="CHG_ACCT_ENBL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T01:24:12.866323Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="AAAABBBB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_fc_in: str = Field(
        ...,
        alias="GST_FC_IN",
        name="",
        description="",
        example="N",
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

    prtcpt_in: str = Field(
        ...,
        alias="PRTCPT_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sld_id_vl: Optional[str] = Field(
        None,
        alias="SLD_ID_VL",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=1412,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-16T10:42:04.215000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="AAAA0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingTxnAcctCtrModel(BaseModel):
    """Payload class for Dreams Transaction Account Center"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Account Center"
        stream_name = ""
        description = """Transaction Account Center IDs that are only Transaction Accounts"""
        unique_identifier = ["data.TXN_ACCT_CTR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TXN_ACCT_CTR"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
