"""Source Data Contract Template for LOCALE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox LOCALE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LANGUAGE: str = Field(
        ...,
        alias="LANGUAGE",
        name="",
        description="""language code of the locale""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: Optional[str] = Field(
        None,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VARIANT: Optional[str] = Field(
        None,
        alias="VARIANT",
        name="",
        description="""Any arbitrary value used to indicate a variation of a Locale""",
        example="""oNskNDUVaDZDdRwJXBFx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""English""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BASE: str = Field(
        ...,
        alias="BASE",
        name="",
        description="""whether this is the base language of the TBX or not : 1 or 0 value""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FONT: str = Field(
        ...,
        alias="FONT",
        name="",
        description="""Font name for a particular locale""",
        example="""Tahoma""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISO_CODE: str = Field(
        ...,
        alias="ISO_CODE",
        name="",
        description="""NaN""",
        example="""ENG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox LOCALE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:18.887383""",
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
        example="""LOCALE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=25544661654039,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestLocaleModel(BaseModel):
    """
    Payload class for TravelBox LOCALE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Locale"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table contains the Travelbox locales which are used in Content Manager. Set up at 'Locale' under Setup menu in Customer Profiles Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LOCALE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
