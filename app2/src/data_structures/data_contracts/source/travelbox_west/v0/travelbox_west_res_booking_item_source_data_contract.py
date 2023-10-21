"""Source Data Contract Template for RES_BOOKING_ITEM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM Data
    """

    PRINT_OPTION: Optional[str] = Field(
        None,
        alias="PRINT_OPTION",
        name="",
        description="""NaN""",
        example="""rTZmKDcgTMqayHhhgMTM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GUARANTEED_STATUS: Optional[str] = Field(
        None,
        alias="GUARANTEED_STATUS",
        name="",
        description="""NaN""",
        example="""ViKcZdRIYwWsCNdxKukj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSR: Optional[str] = Field(
        None,
        alias="RSR",
        name="",
        description="""NaN""",
        example="""OdxaewhDIVBJswFUiOYE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRESS_CHECKOUT: Optional[str] = Field(
        None,
        alias="EXPRESS_CHECKOUT",
        name="",
        description="""NaN""",
        example="""kusWRdGfQqVJNLXploCF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VIP_LEVEL: Optional[str] = Field(
        None,
        alias="VIP_LEVEL",
        name="",
        description="""NaN""",
        example="""PuisMBVRCCFIGHYaItVf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT_TYPE: Optional[str] = Field(
        None,
        alias="TAX_EXEMPT_TYPE",
        name="",
        description="""NaN""",
        example="""xzicalzZKFlLRgWmquUl""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BKG_ACCESS_SECURITY: Optional[str] = Field(
        None,
        alias="BKG_ACCESS_SECURITY",
        name="",
        description="""NaN""",
        example="""fAhljYtaSgnsbyEwgCHu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MARKET_SEGMENT_CODE: Optional[str] = Field(
        None,
        alias="MARKET_SEGMENT_CODE",
        name="",
        description="""NaN""",
        example="""qCMZtpRhGSNUZFiUNFHc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_MASTER_ID: Optional[int] = Field(
        None,
        alias="GROUP_MASTER_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_NAME: Optional[str] = Field(
        None,
        alias="CONTACT_NAME",
        name="",
        description="""NaN""",
        example="""dmjHXFrvcgVqZelATPAO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_BOOKING_SUB_STATUS: Optional[int] = Field(
        None,
        alias="RES_BOOKING_SUB_STATUS",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_SRC_BOOKING_ID: Optional[int] = Field(
        None,
        alias="EXTENDED_SRC_BOOKING_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_SRC_PRODUCT_CODE: Optional[str] = Field(
        None,
        alias="EXTENDED_SRC_PRODUCT_CODE",
        name="",
        description="""NaN""",
        example="""QanmBnPbqtZIDDVjPcqz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_SRC_ITEM_NO: Optional[int] = Field(
        None,
        alias="EXTENDED_SRC_ITEM_NO",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GUARANTEED_CARD_IDENTIFIER: Optional[str] = Field(
        None,
        alias="GUARANTEED_CARD_IDENTIFIER",
        name="",
        description="""NaN""",
        example="""aQMauwmqqMtBGDVeIBLG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    QUOTE_BEFORE_CONV: Optional[str] = Field(
        None,
        alias="QUOTE_BEFORE_CONV",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GEN_BOOKING_REF_ID: Optional[int] = Field(
        None,
        alias="GEN_BOOKING_REF_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ELEMENT_NAME: Optional[str] = Field(
        None,
        alias="PKG_ELEMENT_NAME",
        name="",
        description="""Pre package element name""",
        example="""2022_EXA_SGL_DOP_LL_RISE_V1 - EXADL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSOCIATE_PRODUCT_CODE: Optional[str] = Field(
        None,
        alias="ASSOCIATE_PRODUCT_CODE",
        name="",
        description="""This property is used for store the canceled Item product code information in OTA Amendment flow.""",
        example="""tEsrMmOuChIaiNcvCTag""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSOCIATE_ITEM_NO: int = Field(
        ...,
        alias="ASSOCIATE_ITEM_NO",
        name="",
        description="""This property is used for store the canceled Item item no information in OTA Amendment flow.""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSOCIATE_SESSION_ID: Optional[str] = Field(
        None,
        alias="ASSOCIATE_SESSION_ID",
        name="",
        description="""NaN""",
        example="""JpzllAjWMcHUhEpbuhSP""",
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

    ITEM_BKG_SOURCE: Optional[str] = Field(
        None,
        alias="ITEM_BKG_SOURCE",
        name="",
        description="""NaN""",
        example="""I""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BREAKAGE: float = Field(
        ...,
        alias="BREAKAGE",
        name="",
        description="""Supplier breakage amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_CODE: Optional[str] = Field(
        None,
        alias="GROUP_CODE",
        name="",
        description="""Deprecated""",
        example="""jENRAXobdXznaxyEUoHi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_TYPE: Optional[str] = Field(
        None,
        alias="GROUP_TYPE",
        name="",
        description="""NaN""",
        example="""dcHoelsQLNyUltbVoHYa""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_STATUS: Optional[str] = Field(
        None,
        alias="FULFILLMENT_STATUS",
        name="",
        description="""NaN""",
        example="""KnRVwhVmeqFLEJTaBbkV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONFIDENTIAL_RATE: Optional[str] = Field(
        None,
        alias="CONFIDENTIAL_RATE",
        name="",
        description="""NaN""",
        example="""mLBqQGxvWqkOYlmhwTks""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=1004082694,
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
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_STATUS: int = Field(
        ...,
        alias="BOOKING_STATUS",
        name="",
        description="""Not in the disney scope""",
        example=1000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=22538,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: int = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=32261,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FROM_DATE: datetime = Field(
        ...,
        alias="FROM_DATE",
        name="",
        description="""The start date of the date range for which the allocations are defined for""",
        example="""2023-05-14 18:02:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TO_DATE: datetime = Field(
        ...,
        alias="TO_DATE",
        name="",
        description="""The end date of the date range for which the allocations are defined for""",
        example="""2006-11-14 05:11:09""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT: int = Field(
        ...,
        alias="ADULT",
        name="",
        description="""Number of  Adult passengers of the sharing rule""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD: int = Field(
        ...,
        alias="CHILD",
        name="",
        description="""Number of  Child passengers of the sharing rule""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT: int = Field(
        ...,
        alias="INFANT",
        name="",
        description="""Number of  Infant passengers of the sharing rule""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE: float = Field(
        ...,
        alias="PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST: float = Field(
        ...,
        alias="COST",
        name="",
        description="""Debit credit note cost amount_x000D_
- If credit negative value_x000D_
- If debit positive value""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_IN_CONTRACT: float = Field(
        ...,
        alias="COST_IN_CONTRACT",
        name="",
        description="""Cost of the booking item in contract currency""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY_IN_CONTRACT: str = Field(
        ...,
        alias="CURRENCY_IN_CONTRACT",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_DATE: datetime = Field(
        ...,
        alias="BOOKED_DATE",
        name="",
        description="""Credit debit note related booking created date""",
        example="""2019-12-01 01:22:00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_PAYMENT_STATUS: int = Field(
        ...,
        alias="SUPPLIER_PAYMENT_STATUS",
        name="",
        description="""SUPPLIER_PAYMENT_STATUS_UNPAID = 10_x000D_
SUPPLIER_PAYMENT_STATUS_PARTIALLY_PAID = 20_x000D_
SUPPLIER_PAYMENT_STATUS_DEPOSIT_PAID = 30_x000D_
SUPPLIER_PAYMENT_STATUS_FULLYPAID = 40_x000D_
SUPPLIER_PAYMENT_STATUS_SETTLED = 50""",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_PAYMENT_DATE: Optional[datetime] = Field(
        None,
        alias="PRE_PAYMENT_DATE",
        name="",
        description="""The date which supplier pre payment is due""",
        example="""1972-09-06 21:17:03""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_PAYMENT: float = Field(
        ...,
        alias="PRE_PAYMENT",
        name="",
        description="""booking item pre payment""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_PAYMENT_DATE: Optional[datetime] = Field(
        None,
        alias="POST_PAYMENT_DATE",
        name="",
        description="""The date which supplier post payment is due""",
        example="""1977-11-17 18:40:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_PAYMENT: float = Field(
        ...,
        alias="POST_PAYMENT",
        name="",
        description="""post payment for perticular booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHERS_SENT: str = Field(
        ...,
        alias="VOUCHERS_SENT",
        name="",
        description="""For generic booking items (e.g. disney park tickets), this flag indicates whether the voucher has been dispached or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_AS_AGENT: str = Field(
        ...,
        alias="BOOKED_AS_AGENT",
        name="",
        description="""A flag to indicate whether the booking item is booked as agent or not._x000D_
Reservation manager > Booking Item Summery > Other Information > Booked as Agent""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOREIGN_BOOKING_ID: Optional[str] = Field(
        None,
        alias="FOREIGN_BOOKING_ID",
        name="",
        description="""Foreign booking id of the booking to which the credit debit note is issued""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOREIGN_CRS: str = Field(
        ...,
        alias="FOREIGN_CRS",
        name="",
        description="""H2H system Id. This is a foreign key reference from the table H2H_SYSTEM.""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_ADDED: str = Field(
        ...,
        alias="MANUALLY_ADDED",
        name="",
        description="""Flag to check whether manually added or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_MARKUP: float = Field(
        ...,
        alias="AGENT_MARKUP",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFORM_SUPPLIER: str = Field(
        ...,
        alias="INFORM_SUPPLIER",
        name="",
        description="""INFORM SUPPLIER""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONVERTED: str = Field(
        ...,
        alias="CONVERTED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONVERTED_MESSAGE: str = Field(
        ...,
        alias="CONVERTED_MESSAGE",
        name="",
        description="""Deprecated""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_PRICE: float = Field(
        ...,
        alias="TOTAL_PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_COST: float = Field(
        ...,
        alias="TOTAL_COST",
        name="",
        description="""The total cost of the booking""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE_FOR_QUOTE: str = Field(
        ...,
        alias="ACTIVE_FOR_QUOTE",
        name="",
        description="""Flag to indicate if the booking item is active for quoting_x000D_
1 - active_x000D_
0 - not active""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_IN_CONTRACT_ADJUSTMENT: float = Field(
        ...,
        alias="COST_IN_CONTRACT_ADJUSTMENT",
        name="",
        description="""Adjustment for cost in contract""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_TO_SELLING_EXC_RATE: float = Field(
        ...,
        alias="CONTRACT_TO_SELLING_EXC_RATE",
        name="",
        description="""The ratio of contract currency to the selling currency""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROVISIONAL: str = Field(
        ...,
        alias="PROVISIONAL",
        name="",
        description="""A flag to indicate whether the booking item is provinsional or not. This is defined by the contract state and stage.""",
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
        example="""1999-04-11 20:30:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    QUOTE_PRICE_EXPIRY_DATE: Optional[datetime] = Field(
        None,
        alias="QUOTE_PRICE_EXPIRY_DATE",
        name="",
        description="""For quotes. the quote price expiry date of the booking item.""",
        example="""2016-12-22 13:10:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGREED_COST_IN_CONTRACT: float = Field(
        ...,
        alias="AGREED_COST_IN_CONTRACT",
        name="",
        description="""Agreed cost in contract.""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANIFESTED: Optional[str] = Field(
        None,
        alias="MANIFESTED",
        name="",
        description="""NaN""",
        example="""ymhkJslDBtzANjQXaQeP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_TYPE: Optional[str] = Field(
        None,
        alias="RATE_TYPE",
        name="",
        description="""NM = NETT AND MARKUP, GC = GROSS AND COMMISSION, NG = GROSS OEM_sqlplus_input_finished, GO = GROSS ONLY""",
        example="""GO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_BOOKING_ID: Optional[int] = Field(
        None,
        alias="PACKAGE_BOOKING_ID",
        name="",
        description="""Deprecated""",
        example=9862,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_NO: Optional[int] = Field(
        None,
        alias="PACKAGE_NO",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_RES_REF: Optional[str] = Field(
        None,
        alias="SUPPLIER_RES_REF",
        name="",
        description="""SUPPLIER RESERVATION REFERENCE. THIS IS SEND THEN THE ITEM IS CONFIRMED""",
        example="""OcpMYRYfvNRlDjllzDob""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MARKUP_REF: Optional[str] = Field(
        None,
        alias="MARKUP_REF",
        name="",
        description="""The TravelBox reference of the applied markup for the room""",
        example="""ZbzJMGIJTfGIsFihJXFi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_ORDER: Optional[int] = Field(
        None,
        alias="ITINERARY_ORDER",
        name="",
        description="""position in the itinerary order of all items within the booking. By Clicking on Reservation Client 'Itinerary' node will show the itinerary in this order. User can change the order (position) manually. This is -1 for Transfer items""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BRAND: str = Field(
        ...,
        alias="BRAND",
        name="",
        description="""The TravelBox code of the brand for which the limit is defined for""",
        example="""CORE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FROM_PACKAGE: str = Field(
        ...,
        alias="FROM_PACKAGE",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_STATE: int = Field(
        ...,
        alias="COST_STATE",
        name="",
        description="""Deprecated""",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ELEMENT_NO: Optional[int] = Field(
        None,
        alias="PKG_ELEMENT_NO",
        name="",
        description="""Deprecated""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ALT_NO: Optional[int] = Field(
        None,
        alias="PKG_ALT_NO",
        name="",
        description="""Deprecated""",
        example=5048,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_UPG_NO: Optional[int] = Field(
        None,
        alias="PKG_UPG_NO",
        name="",
        description="""Deprecated""",
        example=2125,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION: float = Field(
        ...,
        alias="COMMISSION",
        name="",
        description="""The commission percentage recieved by the tour operator""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION_PERCENTAGE: float = Field(
        ...,
        alias="COMMISSION_PERCENTAGE",
        name="",
        description="""The percentage of the commission""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_COMM: str = Field(
        ...,
        alias="MANUAL_COMM",
        name="",
        description="""A flag to indicate whether the commission is calculated manually. if true, commission calculation is skipped.""",
        example="""0""",
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

    COUNTRY_CODE: Optional[str] = Field(
        None,
        alias="COUNTRY_CODE",
        name="",
        description="""Travelox code of the country, currently cannot insert from TBX UI, have to insert to database directly""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE_CODE: Optional[str] = Field(
        None,
        alias="STATE_CODE",
        name="",
        description="""The code of the state where the booking item is.""",
        example="""UwWKPuGrDruimphHxbMf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGREED_COST_LOCK: Optional[str] = Field(
        None,
        alias="AGREED_COST_LOCK",
        name="",
        description="""Deprecated""",
        example="""ZOAuCQmugxJeAsbPmxIh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_DESC: Optional[str] = Field(
        None,
        alias="ITEM_DESC",
        name="",
        description="""Description of the booking item_x000D_
If the booking is no flights then main airline name will appear here_x000D_
If it is a hotel then supplier name will appear here._x000D_
If it is a tour or transfer then tour/transfer name will appear here._x000D_
If it is a car booking the car name will appear here""",
        example="""Disneyland-EXA Ride Admission(Star Wars:  Rise of the Resistance)""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_TAX_PRICE: float = Field(
        ...,
        alias="TOTAL_TAX_PRICE",
        name="",
        description="""Total tax price applied for the booking""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_TAX_COST: float = Field(
        ...,
        alias="TOTAL_TAX_COST",
        name="",
        description="""Total tax cost applied for the booking""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_COST_IN_CONTRACT: float = Field(
        ...,
        alias="TOTAL_COST_IN_CONTRACT",
        name="",
        description="""Total cost of the booking item in contract currency""",
        example=50.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OVERIDDEN_COMM_RATE: Optional[float] = Field(
        None,
        alias="OVERIDDEN_COMM_RATE",
        name="",
        description="""Overridden commission rate._x000D_
If positive value is present ( and it is greater than the commission rate ),_x000D_
overridden commission rate would be used to calculate commission instead of the commision rate.""",
        example=46752.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_OVERRIDE: Optional[float] = Field(
        None,
        alias="MANUAL_OVERRIDE",
        name="",
        description="""Deprecated""",
        example=76783.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_ADULT: float = Field(
        ...,
        alias="GROSS_ADULT",
        name="",
        description="""The total adult price of this discount in selling currency""",
        example=50.0,
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

    BOOKED_USER: Optional[int] = Field(
        None,
        alias="BOOKED_USER",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=15418,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_INCLUDED: str = Field(
        ...,
        alias="TAX_INCLUDED",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ITEM_ORDER: Optional[int] = Field(
        None,
        alias="PKG_ITEM_ORDER",
        name="",
        description="""If the booking item belongs to a package, the order number of the booking item within the package.""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    START_TIME: Optional[datetime] = Field(
        None,
        alias="START_TIME",
        name="",
        description="""Start timestamp of the booking item""",
        example="""1988-06-24 12:12:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    END_TIME: Optional[datetime] = Field(
        None,
        alias="END_TIME",
        name="",
        description="""End timestamp of the booking item""",
        example="""1977-11-12 06:22:44""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_TO_BASE_EX_RATE: float = Field(
        ...,
        alias="CONTRACT_TO_BASE_EX_RATE",
        name="",
        description="""Contract currency to base currency exchange rate""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_ADULT: float = Field(
        ...,
        alias="NETT_ADULT",
        name="",
        description="""The total adult cost of this discount in selling currency""",
        example=50.0,
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

    CITY_CODE: Optional[str] = Field(
        None,
        alias="CITY_CODE",
        name="",
        description="""The Travelox code of the city, currently cannot insert from TBX UI, have to insert data to database directly""",
        example="""paDSjqIMjxCqWTGPwHoC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_MANUAL_OVERRIDE: Optional[float] = Field(
        None,
        alias="ADT_MANUAL_OVERRIDE",
        name="",
        description="""The amount added to adult price as manual override. This is done in hotel detail result panel""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_MANUAL_OVERRIDE: Optional[float] = Field(
        None,
        alias="CHD_MANUAL_OVERRIDE",
        name="",
        description="""The amount added to child price as manual override. Manually overriding the child price is done in hotel detail result panel""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_MANUAL_OVERRIDE: Optional[float] = Field(
        None,
        alias="INF_MANUAL_OVERRIDE",
        name="",
        description="""The amount added to the infant price as manual override. Manually overriding the infant price is done in hotel detail result panel""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGREED_C_I_C_TAXABLE: str = Field(
        ...,
        alias="AGREED_C_I_C_TAXABLE",
        name="",
        description="""A flag to indicate whether the agreed cost in contract is taxable or not.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CACHE_PRICE_ADJUSTMENT: Optional[float] = Field(
        None,
        alias="CACHE_PRICE_ADJUSTMENT",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOREIGN_REFERENCES: Optional[str] = Field(
        None,
        alias="FOREIGN_REFERENCES",
        name="",
        description="""A search token returned from Peguses H2H system. [Not In Disney Scope]""",
        example="""rRtGHLbFJOyJQLPEYqhD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_COMMISSION: float = Field(
        ...,
        alias="SUPPLIER_COMMISSION",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOLIDAY_TEMPLATE_ID: Optional[int] = Field(
        None,
        alias="HOLIDAY_TEMPLATE_ID",
        name="",
        description="""If the booking item is booked through wide search, the ide search template id.""",
        example=3456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPOSITION_ID: Optional[int] = Field(
        None,
        alias="COMPOSITION_ID",
        name="",
        description="""This is the wide search holiday composition id - used only for wide search""",
        example=63003,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PARENT_ITEM_NO: Optional[int] = Field(
        None,
        alias="PARENT_ITEM_NO",
        name="",
        description="""Keep parent item no when spliting an item when amending""",
        example=4302,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NON_COMMISSIONABLE_PRICE: float = Field(
        ...,
        alias="NON_COMMISSIONABLE_PRICE",
        name="",
        description="""Non commissionable price component of the booking.""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_VERSION: Optional[int] = Field(
        None,
        alias="CONTRACT_VERSION",
        name="",
        description="""The version of the contract which has used to do this booking""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORG_PACKAGE_NO: Optional[int] = Field(
        None,
        alias="ORG_PACKAGE_NO",
        name="",
        description="""Stores the original package number the booking item is belong to._x000D_
Initialized to PACKAGE_NO by triggers when inserting and will not alter later.""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_ITEM_NO: Optional[int] = Field(
        None,
        alias="ITINERARY_ITEM_NO",
        name="",
        description="""The system generated  number of the package itinerary item""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VCC_CARD_ID: Optional[str] = Field(
        None,
        alias="VCC_CARD_ID",
        name="",
        description="""Virtual Credit card ID (Used for H2H supplier payments) - Not in Disney Scope""",
        example="""vxMFXFaIUYCUGXwUhbOD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SCHEME_ID: Optional[int] = Field(
        None,
        alias="PAY_SCHEME_ID",
        name="",
        description="""Primary key of the table""",
        example=2776,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SCHEME_TYPE: Optional[str] = Field(
        None,
        alias="PAY_SCHEME_TYPE",
        name="",
        description="""Deprecated""",
        example="""crfwvvEoHkkLeFjEjaUW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_ID: Optional[str] = Field(
        None,
        alias="GROUP_ID",
        name="",
        description="""System generated group id""",
        example="""FSZixKDlFfSPwsHzBkeo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_ITEM: Optional[str] = Field(
        None,
        alias="MANUAL_ITEM",
        name="",
        description="""A flag to indicate that the booking item is a manual item. The product code for manual items are MAN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_TAX_ON_COMMISION: Optional[float] = Field(
        None,
        alias="SUPPLIER_TAX_ON_COMMISION",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INTERNAL_RQ: Optional[str] = Field(
        None,
        alias="INTERNAL_RQ",
        name="",
        description="""This is a flag representing whether allocation limit is 'Rq' or not. If the limit is marked as 'Rq', at the time of search, room type will be shown as On-Request(Internal). Such bookings will appear on 'Internal Onrequest' queue. A user can confirm the booking using this queue. At the time of confirming, user does not have to call the supplier to get an extra allocation. Instead, system will allow confimation if there are allocation in the main pool. Once confirmed, the available allocations in the main pool will be reduced.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_ATOL_RECEIPT: Optional[str] = Field(
        None,
        alias="ISSUE_ATOL_RECEIPT",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    H2H_PRICE_DIFF: Optional[float] = Field(
        None,
        alias="H2H_PRICE_DIFF",
        name="",
        description="""Price difference between purchase cost from H2H and Cost in contract in TBX""",
        example=29096.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAX_WISE: Optional[str] = Field(
        None,
        alias="PAX_WISE",
        name="",
        description="""A flag indicating the discount fares are defined passenger wise ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OLD_SUPPLIER_RES_REF: Optional[str] = Field(
        None,
        alias="OLD_SUPPLIER_RES_REF",
        name="",
        description="""When 'SUPPLIER_RES_REF' is changed, old value is stored here.""",
        example="""WIvLSeAcSkElxhWjGkVO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SWAP_ITINERARY_ITEM_NO: Optional[int] = Field(
        None,
        alias="SWAP_ITINERARY_ITEM_NO",
        name="",
        description="""For package items, if the booking item is swapped, this field contains the swapped itinerary item number._x000D_
If it is not swapped (booked as it is), -1 is saved.""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPTIONAL_PKG_ITEM: Optional[str] = Field(
        None,
        alias="OPTIONAL_PKG_ITEM",
        name="",
        description="""A flag to indicate whether the booked item is an optional package item or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="ADT_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for adults of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="CHD_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for children of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="INF_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for infants of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_COM_PKG_ITEM: str = Field(
        ...,
        alias="MANUALLY_COM_PKG_ITEM",
        name="",
        description="""A flag to indicate whether the item is added to a package manually or not.""",
        example="""0""",
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

    NON_AMENDABLE: Optional[str] = Field(
        None,
        alias="NON_AMENDABLE",
        name="",
        description="""A flag to indicate whether the item is amenable or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ON_SAVE: str = Field(
        ...,
        alias="ON_SAVE",
        name="",
        description="""This specifies whether applicable force componets are notified to user 'On Save' or not.(Possible values are 1 and 0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_TRACKABLE: Optional[str] = Field(
        None,
        alias="ITEM_TRACKABLE",
        name="",
        description="""A flag to indicate whether the booking item is trackable or not. if true voucher status can be changeable.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_STATUS: Optional[str] = Field(
        None,
        alias="VOUCHER_STATUS",
        name="",
        description="""Voucher status of the Booking Item. Possible values OUTSTANDING, RETURNED, REDEEMED""",
        example="""gYdqZiCxnoTFIJpnXHjw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:50.902449""",
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
        example="""RES_BOOKING_ITEM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=45695481906953,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResBookingItemModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_ITEM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Item"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains all the basic information of Booking Product Items common to all product types."""  # optional
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
        key_path_value = "RES_BOOKING_ITEM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
