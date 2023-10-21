"""Source Data Contract Template for txn_pty_lctr_xref.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_pty_lctr_xref"""

    txn_pty_lctr_extnl_ref_id: int = Field(
        ...,
        alias="TXN_PTY_LCTR_EXTNL_REF_ID",
        name="",
        description="",
        example=831884103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_pty_lctr_id: int = Field(
        ...,
        alias="TXN_PTY_LCTR_ID",
        name="",
        description="",
        example=911025196,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lctr_extnl_src_nm: str = Field(
        ...,
        alias="LCTR_EXTNL_SRC_NM",
        name="",
        description="",
        example="ODS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lctr_extnl_ref_vl: str = Field(
        ...,
        alias="LCTR_EXTNL_REF_VL",
        name="",
        description="",
        example="889508378",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="GOMER168",
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
        example="GOMER168",
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


class DREAMSGuestTxnPtyLctrXrefModel(BaseModel):
    """DREAMSGuestTxnPtyLctrXrefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party Locator Cross Reference"
        stream_name = ""
        description = "This table provides a reference to locator IDs in GOMaster"  # optional
        unique_identifier = ["data.TXN_PTY_LCTR_EXTNL_REF_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty_lctr_xref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
