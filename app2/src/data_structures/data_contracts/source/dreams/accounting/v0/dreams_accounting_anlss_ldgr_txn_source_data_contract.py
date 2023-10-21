"""Source Data Contract Template for dreams_accounting_anlss_ldgr_txn_source_data_contract_sample.json"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class"""

    anlss_ldgr_txn_id: int = Field(
        ...,
        alias="ANLSS_LDGR_TXN_ID",
        name="",
        description="",
        example=2750469756,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_typ_nm: str = Field(
        ...,
        alias="FOLIO_TXN_TYP_NM",
        name="",
        description="",
        example="SALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dt: datetime = Field(
        ...,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-05-23T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_txn_pst_dts: datetime = Field(
        ...,
        alias="ACCT_TXN_PST_DTS",
        name="",
        description="",
        example="2023-05-23T17:28:35.650000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_prmy_pty_nm: str = Field(
        ...,
        alias="TXN_PRMY_PTY_NM",
        name="",
        description="",
        example="Mouse, Mickey|123345678912",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=14,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_id: int = Field(
        ...,
        alias="FOLIO_ID",
        name="",
        description="",
        example=266308453,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_id: int = Field(
        ...,
        alias="FOLIO_ITEM_ID",
        name="",
        description="",
        example=18190399892,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_sap_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_SAP_ID",
        name="",
        description="",
        example=11700,
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
    tax_exmpt_txn_in: str = Field(
        ...,
        alias="TAX_EXMPT_TXN_IN",
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
        example="RecoRev_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-23T17:14:51.064000Z",
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


class DREAMSAccountingAnlssLdgrTxnModel(BaseModel):
    """Payload class for DREAMSAccountingAnlssLdgrTxnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Analysis Ledger Transaction"
        stream_name = ""
        description = "This table ties to the ALT Entry table for analysis purposes"  # optional
        unique_identifier = ["data.ANLSS_LDGR_TXN_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "anlss_ldgr_txn"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
