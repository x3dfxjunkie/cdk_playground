"""Source Data Contract Template for ACT_CLIENT_IBTX"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_IBTX Data
    """

    TRIGGER_TYPE: Optional[str] = Field(
        None,
        alias="TRIGGER_TYPE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=1003984198,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_INDEX: int = Field(
        ...,
        alias="RECEIPT_INDEX",
        name="",
        description="""A foreign key which refers to the field RECEIPT_INDEX of the ACT_CLIENT_ACCOUNT_RECEIPT table""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FROM_BOOKING: int = Field(
        ...,
        alias="FROM_BOOKING",
        name="",
        description="""Booking id of the money credited booking (if own booking then value = -1)""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FROM_RECEIPT_INDEX: int = Field(
        ...,
        alias="FROM_RECEIPT_INDEX",
        name="",
        description="""Money credited booking receipt number""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TO_BOOKING: Optional[int] = Field(
        None,
        alias="TO_BOOKING",
        name="",
        description="""Booking id of the money debited booking (if own booking then value = -1)""",
        example=1003988584,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2009-07-09 18:49:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_IBTX Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:47:14.868563""",
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
        example="""ACT_CLIENT_IBTX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=53862551941748,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestActClientIbtxModel(BaseModel):
    """
    Payload class for TravelBox ACT_CLIENT_IBTX
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Client IBTX"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store information of IBTX payments. The values are setup in 'Search Receipts->
IBTX' in Accounts Client"""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.RECEIPT_INDEX",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACT_CLIENT_IBTX"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
