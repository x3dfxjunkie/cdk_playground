"""Source Data Contract Template for GEN_PRODUCT_GROUP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_PRODUCT_GROUP Data
    """

    SYSTEM_DEFINED: Optional[str] = Field(
        None,
        alias="SYSTEM_DEFINED",
        name="",
        description="""Whether this is a user added or system defned voucher type""",
        example="""ACyuzMiVHSpcgIXXpMMI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVENT: str = Field(
        ...,
        alias="EVENT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BASELINE_PRICE: str = Field(
        ...,
        alias="BASELINE_PRICE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_ID: int = Field(
        ...,
        alias="PRODUCT_ID",
        name="",
        description="""The TravelBox id of the generic product group for which the scheme is applicable""",
        example=3768,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""MEMMKR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Memory Maker""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREBOOKED: str = Field(
        ...,
        alias="PREBOOKED",
        name="",
        description="""If this is true (value 1 )the customer needs to get the Generic item on  particular specified date""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_PER_DAY: Optional[str] = Field(
        None,
        alias="VOUCHER_PER_DAY",
        name="",
        description="""true false value which control voucher issued period : if this is true (value 1) voucher is issued per day""",
        example="""uBsZaEVdFPYWUWophcfF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MULTIPLE: Optional[str] = Field(
        None,
        alias="MULTIPLE",
        name="",
        description="""Multiple""",
        example="""bWESvQILqRQLQWiRJEsW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXCLUDE_FROM_NORMAL_SEARCH: Optional[str] = Field(
        None,
        alias="EXCLUDE_FROM_NORMAL_SEARCH",
        name="",
        description="""True false value : the generic item will not_x000D_appear on a Component Search  in the Reservation_x000D_Manager and those generic products will only be available_x000D_as forced Component in wide search""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GP_LITE: Optional[str] = Field(
        None,
        alias="GP_LITE",
        name="",
        description="""This is to identify only the GP lite contracts.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVOICE_SECTION: Optional[str] = Field(
        None,
        alias="INVOICE_SECTION",
        name="",
        description="""Where in the invoice the name of the element group should appear_x000D_
INVOICE_HEADER_CODE = 'HEADER'_x000D_
INVOICE_BODY_CODE = 'BODY'_x000D_
INVOICE_PRICE_SECTION_CODE = 'PRICE'_x000D_
INVOICE_ITINERARY_SECTION_CODE = 'ITIN'_x000D_
INVOICE_PRICE_INCLUEDS_SECTION_CODE = 'PRICE_IN'""",
        example="""BODY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANCILLARY: str = Field(
        ...,
        alias="ANCILLARY",
        name="",
        description="""Atol Ancillary product definition""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_PRODUCT_GROUP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:37.134529""",
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
        example="""GEN_PRODUCT_GROUP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=94099271638259,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastGenProductGroupModel(BaseModel):
    """
    Payload class for TravelBox GEN_PRODUCT_GROUP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic Product Group"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This contains the element groups list used for generic contracts. Set up at 'Element Groups' menu item in Setup menu of Generic Loading Client"""  # optional
        unique_identifier = ["data.PRODUCT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_PRODUCT_GROUP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
