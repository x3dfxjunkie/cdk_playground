"""Source Data Contract for CME WDW Shedlock"""
from __future__ import annotations
from typing import Optional
from datetime import datetime

from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    name: str = Field(
        ...,
        alias="name",
        name="Name",
        description="Scheduled / system job name",
        example="TaskScheduler_scheduledTask",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    lock_until: Optional[datetime] = Field(
        None,
        alias="lock_until",
        name="Lock Until",
        description="Job to be locked until specified date/time",
        example="2023-04-30T19:05:00.001",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    locked_at: Optional[datetime] = Field(
        None,
        alias="locked_at",
        name="Locked At",
        description="Job locked at specified dateto,e",
        example="2023-04-30T09:05:00.001",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    locked_by: Optional[str] = Field(
        None,
        alias="locked_by",
        name="Locked By",
        description="user/system reference that locked a specific job",
        example="a1aabb12345a",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class CMEWDWShedlockModel(BaseModel):
    """CME WDW Shedlock Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Shedlock"
        stream_name = ""  # info not available yet
        description = ""
        unique_identifier = ["data.name"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "shedlock"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
