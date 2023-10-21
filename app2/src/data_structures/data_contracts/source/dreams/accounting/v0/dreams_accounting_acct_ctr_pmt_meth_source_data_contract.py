"""Source Data Contract for DREAMS Account Center Payment Method"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Center Payment Method Data"""

    acct_ctr_pmt_meth_id: int = Field(
        ...,
        alias="ACCT_CTR_PMT_METH_ID",
        name="",
        description="",
        example=7031,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_nb: Optional[str] = Field(
        None,
        alias="CC_MRCHT_NB",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mkt_indctn_cd: Optional[str] = Field(
        None,
        alias="MKT_INDCTN_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_drop_cd: Optional[str] = Field(
        None,
        alias="BANK_DROP_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_id: int = Field(
        ...,
        alias="PMT_METH_ID",
        name="",
        description="",
        example=10005,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_seq_nb: int = Field(
        ...,
        alias="RFND_SEQ_NB",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_dly_dy_cn: Optional[int] = Field(
        None,
        alias="RFND_DLY_DY_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    min_sty_dy_cn: int = Field(
        ...,
        alias="MIN_STY_DY_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cr_wroff_max_am: int = Field(
        ...,
        alias="CR_WROFF_MAX_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cr_wroff_max_crncy_cd: str = Field(
        ...,
        alias="CR_WROFF_MAX_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_proc_req_in: str = Field(
        ...,
        alias="BANK_IN_PROC_REQ_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    till_req_in: str = Field(
        ...,
        alias="TILL_REQ_IN",
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
        example="2010-06-18T18:25:30.421Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC6_S1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-06-18T18:25:30.421Z",
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
    prtl_auth_in: str = Field(
        ...,
        alias="PRTL_AUTH_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctCtrPmtMethModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrPmtMethModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Payment Method"
        stream_name = ""
        description = (
            """This table has IDs and information related to the account center and the payment methods for them"""
        )
        unique_identifier = ["data.ACCT_CTR_PMT_METH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR_PMT_METH"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
