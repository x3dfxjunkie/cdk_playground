"""Source Data Contract Template for CLI_PROFILE_ATTRIBUTE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_PROFILE_ATTRIBUTE Data
    """

    ATTRIBUTE_ID: int = Field(
        ...,
        alias="ATTRIBUTE_ID",
        name="",
        description="""User defined attribute id""",
        example=103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: int = Field(
        ...,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=32617,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALUE: Optional[str] = Field(
        None,
        alias="VALUE",
        name="",
        description="""The amount/percentage value of the variation""",
        example="""2423151617""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_NAME: Optional[str] = Field(
        None,
        alias="ATTRIBUTE_NAME",
        name="",
        description="""Passenger Attribute Name""",
        example="""GlobalGuestID""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_TYPE: Optional[str] = Field(
        None,
        alias="ATTRIBUTE_TYPE",
        name="",
        description="""Attribute type of parent table : 0-free text,1-single select, 2-multi select""",
        example="""EXT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1989-10-19 21:55:46""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_PROFILE_ATTRIBUTE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:48.531091""",
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
        example="""CLI_PROFILE_ATTRIBUTE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=79793191047135,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliProfileAttributeModel(BaseModel):
    """
    Payload class for TravelBox CLI_PROFILE_ATTRIBUTE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Profile Attribute"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store passenger attribute values with respect to each Passenger Profiles.
Passenger profile attribute values are entered in Attributes panel of the Direct Client"""  # optional
        unique_identifier = ["data.ATTRIBUTE_ID", "data.PROFILE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_PROFILE_ATTRIBUTE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
