"""Source Data Contract Template for AIM_BLOCK_INVENTORY"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIM_BLOCK_INVENTORY Data
    """

    blk_code: str = Field(
        ...,
        alias="BLK_CODE",
        name="",
        description="Block code",
        example="GTA001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accom_code: str = Field(
        ...,
        alias="ACCOM_CODE",
        name="",
        description="Resort code",
        example="FALCH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    room_code: str = Field(
        ...,
        alias="ROOM_CODE",
        name="",
        description="Room Code",
        example="CW4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rate_code: str = Field(
        ...,
        alias="RATE_CODE",
        name="",
        description="Rate Code",
        example="GEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_date: datetime = Field(
        ...,
        alias="SERVICE_DATE",
        name="",
        description="Service Date",
        example="2023-09-29T18:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_inv_count: Optional[int] = Field(
        None,
        alias="BLOCK_INV_COUNT",
        name="",
        description="Block count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_alot_count: Optional[int] = Field(
        None,
        alias="BLOCK_ALOT_COUNT",
        name="",
        description="Allotment Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    book_count: Optional[int] = Field(
        None,
        alias="BOOK_COUNT",
        name="",
        description="Book Count",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hold_count: Optional[int] = Field(
        None,
        alias="HOLD_COUNT",
        name="",
        description="Freeze count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    blk_inv_wash_factor: Optional[float] = Field(
        None,
        alias="BLK_INV_WASH_FACTOR",
        name="",
        description="Wash Factor",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bk_blk_impact_count: Optional[int] = Field(
        None,
        alias="BK_BLK_IMPACT_COUNT",
        name="",
        description="Book Block Impact Count",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bk_alot_impact_count: Optional[int] = Field(
        None,
        alias="BK_ALOT_IMPACT_COUNT",
        name="",
        description="Book Allotment Impact Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_brw_impact_count: Optional[int] = Field(
        None,
        alias="PRNT_BRW_IMPACT_COUNT",
        name="",
        description="Parent Borrowed Impact Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_date: datetime = Field(
        ...,
        alias="CREATED_DATE",
        name="",
        description="Date Created",
        example="2023-09-13T18:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_user: Optional[str] = Field(
        None,
        alias="CREATED_USER",
        name="",
        description="Created user",
        example="System",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modified_date: datetime = Field(
        ...,
        alias="MODIFIED_DATE",
        name="",
        description="Last modified date",
        example="2023-09-30T18:02:12.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modified_user: Optional[str] = Field(
        None,
        alias="MODIFIED_USER",
        name="",
        description="Last Modified User",
        example="System",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    syatem_created: str = Field(
        ...,
        alias="SYATEM_CREATED",
        name="",
        description="Whether the inventory record is created manually or system generated",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trim_count: int = Field(
        ...,
        alias="TRIM_COUNT",
        name="",
        description="Last trim amount from the schedule run",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modification_type: Optional[str] = Field(
        None,
        alias="MODIFICATION_TYPE",
        name="",
        description="Modification type default set to NOTSET",
        example="NOT_SET",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    book_limit: Optional[int] = Field(
        None,
        alias="BOOK_LIMIT",
        name="",
        description="NA",
        example=23,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    root_brw_impact_count: Optional[int] = Field(
        None,
        alias="ROOT_BRW_IMPACT_COUNT",
        name="",
        description="NA",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AIM_BLOCK_INVENTORY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:30.613078""",
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
        example="""AIM_BLOCK_INVENTORY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=92646681613482,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAimBlockInventoryModel(BaseModel):
    """
    Payload class for TravelBox AIM_BLOCK_INVENTORY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Inventory Management Block Inventory"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = "Block Inventory"  # optional
        unique_identifier = [
            "data.BLK_CODE",
            "data.ACCOM_CODE",
            "data.ROOM_CODE",
            "data.RATE_CODE",
            "data.SERVICE_DATE",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIM_BLOCK_INVENTORY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
