"""Source Data Contract Template for txn_pty_lctr.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_pty_lctr"""

    txn_pty_lctr_id: int = Field(
        ...,
        alias="TXN_PTY_LCTR_ID",
        name="",
        description="",
        example=911025202,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lctr_typ_nm: str = Field(
        ...,
        alias="LCTR_TYP_NM",
        name="",
        description="",
        example="Email",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lctr_usg_typ_nm: str = Field(
        ...,
        alias="LCTR_USG_TYP_NM",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_id: int = Field(
        ...,
        alias="TXN_PTY_ID",
        name="",
        description="",
        example=763336603,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_lctr_prmy_in: str = Field(
        ...,
        alias="TXN_PTY_LCTR_PRMY_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cnfrm_in: str = Field(
        ...,
        alias="CNFRM_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_bill_in: str = Field(
        ...,
        alias="ALLOW_BILL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_mkt_in: str = Field(
        ...,
        alias="ALLOW_MKT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntry_nm: Optional[str] = Field(
        None,
        alias="CNTRY_NM",
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
        example="2023-07-14T21:15:46Z",
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


class DREAMSGuestTxnPtyLctrModel(BaseModel):
    """DREAMSGuestTxnPtyLctrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party Locator"
        stream_name = ""
        description = "Locator ID and Type associated to a Transactional Party ID"  # optional
        unique_identifier = ["data.TXN_PTY_LCTR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty_lctr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
