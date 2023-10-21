"""Source Data Contract Template for DREAMS Bank Deposit"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Bank Deposit Data"""

    bank_dpst_id: int = Field(
        ...,
        alias="BANK_DPST_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_id: int = Field(
        ...,
        alias="BANK_IN_ID",
        name="",
        description="",
        example=2383075,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_dpst_typ_nm: str = Field(
        ...,
        alias="BANK_DPST_TYP_NM",
        name="",
        description="",
        example="LATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_dpst_acct_dt: datetime = Field(
        ...,
        alias="BANK_DPST_ACCT_DT",
        name="",
        description="",
        example="2011-01-25T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dpst_bag_id: str = Field(
        ...,
        alias="DPST_BAG_ID",
        name="",
        description="",
        example="42803",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_dpst_dts: datetime = Field(
        ...,
        alias="BANK_DPST_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:33.193Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cash_dpst_am: float = Field(
        ...,
        alias="CASH_DPST_AM",
        name="",
        description="",
        example=-63.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    csh_dpst_crncy_cd: str = Field(
        ...,
        alias="CSH_DPST_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    frgn_dpst_am: Optional[int] = Field(
        None,
        alias="FRGN_DPST_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    frgn_dpst_crncy_cd: Optional[str] = Field(
        None,
        alias="FRGN_DPST_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_off_dt: Optional[datetime] = Field(
        None,
        alias="WRK_OFF_DT",
        name="",
        description="",
        example="2011-01-25T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="HITSJ001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="HITSJ001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
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


class DREAMSFolioBankDpstModel(BaseModel):
    """Payload class for DREAMSFolioBankDpstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bank Deposit"
        stream_name = ""
        description = (
            """This table provides information regarding a front desk cashier deposit at the end of their shift"""
        )
        unique_identifier = ["data.BANK_DPST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BANK_DPST"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
