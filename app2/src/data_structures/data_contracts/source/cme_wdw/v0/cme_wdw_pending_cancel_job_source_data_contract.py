"""Source Data Contract for CME WDW Pending Cancel Job"""


from __future__ import annotations

from datetime import datetime, date
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    id: int = Field(
        ...,
        alias="id",
        name="Record Identifier",
        description="",
        example=5702899,
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    reservation_id: int = Field(
        ...,
        alias="reservation_id",
        name="Reservation Identifier",
        description="Reservation Identifier",
        example=66993791,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    send_guest_email: Optional[int] = Field(
        None,
        alias="send_guest_email",
        name="Send Guest Email",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exp_date: date = Field(
        ...,
        alias="exp_date",
        name="Expiration Date",
        description="Job expiration date",
        example="2023-05-28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    retry_count: Optional[int] = Field(
        None,
        alias="retry_count",
        name="Retry Count",
        description="Retry count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="Record status",
        example="COMPLETED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created: datetime = Field(
        ...,
        alias="created",
        name="Created",
        description="Record created date timestamp",
        example="2023-04-25T14:21:14Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_updated: datetime = Field(
        ...,
        alias="lastUpdated",
        name="Last Updated",
        description="Record last updated date timestamp",
        example="2023-04-25T14:53:23Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="",
        example="SNAPP_VOIDED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWPendingCancelJobModel(BaseModel):
    """CME WDW Pending Cancel Job Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Pending Cancel Job"
        stream_name = ""  # Info not yet available
        description = ""  # optional
        unique_identifier = ["data.id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table_name"
        key_path_value = "pending_cancel_job"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
