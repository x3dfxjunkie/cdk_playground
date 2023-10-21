"""Source Data Contract Template for wdpr-dpp-BAPP0198288-use1-prd-dreams-accnting-ACCT-RCV.json"""

from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Accounting - ACCT_RCV Data"""

    acct_rcv_id: int = Field(
        ...,
        alias="ACCT_RCV_ID",
        name="",
        description="",
        example=14579377,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_div_cd: int = Field(
        ...,
        alias="SAP_DIV_CD",
        name="",
        description="",
        example=11,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_sls_org_cd: int = Field(
        ...,
        alias="SAP_SLS_ORG_CD",
        name="",
        description="",
        example=1840,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cust_nb: str = Field(
        ...,
        alias="SAP_CUST_NB",
        name="",
        description="",
        example="0080126327",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_nm: str = Field(
        ...,
        alias="FAC_NM",
        name="",
        description="",
        example="Aulani, A Disney Resort & Spa, Ko Olina, Hawaii",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_grp_id: int = Field(
        ...,
        alias="SLS_GRP_ID",
        name="",
        description="",
        example=102,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_ofc_id: int = Field(
        ...,
        alias="SLS_OFC_ID",
        name="",
        description="",
        example=1105,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ord_typ_nm: str = Field(
        ...,
        alias="ORD_TYP_NM",
        name="",
        description="",
        example="ZIRI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_dt: datetime = Field(
        ...,
        alias="AR_DT",
        name="",
        description="",
        example="2023-06-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="AR_8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-16T09:00:08.633000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="AR_8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-16T09:00:08.633000Z",
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
    sap_dstr_chan_cd: int = Field(
        ...,
        alias="SAP_DSTR_CHAN_CD",
        name="",
        description="",
        example=11,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001240060",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281303898,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_prtnr_nm: Optional[str] = Field(
        None,
        alias="AR_PRTNR_NM",
        name="",
        description="",
        example="Mouse, Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_addr_ln_1_tx: Optional[str] = Field(
        None,
        alias="AR_ADDR_LN_1_TX",
        name="",
        description="",
        example="92-1185 Aliinui Drive",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_addr_ln_2_tx: Optional[str] = Field(
        None,
        alias="AR_ADDR_LN_2_TX",
        name="",
        description="",
        example="second address",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-06-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_city_nm: Optional[str] = Field(
        None,
        alias="AR_CITY_NM",
        name="",
        description="",
        example="Kapolei",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_pstl_cd: Optional[str] = Field(
        None,
        alias="AR_PSTL_CD",
        name="",
        description="",
        example="96707",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_cntry_cd: Optional[str] = Field(
        None,
        alias="AR_CNTRY_CD",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_rgn_nm: Optional[str] = Field(
        None,
        alias="AR_RGN_NM",
        name="",
        description="",
        example="HI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ar_intfc_id: Optional[int] = Field(
        None,
        alias="AR_INTFC_ID",
        name="",
        description="",
        example=20230616090311,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctRcvModel(BaseModel):
    """Payload class for DREAMSAccountingAcctRcvModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Receivable"
        stream_name = ""
        description = "Account Receivable information from SAP and Accounting, ie: PMT_ID, CAMPUS and the Business Organization ID, etc"  # optional
        unique_identifier = ["data.ACCT_RCV_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "acct_rcv"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
