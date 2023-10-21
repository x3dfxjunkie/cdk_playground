"""Source Data Contract Template for PAX_SUB_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PAX_SUB_TYPE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Adult""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIN_TYPE: str = Field(
        ...,
        alias="MAIN_TYPE",
        name="",
        description="""The TravelBox code of the main passenger type_x000D_
A - Adult_x000D_
C - Child_x000D_
I - Infant""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PAX_SUB_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:20.091031""",
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
        example="""PAX_SUB_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=46274389985443,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastPaxSubTypeModel(BaseModel):
    """
    Payload class for TravelBox PAX_SUB_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Passenger Sub-Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Different types of passengers based off the default passenger types. Set up under 'Pax Types' in 'General' menu of Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PAX_SUB_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
