"""Source Data Contract Template for RES_BOOKING_PACKAGE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_PACKAGE Data
    """

    PRICE_DIFF: float = Field(
        ...,
        alias="PRICE_DIFF",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_DIFF: float = Field(
        ...,
        alias="TAX_DIFF",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_DEST_BOOKING_ID: Optional[int] = Field(
        None,
        alias="EXTENDED_DEST_BOOKING_ID",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_DEST_PACKAGE_NO: Optional[int] = Field(
        None,
        alias="EXTENDED_DEST_PACKAGE_NO",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_ITINERARY_CODE: Optional[str] = Field(
        None,
        alias="CMS_ITINERARY_CODE",
        name="",
        description="""NaN""",
        example="""NqcuLQIiYQVjlaOvbyiO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_GRID_CODE: Optional[str] = Field(
        None,
        alias="CMS_GRID_CODE",
        name="",
        description="""NaN""",
        example="""aFwiXMQfGVlMSgaEMaFV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROUND_ERR_ON_TOT_PRICE: Optional[float] = Field(
        None,
        alias="ROUND_ERR_ON_TOT_PRICE",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESERVATION_ID: Optional[int] = Field(
        None,
        alias="RESERVATION_ID",
        name="",
        description="""The system generated id of the reservation""",
        example=8811,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUB_TYPE: Optional[str] = Field(
        None,
        alias="SUB_TYPE",
        name="",
        description="""1 = TYPE1 (GET % OR AMOUNT IN DISCOUNT BEFORE SPECIFIC BOOKING DATE),_x000D_
2 = TYPE2 (NON CALCULATED DESCRIPTION)_x000D_
3 = TYPE3 ((GET % OR AMOUNT IN DISCOUNT  BASED ON BOOKING TO DEPARTURE DURATION)""",
        example="""DEtQEvTDlaJHKTOnVCKa""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSOCIATE_PKG_NO: int = Field(
        ...,
        alias="ASSOCIATE_PKG_NO",
        name="",
        description="""This property is used for store the canceled package item no information in OTA Amendment flow.""",
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
        example="""294912b2-5dc6-4c36-9013-05341fb41fea""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1991-03-10 15:13:06""",
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

    NIGHTLY_PRICES: Optional[str] = Field(
        None,
        alias="NIGHTLY_PRICES",
        name="",
        description="""NaN""",
        example="""OxHTDJorMIlTFzkcXeTb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BYPASS_AVAILABILITY: str = Field(
        ...,
        alias="BYPASS_AVAILABILITY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEND_TO_PROPERTY: Optional[str] = Field(
        None,
        alias="SEND_TO_PROPERTY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEND_TO_PROPERTY_STATUS: Optional[str] = Field(
        None,
        alias="SEND_TO_PROPERTY_STATUS",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_DURATION: Optional[int] = Field(
        None,
        alias="TOTAL_DURATION",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LINK_PKG_REFERENCE: Optional[str] = Field(
        None,
        alias="LINK_PKG_REFERENCE",
        name="",
        description="""NaN""",
        example="""QtsPzncfGHavBGDgAxue""",
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

    BASELINE_PRICED: Optional[str] = Field(
        None,
        alias="BASELINE_PRICED",
        name="",
        description="""NaN""",
        example="""1""",
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
        example="""wlhoaPxgdKweYARxcwRt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENDED_SRC_PACKAGE_NO: Optional[int] = Field(
        None,
        alias="EXTENDED_SRC_PACKAGE_NO",
        name="",
        description="""NaN""",
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
        example=1003825368,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_NO: int = Field(
        ...,
        alias="PACKAGE_NO",
        name="",
        description="""Oracle managed system tables used for materialised views""",
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
        example="""PBP""",
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

    ADULT_COST: float = Field(
        ...,
        alias="ADULT_COST",
        name="",
        description="""Reserved for future implementations""",
        example=30.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_COST: float = Field(
        ...,
        alias="CHILD_COST",
        name="",
        description="""Per Child cost for a particuler Other Cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_COST: float = Field(
        ...,
        alias="INFANT_COST",
        name="",
        description="""Infant cost for a particuler Other Cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_PRICE: float = Field(
        ...,
        alias="ADULT_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=30.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_PRICE: float = Field(
        ...,
        alias="CHILD_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_PRICE: float = Field(
        ...,
        alias="INFANT_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_COST: float = Field(
        ...,
        alias="TOTAL_COST",
        name="",
        description="""The total cost of the booking""",
        example=30.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_PRICE: float = Field(
        ...,
        alias="TOTAL_PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=30.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_DESCRIPTION: str = Field(
        ...,
        alias="PACKAGE_DESCRIPTION",
        name="",
        description="""The description of the package""",
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

    PRICE_OVERRIDDEN: str = Field(
        ...,
        alias="PRICE_OVERRIDDEN",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_DATE: datetime = Field(
        ...,
        alias="DEPARTURE_DATE",
        name="",
        description="""Departure date for bookings""",
        example="""1978-02-01 22:18:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OVERALL_MARGIN: float = Field(
        ...,
        alias="OVERALL_MARGIN",
        name="",
        description="""NaN""",
        example=-1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_ID: Optional[int] = Field(
        None,
        alias="PACKAGE_ID",
        name="",
        description="""The foreign key which refers the field PACKAGE_ID of the table PKG_HOLIDAY""",
        example=98607,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_NO: Optional[int] = Field(
        None,
        alias="ITINERARY_NO",
        name="",
        description="""The foreign key which refers the field ITINERARY_NO of the table PKG_ITINERARY""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_GROUP: Optional[str] = Field(
        None,
        alias="PRODUCT_GROUP",
        name="",
        description="""Other Cost applicable Product Group Code""",
        example="""EXA_SINGLE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_TYPE: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPE",
        name="",
        description="""Other Cost applicable Product Type Code""",
        example="""12811""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOLIDAY_TYPE: Optional[str] = Field(
        None,
        alias="HOLIDAY_TYPE",
        name="",
        description="""The TravelBox code of the holiday type for which the limit is defined for""",
        example="""EXA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_CODE: str = Field(
        ...,
        alias="PACKAGE_CODE",
        name="",
        description="""If this is a pre-built package reservation, this field holds the TravelBox code of the relevant package. If this is a component reservation, this is null.pre-built """,
        example="""2022_EXA_SGL_DOP_LL_RACE_V1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_NAME: Optional[str] = Field(
        None,
        alias="PACKAGE_NAME",
        name="",
        description="""The TravelBox name of the package""",
        example="""2022 EXA Lightning Lane - Radiator Springs Racers""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NIGHTS: Optional[int] = Field(
        None,
        alias="NIGHTS",
        name="",
        description="""This is 1 since the rates are for a day.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STOP_SALE: str = Field(
        ...,
        alias="STOP_SALE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STOP_SALE_REASON: Optional[str] = Field(
        None,
        alias="STOP_SALE_REASON",
        name="",
        description="""NaN""",
        example="""vYXkbOHaorfUMcMmvJSM""",
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

    BASE_PACKAGE_NO: Optional[int] = Field(
        None,
        alias="BASE_PACKAGE_NO",
        name="",
        description="""Deprecated""",
        example=1060,
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

    MARKUP_INDIVIDUALLY: str = Field(
        ...,
        alias="MARKUP_INDIVIDUALLY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT: float = Field(
        ...,
        alias="DISCOUNT",
        name="",
        description="""Invoice line Discount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_OCC_SCHEME_KEY: Optional[str] = Field(
        None,
        alias="PKG_OCC_SCHEME_KEY",
        name="",
        description="""NaN""",
        example="""200x1 """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKED_DATE: Optional[datetime] = Field(
        None,
        alias="BOOKED_DATE",
        name="",
        description="""Credit debit note related booking created date""",
        example="""1981-11-01 20:50:55""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_PRICE_ADJUSTMENT: Optional[float] = Field(
        None,
        alias="ADULT_PRICE_ADJUSTMENT",
        name="",
        description="""Price mention in manual addition for adult  in package components dialog""",
        example=3133.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_PRICE_ADJUSTMENT: Optional[float] = Field(
        None,
        alias="CHILD_PRICE_ADJUSTMENT",
        name="",
        description="""Price mention in manual addition for child in package components dialog""",
        example=41180.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_PRICE_ADJUSTMENT: Optional[float] = Field(
        None,
        alias="INFANT_PRICE_ADJUSTMENT",
        name="",
        description="""Price mention in manual addition for infant in package components dialog""",
        example=62946.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CF_SCORE: Optional[float] = Field(
        None,
        alias="CF_SCORE",
        name="",
        description="""NaN""",
        example=-1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WS_SESSION_ID: Optional[str] = Field(
        None,
        alias="WS_SESSION_ID",
        name="",
        description="""NaN""",
        example="""UwzxyGorWlMSPXtozdhh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_PKG_MARKUP: float = Field(
        ...,
        alias="ADULT_PKG_MARKUP",
        name="",
        description="""applying package level Markup for the children for pre built package itinerary""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_PKG_MARKUP: float = Field(
        ...,
        alias="CHILD_PKG_MARKUP",
        name="",
        description="""applying package level Markup for the children for pre built package itinerary""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_PKG_MARKUP: float = Field(
        ...,
        alias="INFANT_PKG_MARKUP",
        name="",
        description="""applying package level Markup for the children for pre built package itinerary""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_PKG_DISCOUNT: float = Field(
        ...,
        alias="ADULT_PKG_DISCOUNT",
        name="",
        description="""Total adult amount of package discounts""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_PKG_DISCOUNT: float = Field(
        ...,
        alias="CHILD_PKG_DISCOUNT",
        name="",
        description="""Total child amount of package discounts""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_PKG_DISCOUNT: float = Field(
        ...,
        alias="INFANT_PKG_DISCOUNT",
        name="",
        description="""Total infant amount of package discounts""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_SCHEME_ID: Optional[int] = Field(
        None,
        alias="DISCOUNT_SCHEME_ID",
        name="",
        description="""NaN""",
        example=5760,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALCULATION_TYPE: Optional[str] = Field(
        None,
        alias="CALCULATION_TYPE",
        name="",
        description="""Calculation type. 1 - Daily and Weekly,2 - Daily Rate by duration, 3 - Extra day for long durations""",
        example="""GP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_DISCOUNT: Optional[float] = Field(
        None,
        alias="PKG_DISCOUNT",
        name="",
        description="""Total amount of package discounts applied to the package booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE_GRID_CODE: Optional[str] = Field(
        None,
        alias="PRICE_GRID_CODE",
        name="",
        description="""This is the Package promotional price grid code. This is shown under package summary in Reservation Manager as Promotion Ref""",
        example="""gujQOOdiTcDuTjUMhvRF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION_RATE: Optional[float] = Field(
        None,
        alias="COMMISSION_RATE",
        name="",
        description="""Overriding commission rate""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION_OVERRIDE: Optional[str] = Field(
        None,
        alias="COMMISSION_OVERRIDE",
        name="",
        description="""Specifies whether the commission rate is overriden for supplement""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPEALING: Optional[str] = Field(
        None,
        alias="APPEALING",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    THRESHOLD: Optional[str] = Field(
        None,
        alias="THRESHOLD",
        name="",
        description="""Deprecated""",
        example="""mliSKRozDTjXQkucCrxu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROMOTION: str = Field(
        ...,
        alias="PROMOTION",
        name="",
        description="""The selected promotion of the package""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REMOVED_ITEM_ITIN_NUMS: Optional[str] = Field(
        None,
        alias="REMOVED_ITEM_ITIN_NUMS",
        name="",
        description="""NaN""",
        example="""UnPVwNTFaBMcXaNqqWUn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_NAME: Optional[str] = Field(
        None,
        alias="ITINERARY_NAME",
        name="",
        description="""The name of the itinerary of the package""",
        example="""Itinerary [1 nights] """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_COMBINED_PACKAGE: str = Field(
        ...,
        alias="MANUALLY_COMBINED_PACKAGE",
        name="",
        description="""Whether or not package is manually combined one using (package component menu item) or not, if manually combined -1 else 0.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_PACKAGE_CODE: Optional[str] = Field(
        None,
        alias="CMS_PACKAGE_CODE",
        name="",
        description="""NaN""",
        example="""AMQBtuiIZZALJqsbDVbK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_PACKAGE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:00.882446""",
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
        example="""RES_BOOKING_PACKAGE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=24338249735676,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResBookingPackageModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_PACKAGE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Package"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains booking package level information of all the bookings."""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.PACKAGE_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_PACKAGE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
