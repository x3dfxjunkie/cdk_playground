"""WIP: Global Data Contract: for key fields and classes that will be repeated throughout sources"""
from __future__ import annotations

# from datetime import date, datetime
from enum import Enum
from typing import Optional
from datetime import datetime

# from typing import List, Optional, Union
# from uuid import UUID

from pydantic import BaseModel, Field, constr  # , ValidationError, validator


"""Data Contracts that need references to this will need to import the global_source_data_contract.py file.
Python Syntax Example:
from app.src.data_structures.dataclasses.source import global_source_data_contract
global_source_data_contract.Swid
"""


class DataClassification(Enum):
    PI = "PI"
    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"


# class Swid(BaseModel):
#     __root__: Optional[
#         constr(
#             regex=r"^\{[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\}$", min_length=36, max_length=38
#         )
#     ] = Field(
#         None,
#         alias="",
#         name="",
#         description="Registered Guest Starwave ID",
#         example="",
#         guest_identifier=True,
#         identifier_tag="Indirect",
#         transaction_identifier=False,
#     )  # type: ignore


# class Pernr(BaseModel):
#     __root__: Optional[constr(regex=r"^\d{8}$", min_length=8, max_length=8)] = Field(
#         None,
#         alias="pernr",
#         name="PERNER",
#         description="PERNER - Cast Member Identifier",
#         example="90123456",
#         guest_identifier=True,
#         identifier_tag="Indirect",
#         transaction_identifier=False,
#     )


class GlobalAdditionalDMSMetadata(BaseModel):
    """Global Dreams Metadata Class"""

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


class SourceMetadataAndGlobalAdditionalDMSMetadata(BaseModel):
    """Global Source and DMS Metadata Class"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:01.378618""",
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
        example="""SFLNSMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""AP_LVL_N_ENTTL_FISCAL_DT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=59558768559209,
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
