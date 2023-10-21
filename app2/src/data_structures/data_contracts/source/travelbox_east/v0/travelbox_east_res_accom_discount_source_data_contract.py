"""Source Data Contract Template for RES_ACCOM_DISCOUNT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_ACCOM_DISCOUNT Data
    """

    CNX_SCHEME: Optional[int] = Field(
        None,
        alias="CNX_SCHEME",
        name="",
        description="""If a supplier cancellation scheme has specifically been defined for the discount, this field holds the TravelBox code of the cancellation scheme. Otherwise this is null meaning the cancellation scheme applied to the contract is considered for the discount.""",
        example=2879,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANCILLARY_PAX: Optional[int] = Field(
        None,
        alias="ANCILLARY_PAX",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2020-06-01 14:38:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=10013767,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""HTL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: int = Field(
        ...,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_NO: int = Field(
        ...,
        alias="DISCOUNT_NO",
        name="",
        description="""The system generated number of the discount which belongs to the group""",
        example=28,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_CODE: Optional[str] = Field(
        None,
        alias="DISCOUNT_CODE",
        name="",
        description="""The TravelBox code of the discount, possible values are_x000D_
EBR - Early Bird_x000D_
PRI - Price_x000D_
FRN - Free Night_x000D_
HNY - Honeymoon Offer_x000D_
FAM - Family Offer_x000D_
ANY - Wedding Anniversary_x000D_
SNR - Senior Citizen_x000D_
FRE - Free Traveller""",
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
        example="""ePfPfJeDoLBXlnDkIdnl""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ADULT_DIS_COST: Optional[float] = Field(
        None,
        alias="CONTRACT_ADULT_DIS_COST",
        name="",
        description="""The total adult cost of this discount in contract currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_CHILD_DIS_COST: Optional[float] = Field(
        None,
        alias="CONTRACT_CHILD_DIS_COST",
        name="",
        description="""The total child cost of this discount in contract currency""",
        example=40848.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_INFANT_DIS_COST: Optional[float] = Field(
        None,
        alias="CONTRACT_INFANT_DIS_COST",
        name="",
        description="""The total infant discount cost for this discount in contract currency""",
        example=88978.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_DIS_IN_SELLING: Optional[float] = Field(
        None,
        alias="ADULT_DIS_IN_SELLING",
        name="",
        description="""Deprecated""",
        example=88624.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_DIS_IN_SELLING: Optional[float] = Field(
        None,
        alias="CHILD_DIS_IN_SELLING",
        name="",
        description="""Deprecated""",
        example=26281.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_DIS_IN_SELLING: Optional[float] = Field(
        None,
        alias="INFANT_DIS_IN_SELLING",
        name="",
        description="""Deprecated""",
        example=64893.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_DISCOUNT_COST: Optional[str] = Field(
        None,
        alias="CONTRACT_DISCOUNT_COST",
        name="",
        description="""The total cost of this discount in contract currency""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_DISCOUNT_PRICE: Optional[str] = Field(
        None,
        alias="CONTRACT_DISCOUNT_PRICE",
        name="",
        description="""The total price of this discount in contract currency""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_ADULT: float = Field(
        ...,
        alias="NETT_ADULT",
        name="",
        description="""The total adult cost of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_CHILD: float = Field(
        ...,
        alias="NETT_CHILD",
        name="",
        description="""The total child cost of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_INFANT: float = Field(
        ...,
        alias="NETT_INFANT",
        name="",
        description="""The total infant cost of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_ADULT: float = Field(
        ...,
        alias="GROSS_ADULT",
        name="",
        description="""The total adult price of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_CHILD: float = Field(
        ...,
        alias="GROSS_CHILD",
        name="",
        description="""The total child price of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_INFANT: float = Field(
        ...,
        alias="GROSS_INFANT",
        name="",
        description="""The total infant price of this discount in selling currency""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_SCHEME: Optional[int] = Field(
        None,
        alias="PAYMENT_SCHEME",
        name="",
        description="""If a payment scheme has specifically been defined for the discount, this field holds the TravelBox code of the payment scheme. Otherwise this is null meaning the payment scheme applied to the contract is considered for the discount.""",
        example=5237,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMD_SCHEME: Optional[int] = Field(
        None,
        alias="AMD_SCHEME",
        name="",
        description="""If a supplier amendment scheme has specifically been defined for the discount, this field holds the TravelBox code of the amendment scheme. Otherwise this is null meaning the amendment scheme applied to the contract is considered for the discount.""",
        example=3292,
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

    NON_PAYING_PAX: Optional[int] = Field(
        None,
        alias="NON_PAYING_PAX",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_ADDED: Optional[str] = Field(
        None,
        alias="MANUALLY_ADDED",
        name="",
        description="""Flag to check whether manually added or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_ACCOM_DISCOUNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:02.367059""",
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
        example="""RES_ACCOM_DISCOUNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=75865710038412,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResAccomDiscountModel(BaseModel):
    """
    Payload class for TravelBox RES_ACCOM_DISCOUNT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Accommodation Discount"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This stores information related to booking item Discounts which are offered at the accommodation contractlevel."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
            "data.DISCOUNT_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_ACCOM_DISCOUNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
