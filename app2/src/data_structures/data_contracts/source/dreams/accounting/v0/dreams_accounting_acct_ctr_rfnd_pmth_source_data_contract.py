"""Source Data Contract for DREAMS Account Center Refund Payment Method"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Refund Payment Method Data"""

    acct_ctr_rfnd_pmt_meth_id: int = Field(
        ...,
        alias="ACCT_CTR_RFND_PMT_METH_ID",
        name="",
        description="",
        example=501,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pmt_meth_id: int = Field(
        ...,
        alias="ACCT_CTR_PMT_METH_ID",
        name="",
        description="",
        example=5274,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_pmt_meth_id: int = Field(
        ...,
        alias="RFND_PMT_METH_ID",
        name="",
        description="",
        example=10006,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_rfnd_pmt_meth_in: str = Field(
        ...,
        alias="DFLT_RFND_PMT_METH_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_pmt_meth_seq_nb: int = Field(
        ...,
        alias="RFND_PMT_METH_SEQ_NB",
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
        example="MDMUPD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-03-19T02:11:35.613Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5_SS1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-03-19T02:11:35.613Z",
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


class DREAMSAccountingAcctCtrRfndPmthModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrRfndPmthModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Refund Payment Method"
        stream_name = ""
        description = """This table associates the account center payment method to a refund payment method"""
        unique_identifier = ["data.ACCT_CTR_RFND_PMT_METH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR_RFND_PMTH"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
