"""Source Data Contract for CME DLR Destination"""
from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)


class Data(BaseModel):
    """Class data"""

    id: str = Field(
        ...,
        alias="id",
        name="Destination Identifier",
        description="Identifies destination by a CME internal identifier",
        example="DLR",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    name: str = Field(
        ...,
        alias="name",
        name="Destination Name",
        description="identifies destination by CME internal name",
        example="Disneyland Resort",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    time_zone: str = Field(
        ...,
        alias="time_zone",
        name="Destination's time zone",
        description="identifies destination's time zone",
        example="America/Los_Angeles",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRDestinationModel(BaseModel):
    """CME DLR Destination Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Destination"
        stream_name = ""  # info not available yet
        description = "Internal Lookup table for Destination ID"  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "destination"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
