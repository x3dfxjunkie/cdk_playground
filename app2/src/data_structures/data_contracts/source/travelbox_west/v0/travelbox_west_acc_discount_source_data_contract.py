"""Source Data Contract Template for ACC_DISCOUNT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACC_DISCOUNT Data
    """

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=55532,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_NO: int = Field(
        ...,
        alias="DISCOUNT_NO",
        name="",
        description="""The system generated number of the discount which belongs to the group""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFERENCE: Optional[str] = Field(
        None,
        alias="REFERENCE",
        name="",
        description="""CODE TO IDENTIFY THE DISCOUNT (OPTIONAL)""",
        example="""Q3 BROAD STD""",
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

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""QnczeAlEIEJWmtYcYZEz""",
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

    DISCOUNT_CALCULATION_ORDER: int = Field(
        ...,
        alias="DISCOUNT_CALCULATION_ORDER",
        name="",
        description="""The discount applying order""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOC_NOTES: Optional[str] = Field(
        None,
        alias="DOC_NOTES",
        name="",
        description="""A description of the discount to be appeared on the documents specified in DOC_TYPES""",
        example="""iLImXoDUBNgrDKUCXzaC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOC_TYPES: Optional[str] = Field(
        None,
        alias="DOC_TYPES",
        name="",
        description="""The comma separated document types on which the DOC_NOTES needs to be appeared. Possible values are_x000D_
INV - Invoice_x000D_
ITN - Itinerary_x000D_
SUP - Supplier_x000D_
VOU - Voucher""",
        example="""TjuMksjEZYneVIEaeNGQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASS_PERCENTAGE_BAK: Optional[float] = Field(
        None,
        alias="PASS_PERCENTAGE_BAK",
        name="",
        description="""Deprecated""",
        example=89234.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_SCHEME: Optional[int] = Field(
        None,
        alias="PAYMENT_SCHEME",
        name="",
        description="""If a payment scheme has specifically been defined for the discount, this field holds the TravelBox code of the payment scheme. Otherwise this is null meaning the payment scheme applied to the contract is considered for the discount.""",
        example=7482,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_SCHEME: Optional[int] = Field(
        None,
        alias="CNX_SCHEME",
        name="",
        description="""If a supplier cancellation scheme has specifically been defined for the discount, this field holds the TravelBox code of the cancellation scheme. Otherwise this is null meaning the cancellation scheme applied to the contract is considered for the discount.""",
        example=4345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMD_SCHEME: Optional[int] = Field(
        None,
        alias="AMD_SCHEME",
        name="",
        description="""If a supplier amendment scheme has specifically been defined for the discount, this field holds the TravelBox code of the amendment scheme. Otherwise this is null meaning the amendment scheme applied to the contract is considered for the discount.""",
        example=2900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: Optional[datetime] = Field(
        None,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""2019-06-19 05:02:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: Optional[datetime] = Field(
        None,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""1995-07-18 15:44:28""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_FROM_TO: Optional[str] = Field(
        None,
        alias="BOOKED_FROM_TO",
        name="",
        description="""A flag indicating the discount has a booked from - booked to date range been specified""",
        example="""0""",
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

    DISCOUNTABLE_SUPPLIMENTS: Optional[str] = Field(
        None,
        alias="DISCOUNTABLE_SUPPLIMENTS",
        name="",
        description="""The system generated numbers of the supplements on which the discount is applicable. Multiple entries are comma seperated.""",
        example="""jjbwtMgNNPEVOuwxmYui""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1988-12-21 23:14:28""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: Optional[datetime] = Field(
        None,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2008-10-04 01:54:04""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: Optional[int] = Field(
        None,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15125,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""2023-05-03 11:30:09""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=15057,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACC_DISCOUNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:51.509957""",
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
        example="""ACC_DISCOUNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=24015911304659,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAccDiscountModel(BaseModel):
    """
    Payload class for TravelBox ACC_DISCOUNT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Discount"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store Discounts information. The values are setup in 'Discounts' node in Accommodation Manager"""  # optional
        unique_identifier = ["data.CONTRACT_ID", "data.DISCOUNT_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACC_DISCOUNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
