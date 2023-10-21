"""Source Data Contract for DREAMS Bank Account Center"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Bank Account Center Data"""

    bank_acct_ctr_id: int = Field(
        ...,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_id: int = Field(
        ...,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dsny_sys_cd: str = Field(
        ...,
        alias="DSNY_SYS_CD",
        name="",
        description="",
        example="WDRMB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tcr_loc_in: str = Field(
        ...,
        alias="TCR_LOC_IN",
        name="",
        description="",
        example="N",
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
    bank_out_in: str = Field(
        ...,
        alias="BANK_OUT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ovr_shrt_csh_am: int = Field(
        ...,
        alias="OVR_SHRT_CSH_AM",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ovr_shrt_crncy_cd: str = Field(
        ...,
        alias="OVR_SHRT_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    barcd_prt_in: str = Field(
        ...,
        alias="BARCD_PRT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    till_dspns_in: str = Field(
        ...,
        alias="TILL_DSPNS_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_term_nb: int = Field(
        ...,
        alias="STRTS_TERM_NB",
        name="",
        description="",
        example=6310,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgstr_nb_vl: str = Field(
        ...,
        alias="RGSTR_NB_VL",
        name="",
        description="",
        example="DRM1141348",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T06:14:22.782Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UAT1_GLC_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-13T23:16:08.301Z",
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
    cc_mrcht_nm: Optional[str] = Field(
        None,
        alias="CC_MRCHT_NM",
        name="",
        description="",
        example="WDW_CRO_REF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_addr_mrcht_ln_1_val: Optional[str] = Field(
        None,
        alias="CC_ADDR_MRCHT_LN_1_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_addr_mrcht_ln_2_val: Optional[str] = Field(
        None,
        alias="CC_ADDR_MRCHT_LN_2_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_cty_nm: Optional[str] = Field(
        None,
        alias="CC_MRCHT_CTY_NM",
        name="",
        description="",
        example="Lake Buena Vista",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_pstl_cd: Optional[str] = Field(
        None,
        alias="CC_MRCHT_PSTL_CD",
        name="",
        description="",
        example="32830",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_rgn_cd: Optional[str] = Field(
        None,
        alias="CC_MRCHT_RGN_CD",
        name="",
        description="",
        example="FL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_cntry_cd: Optional[str] = Field(
        None,
        alias="CC_MRCHT_CNTRY_CD",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_phn_nb_val: Optional[str] = Field(
        None,
        alias="CC_MRCHT_PHN_NB_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cc_mrcht_rgn_nm: Optional[str] = Field(
        None,
        alias="CC_MRCHT_RGN_NM",
        name="",
        description="",
        example="None",
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
    gst_fc_mrcht_ref_val: Optional[str] = Field(
        None,
        alias="GST_FC_MRCHT_REF_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_gst_fc_mrcht_ref_val: Optional[str] = Field(
        None,
        alias="NON_GST_FC_MRCHT_REF_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingBankAcctCtrModel(BaseModel):
    """Payload class for DREAMSAccountingBankAcctCtrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Bank Account Center"
        stream_name = ""
        description = """This holds information about the Accounting Centers where payments are taken"""
        unique_identifier = ["data.BANK_ACCT_CTR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "BANK_ACCT_CTR"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
