"""Source Data Contract for DREAMS Accounting Refund Accounts Payable"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Accounting Refund Accounts Payable Data"""

    acct_dt: datetime = Field(
        ...,
        alias="ACCT_DT",
        name="",
        description="",
        example="2022-03-27T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_am: float = Field(
        ...,
        alias="AP_AM",
        name="",
        description="",
        example=55.45,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_dts: datetime = Field(
        ...,
        alias="AP_DTS",
        name="",
        description="",
        example="2022-03-28T03:13:01.271504Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_id: int = Field(
        ...,
        alias="AP_ID",
        name="",
        description="",
        example=13018005,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_addr_ln_1_tx: str = Field(
        ...,
        alias="AP_PTNR_ADDR_LN_1_TX",
        name="",
        description="",
        example="1110 Jones Mill Rd",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_addr_ln_2_tx: Optional[str] = Field(
        None,
        alias="AP_PTNR_ADDR_LN_2_TX",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_city_nm: str = Field(
        ...,
        alias="AP_PTNR_CITY_NM",
        name="",
        description="",
        example="Chatham",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_cntry_cd: str = Field(
        ...,
        alias="AP_PTNR_CNTRY_CD",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_nm: str = Field(
        ...,
        alias="AP_PTNR_NM",
        name="",
        description="",
        example="Jennifer Oakes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_pstl_cd: str = Field(
        ...,
        alias="AP_PTNR_PSTL_CD",
        name="",
        description="",
        example="24531",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_rgn_cd: Optional[str] = Field(
        None,
        alias="AP_PTNR_RGN_CD",
        name="",
        description="",
        example="VA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ap_ptnr_rgn_nm: Optional[str] = Field(
        None,
        alias="AP_PTNR_RGN_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=1,
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
        example="2022-03-28T03:13:01.271504Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="APREF",
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
    doc_typ_cd: str = Field(
        ...,
        alias="DOC_TYP_CD",
        name="",
        description="",
        example="INV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: str = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example="80007798",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    orig_doc_id: str = Field(
        ...,
        alias="ORIG_DOC_ID",
        name="",
        description="",
        example="520861212879",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2022-03-28T03:13:01.271504Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_ap_intfc_id: Optional[int] = Field(
        None,
        alias="RFND_AP_INTFC_ID",
        name="",
        description="",
        example=20220328031429,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_pmt_id: int = Field(
        ...,
        alias="RFND_PMT_ID",
        name="",
        description="",
        example=267087918,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_bus_area_cd: str = Field(
        ...,
        alias="SAP_BUS_AREA_CD",
        name="",
        description="",
        example="138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cost_ctr_cd: str = Field(
        ...,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="0005151157",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_co_cd: str = Field(
        ...,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000260067",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001143455",
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


class DREAMSAccountingRfndApModel(BaseModel):
    """Payload class for DREAMSAccountingRfndApModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accounting Refund Accounts Payable"
        stream_name = ""
        description = "Accounts Payable Refund Transactions with SAP and Accounting Center information"  # optional
        unique_identifier = ["data.AP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "rfnd_ap"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
