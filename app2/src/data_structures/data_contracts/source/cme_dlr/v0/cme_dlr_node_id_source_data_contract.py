"""Source Data Contract Template for CME DLR Node ID"""


from __future__ import annotations
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_id: int = Field(
        ...,
        alias="max_id",
        name="",
        description="",
        example=2612,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRNodeIdModel(BaseModel):
    """Payload class for CMEDLRNodeIdModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Node Identifier"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "node_id"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
