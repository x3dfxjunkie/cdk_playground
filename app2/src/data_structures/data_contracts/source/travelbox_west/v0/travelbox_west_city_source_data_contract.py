"""Source Data Contract Template for CITY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CITY Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""BFU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Bengbu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: str = Field(
        ...,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""CN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""pMAFipxkpLgCSgatVpRG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SERIALIZED: str = Field(
        ...,
        alias="SERIALIZED",
        name="",
        description="""Flag to indicate if the airport is serialized ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_DATE: datetime = Field(
        ...,
        alias="MODIFIED_DATE",
        name="",
        description="""Batch receipt charge last modified date""",
        example="""1977-01-25 19:55:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[float] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=65699.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[float] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=12915.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_E: Optional[float] = Field(
        None,
        alias="LONGITUDE_E",
        name="",
        description="""The east longitude of the city""",
        example=67081.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_W: Optional[float] = Field(
        None,
        alias="LONGITUDE_W",
        name="",
        description="""The west longitude of the city""",
        example=70344.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_N: Optional[float] = Field(
        None,
        alias="LATITUDE_N",
        name="",
        description="""The north latitude of the city""",
        example=30484.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_S: Optional[float] = Field(
        None,
        alias="LATITUDE_S",
        name="",
        description="""The south latitude of the city""",
        example=27817.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UIC_CODE: Optional[str] = Field(
        None,
        alias="UIC_CODE",
        name="",
        description="""NaN""",
        example="""CAhQgxaUpMIVzMwzdibb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CITY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:41.661990""",
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
        example="""CITY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=39990074460087,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCityModel(BaseModel):
    """
    Payload class for TravelBox CITY
    """

    class Config:
        """Payload Level Metadata"""

        title = "City"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table contains user defined city information for a specific region and a country. Set up at Country/City/State/Resort panel in Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CITY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
