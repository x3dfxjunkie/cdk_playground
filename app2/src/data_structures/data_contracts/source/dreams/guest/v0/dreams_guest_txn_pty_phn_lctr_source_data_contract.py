"""Source Data Contract Template for txn_pty_phn_lctr.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_pty_phn_lctr"""

    txn_pty_phn_lctr_id: int = Field(
        ...,
        alias="TXN_PTY_PHN_LCTR_ID",
        name="",
        description="",
        example=911025203,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phn_dev_typ_nm: str = Field(
        ...,
        alias="PHN_DEV_TYP_NM",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phn_nb: str = Field(
        ...,
        alias="PHN_NB",
        name="",
        description="",
        example="19375543212",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    phn_ext_nb: Optional[str] = Field(
        None,
        alias="PHN_EXT_NB",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_phn_in: str = Field(
        ...,
        alias="ALLOW_PHN_IN",
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
        example="WDPRO",
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
        example="WDPRO",
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
    allow_phn_ind: Optional[str] = Field(
        None,
        alias="ALLOW_PHN_IND",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestTxnPtyPhnLctrModel(BaseModel):
    """DREAMSGuestTxnPtyPhnLctrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party Phone Locator"
        stream_name = ""
        description = "Transaction Party Phone Locator"  # optional
        unique_identifier = ["data.TXN_PTY_PHN_LCTR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty_phn_lctr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
