"""Source Data Contract Template for Dreams - Dining Reservation Management Message"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Reservation Management Message Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2020-03-06T12:57:49.727000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="FAKEU008",
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

    rcpnt_txn_idvl_pty_id: int = Field(
        ...,
        alias="RCPNT_TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=111112370,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_dlvr_sts_nm: str = Field(
        ...,
        alias="RES_MGMT_DLVR_STS_NM",
        name="",
        description="",
        example="Undelivered",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="",
        description="",
        example=1111180885,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2020-03-06T12:57:49.727000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="FAKEU008",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    msg_src_nm: Optional[str] = Field(
        None,
        alias="MSG_SRC_NM",
        name="",
        description="",
        example="Fort Wilderness Front Desk",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningResMgmtMsgModel(BaseModel):
    """Payload class for Dreams - Dining Reservation Management Message Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Management Message"
        stream_name = ""
        description = """This table indicates if a guests package or message was delivered."""
        unique_identifier = ["data.RES_MGMT_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_mgmt_msg"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
