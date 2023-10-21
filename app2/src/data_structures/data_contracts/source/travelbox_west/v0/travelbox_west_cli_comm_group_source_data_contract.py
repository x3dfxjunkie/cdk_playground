"""Source Data Contract Template for CLI_COMM_GROUP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_COMM_GROUP Data
    """

    REF_CODE: Optional[str] = Field(
        None,
        alias="REF_CODE",
        name="",
        description="""NaN""",
        example="""F9500CE4""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_GROUP_ID: int = Field(
        ...,
        alias="COMM_GROUP_ID",
        name="",
        description="""System generated id of the CommGroup (Client Commission Group)""",
        example=2106,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Wholesale: Internet Aggregator""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_PRIORITY: str = Field(
        ...,
        alias="SALES_PRIORITY",
        name="",
        description="""Flag to indicate if the priority is given to Sales (1) or Pax (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: Optional[str] = Field(
        None,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_DATE_TYPE: str = Field(
        ...,
        alias="APPLICABLE_DATE_TYPE",
        name="",
        description="""Flag to indicate if the applicable date  is a Booking Date (1) or a Travel Date (0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_PRODUCT: str = Field(
        ...,
        alias="APPLICABLE_PRODUCT",
        name="",
        description="""Flag to indicate if the applicable type is for Products (1) or for Product Combinations (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_LIMIT_BOOKING: str = Field(
        ...,
        alias="APPLICABLE_LIMIT_BOOKING",
        name="",
        description="""Flag to indicate if the applicable booking limit is for a Single Booking (1) or Bookings in a Period (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNAL_REF: Optional[str] = Field(
        None,
        alias="EXTERNAL_REF",
        name="",
        description="""references to any Commission Group that is setup in a third party travelbox system.""",
        example="""TOIA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COM_GRP_PRIORITY: int = Field(
        ...,
        alias="COM_GRP_PRIORITY",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_COMM_GROUP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:15.867756""",
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
        example="""CLI_COMM_GROUP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=57258307416457,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliCommGroupModel(BaseModel):
    """
    Payload class for TravelBox CLI_COMM_GROUP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Commission Group"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store Client Commission Group information."""  # optional
        unique_identifier = ["data.COMM_GROUP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_COMM_GROUP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
