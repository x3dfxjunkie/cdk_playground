"""Source Data Contract Template for AMDCNX_CAUSE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AMDCNX_CAUSE Data
    """

    ID: int = Field(
        ...,
        alias="ID",
        name="",
        description="""System generated - auto incrementing field to uniquqly identify the contract to selling exchange rate""",
        example=970,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: str = Field(
        ...,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""WAIVE FEES""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE: str = Field(
        ...,
        alias="ACTIVE",
        name="",
        description="""Whether 3D secure filter is active or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AMDCNX_CAUSE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:07.810451""",
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
        example="""AMDCNX_CAUSE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=24792777603313,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAmdcnxCauseModel(BaseModel):
    """
    Payload class for TravelBox AMDCNX_CAUSE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Amendment Cancellation Reason"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains predefining causes for an amendment or cancellation of a booking. Set up at Reservation in Setup Client"""  # optional
        unique_identifier = ["data.ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AMDCNX_CAUSE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
