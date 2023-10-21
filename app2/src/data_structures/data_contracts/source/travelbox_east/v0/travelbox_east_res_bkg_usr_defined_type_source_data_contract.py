"""Source Data Contract Template for RES_BKG_USR_DEFINED_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BKG_USR_DEFINED_TYPE Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2008-09-27 12:41:12""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_VALUE: Optional[datetime] = Field(
        None,
        alias="DATE_VALUE",
        name="",
        description="""NaN""",
        example="""1982-09-29 01:38:24""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INDEX_NO: int = Field(
        ...,
        alias="INDEX_NO",
        name="",
        description="""The system generated number for the discount rate""",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=10005657,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: Optional[str] = Field(
        None,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""nYkTvWAdFEYFuCHzZsJB""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: Optional[int] = Field(
        None,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=6637,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_ID: float = Field(
        ...,
        alias="ATTRIBUTE_ID",
        name="",
        description="""User defined attribute id""",
        example=1183.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_TYPE: Optional[int] = Field(
        None,
        alias="ATTRIBUTE_TYPE",
        name="",
        description="""Attribute type of parent table : 0-free text,1-single select, 2-multi select""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_NO: Optional[int] = Field(
        None,
        alias="PACKAGE_NO",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FREE_TEXT: Optional[str] = Field(
        None,
        alias="FREE_TEXT",
        name="",
        description="""Free text allows to update in user defined type""",
        example="""5D - Base + Park Hopper  755""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BKG_USR_DEFINED_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:27.367485""",
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
        example="""RES_BKG_USR_DEFINED_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=85328552322301,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResBkgUsrDefinedTypeModel(BaseModel):
    """
    Payload class for TravelBox RES_BKG_USR_DEFINED_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking User Defined Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """User defined types related to reservation bookings"""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.INDEX_NO",
            "data.ATTRIBUTE_ID",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BKG_USR_DEFINED_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
