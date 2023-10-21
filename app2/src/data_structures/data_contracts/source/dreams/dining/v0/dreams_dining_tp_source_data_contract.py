"""Source Data Contract for Dreams Dining TP"""
from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
    GlobalDreamsTpId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
)
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Data(GlobalDreamsTpId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams Dining TP Data"""

    tp_strt_dt: datetime = Field(
        ...,
        alias="TP_STRT_DT",
        name="Travel Party Start Date Time",
        description="Effective date and time for when a travel component, a product or service, can be used",
        example="2023-05-06T00:00:00Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tp_end_dt: datetime = Field(
        ...,
        alias="TP_END_DT",
        name="Travel Party End Date Time",
        description="Last date and time that a product or service can be actively used.",
        example="2023-05-11T00:00:00Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTpModel(BaseModel):
    """Payload class for DREAMSDiningTpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan"
        stream_name = "guest360-dreams-resm-stream"
        description = "This is the highest level of the guest Travel Plan, it ties together any room reservations or dining reservations associated to said Travel Plan. It includes the Travel Plan start and end dates"
        unique_identifier = ["data.TP_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "TP"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
