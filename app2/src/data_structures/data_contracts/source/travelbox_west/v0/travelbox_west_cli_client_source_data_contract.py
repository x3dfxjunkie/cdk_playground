"""Source Data Contract Template for CLI_CLIENT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_CLIENT Data
    """

    UNAVAILABLE: Optional[str] = Field(
        None,
        alias="UNAVAILABLE",
        name="",
        description="""NaN""",
        example="""tgJFKjzztRXkvkNoLqRi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1986-12-18 19:03:48""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNAL_REF_ID: Optional[str] = Field(
        None,
        alias="EXTERNAL_REF_ID",
        name="",
        description="""NaN""",
        example="""lpedpLWMjBKVypsiJomj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=11674,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: str = Field(
        ...,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""TRADE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_REF: Optional[str] = Field(
        None,
        alias="CLIENT_REF",
        name="",
        description="""Client Reference of the Booking""",
        example="""31523590""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""ALL WAYS TRAVEL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_STATUS: str = Field(
        ...,
        alias="CLIENT_STATUS",
        name="",
        description="""Flag to indicate the client status associated with the Scheme Rule._x000D_
1 - Active_x000D_
0 - Inactive""",
        example="""Active""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEDIA: Optional[str] = Field(
        None,
        alias="MEDIA",
        name="",
        description="""The code of the Media Type associated with the client""",
        example="""XHNaHPFmndXfsWeqbnJo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REGISTERED_DATE: datetime = Field(
        ...,
        alias="REGISTERED_DATE",
        name="",
        description="""Registered Date""",
        example="""1980-07-23 02:22:36""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_GROUP: str = Field(
        ...,
        alias="CLIENT_GROUP",
        name="",
        description="""The TravelBox code of the client group for which the limit is defined for""",
        example="""TA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: datetime = Field(
        ...,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""1996-11-30 15:09:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1982-07-19 18:26:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REGISTERED_CHANNEL: Optional[str] = Field(
        None,
        alias="REGISTERED_CHANNEL",
        name="",
        description="""The code of the Channel that associated with the client""",
        example="""qUXCeHBPTYaCNYOrnoXL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=2095,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15416,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_SALES_AGENT: Optional[int] = Field(
        None,
        alias="PRIMARY_SALES_AGENT",
        name="",
        description="""The id of the primary sales agent""",
        example=1469,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS_MESSAGE: Optional[str] = Field(
        None,
        alias="STATUS_MESSAGE",
        name="",
        description="""Status message""",
        example="""eRkedGCePzKswrlUodfz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: Optional[str] = Field(
        None,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""UBuMVLARyKCPjEyiqkGV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: Optional[str] = Field(
        None,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""PcZWEYPeJMAMrdYuTHDb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRADE_ID: Optional[int] = Field(
        None,
        alias="GRADE_ID",
        name="",
        description="""Grade Id""",
        example=8878,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEALING_COMPANY: Optional[str] = Field(
        None,
        alias="DEALING_COMPANY",
        name="",
        description="""Code of the Company that associated with the client""",
        example="""jcVtMukbqIwxmzYnnDBt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEALING_DIVISION: Optional[str] = Field(
        None,
        alias="DEALING_DIVISION",
        name="",
        description="""Code of the Division that associated with the client""",
        example="""AsriAVJFEULsosYGWCuI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: Optional[str] = Field(
        None,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
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

    DEALING_BRAND: Optional[str] = Field(
        None,
        alias="DEALING_BRAND",
        name="",
        description="""Code of the Brand that associated with the client""",
        example="""VONoWbvFNaCyTaZYcfRY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCALE: str = Field(
        ...,
        alias="LOCALE",
        name="",
        description="""The TravelBox code of the locale""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_CLIENT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:25.681376""",
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
        example="""CLI_CLIENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=60262672354557,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliClientModel(BaseModel):
    """
    Payload class for TravelBox CLI_CLIENT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store TravelBox client information."""  # optional
        unique_identifier = ["data.CLIENT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_CLIENT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
