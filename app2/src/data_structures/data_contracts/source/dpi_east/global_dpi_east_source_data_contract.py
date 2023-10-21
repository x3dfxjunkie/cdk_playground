"""DPI EAST Global dataclass: for key fields and classes that will be repeated throughout DPI EAST only"""
from __future__ import annotations
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

"""Dataclasses that need references to this will need to import the global_dpi_east_source_data_contract.py file"""


class GlobalDPIEASTSchemaName(Enum):
    """Global DPI EAST schema name"""

    AWAKENING = "wdw_photopass"


class GlobalDPIEASTTableName(Enum):
    """Global DPI EAST list of tables"""

    SUBJECTS = "subjects"
    MEDIADOWNLOADS = "mediadownloads"
    MEDIA = "media"
    ASSOCIATIONS = "associations"
    ASSOCIATIONS_MSG = "associations_msg"
    META_LOCATION = "meta_location"
    META_SUBJECT = "meta_subject"
    META_VENUE = "meta_venue"


class GlobalDPIEASTOperation(Enum):
    """DPI EAST Data Operation type"""

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    LOAD = "load"


class GlobalDPIEASTMetadata(BaseModel):
    """Global DPI EAST Metadata Class Data"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Record Timestamp",
        description="",
        example="2023-04-17T13:33:15.230Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    record_type: str = Field(
        ...,
        alias="record-type",
        name="Record Type",
        description="Record Type",
        example="data",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    operation: GlobalDPIEASTOperation = Field(
        ...,
        alias="operation",
        name="Operation",
        description="Specifies record operation as Insert or Update",
        example="Update",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="Partition Key Type",
        description="Partition Key Type",
        example="schema-table",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    schema_name: GlobalDPIEASTSchemaName = Field(
        ...,
        alias="schema-name",
        name="Schema Name",
        description="Database schema name storing the record",
        example="awakening",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    table_name: GlobalDPIEASTTableName = Field(
        ...,
        alias="table-name",
        name="Table Name",
        description="Database table name storing the record",
        example="associations_msg",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
