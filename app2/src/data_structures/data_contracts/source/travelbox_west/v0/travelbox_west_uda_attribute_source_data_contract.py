"""Source Data Contract Template for UDA_ATTRIBUTE"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox UDA_ATTRIBUTE Data
    """

    attribute_id: int = Field(
        ...,
        alias="ATTRIBUTE_ID",
        name="",
        description="Auot generated number",
        example=421,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    attribute_name: Optional[str] = Field(
        None,
        alias="ATTRIBUTE_NAME",
        name="",
        description="Name of the attribute",
        example="Avail Room Type Surrogate",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    level_id: int = Field(
        ...,
        alias="LEVEL_ID",
        name="",
        description="Foreign key of level",
        example=41,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    active: str = Field(
        ...,
        alias="ACTIVE",
        name="",
        description="Flag of active",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    system_defined: str = Field(
        ...,
        alias="SYSTEM_DEFINED",
        name="",
        description="Flag of SYSTEM_DEFINED",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default: Optional[str] = Field(
        None,
        alias="DEFAULT",
        name="",
        description="Default free text value",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mandatory: str = Field(
        ...,
        alias="MANDATORY",
        name="",
        description="Flag of mandatory",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: int = Field(
        ...,
        alias="TYPE",
        name="",
        description="Type: 0-free text, 1-single select, 2-multy select ",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified_time: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="The time at which the last modification has done",
        example="2020-05-11T18:44:22.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    min_length: Optional[int] = Field(
        None,
        alias="MIN_LENGTH",
        name="",
        description="NA",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_length: Optional[int] = Field(
        None,
        alias="MAX_LENGTH",
        name="",
        description="NA",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    attribute_code: Optional[str] = Field(
        None,
        alias="ATTRIBUTE_CODE",
        name="",
        description="NA",
        example="UDA_CODE_1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox UDA_ATTRIBUTE Metadata
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
        example="""UDA_ATTRIBUTE""",
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


class TravelBoxWestUdaAttributeModel(BaseModel):
    """
    Payload class for TravelBox UDA_ATTRIBUTE
    """

    class Config:
        """Payload Level Metadata"""

        title = "User Defined Attribute"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = "NA"  # optional
        unique_identifier = ["data.ATTRIBUTE_ID", "data.TYPE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "UDA_ATTRIBUTE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
