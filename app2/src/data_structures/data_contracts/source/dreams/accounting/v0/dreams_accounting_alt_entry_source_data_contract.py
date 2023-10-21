"""Source Data Contract Template for wdpr-dpp-BAPP0198288-use1-prd-dreams-accnting-ALT_ENTRY.json"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data contract"""

    anlss_ldgr_txn_entry_id: int = Field(
        ...,
        alias="ANLSS_LDGR_TXN_ENTRY_ID",
        name="",
        description="",
        example=17740752730,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    anlss_ldgr_txn_id: int = Field(
        ...,
        alias="ANLSS_LDGR_TXN_ID",
        name="",
        description="",
        example=2755154765,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pst_acct_id: int = Field(
        ...,
        alias="PST_ACCT_ID",
        name="",
        description="",
        example=20228,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pst_acct_ctr_id: int = Field(
        ...,
        alias="PST_ACCT_CTR_ID",
        name="",
        description="",
        example=11312,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_acct_ctr_id: int = Field(
        ...,
        alias="CHRG_ACCT_CTR_ID",
        name="",
        description="",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_gl_ref_id: int = Field(
        ...,
        alias="SAP_GL_REF_ID",
        name="",
        description="",
        example=55046,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_acct_ctr_sap_id: int = Field(
        ...,
        alias="CHRG_ACCT_CTR_SAP_ID",
        name="",
        description="",
        example=11199,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    natr_acct_in: str = Field(
        ...,
        alias="NATR_ACCT_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pst_acct_am: float = Field(
        ...,
        alias="PST_ACCT_AM",
        name="",
        description="",
        example=18.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pst_acct_crncy_cd: str = Field(
        ...,
        alias="PST_ACCT_CRNCY_CD",
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
        example="2023-06-11T10:18:29.606000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="RecoRev_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-11T10:18:29.606000Z",
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
        example="2023-06-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingAltEntryModel(BaseModel):
    """Payload class for DREAMSAccountingAltEntryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Analysis Ledger Transacton Entry"
        stream_name = ""
        description = "Provides a means of distributing transaction values to ledger accounts together with analysis information, this table represents the record-keeping system for a company's financial data, with debit and credit account records validated by a trial balance."  # optional
        unique_identifier = ["data.ANLSS_LDGR_TXN_ENTRY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "alt_entry"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
