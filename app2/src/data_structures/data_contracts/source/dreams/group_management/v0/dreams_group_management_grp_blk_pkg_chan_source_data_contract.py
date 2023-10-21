"""Source Data Contract for Dreams Group Management Group Block Package Channel"""
from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Block Package Channel Data"""

    blk_cd: str = Field(
        ...,
        alias="BLK_CD",
        name="",
        description="",
        example="G0835334",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_chan_id: int = Field(
        ...,
        alias="PKG_CHAN_ID",
        name="",
        description="",
        example=8818071,
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


class DREAMSGroupManagementGrpBlkPkgChanModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpBlkPkgChanModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Block Package Channel"
        stream_name = ""
        description = "Last Load 01/21/2022"
        unique_identifier = ["data.BLK_CD", "data.PKG_CHAN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_blk_pkg_chan"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
