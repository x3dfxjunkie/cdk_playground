"""Source Data Contract Template for RES_GENERIC_SUPPLEMENT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_GENERIC_SUPPLEMENT Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=14619346,
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
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLEMENT_NO: int = Field(
        ...,
        alias="SUPPLEMENT_NO",
        name="",
        description="""The system generated number of the supplement of the contract""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NET_ADULT: float = Field(
        ...,
        alias="NET_ADULT",
        name="",
        description="""Total adult cost of the supplement""",
        example=1.68,
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

    GROSS_ADULT: float = Field(
        ...,
        alias="GROSS_ADULT",
        name="",
        description="""The total adult price of this discount in selling currency""",
        example=3.02,
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

    COMPULSARY: str = Field(
        ...,
        alias="COMPULSARY",
        name="",
        description="""A flag indicating the board basis is compulsory ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: str = Field(
        ...,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Pin & Lanyard - Collectible Pin & Lanyard""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FREE: str = Field(
        ...,
        alias="FREE",
        name="",
        description="""A flag indicating whether supplement is free or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCLUDED: str = Field(
        ...,
        alias="INCLUDED",
        name="",
        description="""A flag indicating the supplement is included in the contract fare ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SUPPLIER_LOCALY: Optional[str] = Field(
        None,
        alias="PAY_SUPPLIER_LOCALY",
        name="",
        description="""Refer PAY_SUPPLIER_DIRECTLY column in ACC_SUPPLEMENT table""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: Optional[str] = Field(
        None,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""OPWvkGfvEIEdjfFJEOqi""",
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

    APPLICABLE_ADULT: Optional[int] = Field(
        None,
        alias="APPLICABLE_ADULT",
        name="",
        description="""Number of adults belong to the supplement""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_CHILD: Optional[int] = Field(
        None,
        alias="APPLICABLE_CHILD",
        name="",
        description="""Number of Child belong to the supplement""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_INFANT: Optional[str] = Field(
        None,
        alias="APPLICABLE_INFANT",
        name="",
        description="""Number of Infants belong to the supplement""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNITS: Optional[int] = Field(
        None,
        alias="UNITS",
        name="",
        description="""The number of allocations""",
        example=1,
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
        example="""2010-03-20 16:23:46""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_FREQ: Optional[str] = Field(
        None,
        alias="FULFILLMENT_FREQ",
        name="",
        description="""Specify the frequency type of gategory, P: per Person, I: Per Item""",
        example="""P""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_GENERATED: str = Field(
        ...,
        alias="VOUCHER_GENERATED",
        name="",
        description="""Is Voucher Entry Generated For Booking Item""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_GENERIC_SUPPLEMENT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:06.424893""",
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
        example="""RES_GENERIC_SUPPLEMENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=32085043983900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResGenericSupplementModel(BaseModel):
    """
    Payload class for TravelBox RES_GENERIC_SUPPLEMENT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Generic Supplement"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This holds information related to the Supplementory items booked with Generic itemes. These Supplements are offered / defined at the Generic contract."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
            "data.SUPPLEMENT_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_GENERIC_SUPPLEMENT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
