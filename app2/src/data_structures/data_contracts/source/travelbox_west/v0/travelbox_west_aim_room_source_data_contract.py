"""Source Data Contract Template for AIM_ROOM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIM_ROOM Data
    """

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2007-04-11 02:23:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHORT_NAME: Optional[str] = Field(
        None,
        alias="SHORT_NAME",
        name="",
        description="""NaN""",
        example="""Standard View  - Club Level """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INHERIT_PRICE: str = Field(
        ...,
        alias="INHERIT_PRICE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COSTING_BOARD_BASIS: Optional[str] = Field(
        None,
        alias="COSTING_BOARD_BASIS",
        name="",
        description="""The TravelBox code of the board basis which is included in the rates defined for the room/apartment""",
        example="""RO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMPORT_CONTRACT: str = Field(
        ...,
        alias="IMPORT_CONTRACT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LIMITED_INVENTORY: Optional[str] = Field(
        None,
        alias="LIMITED_INVENTORY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_CATEGORY_GROUP: Optional[str] = Field(
        None,
        alias="RATE_CATEGORY_GROUP",
        name="",
        description="""Rate category group""",
        example="""All""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""DC5""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_SYSTEM_CODE: str = Field(
        ...,
        alias="EXT_SYSTEM_CODE",
        name="",
        description="""NaN""",
        example="""C5""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: float = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=29926.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Standard View - Club Level - Two Queen Beds and Day Bed""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BASE_ROOM_CODE: Optional[str] = Field(
        None,
        alias="BASE_ROOM_CODE",
        name="",
        description="""NaN""",
        example="""DCON""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCESSIBLE_ROOM_IND: Optional[str] = Field(
        None,
        alias="ACCESSIBLE_ROOM_IND",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VIRTUAL_ROOM_IND: Optional[str] = Field(
        None,
        alias="VIRTUAL_ROOM_IND",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BASE_ROOM_IND: Optional[str] = Field(
        None,
        alias="BASE_ROOM_IND",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BEDDING_TYPE: Optional[str] = Field(
        None,
        alias="BEDDING_TYPE",
        name="",
        description="""NaN""",
        example="""XfvLsFLuWarOJIszTIRA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROOM_CATEGORY: Optional[str] = Field(
        None,
        alias="ROOM_CATEGORY",
        name="",
        description="""NaN""",
        example="""Conc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_OCC: Optional[int] = Field(
        None,
        alias="MIN_OCC",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_OCC: Optional[int] = Field(
        None,
        alias="MAX_OCC",
        name="",
        description="""NaN""",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STD_OCC: Optional[int] = Field(
        None,
        alias="STD_OCC",
        name="",
        description="""NaN""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EFFECTIVE_START_DATE: datetime = Field(
        ...,
        alias="EFFECTIVE_START_DATE",
        name="",
        description="""NaN""",
        example="""1987-03-25 16:13:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EFFECTIVE_END_DATE: datetime = Field(
        ...,
        alias="EFFECTIVE_END_DATE",
        name="",
        description="""NaN""",
        example="""1983-11-17 09:26:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEQUENCE_NO: int = Field(
        ...,
        alias="SEQUENCE_NO",
        name="",
        description="""The system generated number of the discount combination with entry""",
        example=24,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Standard View - Club Level""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_DATE: Optional[datetime] = Field(
        None,
        alias="CREATED_DATE",
        name="",
        description="""Currency Account created date""",
        example="""2007-03-25 17:55:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_DATE: Optional[datetime] = Field(
        None,
        alias="LAST_MODIFIED_DATE",
        name="",
        description="""Last Modified date""",
        example="""1995-12-23 18:13:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_USER: Optional[str] = Field(
        None,
        alias="CREATED_USER",
        name="",
        description="""Task created user""",
        example="""scanb001""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_USER: Optional[str] = Field(
        None,
        alias="LAST_MODIFIED_USER",
        name="",
        description="""Queue record last modified user""",
        example="""SCANB001""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OCCUPANCY_TYPE: Optional[str] = Field(
        None,
        alias="OCCUPANCY_TYPE",
        name="",
        description="""The method used to define occupancies for the room/apartment_x000D_
P - By predefine rule_x000D_
O - By occupancy rule_x000D_
S - By sharing rule""",
        example="""S""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AIM_ROOM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:11.578974""",
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
        example="""AIM_ROOM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=97877423496885,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAimRoomModel(BaseModel):
    """
    Payload class for TravelBox AIM_ROOM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Inventory Management Room"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Room Setup Data"""  # optional
        unique_identifier = ["data.CODE", "data.SUPPLIER_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIM_ROOM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
