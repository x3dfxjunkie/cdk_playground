"""Source Data Contract Template for Mediadownloads"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Class for DPI-East Mediadownloads data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=136743,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2019-03-15T18:40:26Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2019-03-15T18:40:26Z",
        guest_identifier=False,
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

    expirationdate: datetime = Field(
        ...,
        alias="expirationdate",
        name="",
        description="",
        example="2020-05-15T00:00:00Z",
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
        example="WDW_WEB_MEMORY_MAKER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    download_type: str = Field(
        ...,
        alias="download_type",
        name="",
        description="",
        example="multiple",
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
        example="41947204-018c-4541-9ca7-ff5c687112ef/f5b1e6df-b93d-4847-a191-ccc04aec1d10.jpg",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_guestmediaid: int = Field(
        ...,
        alias="job_guestmediaid",
        name="",
        description="",
        example=112587,
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

    job_request_id: str = Field(
        ...,
        alias="job_request_id",
        name="",
        description="",
        example="d2ad9a7b-a4b5-4019-8e40-3b37e50c8f8a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    job_status: str = Field(
        ...,
        alias="job_status",
        name="",
        description="",
        example="failed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    platform: str = Field(
        ...,
        alias="platform",
        name="",
        description="",
        example="MXP_WEB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    swid: str = Field(
        ...,
        alias="swid",
        name="",
        description="",
        example="{AAAAAAAA-ABCD-ABCD-ABCD-111111111111}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=9277,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastMediadownloadsModel(BaseModel):
    """Payload class for DPIEastMediadownloadsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Mediadownloads"
        stream_name = ""
        description = "Mediadownloads"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "mediadownloads"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
