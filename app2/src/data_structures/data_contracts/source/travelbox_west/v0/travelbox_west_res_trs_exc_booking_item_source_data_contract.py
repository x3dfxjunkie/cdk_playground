"""Source Data Contract Template for RES_TRS_EXC_BOOKING_ITEM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_TRS_EXC_BOOKING_ITEM Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=13913582,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""TRS""",
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

    TYPE: str = Field(
        ...,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""T""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_NO: int = Field(
        ...,
        alias="TRANSFER_NO",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_POINT: str = Field(
        ...,
        alias="PICKUP_POINT",
        name="",
        description="""Pick up point of the transfer or excursion""",
        example="""Santa Ana John Wayne Apt , Santa Ana , United States of America""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_POINT: str = Field(
        ...,
        alias="DROPOFF_POINT",
        name="",
        description="""Drop off point of the transfer or excursion""",
        example="""DLR Resort , Anaheim , United States of America""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""QoXkdqQppDMTgzQAfeZy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_MODE_CODE: str = Field(
        ...,
        alias="TRANSFER_MODE_CODE",
        name="",
        description="""Transfer mode code, Car- CAR, Seat in Coach - SIC, Lux Bus - LUB, Limo - Limo""",
        example="""KS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_MODE: Optional[str] = Field(
        None,
        alias="TRANSFER_MODE",
        name="",
        description="""Deprecated""",
        example="""Karmel Shared Shuttle""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_POINT_CODE: str = Field(
        ...,
        alias="PICKUP_POINT_CODE",
        name="",
        description="""Deprecated""",
        example="""SNA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PICKUP_POINT_TYPE: str = Field(
        ...,
        alias="PICKUP_POINT_TYPE",
        name="",
        description="""Deprecated""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_POINT_CODE: str = Field(
        ...,
        alias="DROPOFF_POINT_CODE",
        name="",
        description="""Corresponding code in the city table to the drop off city""",
        example="""DISNEY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DROPOFF_POINT_TYPE: str = Field(
        ...,
        alias="DROPOFF_POINT_TYPE",
        name="",
        description="""Deprecated""",
        example="""R""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXC_LOCATION_ID: Optional[int] = Field(
        None,
        alias="EXC_LOCATION_ID",
        name="",
        description="""Deprecated""",
        example=3719,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXC_LOCATION: Optional[str] = Field(
        None,
        alias="EXC_LOCATION",
        name="",
        description="""Excursion location description""",
        example="""wwqpENQGrgIBcXXTQmXw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_MODE_NO: int = Field(
        ...,
        alias="TRANSFER_MODE_NO",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MINIMUM_VEHICLES: Optional[int] = Field(
        None,
        alias="MINIMUM_VEHICLES",
        name="",
        description="""The minimum number of vehicles associated with the transfer/excursion booking item""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RETURN_COMPULSORY: str = Field(
        ...,
        alias="RETURN_COMPULSORY",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_NAME: Optional[str] = Field(
        None,
        alias="TRANSFER_NAME",
        name="",
        description="""Name of the transfer""",
        example="""2022 Karmel Shared SNA/ANA 5 Max CC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_PRODUCT_ID: Optional[int] = Field(
        None,
        alias="H2H_PRODUCT_ID",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_BOOKING_TYPE_ID: Optional[int] = Field(
        None,
        alias="H2H_BOOKING_TYPE_ID",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_FLIGHT_NO: Optional[str] = Field(
        None,
        alias="OUTBOUND_FLIGHT_NO",
        name="",
        description="""NaN""",
        example="""wGNoucWdHNUhKwIYgvea""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_DEP_APT: Optional[str] = Field(
        None,
        alias="OUTBOUND_DEP_APT",
        name="",
        description="""NaN""",
        example="""XgyuomPwVrXIHtmYvvzN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_ARR_TIME: Optional[datetime] = Field(
        None,
        alias="OUTBOUND_ARR_TIME",
        name="",
        description="""NaN""",
        example="""2003-09-12 11:45:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_AIRLINE: Optional[str] = Field(
        None,
        alias="OUTBOUND_AIRLINE",
        name="",
        description="""IATA code of destination airport""",
        example="""BKkiGilodagOBlvbAdsz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_FLIGHT_NO: Optional[str] = Field(
        None,
        alias="INBOUND_FLIGHT_NO",
        name="",
        description="""NaN""",
        example="""HiGzuttTWQbFUXNNIHpD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_ARR_APT: Optional[str] = Field(
        None,
        alias="INBOUND_ARR_APT",
        name="",
        description="""NaN""",
        example="""SYSOBTzptxRTmzMIPTmw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_DEP_TIME: Optional[datetime] = Field(
        None,
        alias="INBOUND_DEP_TIME",
        name="",
        description="""NaN""",
        example="""2007-01-05 01:45:09""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_AIRLINE: Optional[str] = Field(
        None,
        alias="INBOUND_AIRLINE",
        name="",
        description="""IATA code of inbound airline""",
        example="""jtIeceWRXRdwFMOYarQZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_SHIP_NAME: Optional[str] = Field(
        None,
        alias="OUTBOUND_SHIP_NAME",
        name="",
        description="""NaN""",
        example="""bsYjHEdrFZSBpRsCWJLy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUTBOUND_DEP_PORT: Optional[str] = Field(
        None,
        alias="OUTBOUND_DEP_PORT",
        name="",
        description="""NaN""",
        example="""GbThvfQTgiAFDQfLBuuY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_ARR_PORT: Optional[str] = Field(
        None,
        alias="INBOUND_ARR_PORT",
        name="",
        description="""NaN""",
        example="""NOIagKJrHyRUgyDKNjox""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INBOUND_SHIP_NAME: Optional[str] = Field(
        None,
        alias="INBOUND_SHIP_NAME",
        name="",
        description="""NaN""",
        example="""HRYRAMlOSoCVuAgDZNfi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CRU_FOREIGN_BKNG_ID: Optional[str] = Field(
        None,
        alias="CRU_FOREIGN_BKNG_ID",
        name="",
        description="""NaN""",
        example="""VSBvCjpALpslkjjJOrpx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    START_END_TIMES_EDITED: str = Field(
        ...,
        alias="START_END_TIMES_EDITED",
        name="",
        description="""In reservation transfer summary or reservation transfer loading start and end times edited or not are specified or not, 1 - edited , 0 not not""",
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
        example="""1989-08-26 02:24:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_FREQ: str = Field(
        ...,
        alias="FULFILLMENT_FREQ",
        name="",
        description="""Specify the frequency type of gategory, P: per Person, I: Per Item""",
        example="""I""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_TRS_EXC_BOOKING_ITEM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:33.595731""",
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
        example="""RES_TRS_EXC_BOOKING_ITEM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=82007547243320,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResTrsExcBookingItemModel(BaseModel):
    """
    Payload class for TravelBox RES_TRS_EXC_BOOKING_ITEM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Transfer Excursion"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table holds itinerary level information related to Transfer bookings."""  # optional
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
        key_path_value = "RES_TRS_EXC_BOOKING_ITEM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
