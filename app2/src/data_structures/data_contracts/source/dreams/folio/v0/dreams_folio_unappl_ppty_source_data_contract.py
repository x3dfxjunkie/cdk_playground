"""Source Data Contract for  Dreams Folio Unapplied Payment"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Unapplied Payment Data"""

    unappl_ppty_id: int = Field(
        ...,
        alias="UNAPPL_PPTY_ID",
        name="",
        description="",
        example=6447051,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    usr_data_entry_nm: str = Field(
        ...,
        alias="USR_DATA_ENTRY_NM",
        name="",
        description="",
        example="BookingSource",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_usr_data_entry_vl: Optional[str] = Field(
        None,
        alias="FOLIO_TXN_USR_DATA_ENTRY_VL",
        name="",
        description="",
        example="DREAMS_TPS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-08T20:37:37.616179Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-08T20:37:37.616179Z",
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
    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281057252,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-06-08T20:37:37.616179Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioUnapplPptyModel(BaseModel):
    """Payload class for DREAMSFolioUnapplPptyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Unapplied Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.UNAPPL_PPTY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "UNAPPL_PPTY"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
