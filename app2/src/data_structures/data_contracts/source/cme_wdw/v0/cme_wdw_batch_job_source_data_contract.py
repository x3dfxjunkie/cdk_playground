"""Source Data Contract Template for CME WDW Batch Job"""

from __future__ import annotations

from datetime import datetime
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2023-08-18T13:42:59Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=1234,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inventory_override: int = Field(
        ...,
        alias="inventoryOverride",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_updated: datetime = Field(
        ...,
        alias="lastUpdated",
        name="",
        description="",
        example="2023-08-18T13:53:20Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    owner_email: str = Field(
        ...,
        alias="ownerEmail",
        name="",
        description="",
        example="mickey.mouse@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    reservation_origin: str = Field(
        ...,
        alias="reservationOrigin",
        name="",
        description="",
        example="Bulk Upload Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="PROCESSING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    swid: str = Field(
        ...,
        alias="swid",
        name="",
        description="",
        example="",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWBatchJobModel(BaseModel):
    """Payload class for CME WDW Batch Job Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Batch Job"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "batch_job"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
