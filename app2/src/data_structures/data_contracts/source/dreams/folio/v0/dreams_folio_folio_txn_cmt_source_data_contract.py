"""Source Data Contract Template for FOLIO_TXN_CMT.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_TXN_CMT"""

    folio_txn_cmt_id: int = Field(
        ...,
        alias="FOLIO_TXN_CMT_ID",
        name="",
        description="",
        example=32278826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_id: int = Field(
        ...,
        alias="FOLIO_TXN_ID",
        name="",
        description="",
        example=1563946925,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_rsn_cd: Optional[str] = Field(
        None,
        alias="TXN_RSN_CD",
        name="",
        description="",
        example="ACOTH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_cmt_tx: Optional[str] = Field(
        None,
        alias="FOLIO_TXN_CMT_TX",
        name="",
        description="",
        example="7 night pet stay",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_cmt_actv_in: str = Field(
        ...,
        alias="FOLIO_CMT_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SCHIM089",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-10T12:25:05.825000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SCHIM089",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-10T12:25:05.825000Z",
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
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioFolioTxnCmtModel(BaseModel):
    """Payload class for DREAMSFolioFolioTxnCmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Transaction Comments"
        stream_name = ""
        description = "This table ties Freeform text column Folio Transaction Comment Text"  # optional
        unique_identifier = ["data.FOLIO_TXN_CMT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_TXN_CMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
