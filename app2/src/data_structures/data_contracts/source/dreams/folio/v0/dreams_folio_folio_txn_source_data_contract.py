"""Source Data Contract Template for FOLIO_TXN.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_TXN"""

    folio_txn_id: int = Field(
        ...,
        alias="FOLIO_TXN_ID",
        name="",
        description="",
        example=1563772707,
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
    folio_txn_dts: datetime = Field(
        ...,
        alias="FOLIO_TXN_DTS",
        name="",
        description="",
        example="2023-06-09T10:05:23.474000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="2207",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T10:05:22Z",
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


class DREAMSFolioFolioTxnModel(BaseModel):
    """Payload class for DREAMSFolioFolioTxnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Transaction"
        stream_name = ""
        description = (
            "This table ties the Folio Transaction type name and the Folio Transaction date time stamp"  # optional
        )
        unique_identifier = ["data.FOLIO_TXN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_TXN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
