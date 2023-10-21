"""Source Data Contract Template for BANK_OUT.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for BANK_OUT"""

    bank_out_id: int = Field(
        ...,
        alias="BANK_OUT_ID",
        name="",
        description="",
        example=24558356,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_typ_nm: str = Field(
        ...,
        alias="BANK_OUT_TYP_NM",
        name="",
        description="",
        example="MANUAL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_id: int = Field(
        ...,
        alias="BANK_IN_ID",
        name="",
        description="",
        example=27351873,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_acct_dt: datetime = Field(
        ...,
        alias="BANK_OUT_ACCT_DT",
        name="",
        description="",
        example="2023-06-11T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dpst_bag_id: str = Field(
        ...,
        alias="DPST_BAG_ID",
        name="",
        description="",
        example="61223",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_dts: datetime = Field(
        ...,
        alias="BANK_OUT_DTS",
        name="",
        description="",
        example="2023-06-11T15:00:45Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_out_comp_dts: Optional[datetime] = Field(
        None,
        alias="BANK_OUT_COMP_DTS",
        name="",
        description="",
        example="2023-06-11T15:00:45.906000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgstr_am: float = Field(
        ...,
        alias="RGSTR_AM",
        name="",
        description="",
        example=552.96,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgstr_crncy_cd: str = Field(
        ...,
        alias="RGSTR_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_cash_am: float = Field(
        ...,
        alias="TOT_CASH_AM",
        name="",
        description="",
        example=2457.26,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_csh_crncy_cd: str = Field(
        ...,
        alias="TOT_CSH_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_non_csh_am: float = Field(
        ...,
        alias="TOT_NON_CSH_AM",
        name="",
        description="",
        example=315.62,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_non_csh_crncy_cd: str = Field(
        ...,
        alias="TOT_NON_CSH_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_edc_am: float = Field(
        ...,
        alias="TOT_EDC_AM",
        name="",
        description="",
        example=552.96,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_edc_crncy_cd: str = Field(
        ...,
        alias="TOT_EDC_CRNCY_CD",
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
        example="MILAM004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-11T15:00:45.827000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MILAM004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-11T15:00:45.827000Z",
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
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioBankOutModel(BaseModel):
    """Payload class for DREAMSFolioBankOutModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bank Out"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.BANK_OUT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BANK_OUT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
