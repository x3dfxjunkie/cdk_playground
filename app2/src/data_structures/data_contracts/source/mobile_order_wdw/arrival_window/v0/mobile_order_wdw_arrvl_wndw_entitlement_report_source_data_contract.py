"""Source Data Contract Template for Arrival Window Entitlement Report"""

from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import date, datetime
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """Data Payload for Entitlement Report"""

    booking_opened: datetime = Field(
        ...,
        alias="booking_opened",
        name="",
        description="",
        example="2023-09-12T12:17:48.830098Z",
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

    end_time: datetime = Field(
        ...,
        alias="end_time",
        name="",
        description="",
        example="2023-09-12T13:40:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest: str = Field(
        ...,
        alias="guest",
        name="",
        description="",
        example="{AAAAAAAA-BBBB-CCCC-DDDD-EE0123456789}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location: str = Field(
        ...,
        alias="location",
        name="",
        description="",
        example="Jolly Holiday Bakery Caf\xe9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meal_period: str = Field(
        ...,
        alias="meal_period",
        name="",
        description="",
        example="Jolly Holiday Bakery Caf\xe9 Lunch And Dinner",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    order_id: int = Field(
        ...,
        alias="order_id",
        name="",
        description="",
        example=12345678,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_time: datetime = Field(
        ...,
        alias="start_time",
        name="",
        description="",
        example="2023-09-12T13:10:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="RED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_date: datetime = Field(
        ...,
        alias="updated_date",
        name="",
        description="",
        example="2023-09-12T15:17:48.835842Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MobileOrderWDWArrvlWndwEntitlementReportModel(BaseModel):
    """Payload class for MobileOrderWDWArrvlWndwEntitlementReportModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Report"
        stream_name = ""
        description = ""
        unique_identifier = ["data.order_id"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "enttl_report"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
