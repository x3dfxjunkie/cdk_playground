"""Source Data Contract Template for RES_FLIGHT_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_FLIGHT_BOOKING Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2000-03-25 13:24:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEAT_TYPE: Optional[str] = Field(
        None,
        alias="SEAT_TYPE",
        name="",
        description="""Requested Seat Type in the Flight Booking_x000D_
""",
        example="""ST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GDS_QUEUE_ERROR_ID: Optional[float] = Field(
        None,
        alias="GDS_QUEUE_ERROR_ID",
        name="",
        description="""NaN""",
        example=35537.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MASK: Optional[str] = Field(
        None,
        alias="MASK",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IS_LCC_RESULT: str = Field(
        ...,
        alias="IS_LCC_RESULT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSPORT_TYPE: str = Field(
        ...,
        alias="TRANSPORT_TYPE",
        name="",
        description="""NaN""",
        example="""AIR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORG_FARE_TYPE: Optional[str] = Field(
        None,
        alias="ORG_FARE_TYPE",
        name="",
        description="""NaN""",
        example="""PVT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOC_DELIVERY_EMAIL: Optional[str] = Field(
        None,
        alias="DOC_DELIVERY_EMAIL",
        name="",
        description="""NaN""",
        example="""vhvoYgRahvGhOWZhHLzM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INSTANT_TICKETED: Optional[str] = Field(
        None,
        alias="INSTANT_TICKETED",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IS_TBX_ONLY_NAME_CHANGE: str = Field(
        ...,
        alias="IS_TBX_ONLY_NAME_CHANGE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DYNAMIC_PTC: str = Field(
        ...,
        alias="DYNAMIC_PTC",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WHOLE_SALE_COMM: Optional[float] = Field(
        None,
        alias="WHOLE_SALE_COMM",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WHOLE_SALE_COMM_TYPE: Optional[str] = Field(
        None,
        alias="WHOLE_SALE_COMM_TYPE",
        name="",
        description="""Deprecated""",
        example="""ivUPKAEIcprdmeAIOcSb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USER_LETTER_GENERATED: str = Field(
        ...,
        alias="USER_LETTER_GENERATED",
        name="",
        description="""A flag to indicate whether the user letter is generated after schedule change by pnr processing job.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKETED_USER: Optional[int] = Field(
        None,
        alias="TICKETED_USER",
        name="",
        description="""The user associated with ticket issuance""",
        example=15662,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BSP_TRAVEL_CODE: Optional[str] = Field(
        None,
        alias="BSP_TRAVEL_CODE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""hEexdqKGrnkwsPVrlEDh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CRS_RULES: Optional[str] = Field(
        None,
        alias="CRS_RULES",
        name="",
        description="""Fare rules returned by the CRS in case of CRS involved flight booking""",
        example="""No Rules Returned from CRS.""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANCEL_PNR: str = Field(
        ...,
        alias="CANCEL_PNR",
        name="",
        description="""Specifies whether there exists a PNR that can be cancelled""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONNECTED_ITEM_NO: Optional[int] = Field(
        None,
        alias="CONNECTED_ITEM_NO",
        name="",
        description="""Only for flight booking items. If there are multiple flight items in the booking with same pax key, the first flight item's number will be set as the connected item number in other flight items.""",
        example=5878,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MINIMAL_DEPOSIT_AMOUNT: Optional[float] = Field(
        None,
        alias="MINIMAL_DEPOSIT_AMOUNT",
        name="",
        description="""Minimal deposit amount for the booking item,""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPOSIT_DATE_EMERGENCY: str = Field(
        ...,
        alias="DEPOSIT_DATE_EMERGENCY",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_FOR_TICKETING: str = Field(
        ...,
        alias="VALID_FOR_TICKETING",
        name="",
        description="""FLIGHT ITEM WISE CAN TICKETING""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_TICKET_ONLY: str = Field(
        ...,
        alias="MANUAL_TICKET_ONLY",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PNR_PRICE_OVERRIDE_DATE: Optional[datetime] = Field(
        None,
        alias="PNR_PRICE_OVERRIDE_DATE",
        name="",
        description="""Deprecated""",
        example="""1995-08-08 21:56:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_PRICED_FLIGHT: str = Field(
        ...,
        alias="MANUALLY_PRICED_FLIGHT",
        name="",
        description="""Specifies whether flight item is manually priced or not Priced - 1, Not priced - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PNR_CNX_CHECKED: str = Field(
        ...,
        alias="PNR_CNX_CHECKED",
        name="",
        description="""A flag to indicate whether it's checked pnr cancellation status or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SSR_NOTES: Optional[str] = Field(
        None,
        alias="SSR_NOTES",
        name="",
        description="""Special service request notes""",
        example="""DlqTffbIBSaiOTLcYKJg""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CORPORATE_ID: Optional[str] = Field(
        None,
        alias="CORPORATE_ID",
        name="",
        description="""Deprecated""",
        example="""FiADFMqKULURXQLTjEDC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_HOLD_RELEASE_TIME: Optional[datetime] = Field(
        None,
        alias="H2H_HOLD_RELEASE_TIME",
        name="",
        description="""Specifies the booking hold time for H2H bookings""",
        example="""1984-04-01 11:09:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GDS_QUEUE_MSG: Optional[str] = Field(
        None,
        alias="GDS_QUEUE_MSG",
        name="",
        description="""GDS message returned from the pnr processing job.""",
        example="""Error in remove PNR from AMD queue 51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIGINAL_CRS: Optional[str] = Field(
        None,
        alias="ORIGINAL_CRS",
        name="",
        description="""The CRS of PNR before the migration""",
        example="""fttNDVCgEmofwxCwVZHL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIGINAL_PNR: Optional[str] = Field(
        None,
        alias="ORIGINAL_PNR",
        name="",
        description="""The PNR number before the migration""",
        example="""IFkLBwyeOANkAFJQMoLA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIGRATED_DATE: Optional[datetime] = Field(
        None,
        alias="MIGRATED_DATE",
        name="",
        description="""Migrated date of PNR, in case of PNR migration from a GDS to some other GDS""",
        example="""1978-04-22 06:50:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APIS_INFO_SENT: str = Field(
        ...,
        alias="APIS_INFO_SENT",
        name="",
        description="""Specifies whether advance passenger information is sent to GDS or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=11581832,
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
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_TYPE: str = Field(
        ...,
        alias="CONTRACT_TYPE",
        name="",
        description="""H = HOTEL, A = APARTMENT, G = GROUP""",
        example="""FLT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FARE_TYPE: str = Field(
        ...,
        alias="FARE_TYPE",
        name="",
        description="""Specifies the supplement fare type_x000D_
Daily - D_x000D_
Weekly - W_x000D_
Whole trip - T""",
        example="""PVT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_CONTRACT: int = Field(
        ...,
        alias="OUT_CONTRACT",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_RULE: int = Field(
        ...,
        alias="OUT_RULE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_ROUTE_GROUP: int = Field(
        ...,
        alias="OUT_ROUTE_GROUP",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_ROUTE: int = Field(
        ...,
        alias="OUT_ROUTE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_TICKET_INFO_ID: int = Field(
        ...,
        alias="OUT_TICKET_INFO_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_CONTRACT: int = Field(
        ...,
        alias="IN_CONTRACT",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_RULE: int = Field(
        ...,
        alias="IN_RULE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_ROUTE_GROUP: int = Field(
        ...,
        alias="IN_ROUTE_GROUP",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_ROUTE: int = Field(
        ...,
        alias="IN_ROUTE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_TICKET_INFO_ID: int = Field(
        ...,
        alias="IN_TICKET_INFO_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PNR: Optional[str] = Field(
        None,
        alias="PNR",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""PFTQV9""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKETING_DEADLINE: datetime = Field(
        ...,
        alias="TICKETING_DEADLINE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""2010-10-10 17:14:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKETED: str = Field(
        ...,
        alias="TICKETED",
        name="",
        description="""Specifies whether the tickets have been issued for flight booking item Ticketed - 1, Not ticketed - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKET_ISSUE_DATE: Optional[datetime] = Field(
        None,
        alias="TICKET_ISSUE_DATE",
        name="",
        description="""The date which the tickets have been issued for flight booking item""",
        example="""1989-11-29 08:36:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_OFFSET: float = Field(
        ...,
        alias="COST_OFFSET",
        name="",
        description="""Offset of the cost if the cost is changed manually.""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OFFSET: float = Field(
        ...,
        alias="TAX_OFFSET",
        name="",
        description="""Offset of the tax if the tax is changed manually.""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRLINE_FOR_COMM_CALC: Optional[str] = Field(
        None,
        alias="AIRLINE_FOR_COMM_CALC",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""AS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOMESTIC_FOR_COMM_CALC: Optional[str] = Field(
        None,
        alias="DOMESTIC_FOR_COMM_CALC",
        name="",
        description="""A flag to indicate whether to consider the flight booking as domestic or not for commission calculations._x000D_
Flight booking is considered domestic if all the flight sectors are domestic (departure airport country and destination airport country are same as company country).""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HISTORY_CREATED: str = Field(
        ...,
        alias="HISTORY_CREATED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OUT_CABIN: Optional[str] = Field(
        None,
        alias="OUT_CABIN",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""ECONOMY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IN_CABIN: Optional[str] = Field(
        None,
        alias="IN_CABIN",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""ECONOMY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKET_TYPE: Optional[str] = Field(
        None,
        alias="TICKET_TYPE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""oGvWjjjnnKOkTIimvVUp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CRS: Optional[str] = Field(
        None,
        alias="CRS",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""AMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FARE_DIFF_WITH_BASIC_FLIGHT: int = Field(
        ...,
        alias="FARE_DIFF_WITH_BASIC_FLIGHT",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_CHARGE: int = Field(
        ...,
        alias="EXT_CHARGE",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLASS_UPGRADE_CHARGE: int = Field(
        ...,
        alias="CLASS_UPGRADE_CHARGE",
        name="",
        description="""Charge associated with cabin class upgrade""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLEMENT_CHARGE: int = Field(
        ...,
        alias="SUPPLEMENT_CHARGE",
        name="",
        description="""The charge associated with the supplements that have been added to booking""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON_CHARGE: int = Field(
        ...,
        alias="ADDON_CHARGE",
        name="",
        description="""Addon charge for domestic flights""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FARE_CREATED_OFFICE_ID: Optional[str] = Field(
        None,
        alias="FARE_CREATED_OFFICE_ID",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""SNADL3100""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOUR_CODE: Optional[str] = Field(
        None,
        alias="TOUR_CODE",
        name="",
        description="""Tour itinerary identification data of the selected 'Tour Code' parameter in discount scheme setup.Format will be <Contract_Id>:<Tour Itinerary Number>""",
        example="""gMPFpbbArUwGQooNyZxm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENDORSEMENT: Optional[str] = Field(
        None,
        alias="ENDORSEMENT",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""sKDKEQbuQOiWqnRTGhsk""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IATA_COMM_PERSC: Optional[float] = Field(
        None,
        alias="IATA_COMM_PERSC",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_FLIGHT_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:32.382754""",
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
        example="""RES_FLIGHT_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=81350959656419,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResFlightBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_FLIGHT_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Flight Booking"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains all the Booking Item level information specif for flight bookings."""  # optional
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
        key_path_value = "RES_FLIGHT_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
