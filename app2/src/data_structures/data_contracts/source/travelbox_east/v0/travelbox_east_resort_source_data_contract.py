"""Source Data Contract Template for RESORT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RESORT Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""IDR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Good Neighbor Hotels International Drive""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: str = Field(
        ...,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""ORL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: str = Field(
        ...,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""FL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[float] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=88357.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[float] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=31362.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_E: Optional[float] = Field(
        None,
        alias="LONGITUDE_E",
        name="",
        description="""The east longitude of the city""",
        example=39514.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_W: Optional[float] = Field(
        None,
        alias="LONGITUDE_W",
        name="",
        description="""The west longitude of the city""",
        example=68216.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_N: Optional[float] = Field(
        None,
        alias="LATITUDE_N",
        name="",
        description="""The north latitude of the city""",
        example=92657.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_S: Optional[float] = Field(
        None,
        alias="LATITUDE_S",
        name="",
        description="""The south latitude of the city""",
        example=31443.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RESORT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:33.376504""",
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
        example="""RESORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=64478739891344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResortModel(BaseModel):
    """
    Payload class for TravelBox RESORT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Resort"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """The tourist resorts defined for a particular city. Set up at 'Country/City/State/Resort' under 'Destinations' menu in Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RESORT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
