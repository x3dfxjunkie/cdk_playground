"""Source Data Contract for CME WDW Res Guest Links"""
from __future__ import annotations
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)


class Data(BaseModel):
    """Class data"""

    id: int = Field(
        ...,
        alias="id",
        name="Record Identifier",
        description="Auto-Increment Record Identifier",
        example=12345678,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    reservation_id: str = Field(
        ...,
        alias="reservation_id",
        name="Reservation Table Record Identifier",
        description="Record Identifier for the Reservation (Not reservation id)",
        example="51191889",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    swid: Optional[str] = Field(
        None,
        alias="swid",
        name="Starwave ID",
        description="Registered Guest Starwave ID",
        example="{2490CA47-AAAA-BBBB-9397-84F343B7B726}",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    guid: Optional[UUID] = Field(
        None,
        alias="uuid",
        name="Unmanaged Guest Identifier",
        description="Unique guest identifier for unmanaged guest accounts",
        example=UUID("7b1b63cf-3247-9c75-71e2-ee40b29221f7"),
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    resort_res_id: Optional[str] = Field(
        None,
        alias="resort_res_id",
        name="Resort Reservation Identifier",
        description="Associated Resort Reservation identifier from TBX / Wholesaler Reservation If populated",
        example="24242424",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    tp_seg_id: Optional[str] = Field(
        None,
        alias="tpsegid",
        name="Travel Plan Segment Identifier",
        description="Associated Travel Plan Segment identifier from DREAMs (resort reservation) for the guest",
        example="521123333333",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=True,
    )
    tg_id: Optional[str] = Field(
        None,
        alias="tgid",
        name="Travel Guest Identifier",
        description="Guest Identifier from DREAMs",
        example="123456789",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    alt_guest_id: Optional[str] = Field(
        None,
        alias="alt_guest_id",
        name="Alternatie Guest Identifier",
        description="Alternate guest identifier",
        example="90ZAECHS1RGE2ZBBBAAA",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    alt_guest_id_type: Optional[str] = Field(
        None,
        alias="alt_guest_id_type",
        name="Alternate Guest Identifier Type",
        description="specifies the type of alternate guest identifier",
        example="ADMISSION_LINK_ID",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    pending_cancel_job_id: Optional[int] = Field(
        None,
        alias="pending_cancel_job_id",
        name="Pending Cancel Job Record Identifier",
        description="specifies Pending Cancel Job record identifier that processes cancellations from related products like tickets/packages",
        example=10020302,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEWDWResGuestLinksModel(BaseModel):
    """CME Reservation Guest Links Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Guest Links"
        stream_name = ""  # info not available yet
        description = "Reservation Guest Link table providing guest identifiers to specific guests for the corresponding reservation"
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "res_guest_links"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
