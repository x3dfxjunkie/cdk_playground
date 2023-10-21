"""Source Data Contract for CME DLR Reservation Note"""
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
        description="Reservation ID the reservation note is referencing",
        example="999340954407116999",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    note: Optional[str] = Field(
        None,
        alias="note",
        name="Note",
        description="Additional and optional notes relating to the reservation added by cast members",
        example="Guest unable to complete ticket purchase due to payment processing error. Assisted with reservation per leadership. CM has informed guest of the Terms & Conditions. Guest has agreed to them.",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reported_dts: datetime = Field(
        ...,
        alias="reported_dts",
        name="Reported Date Timestamp",
        description="Reservation Note reported date timestamp",
        example="2023-04-30T12:06:39Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reported_by: str = Field(
        ...,
        alias="reportedBy",
        name="Reported By",
        description="Reservation note reported by",
        example="mickey.mouse@disney.com",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRReservationNoteModel(BaseModel):
    """CME DLR Reservation Note Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Note"
        stream_name = ""  # info not available yet
        description = ""
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "reservation_note"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
