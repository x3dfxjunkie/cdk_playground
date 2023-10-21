"""Source Data Contract Template for RES_FLIGHT_SECTOR"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_FLIGHT_SECTOR Data
    """

    BOOKING_TOKEN: Optional[str] = Field(
        None,
        alias="BOOKING_TOKEN",
        name="",
        description="""NaN""",
        example="""VPzJJRAgfdHWOJThaXTm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HELD_BY: Optional[str] = Field(
        None,
        alias="HELD_BY",
        name="",
        description="""Deprecated""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CRS_SEATS: Optional[int] = Field(
        None,
        alias="CRS_SEATS",
        name="",
        description="""Number of seats reserved in CRS, associated with the sector""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_CONTRACT_ID: int = Field(
        ...,
        alias="ALLOC_CONTRACT_ID",
        name="",
        description="""Reference to the Contract_Id field of the contract where allocation is taken from. In a scenario where a  contract does not have allocations within itself but is getting allocations from another contract through shared allocations, this will refer the contract having the allocations.""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_LEG_NO: int = Field(
        ...,
        alias="ALLOC_LEG_NO",
        name="",
        description="""System generated id of the allocation leg""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_BLOCK_NO: int = Field(
        ...,
        alias="ALLOC_BLOCK_NO",
        name="",
        description="""Allocation Block number of the Allocation contract. Field reference to the table FA_ALLOCATION_BLOCK, column BLOCK_NO""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_SECTOR_NO: int = Field(
        ...,
        alias="ALLOC_SECTOR_NO",
        name="",
        description="""Sector number of the allocation contract. Field reference to the FA_SECTOR table, SECTOR_NO column.""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_BRAND: Optional[str] = Field(
        None,
        alias="ALLOC_BRAND",
        name="",
        description="""Deprecated""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_SEATS: Optional[int] = Field(
        None,
        alias="ALLOC_SEATS",
        name="",
        description="""ALLOC_SEATS IN THE RES_FLIGHT_SECTOR""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_PACKAGE_NO: Optional[int] = Field(
        None,
        alias="ALLOC_PACKAGE_NO",
        name="",
        description="""Copy of the RES_FLIGHT_SECTOR table same column name before a schedule change process""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_PACKAGE_SEATS: int = Field(
        ...,
        alias="ALLOC_PACKAGE_SEATS",
        name="",
        description="""Copy of the RES_FLIGHT_SECTOR table same column name before a schedule change process""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAGGAGE: Optional[str] = Field(
        None,
        alias="BAGGAGE",
        name="",
        description="""Baggage information is specified either in pieces(PC) or kilograms(K). All baggage information is specified here in a comma separated manner for each pax type._x000D_
1 PC - 1 piece_x000D_
1 K - 1 Kg""",
        example="""0 PC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOT_VALID_AFTER: Optional[datetime] = Field(
        None,
        alias="NOT_VALID_AFTER",
        name="",
        description="""Deprecated""",
        example="""1992-11-17 16:27:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHECKIN_BEFORE: Optional[str] = Field(
        None,
        alias="CHECKIN_BEFORE",
        name="",
        description="""Time on or before the passengers are supposed to check in""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOUCHDOWN: Optional[str] = Field(
        None,
        alias="TOUCHDOWN",
        name="",
        description="""Touchdown airport codes between departure airport and destination airport""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON_ID: int = Field(
        ...,
        alias="ADDON_ID",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON_SECTOR: int = Field(
        ...,
        alias="ADDON_SECTOR",
        name="",
        description="""The sector number that is associated with a particular addon id""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON_CHARGE_NO: int = Field(
        ...,
        alias="ADDON_CHARGE_NO",
        name="",
        description="""System generated number of addon charge""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_GROUP_ID: int = Field(
        ...,
        alias="ALLOC_GROUP_ID",
        name="",
        description="""System generated id of the allocation contract group""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FARE_BASIS: Optional[str] = Field(
        None,
        alias="FARE_BASIS",
        name="",
        description="""Fare basis rule in free text""",
        example="""XAVNA0EE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PUB_FARE_TYPE_CODE: Optional[str] = Field(
        None,
        alias="PUB_FARE_TYPE_CODE",
        name="",
        description="""Deprecated""",
        example="""pIVnVdwlwJagkiozWLhj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPERATING_AIRLINE: Optional[str] = Field(
        None,
        alias="OPERATING_AIRLINE",
        name="",
        description="""IATA code of operating airline""",
        example="""cEOcnIJmvSmENtbQzlby""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CABIN_CLASS: Optional[str] = Field(
        None,
        alias="CABIN_CLASS",
        name="",
        description="""Cabin class of the cabin""",
        example="""ECONOMY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DURATION: Optional[int] = Field(
        None,
        alias="DURATION",
        name="",
        description="""Duration of the booking item""",
        example=172,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAPPING_FARE_BASIS: Optional[str] = Field(
        None,
        alias="MAPPING_FARE_BASIS",
        name="",
        description="""This is the equivalent Published fare fare basis for a particular Private fare fare basis""",
        example="""XAVNA0EE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NO_OF_STOPS: int = Field(
        ...,
        alias="NO_OF_STOPS",
        name="",
        description="""Specifies the number of touchdowns associated with the sector""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ITEM_ORDER: Optional[int] = Field(
        None,
        alias="PKG_ITEM_ORDER",
        name="",
        description="""If the booking item belongs to a package, the order number of the booking item within the package.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRLINE_LOCATOR: Optional[str] = Field(
        None,
        alias="AIRLINE_LOCATOR",
        name="",
        description="""Airline locator code associated with the respective flight booking""",
        example="""GYM3EE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PUB_TICKET_INFO_ID: Optional[int] = Field(
        None,
        alias="PUB_TICKET_INFO_ID",
        name="",
        description="""Ticket info from the Published fare overriding contract.""",
        example=1640,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE_COMBINATION: Optional[int] = Field(
        None,
        alias="PRICE_COMBINATION",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHANGE_OF_GAUGE: Optional[str] = Field(
        None,
        alias="CHANGE_OF_GAUGE",
        name="",
        description="""Specifies whether the flight sector has a change of equipment""",
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
        example="""1985-07-12 00:46:03""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPERATING_AIRLINE_INFO: Optional[str] = Field(
        None,
        alias="OPERATING_AIRLINE_INFO",
        name="",
        description="""When Shared Airline Designator or Wet Leas Airline Designation situation, operating carrier is not coming from Amadeus. but it's received operating carrier information. this column use for this purpose """,
        example="""COMPASS DBA DELTA CONNECTION""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CO2_INFO: Optional[str] = Field(
        None,
        alias="CO2_INFO",
        name="",
        description="""NaN""",
        example="""zPiIQmsQrgmCjYHKazea""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PUB_CONTRACT_ID: Optional[int] = Field(
        None,
        alias="PUB_CONTRACT_ID",
        name="",
        description="""Published fare override contract id. System generated Id of the overriding contract.""",
        example=8969,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAGGAGE_CHD: Optional[str] = Field(
        None,
        alias="BAGGAGE_CHD",
        name="",
        description="""Deprecated""",
        example="""ZFYuASbIHiHLTCAZZAEf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAGGAGE_INF: Optional[str] = Field(
        None,
        alias="BAGGAGE_INF",
        name="",
        description="""Deprecated""",
        example="""VvoINmlHLBQKmvTYznQx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESIGNATOR: Optional[str] = Field(
        None,
        alias="DESIGNATOR",
        name="",
        description="""Ticket Designator returned from GDS for Cat 25 fares. Only saved if available, otherwise null. (for published and nett fares this would be null)""",
        example="""LN79""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPERATING_AIRLINE_FLT_NO: Optional[str] = Field(
        None,
        alias="OPERATING_AIRLINE_FLT_NO",
        name="",
        description="""Flight no specified by the operating airline""",
        example="""ezvpMLKsHOKvHKgmaNWF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEAT_RELEASED: Optional[str] = Field(
        None,
        alias="SEAT_RELEASED",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFO_ONLY_KEY: Optional[str] = Field(
        None,
        alias="INFO_ONLY_KEY",
        name="",
        description="""NaN""",
        example="""wfmEmPJxUbpQDORUNnQt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEAL_CODE: Optional[str] = Field(
        None,
        alias="MEAL_CODE",
        name="",
        description="""Meal codes returned by Amadeus.""",
        example="""KIVwiudALwhnTAEOjuit""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=11411032,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""FLT""",
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

    SECTOR_NO: int = Field(
        ...,
        alias="SECTOR_NO",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_ORDER: Optional[int] = Field(
        None,
        alias="ITINERARY_ORDER",
        name="",
        description="""position in the itinerary order of all items within the booking. By Clicking on Reservation Client 'Itinerary' node will show the itinerary in this order. User can change the order (position) manually. This is -1 for Transfer items""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LEG_NO: int = Field(
        ...,
        alias="LEG_NO",
        name="",
        description="""Flight leg number""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIRECTION: str = Field(
        ...,
        alias="DIRECTION",
        name="",
        description="""Not in the disney scope""",
        example="""O""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRLINE: str = Field(
        ...,
        alias="AIRLINE",
        name="",
        description="""Unique IATA code of the airline""",
        example="""DL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FLIGHT_NO: Optional[str] = Field(
        None,
        alias="FLIGHT_NO",
        name="",
        description="""The Flight number returned by Amadeus. (Ex: 510)""",
        example="""5763""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_CLASS: str = Field(
        ...,
        alias="BOOKING_CLASS",
        name="",
        description="""This is a temporary table.""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOCATION_CLASS: Optional[str] = Field(
        None,
        alias="ALLOCATION_CLASS",
        name="",
        description="""ALLOCATION CLASS IN THE RES_FLIGHT_SECTOR""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP: str = Field(
        ...,
        alias="DEP",
        name="",
        description="""IATA code of departure airport""",
        example="""SEA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DES: str = Field(
        ...,
        alias="DES",
        name="",
        description="""IATA code of destination airport""",
        example="""SNA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_DATE: datetime = Field(
        ...,
        alias="DEP_DATE",
        name="",
        description="""Booking departure date""",
        example="""1976-06-24 16:50:14""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DES_DATE: datetime = Field(
        ...,
        alias="DES_DATE",
        name="",
        description="""Destination arrival date""",
        example="""2001-01-09 14:15:42""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_TERMINAL: Optional[str] = Field(
        None,
        alias="DEP_TERMINAL",
        name="",
        description="""Departure terminal after changing the flight item""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARR_TERMINAL: Optional[str] = Field(
        None,
        alias="ARR_TERMINAL",
        name="",
        description="""Arrival terminal after changing the flight item""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EQUIPMENT: Optional[str] = Field(
        None,
        alias="EQUIPMENT",
        name="",
        description="""Aircraft details associated with the flight sector""",
        example="""E75""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS_CODE: Optional[str] = Field(
        None,
        alias="STATUS_CODE",
        name="",
        description="""Code that specifies the status of the sector for GDS reserved flights""",
        example="""HK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_FLIGHT_SECTOR Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:19.733391""",
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
        example="""RES_FLIGHT_SECTOR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=99637698902960,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResFlightSectorModel(BaseModel):
    """
    Payload class for TravelBox RES_FLIGHT_SECTOR
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Flight Section"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains all the sector level (itinerary level) information of the flight bookings in TravelBox"""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.PRODUCT_CODE", "data.ITEM_NO", "data.SECTOR_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_FLIGHT_SECTOR"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
