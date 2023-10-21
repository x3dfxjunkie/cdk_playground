"""Global DAS WDW Data Contract: for key fields and classes that will be repeated throughout sources"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# This file allows users to reuse the classes below for inheritance in child data contracts in order to save repeating code
# To use, user needs import the file and then use the necessary class as inheritance for their contract
class GlobalDASWDWSchemaName(Enum):
    """Global DAS WDW schema name Enum"""

    RES_MGMT = "wdw_mmp_das"


# possible payload tables
class GlobalDASWDWTableName(Enum):
    """Global DAS WDW Database Table name Enum"""

    ENTTL = "ENTTL"
    ENTTL_CONF = "ENTTL_CONF"
    ENTTL_LNK = "ENTTL_LNK"
    ENTTL_UPDT_LOG = "ENTTL_UPDT_LOG"
    EXTNL_ACCT_LNK = "EXTNL_ACCT_LNK"
    LNK = "LNK"
    LNK_ASSC = "LNK_ASSC"
    TNC = "TNC"


# table metadata
class GlobalDASWDWMetadata(BaseModel):
    """Global Dreams Metadata Class"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Date Time stamp",
        description="Timestamp for when the record was sent in the stream",
        example="2023-03-29T15:30:19.109655Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    record_type: str = Field(
        ...,
        alias="record-type",
        name="Record Type",
        description="data",
        example="data",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    operation: str = Field(
        ...,
        alias="operation",
        name="Operation",
        description="",
        example="update",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="Partiction Key Type",
        description="",
        example="schema-table",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="Schema Name",
        description="Name of the schema in snowflake",
        example="res_mgmt",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="table-name",
        name="Table Name",
        description="name of the table in snowflake",
        example="tc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="Transaction Identifier",
        description="Unique ID for the stream record",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_record_id: Optional[int] = Field(
        None,
        alias="transaction-record-id",
        name="Transaction Record ID",
        description="Transaction Record ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prev_transaction_id: Optional[int] = Field(
        None,
        alias="prev-transaction-id",
        name="Previous Transaction ID",
        description="Previous Transaction ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prev_transaction_record_id: Optional[int] = Field(
        None,
        alias="prev-transaction-record-id",
        name="Previous Transaction Record ID",
        description="Previous Transaction Record ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    commit_timestamp: Optional[datetime] = Field(
        None,
        alias="commit-timestamp",
        name="Commit Timestamp",
        description="Commit Timestamp",
        example="2023-03-29T15:30:19.109655Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    stream_position: Optional[str] = Field(
        None,
        alias="stream-position",
        name="Stream Position",
        description="Stream Position",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
