"""Source Data Contract for DREAMS Accounting Account Center Post Account"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Accounting - ACCT_CTR_PST_ACCT Data"""

    acct_ctr_pst_acct_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_ID",
        name="",
        description="",
        example=2097700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=178300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_id: Optional[int] = Field(
        None,
        alias="CHRG_ACCT_CTR_ID",
        name="",
        description="",
        example=222600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_acct_strt_dt: datetime = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_STRT_DT",
        name="",
        description="",
        example="2023-06-13T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_acct_end_dt: datetime = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_END_DT",
        name="",
        description="",
        example="2099-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_acct_dspl_seq_nb: int = Field(
        ...,
        alias="ACCT_CTR_PST_ACCT_DSPL_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-13T16:17:24.266000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-13T16:17:24.266000Z",
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
    jdo_cls_nb: int = Field(
        ...,
        alias="JDO_CLS_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctCtrPstAcctModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrPstAcctModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Post Account"
        stream_name = ""
        description = "This table contains the association of the post account start and end dates for the account center and charge account center"
        unique_identifier = ["data.ACCT_CTR_PST_ACCT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "acct_ctr_pst_acct"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
