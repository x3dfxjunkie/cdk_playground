"""Source Data Contract Template for RES_INSURANCE_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_INSURANCE_BOOKING Data
    """

    ORIGINAL_BOOK_DATE: Optional[datetime] = Field(
        None,
        alias="ORIGINAL_BOOK_DATE",
        name="",
        description="""NaN""",
        example="""2018-06-14 20:50:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=15247346,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: int = Field(
        ...,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""INS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POLICY_CODE: str = Field(
        ...,
        alias="POLICY_CODE",
        name="",
        description="""The system code of the policy type of the booking""",
        example="""TI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAMILY: str = Field(
        ...,
        alias="FAMILY",
        name="",
        description="""A flag to indicate whether this is a family insurance or not. This setup is in Insurance Manager.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANNUAL: str = Field(
        ...,
        alias="ANNUAL",
        name="",
        description="""A flag to indicate whether this is an annual insurance or not. This setup is in Insurance Manager.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SENIORS: int = Field(
        ...,
        alias="SENIORS",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX: float = Field(
        ...,
        alias="TAX",
        name="",
        description="""Total tax for the booking""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REGION_GROUP_NO: int = Field(
        ...,
        alias="REGION_GROUP_NO",
        name="",
        description="""Region group number of the selected region from the region groups in insurance contract. This setup is in Insurance Manager.""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_DURATION: int = Field(
        ...,
        alias="MIN_DURATION",
        name="",
        description="""Minimum Duration for booking""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_DURATION: int = Field(
        ...,
        alias="MAX_DURATION",
        name="",
        description="""The maximum duration of the holiday that is covered from insurance policy""",
        example=30,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_PRICE: float = Field(
        ...,
        alias="MIN_PRICE",
        name="",
        description="""Minimum price associated with insurance policy price range entry""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_PRICE: float = Field(
        ...,
        alias="MAX_PRICE",
        name="",
        description="""Maximum price associated with insurance policy price range entry""",
        example=1000000.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_PRODUCTS: Optional[str] = Field(
        None,
        alias="VALID_PRODUCTS",
        name="",
        description="""Deprecated""",
        example="""fdmnvdEzgnBgCRgApJAh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIR_ONLY: str = Field(
        ...,
        alias="AIR_ONLY",
        name="",
        description="""Specifies whether the contract insurance policy is air only or not_x000D_
Air only - 1, Not air only - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SENIOR_ADULT: Optional[int] = Field(
        None,
        alias="SENIOR_ADULT",
        name="",
        description="""Number of senior adults in the insurance booking item.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POLICY_NAME: Optional[str] = Field(
        None,
        alias="POLICY_NAME",
        name="",
        description="""The name of the policy type of the booking""",
        example="""Travel Insurance""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1982-04-05 06:41:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_INSURANCE_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:22.487537""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    record_type: str = Field(
        ...,
        alias="record-type",
        name="",
        description="""Type of record""",
        example="""data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operation: str = Field(
        ...,
        alias="operation",
        name="",
        description="""Type of operation [insert, delete, update]""",
        example="""update""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="",
        description="""Partition key""",
        example="""schema-table""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="""Name of schema""",
        example="""TBX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""RES_INSURANCE_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=82335474812783,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResInsuranceBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_INSURANCE_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Insurance"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = (
            """This table contains all the Booking Item level information specif for insurance bookings."""  # optional
        )
        unique_identifier = ["data.BOOKING_ID", "data.ITEM_NO", "data.PRODUCT_CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_INSURANCE_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
