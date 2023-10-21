"""Source Data Contract Template for AIM_BASE_INVENTORY"""

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIM_BASE_INVENTORY Data
    """

    service_date: datetime = Field(
        ...,
        alias="SERVICE_DATE",
        name="",
        description="Date of the inventory",
        example="2023-12-31T18:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accom_code: str = Field(
        ...,
        alias="ACCOM_CODE",
        name="",
        description="Accommodation",
        example="15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    room_code: str = Field(
        ...,
        alias="ROOM_CODE",
        name="",
        description="Room type code",
        example="V5K",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auth_count: Optional[int] = Field(
        None,
        alias="AUTH_COUNT",
        name="",
        description="Authorization count",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_count: int = Field(
        ...,
        alias="BLOCK_COUNT",
        name="",
        description="Block count",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    book_count: Optional[int] = Field(
        None,
        alias="BOOK_COUNT",
        name="",
        description="Booked Count",
        example=0,
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

    boxed: Optional[str] = Field(
        None,
        alias="BOXED",
        name="",
        description="Is inventory boxed",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ooootm_count: Optional[int] = Field(
        None,
        alias="OOOOTM_COUNT",
        name="",
        description="Out Of Order Off The Market Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_adj_count: Optional[int] = Field(
        None,
        alias="BLOCK_ADJ_COUNT",
        name="",
        description="Block adjustment count",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    netting_adj_count: Optional[int] = Field(
        None,
        alias="NETTING_ADJ_COUNT",
        name="",
        description="Netting Adjustment Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified: datetime = Field(
        ...,
        alias="LAST_MODIFIED",
        name="",
        description="Last Modiied Date Time",
        example="2023-09-04T00:11:42.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_count: int = Field(
        ...,
        alias="BUILT_COUNT",
        name="",
        description="Physical count of the room type",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    manual_adj_count: int = Field(
        ...,
        alias="MANUAL_ADJ_COUNT",
        name="",
        description="Manual Adjustment Count",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    man_adj_user: Optional[str] = Field(
        None,
        alias="MAN_ADJ_USER",
        name="",
        description="NA",
        example="BANUM016",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    man_adj_date: Optional[datetime] = Field(
        None,
        alias="MAN_ADJ_DATE",
        name="",
        description="NA",
        example="2023-07-26T18:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ignore_los: str = Field(
        ...,
        alias="IGNORE_LOS",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified_l: Optional[int] = Field(
        None,
        alias="LAST_MODIFIED_L",
        name="",
        description="NA",
        example=1693831302772,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    man_adj_date_l: Optional[int] = Field(
        None,
        alias="MAN_ADJ_DATE_L",
        name="",
        description="NA",
        example=1690484400000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    closed_to_arrival: Optional[str] = Field(
        None,
        alias="CLOSED_TO_ARRIVAL",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fplos: Optional[str] = Field(
        None,
        alias="FPLOS",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    allowed_14_or_more: Optional[str] = Field(
        None,
        alias="ALLOWED_14_OR_MORE",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boxed_orig: str = Field(
        ...,
        alias="BOXED_ORIG",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ignore_los_orig: str = Field(
        ...,
        alias="IGNORE_LOS_ORIG",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_created: str = Field(
        ...,
        alias="AUTO_CREATED",
        name="",
        description="NA",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_child_adj_count: Optional[int] = Field(
        None,
        alias="BLOCK_CHILD_ADJ_COUNT",
        name="",
        description="NA",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AIM_BASE_INVENTORY Metadata
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
        example="""AIM_BASE_INVENTORY""",
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


class TravelBoxWestAimBaseInventoryModel(BaseModel):
    """
    Payload class for TravelBox AIM_BASE_INVENTORY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Inventory Management Base Inventory"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = "Base Inventory"  # optional
        unique_identifier = ["data.SERVICE_DATE", "data.ACCOM_CODE", "data.ROOM_CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIM_BASE_INVENTORY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
