"""Source Data Contract Template for LOCATION"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox LOCATION Data
    """

    LOCATION_ID: int = Field(
        ...,
        alias="LOCATION_ID",
        name="",
        description="""Location id is saved when the module configuration_x000D_
'STORE_LOCATION_ID' is enabled, otherwise_x000D_
-1""",
        example=5107,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""San Deigo Hotels""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""SAN""",
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

    REGION: Optional[str] = Field(
        None,
        alias="REGION",
        name="",
        description="""The TravelBox code of the region where the airport is located""",
        example="""NAM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESORT: Optional[str] = Field(
        None,
        alias="RESORT",
        name="",
        description="""The foreign Key which refers the field CODE of the ACT_ABSORPTION table""",
        example="""GoaQHFodKSzsCRYXfbIG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION_TYPE: Optional[str] = Field(
        None,
        alias="LOCATION_TYPE",
        name="",
        description="""Car location type code as defined in car setup""",
        example="""aXRYnShMaoqDkpgsWihU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LONGITUDE: Optional[int] = Field(
        None,
        alias="LONGITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=2190,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATITUDE: Optional[int] = Field(
        None,
        alias="LATITUDE",
        name="",
        description="""Latitude of the accommodation""",
        example=6280,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox LOCATION Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:57.054614""",
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
        example="""LOCATION""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=54574281193113,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestLocationModel(BaseModel):
    """
    Payload class for TravelBox LOCATION
    """

    class Config:
        """Payload Level Metadata"""

        title = "Location"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Pick up and Drop off locations for transfers. Set up data under 'Locations' menu item in 'Destinations' menu of Setup Client and 'Setup' menu in Transfer Loading Client"""  # optional
        unique_identifier = ["data.LOCATION_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LOCATION"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
