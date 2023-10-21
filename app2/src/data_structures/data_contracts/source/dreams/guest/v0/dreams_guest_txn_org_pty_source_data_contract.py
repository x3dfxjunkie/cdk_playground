"""Source Data Contract Template for txn_org_pty.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_org_pty_"""

    txn_org_pty_id: int = Field(
        ...,
        alias="TXN_ORG_PTY_ID",
        name="",
        description="",
        example=762990798,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_org_nm: str = Field(
        ...,
        alias="TXN_ORG_NM",
        name="",
        description="",
        example="Travel Beyond the Magic LLC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DELCF001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-13T11:34:20Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DELCF001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-13T11:34:20Z",
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
        example="2023-07-13T11:34:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestTxnOrgPtyModel(BaseModel):
    """DREAMSGuestTxnOrgPtyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Organization Party"
        stream_name = ""
        description = "This table associates Organization Names to transactional Party IDs"  # optional
        unique_identifier = ["data.TXN_ORG_PTY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_org_pty"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
