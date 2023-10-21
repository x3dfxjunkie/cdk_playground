"""Source Data Contract Template for CME DLR Swids To Merge"""

from __future__ import annotations

from datetime import datetime
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    aid: int = Field(
        ...,
        alias="aid",
        name="",
        description="",
        example=45,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="create_dts",
        name="",
        description="",
        example="2022-02-16T01:41:17Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ids_updated: int = Field(
        ...,
        alias="ids_updated",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    new_swid: str = Field(
        ...,
        alias="new_swid",
        name="",
        description="",
        example="{1A1A1A1A-1A1A-1A1A-1A1A-1A1A1A1A1A1A}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    old_swid: str = Field(
        ...,
        alias="old_swid",
        name="",
        description="",
        example="{1A1A1A1A-1A1A-1A1A-1A1A-1A1A1A1A1A1A}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRSwidsToMergeModel(BaseModel):
    """Payload class for CME DLR Swids To Merge Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Swids to Merge"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.aid"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "swids_to_merge"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
