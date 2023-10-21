"""Source Data Contract Template for PKG_GROUP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PKG_GROUP Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1994-06-16 08:47:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALCULATION_TYPE: str = Field(
        ...,
        alias="CALCULATION_TYPE",
        name="",
        description="""Calculation type. 1 - Daily and Weekly,2 - Daily Rate by duration, 3 - Extra day for long durations""",
        example="""GP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""2016_EARLY_RELEASE_DOC_FEE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""2016 Early Release of Documents""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENSION: str = Field(
        ...,
        alias="EXTENSION",
        name="",
        description="""Telephone extension of the user""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELL_ALONE: str = Field(
        ...,
        alias="SELL_ALONE",
        name="",
        description="""SELLABLE ALONE (USED INTOURS WHEN LOADING TOUR ACCOM CONTRACT VIA TOUR BUILDER)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_TYPE: Optional[str] = Field(
        None,
        alias="PKG_TYPE",
        name="",
        description="""Type of the package, possible values are_x000D_
-Passenger Based_x000D_
-Group Based""",
        example="""Passenger Based""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_CODE: Optional[str] = Field(
        None,
        alias="CMS_CODE",
        name="",
        description="""User defined CMS code which is taken as parameter values for tb_code, tb_itin, tb_pricegrid in package, itinerary and price grid respectively in the CMS URL which refers from travelbox to CMS. If this value is not defined the system will take package code, itinerary code and price grid name as default value of above variables.""",
        example="""bILTfwGpfiHMZuPvfWqU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_GROUP_ID: int = Field(
        ...,
        alias="PKG_GROUP_ID",
        name="",
        description="""Id of the Package Group associated with the Scheme Rule.""",
        example=13883,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PKG_GROUP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:27.245741""",
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
        example="""PKG_GROUP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=69799728124758,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestPkgGroupModel(BaseModel):
    """
    Payload class for TravelBox PKG_GROUP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package Group"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Basic details of a package package code, package name are stored"""  # optional
        unique_identifier = ["data.PKG_GROUP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_GROUP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
