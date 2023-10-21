"""Source Data Contract Template for AggReport"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """Data payload for Agg Report"""

    avail_invtry: int = Field(
        ...,
        alias="avail_invtry",
        name="",
        description="",
        example=11,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    booked: int = Field(
        ...,
        alias="booked",
        name="",
        description="",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    business_date: date = Field(
        ...,
        alias="business_date",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cancelled: int = Field(
        ...,
        alias="cancelled",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    consumed: int = Field(
        ...,
        alias="consumed",
        name="",
        description="",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_time: datetime = Field(
        ...,
        alias="end_time",
        name="",
        description="",
        example="2023-09-12T13:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_booked_time: Optional[datetime] = Field(
        None,
        alias="last_booked_time",
        name="",
        description="",
        example="2023-09-12T12:30:02.206004Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location: str = Field(
        ...,
        alias="location",
        name="",
        description="",
        example="Award Wieners",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meal_period: str = Field(
        ...,
        alias="meal_period",
        name="",
        description="",
        example="Award Wieners Lunch And Dinner",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mobile_order: int = Field(
        ...,
        alias="mobile_order",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modified: int = Field(
        ...,
        alias="modified",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    park: str = Field(
        ...,
        alias="park",
        name="",
        description="",
        example="Disney California Adventure Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    planned_unit: int = Field(
        ...,
        alias="planned_unit",
        name="",
        description="",
        example=21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_time: datetime = Field(
        ...,
        alias="start_time",
        name="",
        description="",
        example="2023-09-12T12:30:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MobileOrderDLRArrvlWndwAggReportModel(BaseModel):
    """Payload class for MobileOrderDLRArrvlWndwAggReportModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Agg Report"
        stream_name = ""
        description = ""
        unique_identifier = ["data.business_date", "data.meal_period"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "agg_report"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
