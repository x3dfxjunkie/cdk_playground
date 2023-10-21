"""Source Data Contract Template for txn_idvl_pty_mbshp.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_idvl_pty_mbshp"""

    txn_idvl_pty_mbrshp_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_MBRSHP_ID",
        name="",
        description="",
        example=44821559,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_pty_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=763336637,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mbrshp_id: str = Field(
        ...,
        alias="MBRSHP_ID",
        name="",
        description="",
        example="M:625283224505139015",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mbrshp_end_dt: Optional[datetime] = Field(
        None,
        alias="MBRSHP_END_DT",
        name="",
        description="",
        example="2023-07-13T11:34:23Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=1000004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_chan_id: int = Field(
        ...,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=74,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="2402546.1",
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
        example="2402546.1",
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
        example=1,
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


class DREAMSGuestTxnIdvlPtyMbshpModel(BaseModel):
    """DREAMSGuestTxnIdvlPtyMbshpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Individual Party Membership"
        stream_name = ""
        description = "Membership IDs associated to transactional individual IDs"  # optional
        unique_identifier = ["data.TXN_IDVL_PTY_MBRSHP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_idvl_pty_mbshp"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
