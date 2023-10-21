"""Source Data Contract for DPI-West Mediadownloads"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI-West Mediadownloads"""

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-09-07T13:07:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    customer_id: int = Field(
        ...,
        alias="customer_id",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    download_entitlement_name: str = Field(
        ...,
        alias="download_entitlement_name",
        name="",
        description="",
        example="GeniePlus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    download_type: str = Field(
        ...,
        alias="download_type",
        name="",
        description="",
        example="single",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expirationdate: datetime = Field(
        ...,
        alias="expirationdate",
        name="",
        description="",
        example="2024-11-07T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=129839194,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_download_attempts: int = Field(
        ...,
        alias="job_download_attempts",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_downloaded: int = Field(
        ...,
        alias="job_downloaded",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_filename: str = Field(
        ...,
        alias="job_filename",
        name="",
        description="",
        example="e1c55a50-3d88-44aa-a3b0-fb260cee138d/2032510308-59359400-20230903T121544-689537815-DSC_0791.JPG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_guestmedia_type: str = Field(
        ...,
        alias="job_guestmedia_type",
        name="",
        description="",
        example="high",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_guestmediaid: int = Field(
        ...,
        alias="job_guestmediaid",
        name="",
        description="",
        example=331315773,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_invoicenum: Optional[str] = Field(
        None,
        alias="job_invoicenum",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_request_id: str = Field(
        ...,
        alias="job_request_id",
        name="",
        description="",
        example="5c1c6ef0-7a5c-486a-940f-0a3006366079",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_size: Optional[str] = Field(
        None,
        alias="job_size",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_status: str = Field(
        ...,
        alias="job_status",
        name="",
        description="",
        example="done",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-09-07T13:07:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=229042048,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    platform: str = Field(
        ...,
        alias="platform",
        name="",
        description="",
        example="DLR_MOBILE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    swid: str = Field(
        ...,
        alias="swid",
        name="",
        description="",
        example="{AAAA67EA-DD32-4F35-9781-8FE4F553BBB2}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    version: int = Field(
        ...,
        alias="version",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIWestMediadownloadsModel(BaseModel):
    """Payload class for DPI-West Mediadownloads"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "mediadownloads"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
