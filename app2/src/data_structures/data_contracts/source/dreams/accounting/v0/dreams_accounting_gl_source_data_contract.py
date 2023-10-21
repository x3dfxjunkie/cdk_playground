"""Source Data Contract for DREAMS General Ledger"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS General Ledger Data"""

    acct_dt: datetime = Field(
        ...,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-08-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_bus_area_cd: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_BUS_AREA_CD",
        name="",
        description="",
        example="101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_acct_ctr_co_cd: str = Field(
        ...,
        alias="CHRG_ACCT_CTR_CO_CD",
        name="",
        description="",
        example="1005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-29T06:07:09.659528Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="GL",
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
    ext_src_ref_val: Optional[str] = Field(
        None,
        alias="EXT_SRC_REF_VAL",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gl_am: float = Field(
        ...,
        alias="GL_AM",
        name="",
        description="",
        example=61361.92,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gl_id: int = Field(
        ...,
        alias="GL_ID",
        name="",
        description="",
        example=242113456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gl_natr_in: str = Field(
        ...,
        alias="GL_NATR_IN",
        name="",
        description="",
        example="N",
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
        example="2023-08-29T06:07:09.659528Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prm_pty_nm: Optional[str] = Field(
        None,
        alias="PRM_PTY_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_acct_nm: str = Field(
        ...,
        alias="SAP_ACCT_NM",
        name="",
        description="",
        example="EDC Clearing",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cost_ctr_cd: Optional[str] = Field(
        None,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="None",
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
    sap_dstr_chan_nm: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_NM",
        name="",
        description="",
        example="Retail Consumer",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000105990",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_iss_cd: Optional[str] = Field(
        None,
        alias="SAP_ISS_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_mtrl_cd: Optional[str] = Field(
        None,
        alias="SAP_MTRL_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001101465",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_tax_cd: Optional[str] = Field(
        None,
        alias="SAP_TAX_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_wbs_cd: Optional[str] = Field(
        None,
        alias="SAP_WBS_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_co_cd: str = Field(
        ...,
        alias="SRC_ACCT_CTR_CO_CD",
        name="",
        description="",
        example="1005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=5005,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_bus_area_cd: str = Field(
        ...,
        alias="SRC_BUS_AREA_CD",
        name="",
        description="",
        example="101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exmpt_in: str = Field(
        ...,
        alias="TAX_EXMPT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trdg_ptnr_bus_area_cd: Optional[str] = Field(
        None,
        alias="TRDG_PTNR_BUS_AREA_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trdg_ptnr_co_cd: Optional[str] = Field(
        None,
        alias="TRDG_PTNR_CO_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-29T06:07:09.659528Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="GL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingGlModel(BaseModel):
    """Payload class for DREAMSAccountingGlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "General Ledger"
        stream_name = ""
        description = "Provides an account or record used to store bookkeeping entries for balance-sheet and income-statement transactions"  # optional
        unique_identifier = ["data.GL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "gl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
