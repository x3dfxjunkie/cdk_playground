"""Source Data Contract Template for BANK_IN.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """data for BANK_IN"""

    bank_in_id: int = Field(
        ...,
        alias="BANK_IN_ID",
        name="",
        description="",
        example=27352881,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_acct_dt: datetime = Field(
        ...,
        alias="BANK_IN_ACCT_DT",
        name="",
        description="",
        example="2023-06-11T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_dts: datetime = Field(
        ...,
        alias="BANK_IN_DTS",
        name="",
        description="",
        example="2023-06-11T15:02:09.343000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: int = Field(
        ...,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=10349,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgstr_nb_vl: str = Field(
        ...,
        alias="RGSTR_NB_VL",
        name="",
        description="",
        example="8V651",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_user_id: str = Field(
        ...,
        alias="BANK_IN_USER_ID",
        name="",
        description="",
        example="westn037",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    loc_id: int = Field(
        ...,
        alias="LOC_ID",
        name="",
        description="",
        example=42,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chg_fund_am: int = Field(
        ...,
        alias="CHG_FUND_AM",
        name="",
        description="",
        example=2000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chg_fund_crncy_cd: str = Field(
        ...,
        alias="CHG_FUND_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WESTN037",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-11T15:02:08.986000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WESTN037",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-11T15:02:08.986000Z",
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
    till_typ_nm: Optional[str] = Field(
        None,
        alias="TILL_TYP_NM",
        name="",
        description="",
        example="Cashier",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioBankInModel(BaseModel):
    """Payload class for DREAMSFolioBankInModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bank In"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.BANK_IN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BANK_IN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
