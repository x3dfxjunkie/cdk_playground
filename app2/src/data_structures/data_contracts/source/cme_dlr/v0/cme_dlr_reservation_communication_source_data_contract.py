"""Source Data Contract for CME DLR Reservation Communication"""
from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    conf_id: int = Field(
        ...,
        alias="conf_id",
        name="Confirmation Identifier",
        description="Confirmation Identifier that is linked to Reservation",
        example=123123123123123123,
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    um_broadcast_id: str = Field(
        ...,
        alias="um_broadcast_id",
        name="Broadcast Identifier",
        description="TBD - Communication unique identifier",
        example="88888888-aaaa-bbbb-cccc-888888888888",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="TBD - status of the corresponding reservation",
        example="CANCELED",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    status_desc: Optional[str] = Field(
        None,
        alias="status_desc",
        name="Status Description",
        description="Status Description",
        example="The reservation has been canceled.",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    retry_count: int = Field(
        ...,
        alias="retry_count",
        name="Retry Count",
        description="TBD - count of times communication has been retried",
        example=0,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    created_dts: datetime = Field(
        ...,
        alias="created_dts",
        name="Created Date Timestamp",
        description="Record created date timestamp",
        example="2023-03-10T16:10:21Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="Created User",
        description="User or Application that created the record",
        example="f-cme-reservation",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    updated_dts: Optional[datetime] = Field(
        None,
        alias="updated_dts",
        name="Updated Date Timestamp",
        description="Record updated Date Timestamp",
        example="2023-05-01T18:06:24.913324Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    updated_usr: Optional[str] = Field(
        None,
        alias="updated_usr",
        name="Updated User",
        description="Application/User who last updated the record",
        example="f-cme-reservation",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEDLRReservationCommunicationModel(BaseModel):
    """CME DLR Reservation Communication Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Communication"
        stream_name = ""  # info not available yet
        description = ""
        unique_identifier = ["data.conf_id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "reservation_communication"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
