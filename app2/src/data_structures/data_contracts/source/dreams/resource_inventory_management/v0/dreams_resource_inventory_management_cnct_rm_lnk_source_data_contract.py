"""Source Data Contract for Dreams Resource Inventory Management Connecting Rooms Link"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Connecting Rooms Link"""

    cnctd_rsrc_id: int = Field(
        ...,
        alias="CNCTD_RSRC_ID",
        name="",
        description="",
        example=22966,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cnctg_rsrc_id: int = Field(
        ...,
        alias="CNCTG_RSRC_ID",
        name="",
        description="",
        example=22967,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementCnctRmLnkModel(BaseModel):
    """Payload class for Dreams Resource Inventory Management Connecting Rooms Link"""

    class Config:
        """Payload Level Metadata"""

        title = "Connecting Rooms Link"
        stream_name = ""
        description = """This table holds the IDs of rooms that connect"""
        unique_identifier = ["data.CNCTD_RSRC_ID", "data.CNCTG_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cnct_rm_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
