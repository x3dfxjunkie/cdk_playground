"""Source Data Contract for Dreams Account Center SAP"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Account Center SAP"""

    acct_ctr_id: Optional[int] = Field(
        None,
        alias="ACCT_CTR_ID",
        name="",
        description="",
        example=11425,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_sap_end_dt: Optional[datetime] = Field(
        None,
        alias="ACCT_CTR_SAP_END_DT",
        name="",
        description="",
        example="2023-08-17T12:29:45Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_sap_id: int = Field(
        ...,
        alias="ACCT_CTR_SAP_ID",
        name="",
        description="",
        example=1366200,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    acct_ctr_sap_strt_dt: datetime = Field(
        ...,
        alias="ACCT_CTR_SAP_STRT_DT",
        name="",
        description="",
        example="2023-08-17T12:29:45Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-17T12:29:45.350000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="AAAAA000",
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

    rtl_cust_nb: Optional[str] = Field(
        None,
        alias="RTL_CUST_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_bus_area_cd: Optional[str] = Field(
        None,
        alias="SAP_BUS_AREA_CD",
        name="",
        description="",
        example="138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_cost_ctr_cd: Optional[str] = Field(
        None,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="0005146975",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_co_cd: str = Field(
        ...,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1029",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_div_cd: Optional[str] = Field(
        None,
        alias="SAP_DIV_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_dstr_chan_nm: Optional[str] = Field(
        None,
        alias="SAP_DSTR_CHAN_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_prft_ctr_cd: Optional[str] = Field(
        None,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_sls_org_cd: Optional[str] = Field(
        None,
        alias="SAP_SLS_ORG_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sls_ofc_id: Optional[str] = Field(
        None,
        alias="SLS_OFC_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-17T12:29:45.350000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="AAAAA000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAcctCtrSapModel(BaseModel):
    """Payload class for Dreams Account Center SAP"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center SAP"
        stream_name = ""
        description = """Account Centers associated to relevant SAP fields"""
        unique_identifier = ["data.ACCT_CTR_SAP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ACCT_CTR_SAP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
