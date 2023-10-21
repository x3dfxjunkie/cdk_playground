"""Source Data Contract Template for RES_BOOKING_FEE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_FEE Data
    """

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example="""SNGNdWksemeDJDOGsHBp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1993-05-09 05:19:27""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FEE_CODE_INDEX: int = Field(
        ...,
        alias="FEE_CODE_INDEX",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_USER: Optional[int] = Field(
        None,
        alias="MODIFIED_USER",
        name="",
        description="""Remittance record modified user id""",
        example=201,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=10121559,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FEE_CODE: str = Field(
        ...,
        alias="FEE_CODE",
        name="",
        description="""Reserved for future implementations""",
        example="""FEAFN2LBK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST: float = Field(
        ...,
        alias="COST",
        name="",
        description="""Debit credit note cost amount_x000D_
- If credit negative value_x000D_
- If debit positive value""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE: float = Field(
        ...,
        alias="PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=15.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_COST: Optional[float] = Field(
        None,
        alias="ADT_COST",
        name="",
        description="""Adult cost of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_PRICE: Optional[float] = Field(
        None,
        alias="ADT_PRICE",
        name="",
        description="""Adult price of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_COST: Optional[float] = Field(
        None,
        alias="CHD_COST",
        name="",
        description="""Adult cost of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_PRICE: Optional[float] = Field(
        None,
        alias="CHD_PRICE",
        name="",
        description="""Adult price of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_COST: Optional[float] = Field(
        None,
        alias="INF_COST",
        name="",
        description="""Adult cost of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_PRICE: Optional[float] = Field(
        None,
        alias="INF_PRICE",
        name="",
        description="""Adult price of the booking fee (fee types are pre setup in table FEE_TYPE )""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_FEE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:48:24.139069""",
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
        example="""RES_BOOKING_FEE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=73522733120758,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResBookingFeeModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_FEE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Fee"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table holds the information related to Fees applicable for bookings. Booking Fees can be applied manualy or automatically from Reservation module"""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.FEE_CODE", "data.FEE_CODE_INDEX"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_FEE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
