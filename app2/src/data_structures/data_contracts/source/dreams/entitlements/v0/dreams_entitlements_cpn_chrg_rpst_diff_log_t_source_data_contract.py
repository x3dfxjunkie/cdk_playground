"""Source Data Contract for Dreams Entitlement CPN_CHRG_RPST_DIFF_LOG_T Data"""


from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon CPN_CHRG_RPST_DIFF_LOG_T Data"""

    chrg_rpst_am: float = Field(
        ...,
        alias="CHRG_RPST_AM",
        name="",
        description="",
        example=7.93,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_chrg_rpst_diff_log_id: int = Field(
        ...,
        alias="CPN_CHRG_RPST_DIFF_LOG_ID",
        name="",
        description="",
        example=292907,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_card_nb: str = Field(
        ...,
        alias="EXPRNC_CARD_NB",
        name="",
        description="",
        example="111111111111110101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    extnl_tkt_nb: str = Field(
        ...,
        alias="EXTNL_TKT_NB",
        name="",
        description="",
        example="0000000131",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2017-12-18T10:36:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pst_dts: datetime = Field(
        ...,
        alias="PST_DTS",
        name="",
        description="",
        example="2017-12-18T10:36:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rpst_crncy_cd: str = Field(
        ...,
        alias="RPST_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strts_rtrvl_ref_nb: str = Field(
        ...,
        alias="STRTS_RTRVL_REF_NB",
        name="",
        description="",
        example="111111117707",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tndr_typ_nm: str = Field(
        ...,
        alias="TNDR_TYP_NM",
        name="",
        description="",
        example="32",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=56803,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsCpnChrgRpstDiffLogTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnChrgRpstDiffLogTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A standalone table that records the chronological changes made to obligations that were incurred.  Used to record the changes maded to admission charges.  Captures by date, the ticket number, experience card number, the date of the admission posting, the accounting organization that owns the charge, the kind of tender used for payment and the payment amount for the charge.  If Stratus validation is required for the posting of the payment, the retrieval reference number returned by Stratus is recorded as well."""
        unique_identifier = ["data.CPN_CHRG_RPST_DIFF_LOG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_CHRG_RPST_DIFF_LOG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
