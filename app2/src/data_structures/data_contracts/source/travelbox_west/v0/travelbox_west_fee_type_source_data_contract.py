"""Source Data Contract Template for FEE_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox FEE_TYPE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""ADJSYS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""System Errors""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSIONABLE: Optional[str] = Field(
        None,
        alias="COMMISSIONABLE",
        name="",
        description="""A flag indicating whether the discount is trade client commissionable ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTO: Optional[str] = Field(
        None,
        alias="AUTO",
        name="",
        description="""Indicate payment is added by Auto Payment Scheduler or Manual.  Auto Payment Scheduler =  1, Manual = 0""",
        example="""pbuWKKHQpwvqphQtNiro""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEMWISE: Optional[str] = Field(
        None,
        alias="ITEMWISE",
        name="",
        description="""Deprecated""",
        example="""xcHRCvazJJIBmhUibTqZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMTWISE: Optional[str] = Field(
        None,
        alias="AMTWISE",
        name="",
        description="""Deprecated""",
        example="""oIOpZVnUMBfcGqCAaKJQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAXABLE: str = Field(
        ...,
        alias="TAXABLE",
        name="",
        description="""Whether accounting rule is applicable for taxable items or non taxable items""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DAYS2DEPT: Optional[int] = Field(
        None,
        alias="DAYS2DEPT",
        name="",
        description="""The number of days prior the departure. If the booking date to departure date range is within this period, this fee is applicable for the booking.""",
        example=8770,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PER_PERSON: Optional[str] = Field(
        None,
        alias="PER_PERSON",
        name="",
        description="""A flag indicating the fee type charges are defined per person ( value is 1 ) or per booking( value is null )""",
        example="""pTZNnvFZpHaHBxxSajIx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_TYPE: Optional[str] = Field(
        None,
        alias="CLIENT_TYPE",
        name="",
        description="""Applicable client types of the accounting rule. DIRECT- Direct Client, TRADE-Trade Client.""",
        example="""cosZlPymPvjOufLUQEqb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIST_CHANNEL: Optional[str] = Field(
        None,
        alias="DIST_CHANNEL",
        name="",
        description="""Accounting rule applicable distribution channels""",
        example="""OxkFeLJYpSBOLgCwITBr""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKINGS_FROM: Optional[datetime] = Field(
        None,
        alias="BOOKINGS_FROM",
        name="",
        description="""Deprecated""",
        example="""1975-04-11 05:58:29""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKINGS_TO: Optional[datetime] = Field(
        None,
        alias="BOOKINGS_TO",
        name="",
        description="""Deprecated""",
        example="""2002-08-15 18:07:30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VAR_COMMISN: Optional[str] = Field(
        None,
        alias="VAR_COMMISN",
        name="",
        description="""Deprecated""",
        example="""IEloruyVZXKsgCzgcYWi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REVERSIBLE: str = Field(
        ...,
        alias="REVERSIBLE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRAVEL_START_DATE: Optional[datetime] = Field(
        None,
        alias="TRAVEL_START_DATE",
        name="",
        description="""NaN""",
        example="""2006-06-17 19:10:29""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRAVEL_END_DATE: Optional[datetime] = Field(
        None,
        alias="TRAVEL_END_DATE",
        name="",
        description="""NaN""",
        example="""1991-10-17 17:38:44""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox FEE_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:30.947392""",
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
        example="""FEE_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=55427468600990,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestFeeTypeModel(BaseModel):
    """
    Payload class for TravelBox FEE_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Fee Type"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Additional fee types that will be automatically added to the booking if the specified fee application criteria matches the booking criteria. Set up at 'Fee types' under General menu in Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "FEE_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
