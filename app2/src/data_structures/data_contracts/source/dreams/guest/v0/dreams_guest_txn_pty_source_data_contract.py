"""Source Data Contract Template for txn_pty.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_pty"""

    txn_pty_id: int = Field(
        ...,
        alias="TXN_PTY_ID",
        name="",
        description="",
        example=123052289,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_typ_nm: str = Field(
        ...,
        alias="TXN_PTY_TYP_NM",
        name="",
        description="",
        example="Individual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    unk_txn_pty_nm: Optional[str] = Field(
        None,
        alias="UNK_TXN_PTY_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-22T12:23:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-22T12:23:21Z",
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
        example="2023-05-22T12:23:20Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestTxnPtyModel(BaseModel):
    """DREAMSGuestTxnPtyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party"
        stream_name = ""
        description = "This table contains both Organization Transactional Party ID and Transactional Individual Party ID"  # optional
        unique_identifier = ["data.TXN_PTY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
