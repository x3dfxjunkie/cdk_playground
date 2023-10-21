"""Source Data Contract Template for GEN_DISCOUNT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_DISCOUNT Data
    """

    HISTORY_ID: int = Field(
        ...,
        alias="HISTORY_ID",
        name="",
        description="""History id of the currently running batch""",
        example=1082,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADVANCED_VIEW: Optional[str] = Field(
        None,
        alias="ADVANCED_VIEW",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2004-11-20 20:22:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE_ONLY: Optional[str] = Field(
        None,
        alias="PRICE_ONLY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_ALL_SELECT: str = Field(
        ...,
        alias="CATEGORY_ALL_SELECT",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=22438,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: str = Field(
        ...,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""PRI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_NO: int = Field(
        ...,
        alias="DISCOUNT_NO",
        name="",
        description="""The system generated number of the discount which belongs to the group""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFERENCE: Optional[str] = Field(
        None,
        alias="REFERENCE",
        name="",
        description="""CODE TO IDENTIFY THE DISCOUNT (OPTIONAL)""",
        example="""Complimentary""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""100% Discount""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_FROM: Optional[datetime] = Field(
        None,
        alias="BOOKED_FROM",
        name="",
        description="""The booking start date""",
        example="""2019-06-30 04:28:10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_TO: Optional[datetime] = Field(
        None,
        alias="BOOKED_TO",
        name="",
        description="""The booking end date""",
        example="""1979-03-12 15:19:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_CALCULATION_ORDER: int = Field(
        ...,
        alias="DISCOUNT_CALCULATION_ORDER",
        name="",
        description="""The discount applying order""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASS_PERCENTAGE: float = Field(
        ...,
        alias="PASS_PERCENTAGE",
        name="",
        description="""ONLY THIS AMOUNT IS PASSED TO THE CUSTOMER""",
        example=100.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_DAYS: Optional[int] = Field(
        None,
        alias="MIN_DAYS",
        name="",
        description="""For discount type Early Bird - 0, for free day - number of renting days,  for  price - Minimum days.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEARCH_TYPE: Optional[int] = Field(
        None,
        alias="SEARCH_TYPE",
        name="",
        description="""Only Booking duration given -1, only renting duration given -2, both booking and renting durations were given -3, neither of them given 4. """,
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAY_FROM: Optional[datetime] = Field(
        None,
        alias="STAY_FROM",
        name="",
        description="""The start date of the booking stay date period of the discount. Bookings having their stay date period within this period are applicable for the discount.""",
        example="""1996-05-10 10:41:55""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAY_TO: Optional[datetime] = Field(
        None,
        alias="STAY_TO",
        name="",
        description="""The end date of the booking stay date period of the discount. Bookings having their stay date period within this period are applicable for the discount.""",
        example="""1982-09-27 20:03:44""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAY_DAYS: Optional[str] = Field(
        None,
        alias="STAY_DAYS",
        name="",
        description=""" The days of the week for which the discount is applied_x000D_
  1 - Sunday_x000D_
  2 - Monday_x000D_
  3 - Tuesday_x000D_
  4 - Wednesday_x000D_
  5 - Thursday_x000D_
  6 - Friday_x000D_
  7 - Saturday_x000D_
  Example :-  If the discount is valid for only weekends this value is 17""",
        example="""1234567""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_SCHEME: Optional[int] = Field(
        None,
        alias="PAYMENT_SCHEME",
        name="",
        description="""If a payment scheme has specifically been defined for the discount, this field holds the TravelBox code of the payment scheme. Otherwise this is null meaning the payment scheme applied to the contract is considered for the discount.""",
        example=8388,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_SCHEME: Optional[int] = Field(
        None,
        alias="CNX_SCHEME",
        name="",
        description="""If a supplier cancellation scheme has specifically been defined for the discount, this field holds the TravelBox code of the cancellation scheme. Otherwise this is null meaning the cancellation scheme applied to the contract is considered for the discount.""",
        example=7460,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMD_SCHEME: Optional[int] = Field(
        None,
        alias="AMD_SCHEME",
        name="",
        description="""If a supplier amendment scheme has specifically been defined for the discount, this field holds the TravelBox code of the amendment scheme. Otherwise this is null meaning the amendment scheme applied to the contract is considered for the discount.""",
        example=2588,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_FROM_TO: Optional[str] = Field(
        None,
        alias="BOOKED_FROM_TO",
        name="",
        description="""A flag indicating the discount has a booked from - booked to date range been specified""",
        example="""1""",
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


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_DISCOUNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:02.210237""",
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
        example="""GEN_DISCOUNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=37477053110136,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestGenDiscountModel(BaseModel):
    """
    Payload class for TravelBox GEN_DISCOUNT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic Discount"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Discount information of a particular discount defined at 'Discounts' branch of a generic contract in Generiic Loading Client"""  # optional
        unique_identifier = ["data.CONTRACT_ID", "data.DISCOUNT_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_DISCOUNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
