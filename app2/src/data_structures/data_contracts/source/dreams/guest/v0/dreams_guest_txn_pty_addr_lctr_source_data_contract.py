"""Source Data Contract Template for txn_pty_addr_lctr.json"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data class for txn_pty_addr_lctr"""

    txn_pty_addr_lctr_id: int = Field(
        ...,
        alias="TXN_PTY_ADDR_LCTR_ID",
        name="",
        description="",
        example=911025206,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    addr_ln_1_tx: str = Field(
        ...,
        alias="ADDR_LN_1_TX",
        name="",
        description="",
        example="5552 Maryport Dr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    addr_ln_2_tx: Optional[str] = Field(
        None,
        alias="ADDR_LN_2",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    city_nm: str = Field(
        ...,
        alias="CITY_NM",
        name="",
        description="",
        example="Huntington Beach",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgn_cd: Optional[str] = Field(
        None,
        alias="RGN_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rgn_nm: Optional[str] = Field(
        None,
        alias="RGN_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pstl_cd: Optional[str] = Field(
        None,
        alias="PSTL_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    allow_mail_in: str = Field(
        ...,
        alias="ALLOW_MAIL_IN",
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
        example="TbxSync-DLRU",
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
        example="TbxSync-DLRU",
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
    allow_mail_ind: Optional[str] = Field(
        None,
        alias="ALLOW_MAIL_IND",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestTxnPtyAddrLctrModel(BaseModel):
    """DREAMSGuestTxnPtyAddrLctrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Party Address Locator"
        stream_name = ""
        description = "This holds Address locator IDs and Address information"  # optional
        unique_identifier = ["data.TXN_PTY_ADDR_LCTR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_pty_addr_lctr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
