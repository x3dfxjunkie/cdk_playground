"""Source Data Contract for CME DLR Checkpoint Location"""
from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)

from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    id: int = Field(
        ...,
        alias="id",
        name="Record Identifier",
        description="Record Identifier",
        example=12345678,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reservation_id: str = Field(
        ...,
        alias="reservation_id",
        name="Reservation Identifier",
        description="Reservation ID the record is referencing",
        example="999340954407116999",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    facility: Optional[str] = Field(
        None,
        alias="facility",
        name="Facility",
        description="Parent facility of the checkpoint location",
        example="DLP_DP",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    checkpoint_location: Optional[str] = Field(
        None,
        alias="checkpoint_location",
        name="Checkpoint Locaton",
        description="Checkpoint location",
        example="NODE-007",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reported_dts: datetime = Field(
        ...,
        alias="reported_dts",
        name="Reported Date Timestamp",
        description="Record reported date timestamp",
        example="2023-04-30T12:06:39Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reported_by: str = Field(
        ...,
        alias="reportedBy",
        name="Reported By",
        description="Record reported by",
        example="ParkPass",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRCheckpointLocationModel(BaseModel):
    """CME Checkpoint DLR Location Class"""

    class Config:
        """Payload Level Metadata"""

        name = "Checkpoint Location"
        stream_name = ""  # info not available yet
        description = ""
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "checkpoint_location"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
