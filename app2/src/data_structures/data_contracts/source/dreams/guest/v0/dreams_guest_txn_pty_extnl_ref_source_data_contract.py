"""Source Data Contract for Dreams TXN PTY EXTRNL REF"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-21T16:26:36Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
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
    pty_extnl_src_nm: str = Field(
        ...,
        alias="PTY_EXTNL_SRC_NM",
        name="",
        description="",
        example="ODS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_extnl_ref_id: int = Field(
        ...,
        alias="TXN_PTY_EXTNL_REF_ID",
        name="",
        description="",
        example=1350571563,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_extnl_ref_val: str = Field(
        ...,
        alias="TXN_PTY_EXTNL_REF_VAL",
        name="",
        description="",
        example="4584373235",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_id: int = Field(
        ...,
        alias="TXN_PTY_ID",
        name="",
        description="",
        example=770547731,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-21T16:26:36Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
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


class DREAMSGuestTxnPtyExtnlRefModel(BaseModel):
    """Payload class for DREAMSGuestTxnPtyExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party External Reference"
        stream_name = ""
        description = "This table associates transactional party IDs to External References: ie: SWID, GOMaster ID, Travel agent IATA number"
        unique_identifier = ["data.TXN_PTY_EXTNL_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty_extnl_ref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
