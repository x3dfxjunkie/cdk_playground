"""Source Data Contract Template for CHRG_RPST_DIFF_LOG.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_RPST_DIFF_LOG"""

    chrg_rpst_diff_log_id: int = Field(
        ...,
        alias="CHRG_RPST_DIFF_LOG_ID",
        name="",
        description="",
        example=309049895,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    extnl_tkt_nb: str = Field(
        ...,
        alias="EXTNL_TKT_NB",
        name="",
        description="",
        example="0400101395",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_card_nb: str = Field(
        ...,
        alias="EXPRNC_CARD_NB",
        name="",
        description="",
        example="993753024551406902",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_dts: datetime = Field(
        ...,
        alias="PST_DTS",
        name="",
        description="",
        example="2023-06-10T21:23:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=218202,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tndr_typ_nm: Optional[str] = Field(
        None,
        alias="TNDR_TYP_NM",
        name="",
        description="",
        example="13",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_rpst_am: float = Field(
        ...,
        alias="CHRG_RPST_AM",
        name="",
        description="",
        example=5.5,
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
        example="235181824614",
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


class DREAMSFolioChrgRpstDiffLogModel(BaseModel):
    """Payload class for DREAMSFolioChrgRpstDiffLogModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Repost Differential Log"
        stream_name = ""
        description = "This table holds the information related to a Repost, meaning that the interface between the reservation system and the POS system may not have connected properly and therefore, the charge is reposted and that is monitored by Finance"  # optional
        unique_identifier = ["data.CHRG_RPST_DIFF_LOG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_RPST_DIFF_LOG"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
