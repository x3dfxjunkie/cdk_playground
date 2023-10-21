"""Source Data Contract for Dreams Resource Inventory Management Resource Feature"""


from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=13411,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcFeatModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcFeatModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Feature"
        stream_name = ""
        description = "This table connects the reservable resource and the feature IDs associated to it"
        unique_identifier = ["data.RSRC_ID", "data.FEAT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
