"""Source Data Contract for Dreams Account Center"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Account Center"""

    acct_ctr_cd: str = Field(
        ...,
        alias="ACCT_CTR_CD",
        name="",
        description="",
        example="DSPRJCTMO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_dspl_seq_nb: int = Field(
        ...,
        alias="ACCT_CTR_DSPL_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=224100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_nm: str = Field(
        ...,
        alias="ACCT_CTR_NM",
        name="",
        description="",
        example="DS eet",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_acct_ctr_in: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-04T10:09:26.174000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MONTS120",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    db_wroff_max_am: int = Field(
        ...,
        alias="DB_WROFF_MAX_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    db_wroff_max_crncy_cd: str = Field(
        ...,
        alias="DB_WROFF_MAX_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=10460,
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

    req_nm: Optional[str] = Field(
        None,
        alias="REQ_NM",
        name="",
        description="",
        example="PMSR Conversion",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-16T13:24:21.806000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="VOLLH003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctCtrModel(BaseModel):
    """Payload class for Dreams Account Center"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center"
        stream_name = ""
        description = """This table connects an account center to a campus ID and a FAC ID"""
        unique_identifier = ["data.ACCT_CTR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
