"""Source Data Contract Template for RES_GENERIC_DISCOUNT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_GENERIC_DISCOUNT Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27644293,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""GEN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: int = Field(
        ...,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=4,
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

    REFERENCE: str = Field(
        ...,
        alias="REFERENCE",
        name="",
        description="""CODE TO IDENTIFY THE DISCOUNT (OPTIONAL)""",
        example="""100 PERCENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: str = Field(
        ...,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""If booked from 22/04/2022 to 31/12/2023, get 100 % on Adult, 0 % on Teen, 100 % on Child, 0 % on Infant  discount on price and get Basic Plan - 100% Discount (Subject to availability )""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NET_ADULT: float = Field(
        ...,
        alias="NET_ADULT",
        name="",
        description="""Total adult cost of the supplement""",
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
        example=4.2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_CHILD: float = Field(
        ...,
        alias="GROSS_CHILD",
        name="",
        description="""The total child price of this discount in selling currency""",
        example=1.4,
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

    NET_CHILD: float = Field(
        ...,
        alias="NET_CHILD",
        name="",
        description="""Total child cost of the supplement""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NET_INFANT: float = Field(
        ...,
        alias="NET_INFANT",
        name="",
        description="""Total infant cost of the supplement""",
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
        example=2897,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_SCHEME: Optional[int] = Field(
        None,
        alias="CNX_SCHEME",
        name="",
        description="""If a supplier cancellation scheme has specifically been defined for the discount, this field holds the TravelBox code of the cancellation scheme. Otherwise this is null meaning the cancellation scheme applied to the contract is considered for the discount.""",
        example=2803,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMD_SCHEME: Optional[int] = Field(
        None,
        alias="AMD_SCHEME",
        name="",
        description="""If a supplier amendment scheme has specifically been defined for the discount, this field holds the TravelBox code of the amendment scheme. Otherwise this is null meaning the amendment scheme applied to the contract is considered for the discount.""",
        example=4939,
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

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2018-08-28 04:03:14""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_GENERIC_DISCOUNT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:23.429189""",
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
        example="""RES_GENERIC_DISCOUNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=21675427717238,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResGenericDiscountModel(BaseModel):
    """
    Payload class for TravelBox RES_GENERIC_DISCOUNT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Generic Discount"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This stores information related to booking item Discounts which are offered at the Generic contract level."""  # optional
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
        key_path_value = "RES_GENERIC_DISCOUNT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
