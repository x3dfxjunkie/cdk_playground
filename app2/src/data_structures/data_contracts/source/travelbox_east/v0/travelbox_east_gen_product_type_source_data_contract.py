"""Source Data Contract Template for GEN_PRODUCT_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_PRODUCT_TYPE Data
    """

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2008-08-10 09:26:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNAL_CODE: Optional[str] = Field(
        None,
        alias="EXTERNAL_CODE",
        name="",
        description="""NaN""",
        example="""UKULT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE_ID: int = Field(
        ...,
        alias="TYPE_ID",
        name="",
        description="""The TravelBox id of the generic product type for which the scheme is applicable""",
        example=7166,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_ID: int = Field(
        ...,
        alias="PRODUCT_ID",
        name="",
        description="""The TravelBox id of the generic product group for which the scheme is applicable""",
        example=3708,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""UK Ultimate Ticket""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: Optional[str] = Field(
        None,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""UKULT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""UK Ultimate Ticket""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_TIMES_COMPULSORY: str = Field(
        ...,
        alias="DEPARTURE_TIMES_COMPULSORY",
        name="",
        description="""A flag indicating whether it is compulsory to specify departure times for bookings done from ths product type ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1982-07-28 16:32:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_PRODUCT_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:48:55.994713""",
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
        example="""GEN_PRODUCT_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=84146282574080,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastGenProductTypeModel(BaseModel):
    """
    Payload class for TravelBox GEN_PRODUCT_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic Product Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """The Product Types lits of the Generic Products which belongs to a particular Element Group. Set up at 'Product Types' menu item in Setup menu of Generic Loading Client"""  # optional
        unique_identifier = ["data.TYPE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_PRODUCT_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
