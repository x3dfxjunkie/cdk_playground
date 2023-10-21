"""Source Data Contract Template for wdpr-dpp-BAPP0198288-use1-prd-dreams-accnting-CARD_SETTL.json"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Accounting - CARD SETTL Data"""

    card_settl_id: int = Field(
        ...,
        alias="CARD_SETTL_ID",
        name="",
        description="",
        example=74054391,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_settl_dts: datetime = Field(
        ...,
        alias="CARD_SETTL_DTS",
        name="",
        description="",
        example="2023-06-16T03:19:35.498404Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_typ_nm: str = Field(
        ...,
        alias="PMT_METH_TYP_NM",
        name="",
        description="",
        example="CreditCard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crdt_txn_typ_nm: str = Field(
        ...,
        alias="CRDT_TXN_TYP_NM",
        name="",
        description="",
        example="American Express",
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
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_in: str = Field(
        ...,
        alias="SAP_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dt: datetime = Field(
        ...,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-06-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_res_arr_dt: datetime = Field(
        ...,
        alias="ACM_RES_ARR_DT",
        name="",
        description="",
        example="2023-11-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_settl_card_nb: str = Field(
        ...,
        alias="CARD_SETTL_CARD_NB",
        name="",
        description="",
        example="***********1004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_res_nb: str = Field(
        ...,
        alias="ACM_RES_NB",
        name="",
        description="",
        example="753167326352",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_res_night_cn: int = Field(
        ...,
        alias="ACM_RES_NIGHT_CN",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_gst_nm: str = Field(
        ...,
        alias="ACM_GST_NM",
        name="",
        description="",
        example="JoulesSpencer, Ryan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    post_dts: datetime = Field(
        ...,
        alias="POST_DTS",
        name="",
        description="",
        example="2023-06-16T03:06:12.839000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_div_cd: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_DIV_CD",
        name="",
        description="",
        example="12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_sls_org_cd: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_SLS_ORG_CD",
        name="",
        description="",
        example="1009",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_prft_ctr_cd: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_PRFT_CTR_CD",
        name="",
        description="",
        example="0001141348",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=170,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: int = Field(
        ...,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=170,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_id: int = Field(
        ...,
        alias="CHRG_ACCT_CTR_ID",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_auth_id: int = Field(
        ...,
        alias="CARD_AUTH_ID",
        name="",
        description="",
        example=256070077,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_settl_auth_am: float = Field(
        ...,
        alias="CARD_SETTL_AUTH_AM",
        name="",
        description="",
        example=229.27,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    crncy_iso_cd: str = Field(
        ...,
        alias="CRNCY_ISO_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    data_orig_cd: str = Field(
        ...,
        alias="DATA_ORIG_CD",
        name="",
        description="",
        example=" ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281291948,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dprt_dt: datetime = Field(
        ...,
        alias="DPRT_DT",
        name="",
        description="",
        example="2023-12-12T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_dstr_chan_cd: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_CD",
        name="",
        description="",
        example="10",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_nb: str = Field(
        ...,
        alias="CC_MRCHT_NB",
        name="",
        description="",
        example="1091394395",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_ctgy_nb: int = Field(
        ...,
        alias="CC_MRCHT_CTGY_NB",
        name="",
        description="",
        example=7011,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rtrv_ref_nb: str = Field(
        ...,
        alias="RTRV_REF_NB",
        name="",
        description="",
        example="235788233052",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_in: str = Field(
        ...,
        alias="RFND_IN",
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
        example="CCBATCH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-16T03:19:35.498404Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    card_auth_cd: Optional[str] = Field(
        None,
        alias="CARD_AUTH_CD",
        name="",
        description="",
        example="243810",
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
    card_exp_dt: str = Field(
        ...,
        alias="CARD_EXP_DT",
        name="",
        description="",
        example="ScxiU8jjFt7BJVVUUETLoQ==",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_card_cls_cd: Optional[str] = Field(
        None,
        alias="STRTS_CARD_CLS_CD",
        name="",
        description="",
        example="0123",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    avs_resp_cd: Optional[str] = Field(
        None,
        alias="AVS_RESP_CD",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rtl_cust_nb: Optional[str] = Field(
        None,
        alias="RTL_CUST_NB",
        name="",
        description="",
        example="R1155917",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    int_preauth_amt: Optional[float] = Field(
        None,
        alias="INT_PREAUTH_AMT",
        name="",
        description="",
        example=100.00,
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
    card_settl_intfc_id: Optional[int] = Field(
        None,
        alias="CARD_SETTL_INTFC_ID",
        name="",
        description="",
        example=20200116052004,
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


class DREAMSAccountingCardSettlModel(BaseModel):
    """Payload class for DREAMSAccountingCardSettlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Card Settlement"
        stream_name = ""
        description = "Provides all the information related to the Settlement method (guest putting a credit card on their reservations for incidentals"  # optional
        unique_identifier = ["data.CARD_SETTL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "card_settl"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
