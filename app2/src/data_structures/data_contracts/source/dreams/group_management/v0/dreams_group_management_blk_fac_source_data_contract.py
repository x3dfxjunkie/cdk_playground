"""Source Data Contract for Dreams Group Management Block Facility"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams Group Management Block Facility Data"""

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_cd: str = Field(
        ...,
        alias="BLK_CD",
        name="",
        description="",
        example="G0825390",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_fac_seq_nb: int = Field(
        ...,
        alias="BLK_FAC_SEQ_NB",
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
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementBlkFacModel(BaseModel):
    """Payload class for DREAMSGroupManagementBlkFacModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Block Facility"
        stream_name = ""
        description = "When a group/convention plans a visit to WDW and they plan on staying at a resort a Block of rooms is set aside for them, this table provides the facility ID associated to the Block code and the sequence of use if more than 1 facility is associated"
        unique_identifier = ["data.FAC_ID", "data.BLK_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "blk_fac"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
