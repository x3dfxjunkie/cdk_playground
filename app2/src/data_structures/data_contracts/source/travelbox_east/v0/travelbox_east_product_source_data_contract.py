"""Source Data Contract Template for PRODUCT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PRODUCT Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""EXC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Excursion""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BIT_VALUE: Optional[int] = Field(
        None,
        alias="BIT_VALUE",
        name="",
        description="""The system generated bit value of the brand""",
        example=8192,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PRODUCT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:47:46.314295""",
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
        example="""PRODUCT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=71586492088549,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastProductModel(BaseModel):
    """
    Payload class for TravelBox PRODUCT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Product"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """A system defined table for Travelbox product items name code mapping (FLT:Flights). There is no UI to insert data, have to add manually"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PRODUCT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
