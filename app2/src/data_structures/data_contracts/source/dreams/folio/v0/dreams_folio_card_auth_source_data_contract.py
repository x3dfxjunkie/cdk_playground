"""Source Data Contract Template for CARD_AUTH.json"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CARD_AUTH"""

    auth_ref_vl: Optional[str] = Field(
        None,
        alias="AUTH_REF_VL",
        name="",
        description="",
        example="a1a1a1a1a1a1a1a1a1a1a1a1a1a11a1a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    avs_resp_cd: Optional[str] = Field(
        None,
        alias="AVS_RESP_CD",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_auth_am: float = Field(
        ...,
        alias="CARD_AUTH_AM",
        name="",
        description="",
        example=247.4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_auth_cd: Optional[str] = Field(
        None,
        alias="CARD_AUTH_CD",
        name="",
        description="",
        example="A1A1A1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_auth_crncy_cd: str = Field(
        ...,
        alias="CARD_AUTH_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_auth_dts: datetime = Field(
        ...,
        alias="CARD_AUTH_DTS",
        name="",
        description="",
        example="2023-08-22T18:35:08.867000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_auth_id: int = Field(
        ...,
        alias="CARD_AUTH_ID",
        name="",
        description="",
        example=111111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_entry_mode_cd: Optional[str] = Field(
        None,
        alias="CARD_ENTRY_MODE_CD",
        name="",
        description="",
        example="01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_exp_dt: Optional[str] = Field(
        None,
        alias="CARD_EXP_DT",
        name="",
        description="",
        example="a1a1a1a1a1AAAAAAAAAAAA==",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cc_mrcht_ctgy_nb: Optional[int] = Field(
        None,
        alias="CC_MRCHT_CTGY_NB",
        name="",
        description="",
        example=7011,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cc_mrcht_nb: Optional[str] = Field(
        None,
        alias="CC_MRCHT_NB",
        name="",
        description="",
        example="111111111111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-22T18:35:08.623000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSE1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    e_cmrc_indctn_cd: Optional[str] = Field(
        None,
        alias="E_CMRC_INDCTN_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    int_preauth_amt: Optional[int] = Field(
        None,
        alias="INT_PREAUTH_AMT",
        name="",
        description="",
        example=106,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mc_bnknt_dt: Optional[str] = Field(
        None,
        alias="MC_BNKNT_DT",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mc_bnknt_ref_nb: Optional[str] = Field(
        None,
        alias="MC_BNKNT_REF_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pmt_card_id: int = Field(
        ...,
        alias="PMT_CARD_ID",
        name="",
        description="",
        example=111111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pmt_man_auth_in: str = Field(
        ...,
        alias="PMT_MAN_AUTH_IN",
        name="",
        description="",
        example="N",
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

    strts_auth_typ_nm: str = Field(
        ...,
        alias="STRTS_AUTH_TYP_NM",
        name="",
        description="",
        example="Authorization",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strts_card_cls_cd: Optional[str] = Field(
        None,
        alias="STRTS_CARD_CLS_CD",
        name="",
        description="",
        example="0118",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strts_trmnl_nb: Optional[int] = Field(
        None,
        alias="STRTS_TRMNL_NB",
        name="",
        description="",
        example=6334,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strts_txn_ds_cd: Optional[str] = Field(
        None,
        alias="STRTS_TXN_DS_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    visa_auth_chrctr_cd: Optional[str] = Field(
        None,
        alias="VISA_AUTH_CHRCTR_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    visa_txn_id: Optional[str] = Field(
        None,
        alias="VISA_TXN_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    visa_vld_cd: Optional[str] = Field(
        None,
        alias="VISA_VLD_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioCardAuthModel(BaseModel):
    """Payload class for DREAMSFolioCardAuthModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Card Authorization"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CARD_AUTH_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CARD_AUTH"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
