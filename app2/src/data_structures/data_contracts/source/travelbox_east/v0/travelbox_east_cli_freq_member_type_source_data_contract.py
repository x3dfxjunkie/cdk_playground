"""Source Data Contract Template for CLI_FREQ_MEMBER_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_FREQ_MEMBER_TYPE Data
    """

    REF_CODE: Optional[str] = Field(
        None,
        alias="REF_CODE",
        name="",
        description="""NaN""",
        example="""A4759D2""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2016-05-01 10:47:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ID: int = Field(
        ...,
        alias="ID",
        name="",
        description="""System generated - auto incrementing field to uniquqly identify the contract to selling exchange rate""",
        example=14,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: str = Field(
        ...,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Europe Resident""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_CODE: Optional[str] = Field(
        None,
        alias="CATEGORY_CODE",
        name="",
        description="""Refer to CODE in GEN_CATEGORY table""",
        example="""wngeVgtbsyrkGOjiHJVO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IS_PASSENGER_TYPE: Optional[str] = Field(
        None,
        alias="IS_PASSENGER_TYPE",
        name="",
        description="""Flag to indicate if the type is a passenger type (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENCY_ID: Optional[str] = Field(
        None,
        alias="AGENCY_ID",
        name="",
        description="""Agency code""",
        example="""GShmbzmXFqRFBPfIgVdR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_FREQ_MEMBER_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:51:38.612121""",
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
        example="""CLI_FREQ_MEMBER_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=17721708884883,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliFreqMemberTypeModel(BaseModel):
    """
    Payload class for TravelBox CLI_FREQ_MEMBER_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Frequent Membership Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store Frequent Client Membership Type information.
Frequent Client Membership Types are setup in Customer Profiles setup module, Setup menu"""  # optional
        unique_identifier = ["data.ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_FREQ_MEMBER_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
