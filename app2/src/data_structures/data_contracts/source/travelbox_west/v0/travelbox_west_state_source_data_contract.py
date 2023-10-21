"""Source Data Contract Template for STATE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox STATE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""TAH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Tahiti""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: str = Field(
        ...,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""TA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[float] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=1123.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[float] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=63887.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_E: Optional[float] = Field(
        None,
        alias="LONGITUDE_E",
        name="",
        description="""The east longitude of the city""",
        example=27314.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_W: Optional[float] = Field(
        None,
        alias="LONGITUDE_W",
        name="",
        description="""The west longitude of the city""",
        example=80046.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_N: Optional[float] = Field(
        None,
        alias="LATITUDE_N",
        name="",
        description="""The north latitude of the city""",
        example=12268.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_S: Optional[float] = Field(
        None,
        alias="LATITUDE_S",
        name="",
        description="""The south latitude of the city""",
        example=33800.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1980-02-15 23:26:58""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox STATE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:41.021819""",
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
        example="""STATE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=72984010058633,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestStateModel(BaseModel):
    """
    Payload class for TravelBox STATE
    """

    class Config:
        """Payload Level Metadata"""

        title = "State"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Travelbox geographical 'State' for a particular country. Set up at 'Country/City/State/Resort' under 'Destinations' manu in Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "STATE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
