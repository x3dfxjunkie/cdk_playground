"""Source Data Contract Template for FOLIO_CHKOT_OPT.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for FOLIO_CHKOT_OPT"""

    folio_chkot_opt_id: int = Field(
        ...,
        alias="FOLIO_CHKOT_OPT_ID",
        name="",
        description="",
        example=76466929,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_id: int = Field(
        ...,
        alias="CHRG_GRP_FOLIO_ID",
        name="",
        description="",
        example=276655250,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chkot_opt_typ_nm: str = Field(
        ...,
        alias="CHKOT_OPT_TYP_NM",
        name="",
        description="",
        example="EMAIL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-10T16:24:32.285000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_lctr_id: Optional[int] = Field(
        None,
        alias="TXN_PTY_LCTR_ID",
        name="",
        description="",
        example=908671452,
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


class DREAMSFolioFolioChkotOptModel(BaseModel):
    """Payload class for DREAMSFolioFolioChkotOptModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Checkout Options"
        stream_name = ""
        description = "This table holds the manner in which the guest would like to receive their Folio at Check out:  CHKOT_OPT_TYP_NM( EXPRESS_CHECK_OUT, PRINT, EMAIL)"  # optional
        unique_identifier = ["data.FOLIO_CHKOT_OPT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FOLIO_CHKOT_OPT"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
