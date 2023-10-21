"""Source Data Contract Template for RES_CAR_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_CAR_BOOKING Data
    """

    NO_OF_CARS: Optional[int] = Field(
        None,
        alias="NO_OF_CARS",
        name="",
        description="""No of cars for the booking""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_VOUCHER_ID: float = Field(
        ...,
        alias="CAR_VOUCHER_ID",
        name="",
        description="""Used by Britz and Hertz to store car voucher id.""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DRIVER_PASSENGER_NO: Optional[int] = Field(
        None,
        alias="DRIVER_PASSENGER_NO",
        name="",
        description="""Deprecated""",
        example=2750,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DRIVER_AGE_MIN: Optional[int] = Field(
        None,
        alias="DRIVER_AGE_MIN",
        name="",
        description="""Allowed drivers Minimum age""",
        example=21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DRIVER_AGE_MAX: Optional[int] = Field(
        None,
        alias="DRIVER_AGE_MAX",
        name="",
        description="""Allowed drivers Maximum age""",
        example=120,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_BOOKING_GROUP: Optional[float] = Field(
        None,
        alias="CAR_BOOKING_GROUP",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_PRODUCT_NAME: Optional[str] = Field(
        None,
        alias="CAR_PRODUCT_NAME",
        name="",
        description="""car product name of the contact from 'CAR_MAIN_PRODUCT' table""",
        example="""Car Rental""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1988-11-10 02:36:24""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=14748198,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""CAR""",
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

    PICKUP_LOCATION_ID: int = Field(
        ...,
        alias="PICKUP_LOCATION_ID",
        name="",
        description="""pickup location id of the booking - from'LOCATION' table""",
        example=33538,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_LOCATION_ID: int = Field(
        ...,
        alias="DROPOFF_LOCATION_ID",
        name="",
        description="""dropoff location id of the booking - from'LOCATION' table""",
        example=33538,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_ID: int = Field(
        ...,
        alias="CAR_ID",
        name="",
        description="""System generated id of the car""",
        example=3734,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_PRODUCT: str = Field(
        ...,
        alias="CAR_PRODUCT",
        name="",
        description="""Car Product Item Code if user has selected 'Car Product' from markup rules.""",
        example="""CRENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ONEWAY_FEE: float = Field(
        ...,
        alias="ONEWAY_FEE",
        name="",
        description="""costs when a car is hired for a one way trip""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MULTIHIRE_NO: Optional[int] = Field(
        None,
        alias="MULTIHIRE_NO",
        name="",
        description="""Multi Hire number coming from booking constraints.""",
        example=7341,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_NAME: Optional[str] = Field(
        None,
        alias="CAR_NAME",
        name="",
        description="""combination of the car name and the car model from ::""",
        example="""Economy - Car""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_LOCATION: Optional[str] = Field(
        None,
        alias="PICKUP_LOCATION",
        name="",
        description="""pickup location name of the booking -  from'LOCATION' table""",
        example="""LOS ANGELES INT'L AIRPORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_LOCATION: Optional[str] = Field(
        None,
        alias="DROPOFF_LOCATION",
        name="",
        description="""dropoff location name of the booking -  from'LOCATION' table""",
        example="""LOS ANGELES INT'L AIRPORT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_TIME: Optional[str] = Field(
        None,
        alias="PICKUP_TIME",
        name="",
        description="""time of the pickup for the booking""",
        example="""06:00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_TIME: Optional[str] = Field(
        None,
        alias="DROPOFF_TIME",
        name="",
        description="""drop off of the pickup for the booking""",
        example="""06:00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_CLASS: Optional[str] = Field(
        None,
        alias="CAR_CLASS",
        name="",
        description="""Car class is one of the rule parameters in component markup schemes. When car class is selected as the rule parameter, user can mark multiple car classes valid for the mark-up scheme. For each car class selected there will be a separate entry in this table. If user selects other car parameters such as car product, then the number of entries will be selected car classes X selected car products(i.e.For each car class car product combination, there will be a separate entry)_x000D_
This column represents the car class code""",
        example=""" Alamo Car Rental""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_TYPE: Optional[str] = Field(
        None,
        alias="CAR_TYPE",
        name="",
        description="""Car type code if user has selected 'Car Type' from markup rules.""",
        example="""Economy Car""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_TYPE: Optional[float] = Field(
        None,
        alias="CONTRACT_TYPE",
        name="",
        description="""H = HOTEL, A = APARTMENT, G = GROUP""",
        example=2.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALCULATED_RENTED_DAYS: Optional[float] = Field(
        None,
        alias="CALCULATED_RENTED_DAYS",
        name="",
        description="""No of rented days of that particular car""",
        example=3.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SUPPLIER_DIRECTLY: Optional[str] = Field(
        None,
        alias="PAY_SUPPLIER_DIRECTLY",
        name="",
        description="""Flag for differenciate play supplier directly (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOREIGN_REFERENCE: Optional[str] = Field(
        None,
        alias="FOREIGN_REFERENCE",
        name="",
        description="""Deprecated""",
        example="""pUpQoWaojAvvXIzSIjMR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIR_CONDITIONED: str = Field(
        ...,
        alias="AIR_CONDITIONED",
        name="",
        description="""Specifies whether car is air conditioned or not_x000D_
Air conditioned - 1, Not air conditioned - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSMISSION_TYPE: Optional[str] = Field(
        None,
        alias="TRANSMISSION_TYPE",
        name="",
        description="""Deprecated""",
        example="""ycGwMOoTplOWKrBjUyaN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOOR_COUNT: Optional[float] = Field(
        None,
        alias="DOOR_COUNT",
        name="",
        description="""Deprecated""",
        example=2.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MILEGE_PROPERTY: Optional[str] = Field(
        None,
        alias="MILEGE_PROPERTY",
        name="",
        description="""Deprecated""",
        example="""eKGkhMhXKjbYnLMOmqmS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IMAGE_URL: Optional[str] = Field(
        None,
        alias="IMAGE_URL",
        name="",
        description="""always null and no valid usage in TBX search""",
        example="""aZNjdBCSuSudZhthcqBe""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FUEL_TYPE: Optional[str] = Field(
        None,
        alias="FUEL_TYPE",
        name="",
        description="""Deprecated""",
        example="""xVoMVSVVnxiwgklveLHn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAGGAGES: Optional[float] = Field(
        None,
        alias="BAGGAGES",
        name="",
        description="""No of baggages that car can carried""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DRIVE_TYPE: Optional[str] = Field(
        None,
        alias="DRIVE_TYPE",
        name="",
        description="""Deprecated""",
        example="""sgRMKjXuAijpIIWVfoTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAR_CLASS_ID: Optional[float] = Field(
        None,
        alias="CAR_CLASS_ID",
        name="",
        description="""NaN""",
        example=-1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEAT_COUNT: Optional[float] = Field(
        None,
        alias="SEAT_COUNT",
        name="",
        description="""No of seats available in the car""",
        example=4.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_CAR_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:16.072579""",
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
        example="""RES_CAR_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=48448413436320,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResCarBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_CAR_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Car"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains all the Booking Item level information specif for Car bookings."""  # optional
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
        key_path_value = "RES_CAR_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
