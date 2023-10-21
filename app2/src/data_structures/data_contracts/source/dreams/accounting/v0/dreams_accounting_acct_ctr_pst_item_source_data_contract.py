"""Source Data Contract for DREAMS Accounting ACCT_CTR_PST_ITEM"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Accounting - Account Center Post Item Data"""

    acct_ctr_pst_item_id: int = Field(
        ...,
        alias="ACCT_CTR_PST_ITEM_ID",
        name="",
        description="",
        example=1117700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_item_id: int = Field(
        ...,
        alias="PST_ITEM_ID",
        name="",
        description="",
        example=211300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_ctr_pst_item_ds: Optional[str] = Field(
        None,
        alias="ACCT_CTR_PST_ITEM_DS",
        name="",
        description="",
        example="Trader Sam's Mixology Seminar - Tax_POSTING_ITEM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-01-11T11:17:24.590508Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-01-11T11:11:24.590508Z",
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


class DREAMSAccountingAcctCtrPstItemModel(BaseModel):
    """Payload class for DREAMSAccountingAcctCtrPstItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Account Center Post Item"
        stream_name = ""
        description = "This table associates the post item ID and the post item description"
        unique_identifier = ["data.ACCT_CTR_PST_ITEM_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "acct_ctr_pst_item"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
