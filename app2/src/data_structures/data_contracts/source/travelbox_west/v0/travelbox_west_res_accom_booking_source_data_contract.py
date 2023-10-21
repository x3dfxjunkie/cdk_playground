"""Source Data Contract Template for RES_ACCOM_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_ACCOM_BOOKING Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2015-10-29 18:49:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_RESERVATION_ID: Optional[int] = Field(
        None,
        alias="EXT_RESERVATION_ID",
        name="",
        description="""NaN""",
        example=1631481,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION: Optional[str] = Field(
        None,
        alias="LOCATION",
        name="",
        description="""Booked location""",
        example="""ANA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EC_COST: Optional[float] = Field(
        None,
        alias="EC_COST",
        name="",
        description="""If passengers are check-in early for this hotel, this field holds the total cost for early check in""",
        example=39913.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LC_COST: Optional[float] = Field(
        None,
        alias="LC_COST",
        name="",
        description="""If passengers are check-out late for this hotel, this field holds the total cost for late checkout""",
        example=66618.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_FOR_REPRICE: Optional[str] = Field(
        None,
        alias="VALID_FOR_REPRICE",
        name="",
        description="""A flag indicating whether this booking item is repriceable ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCOM_TYPE: str = Field(
        ...,
        alias="ACCOM_TYPE",
        name="",
        description="""hotel = 'H', apartment = 'A', chainHotels = 'HG', chainApartment = 'AG', groupHotels = 'GH' , groupApartment = 'GA' , prePostHotels = 'PH' , prePostApartment = 'PA'""",
        example="""H""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_COMBINABLE_HOTEL: int = Field(
        ...,
        alias="MIN_COMBINABLE_HOTEL",
        name="",
        description="""Refer MIN_COMBINABLE_HOTEL column in ACC_CONTRACT_GROUP table""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOTEL_ADDRESS: Optional[str] = Field(
        None,
        alias="HOTEL_ADDRESS",
        name="",
        description="""The address of the Hotel""",
        example="""1150 Magic Way""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_RELEASE_DAY: Optional[int] = Field(
        None,
        alias="MAX_RELEASE_DAY",
        name="",
        description="""Maximum day of release allocation  within allocations period of the booking""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_PRICE_DIFF: Optional[float] = Field(
        None,
        alias="H2H_PRICE_DIFF",
        name="",
        description="""Price difference between purchase cost from H2H and Cost in contract in TBX""",
        example=81857.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NON_REFUNDABLE: Optional[str] = Field(
        None,
        alias="NON_REFUNDABLE",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLEMENT_CATEGORY_ID: int = Field(
        ...,
        alias="SUPPLEMENT_CATEGORY_ID",
        name="",
        description="""Refer CATEGORY_ID column in ACC_SUPPLIMENT_TYPE table""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=14711192,
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

    RESERVATION_ID: int = Field(
        ...,
        alias="RESERVATION_ID",
        name="",
        description="""The system generated id of the reservation""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCOM_ID: int = Field(
        ...,
        alias="ACCOM_ID",
        name="",
        description="""The system generated id of the Accom Supplier""",
        example=29926,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NIGHTS: int = Field(
        ...,
        alias="NIGHTS",
        name="",
        description="""This is 1 since the rates are for a day.""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    JOINED_CONTRACT_ID: Optional[int] = Field(
        None,
        alias="JOINED_CONTRACT_ID",
        name="",
        description="""Contract id that if allocation hold from continue contract""",
        example=2021,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOREIGN_ACCOM_ID: Optional[str] = Field(
        None,
        alias="FOREIGN_ACCOM_ID",
        name="",
        description="""If the booking is done in a H2H system, this field stores the booking id of the H2H system""",
        example="""uqUCcMcmVysifAHnapCv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_REQUESTS: Optional[str] = Field(
        None,
        alias="SPECIAL_REQUESTS",
        name="",
        description="""SPECIAL REQUESTS MADE WITH CRITERIA""",
        example="""tplwRXimbUdqxPPJIEwG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOTEL_NAME: str = Field(
        ...,
        alias="HOTEL_NAME",
        name="",
        description="""Hotel name of the hotel which is supplied by the related suppler in the booking item from 'SUPPLIER' table""",
        example="""Disneyland Hotel""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAR_RATING: Optional[str] = Field(
        None,
        alias="STAR_RATING",
        name="",
        description="""Hotel Star Rating code selected for 'Star Rating' parameter  in discount scheme setup.""",
        example="""Superior""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EARLY_CHECKIN: str = Field(
        ...,
        alias="EARLY_CHECKIN",
        name="",
        description="""A flag to indicate whether for this hotel booking, passengers are check-in early than standard time ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LATE_CHECKOUT: str = Field(
        ...,
        alias="LATE_CHECKOUT",
        name="",
        description="""A flag to indicate that whether for this hotel booking, passengers are going to check-out late than standard time ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EC_PRICE: Optional[float] = Field(
        None,
        alias="EC_PRICE",
        name="",
        description="""If passengers are check-in early for this hotel, this field holds the total price for early check in""",
        example=62113.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LC_PRICE: Optional[float] = Field(
        None,
        alias="LC_PRICE",
        name="",
        description="""If passengers are check-out late for this hotel, this field holds the total price for late checkout""",
        example=1875.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_NIGHT_PRICE: Optional[float] = Field(
        None,
        alias="EXT_NIGHT_PRICE",
        name="",
        description="""Deprecated""",
        example=42210.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EC_TIME: Optional[int] = Field(
        None,
        alias="EC_TIME",
        name="",
        description="""If passengers are check-in early for this hotel, this field holds the early check in time""",
        example=7446,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LC_TIME: Optional[int] = Field(
        None,
        alias="LC_TIME",
        name="",
        description="""If passengers are check-out late for this hotel, this field holds the late checkout time""",
        example=4170,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MULTIHIRE_NO: Optional[int] = Field(
        None,
        alias="MULTIHIRE_NO",
        name="",
        description="""Multi Hire number coming from booking constraints.""",
        example=3826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEAL_SCHEME: Optional[str] = Field(
        None,
        alias="MEAL_SCHEME",
        name="",
        description="""The applicable meal plan of the booking item""",
        example="""Room Only""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_POST_SUPPLIER: Optional[int] = Field(
        None,
        alias="PRE_POST_SUPPLIER",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_ACCOM_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:35.435535""",
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
        example="""RES_ACCOM_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=50516573643176,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResAccomBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_ACCOM_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Accommodation"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = (
            """This table contains all the Booking Item level information specif for accom bookings."""  # optional
        )
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_ACCOM_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
