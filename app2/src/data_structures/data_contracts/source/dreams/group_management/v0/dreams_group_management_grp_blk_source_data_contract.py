"""Source Data Contract for Dreams Group Management Group Block"""
from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Block Data"""

    blk_cd: str = Field(
        ...,
        alias="BLK_CD",
        name="",
        description="",
        example="G0835233",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0835233",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_blk_ppty_sync_in: str = Field(
        ...,
        alias="GRP_BLK_PPTY_SYNC_IN",
        name="",
        description="",
        example="Y",
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


class DREAMSGroupManagementGrpBlkModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpBlkModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Block"
        stream_name = ""
        description = "This table just confirms that the Block code is the same as the Group code"
        unique_identifier = ["data.BLK_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = ""

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
