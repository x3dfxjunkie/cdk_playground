"""Source Data Contract for Dreams Resource Inventory Management Room Category Room"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Room Category Room"""

    rm_ctgy_nm: str = Field(
        ...,
        alias="RM_CTGY_NM",
        name="",
        description="",
        example="CONCIERGE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=20407,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRmCtgyRmModel(BaseModel):
    """Payload Class for Dreams Resource Inventory Management Room Category Room"""

    class Config:
        """Payload Level Metadata"""

        title = "Room Category Room"
        stream_name = ""
        description = """This table ties a room category to the reservable resource ID.
SUITE
VIRTUAL_ROOM
DEFAULT_PARENT
TURN_DOWN
CONCIERGE"""
        unique_identifier = ["data.RM_CTGY_NM", "data.RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rm_ctgy_rm"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
