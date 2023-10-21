"""Source Data Contract Template for COUNTRY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox COUNTRY Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""WF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Wallis and Futuna Islands""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REGION: str = Field(
        ...,
        alias="REGION",
        name="",
        description="""The TravelBox code of the region where the airport is located""",
        example="""SWP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NATIONALITY: Optional[str] = Field(
        None,
        alias="NATIONALITY",
        name="",
        description="""The nationality of the country""",
        example="""Wallis and Futuna Islands""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[float] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=-178.16,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[float] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=-14.29,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_E: Optional[float] = Field(
        None,
        alias="LONGITUDE_E",
        name="",
        description="""The east longitude of the city""",
        example=22997.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE_W: Optional[float] = Field(
        None,
        alias="LONGITUDE_W",
        name="",
        description="""The west longitude of the city""",
        example=58157.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_N: Optional[float] = Field(
        None,
        alias="LATITUDE_N",
        name="",
        description="""The north latitude of the city""",
        example=95043.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE_S: Optional[float] = Field(
        None,
        alias="LATITUDE_S",
        name="",
        description="""The south latitude of the city""",
        example=94063.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1978-03-24 22:51:05""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox COUNTRY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:47:35.795842""",
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
        example="""COUNTRY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=49648370598700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCountryModel(BaseModel):
    """
    Payload class for TravelBox COUNTRY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Country"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """The table to store user inserted country information through Supplier Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "COUNTRY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
