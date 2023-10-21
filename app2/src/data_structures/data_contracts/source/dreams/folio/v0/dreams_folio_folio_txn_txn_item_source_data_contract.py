"""Source Data Contract Template for FOLIO_TXN_TXN_ITEM.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_TXN_TXN_ITEM"""

    folio_txn_txn_item_id: int = Field(
        ...,
        alias="FOLIO_TXN_TXN_ITEM_ID",
        name="",
        description="",
        example=956798785,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_id: int = Field(
        ...,
        alias="FOLIO_TXN_ID",
        name="",
        description="",
        example=1564068143,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_proc_typ_nm: str = Field(
        ...,
        alias="TXN_PROC_TYP_NM",
        name="",
        description="",
        example="Created",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_item_typ_nm: str = Field(
        ...,
        alias="FOLIO_TXN_ITEM_TYP_NM",
        name="",
        description="",
        example="CHARGE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="2821",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-11T02:12:06Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_item_id_vl: int = Field(
        ...,
        alias="FOLIO_TXN_ITEM_ID_VL",
        name="",
        description="",
        example=3408690360,
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


class DREAMSFolioFolioTxnTxnItemModel(BaseModel):
    """Payload class for DREAMSFolioFolioTxnTxnItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Transaction Transaction Item"
        stream_name = ""
        description = "This table ties Folio Transaction ID to Folio Transaction Item ID Value by Folio Transaction Item Type Name: FOLIO_TXN_ITEM_TYP_NM CHARGE, PAYMENT, COUPONCHARGE"  # optional
        unique_identifier = ["data.FOLIO_TXN_TXN_ITEM_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_TXN_TXN_ITEM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
