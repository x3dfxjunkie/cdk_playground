"""Source Data Contract Template for CMP_DIVISION"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CMP_DIVISION Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""WDTCDLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPANY: str = Field(
        ...,
        alias="COMPANY",
        name="",
        description="""The TravelBox code of the company for which the limit is defined for""",
        example="""WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""DLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS: Optional[str] = Field(
        None,
        alias="ADDRESS",
        name="",
        description="""Address of the credit card holder for credit card batch payment""",
        example="""IXuWDpEDfTKqcWoEAQKQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_CODE: Optional[str] = Field(
        None,
        alias="POST_CODE",
        name="",
        description="""Postal code of the credit card holder for credit card batch payment""",
        example="""qkYhDKSkvwUbQuwoKsrf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_SELLING_CURRENCY: Optional[str] = Field(
        None,
        alias="DEFAULT_SELLING_CURRENCY",
        name="",
        description="""The TravelBox code of the default selling currency of the division""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TIME_ZONE: Optional[str] = Field(
        None,
        alias="TIME_ZONE",
        name="",
        description="""The time zone of the accommodation""",
        example="""CzHHuHtDBYbKYNKXhAcP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: Optional[str] = Field(
        None,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: Optional[str] = Field(
        None,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""jHFqEaczHvOWusqePqgG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: Optional[str] = Field(
        None,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""SdqNZjYgRBUwMpurBKrh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""nfCyEtFOxiihXeqaBzbE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BIT_VALUE: Optional[int] = Field(
        None,
        alias="BIT_VALUE",
        name="",
        description="""The system generated bit value of the brand""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CMP_DIVISION Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:57.228472""",
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
        example="""CMP_DIVISION""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=95951579512660,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCmpDivisionModel(BaseModel):
    """
    Payload class for TravelBox CMP_DIVISION
    """

    class Config:
        """Payload Level Metadata"""

        title = "Division"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Division(s) information of companies. User can set up division(s) in Division main panel under a specific company in Setup Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CMP_DIVISION"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
