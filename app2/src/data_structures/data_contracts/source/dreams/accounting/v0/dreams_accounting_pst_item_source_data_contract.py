"""Source Data Contract for DREAMS Post Item"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Post Item Data"""

    pst_item_id: int = Field(
        ...,
        alias="PST_ITEM_ID",
        name="",
        description="",
        example=20001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_item_typ_nm: str = Field(
        ...,
        alias="PST_ITEM_TYP_NM",
        name="",
        description="",
        example="Accounts Receivable",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T06:00:30.101Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingPstItemModel(BaseModel):
    """Payload class for DREAMSAccountingPstItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Post Item"
        stream_name = ""
        description = """List of Post item names associated to Post Item IDs"""
        unique_identifier = ["data.PST_ITEM_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PST_ITEM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
