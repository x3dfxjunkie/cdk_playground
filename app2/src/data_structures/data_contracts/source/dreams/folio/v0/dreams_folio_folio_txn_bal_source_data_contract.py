"""Source Data Contract Template for FOLIO_TXN_BAL.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_TXN_BAL"""

    folio_id: int = Field(
        ...,
        alias="FOLIO_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_id: int = Field(
        ...,
        alias="FOLIO_TXN_ID",
        name="",
        description="",
        example=1563757437,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_bal_am: int = Field(
        ...,
        alias="FOLIO_BAL_AM",
        name="",
        description="",
        example=692,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_bal_crncy_cd: str = Field(
        ...,
        alias="FOLIO_BAL_CRNCY_CD",
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
        example="PostPayACC_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T05:32:41.962000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="PostPayACC_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T05:32:41.962000Z",
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


class DREAMSFolioFolioTxnBalModel(BaseModel):
    """Payload class for DREAMSFolioFolioTxnBalModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Transaction Balance"
        stream_name = ""
        description = "This table ties a Folio ID to a Folio Transaction ID and the Folio Balance Amount"  # optional
        unique_identifier = ["data.FOLIO_ID", "data.FOLIO_TXN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_TXN_BAL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
