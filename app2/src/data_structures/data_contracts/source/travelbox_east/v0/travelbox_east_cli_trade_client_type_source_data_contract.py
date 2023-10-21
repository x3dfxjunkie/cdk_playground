"""Source Data Contract Template for CLI_TRADE_CLIENT_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_TRADE_CLIENT_TYPE Data
    """

    TYPE_ID: int = Field(
        ...,
        alias="TYPE_ID",
        name="",
        description="""The TravelBox id of the generic product type for which the scheme is applicable""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: Optional[str] = Field(
        None,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""IND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Independent""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_TRADE_CLIENT_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:51.306962""",
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
        example="""CLI_TRADE_CLIENT_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=22382384460042,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliTradeClientTypeModel(BaseModel):
    """
    Payload class for TravelBox CLI_TRADE_CLIENT_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Trade Client Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store information associated with Trade Client Type"""  # optional
        unique_identifier = ["data.TYPE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_TRADE_CLIENT_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
