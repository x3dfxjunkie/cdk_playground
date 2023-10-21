"""Source Data Contract for Dreams Resource Inventory Management Assigned Owner Guaranteed Feature"""

from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Assigned Owner Guaranteed Feature"""

    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=111111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=253,
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


class DREAMSResourceInventoryManagementAsgnOwnrGuarFeatModel(BaseModel):

    """Payload class for Dreams Resource Inventory Management Assigned Owner Guaranteed Feature"""

    class Config:
        """Payload Level Metadata"""

        title = "Assigned Owner Guaranteed Feature"
        stream_name = ""
        description = """This table links the assigned owner ID to Feature IDs that are guaranteed to be fulfilled"""
        unique_identifier = ["data.FEAT_ID", "data.ASGN_OWNR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "asgn_ownr_guar_feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
