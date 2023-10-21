"""Source Data Contract for Dreams Resource Inventory Management RM SEQ"""


from __future__ import annotations
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2022-07-23T14:19:39.836000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CTASK8667905",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rm_seq_nb: int = Field(
        ...,
        alias="RM_SEQ_NB",
        name="",
        description="",
        example=5219,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=22651,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrt_seq_id: int = Field(
        ...,
        alias="RSRT_SEQ_ID",
        name="",
        description="",
        example=23,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRmSeqModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRmSeqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Room Sequence"
        stream_name = ""
        description = "Room sequence IDs associated to reservable resource IDs"
        unique_identifier = ["data.RSRC_ID", "data.RSRT_SEQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rm_seq"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
