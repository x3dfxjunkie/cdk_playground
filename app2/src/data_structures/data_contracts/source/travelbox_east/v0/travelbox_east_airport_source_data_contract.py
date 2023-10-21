"""Source Data Contract for AIRPORT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIRPORT Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""CPM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Compton Airport""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: str = Field(
        ...,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""CPM""",
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

    REGION: str = Field(
        ...,
        alias="REGION",
        name="",
        description="""The TravelBox code of the region where the airport is located""",
        example="""NAM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""CA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LON_DEG: int = Field(
        ...,
        alias="LON_DEG",
        name="",
        description="""The degrees of the longitude""",
        example=118,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LON_MIN: int = Field(
        ...,
        alias="LON_MIN",
        name="",
        description="""The minutes of the longitude""",
        example=13,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LON_SEC: int = Field(
        ...,
        alias="LON_SEC",
        name="",
        description="""The seconds of the longitude""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAT_DEG: int = Field(
        ...,
        alias="LAT_DEG",
        name="",
        description="""The degrees of the latitude""",
        example=33,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAT_MIN: int = Field(
        ...,
        alias="LAT_MIN",
        name="",
        description="""The miunted of the latitude""",
        example=54,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAT_SEC: int = Field(
        ...,
        alias="LAT_SEC",
        name="",
        description="""The seconds of the latitude""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LON_DIR: str = Field(
        ...,
        alias="LON_DIR",
        name="",
        description="""The direction of the longitude""",
        example="""W""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAT_DIR: str = Field(
        ...,
        alias="LAT_DIR",
        name="",
        description="""The direction of the latitude""",
        example="""N""",
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
        example="""2016-01-04 00:59:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE: Optional[str] = Field(
        None,
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
    Class for TravelBox AIRPORT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:48:37.500579""",
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
        example="""AIRPORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=30825887150180,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastAirportModel(BaseModel):
    """
    Payload class for TravelBox AIRPORT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Airport"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Contains user defined airport location data to calculate the distance between departure and destination points. This will allow identifying the turnaround point of a travel itinerary which in turn will be used to calculate the fare. Set up at Setup Client."""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIRPORT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
