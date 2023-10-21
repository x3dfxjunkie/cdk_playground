"""Source Data Contract Template for GEN_USR_DEFINED_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_USR_DEFINED_TYPE Data
    """

    DURATION_ID: Optional[int] = Field(
        None,
        alias="DURATION_ID",
        name="",
        description="""NaN""",
        example=4097,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_VALUE: Optional[datetime] = Field(
        None,
        alias="DATE_VALUE",
        name="",
        description="""NaN""",
        example="""1992-05-25 23:30:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USER_DEFINED_TYPE_ID: int = Field(
        ...,
        alias="USER_DEFINED_TYPE_ID",
        name="",
        description="""Foreign key of GEN_USR_DEFINED_TYPE""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=10292,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_ID: Optional[int] = Field(
        None,
        alias="CATEGORY_ID",
        name="",
        description="""The system generated id of the supplement type""",
        example=4233,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLEMENT_ID: Optional[int] = Field(
        None,
        alias="SUPPLEMENT_ID",
        name="",
        description="""System generated id of car supplement that additional information is associated with""",
        example=8116,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_ID: Optional[float] = Field(
        None,
        alias="ATTRIBUTE_ID",
        name="",
        description="""User defined attribute id""",
        example=34.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FREE_TEXT_VALUE: Optional[str] = Field(
        None,
        alias="FREE_TEXT_VALUE",
        name="",
        description="""Free text value field""",
        example="""QFDabarXHKyXhojWWxrn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_TYPE_ID: Optional[int] = Field(
        None,
        alias="CATEGORY_TYPE_ID",
        name="",
        description="""Category type foreign key""",
        example=8162,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_TYPE: Optional[int] = Field(
        None,
        alias="ATTRIBUTE_TYPE",
        name="",
        description="""Attribute type of parent table : 0-free text,1-single select, 2-multi select""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2023-01-03 03:28:18""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_USR_DEFINED_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:59.503549""",
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
        example="""GEN_USR_DEFINED_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=88473549083226,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestGenUsrDefinedTypeModel(BaseModel):
    """
    Payload class for TravelBox GEN_USR_DEFINED_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic User Defined Type"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """User defined attribute types related to generic product bookings"""  # optional
        unique_identifier = ["data.USER_DEFINED_TYPE_ID", "data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_USR_DEFINED_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
