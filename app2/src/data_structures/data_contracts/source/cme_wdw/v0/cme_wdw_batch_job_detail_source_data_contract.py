"""Source Data Contract Template for CME WDW Batch Job Detail"""

from __future__ import annotations

from datetime import datetime
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    batch_job_id: int = Field(
        ...,
        alias="batchJobId",
        name="",
        description="",
        example=1234,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2023-06-06T18:04:56Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=123456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_updated: datetime = Field(
        ...,
        alias="lastUpdated",
        name="",
        description="",
        example="2023-06-06T18:08:54Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    reservation_id: int = Field(
        ...,
        alias="reservationId",
        name="",
        description="",
        example=12345678,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="COMPLETED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWBatchJobDetailModel(BaseModel):
    """Payload class for CME WDW Batch Job Detail Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Batch Job Detail"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "batch_job_detail"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
