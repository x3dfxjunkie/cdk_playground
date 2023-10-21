"""Source Data Contract Template for AIM_ROOM_BUILT_COUNT"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIM_ROOM_BUILT_COUNT Data
    """

    supplier_id: int = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="NA",
        example=30103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    room_code: str = Field(
        ...,
        alias="ROOM_CODE",
        name="",
        description="room code",
        example="AA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    index_no: int = Field(
        ...,
        alias="INDEX_NO",
        name="",
        description="NA",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    from_date: datetime = Field(
        ...,
        alias="FROM_DATE",
        name="",
        description="NA",
        example="2016-06-20T06:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    to_date: datetime = Field(
        ...,
        alias="TO_DATE",
        name="",
        description="NA",
        example="2019-12-06T06:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified_time: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="The time at which the last modification has done",
        example="2023-03-15T11:02:32.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_count: Optional[int] = Field(
        None,
        alias="BUILT_COUNT",
        name="",
        description="built count",
        example=14,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AIM_ROOM_BUILT_COUNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:31.731692""",
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
        example="""AIM_ROOM_BUILT_COUNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=78869253490039,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastAimRoomBuiltCountModel(BaseModel):
    """
    Payload class for TravelBox AIM_ROOM_BUILT_COUNT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Inventory Management Room Built count"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = "Built Counts of a room"  # optional
        unique_identifier = ["data.SUPPLIER_ID", "data.ROOM_CODE", "data.INDEX_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIM_ROOM_BUILT_COUNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
