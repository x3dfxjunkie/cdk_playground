"""Source Data Contract Template for RES_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING Data
    """

    DEST_CITY: Optional[str] = Field(
        None,
        alias="DEST_CITY",
        name="",
        description="""Destination city for the items in the booking. Used only in packages.""",
        example="""LKBV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FLIGHT_ONLY: str = Field(
        ...,
        alias="FLIGHT_ONLY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACT_DEST_COUNTRY: Optional[str] = Field(
        None,
        alias="ACT_DEST_COUNTRY",
        name="",
        description="""Accounting destination country code of the booking used for tax calculations""",
        example="""US-LKBV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_ACCT_DEST_CALCULATION: str = Field(
        ...,
        alias="MANUAL_ACCT_DEST_CALCULATION",
        name="",
        description="""A flag to indicate whether to accounting destination of the booking [ACT_DEST_COUNTRY] is manually calculated or not._x000D_
If it is manually calculated, it won't be overridden by the system booking properties calculations (e.g. by schedulers).""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_AIRPORT: Optional[str] = Field(
        None,
        alias="DEP_AIRPORT",
        name="",
        description="""NaN""",
        example="""rvYsYwquPQUtBAVrkJHP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RETURN_DATE: Optional[datetime] = Field(
        None,
        alias="RETURN_DATE",
        name="",
        description="""NaN""",
        example="""1978-11-15 06:45:05""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SOURCE_MARKET: Optional[str] = Field(
        None,
        alias="SOURCE_MARKET",
        name="",
        description="""The TravelBox code of the source market for which the discount group is visible""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALL_DOCS_DISPATCHED: str = Field(
        ...,
        alias="ALL_DOCS_DISPATCHED",
        name="",
        description="""Flag to identify whether all documents related to this booking are dispatched ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_CLIENT_ID: Optional[int] = Field(
        None,
        alias="SECONDARY_CLIENT_ID",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_COMMISSION: float = Field(
        ...,
        alias="SECONDARY_COMMISSION",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_COM_PERCENTAGE: Optional[float] = Field(
        None,
        alias="SECONDARY_COM_PERCENTAGE",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPEC: Optional[str] = Field(
        None,
        alias="OPEC",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LINK_BOOKINGS: Optional[str] = Field(
        None,
        alias="LINK_BOOKINGS",
        name="",
        description="""NaN""",
        example="""uLnvjZKrSmhyaqzVGASX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESERVATION_TIME: Optional[datetime] = Field(
        None,
        alias="RESERVATION_TIME",
        name="",
        description="""NaN""",
        example="""2017-05-23 05:46:56""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_MASTER_ID: Optional[int] = Field(
        None,
        alias="GROUP_MASTER_ID",
        name="",
        description="""NaN""",
        example=4788,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVOICE_STATUS: Optional[str] = Field(
        None,
        alias="INVOICE_STATUS",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANCELLATION_REFERENCE: Optional[str] = Field(
        None,
        alias="CANCELLATION_REFERENCE",
        name="",
        description="""NaN""",
        example="""jfaLspYJvTjlUfJyVQiW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXCLUDE_FROM_AUTO_REFUND: Optional[str] = Field(
        None,
        alias="EXCLUDE_FROM_AUTO_REFUND",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPRESS_CONFIRMATION: Optional[str] = Field(
        None,
        alias="SUPPRESS_CONFIRMATION",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELLING_TO_BASE_EXCHANGE_RATE: float = Field(
        ...,
        alias="SELLING_TO_BASE_EXCHANGE_RATE",
        name="",
        description="""The rate for selling currency to the contract currency ( the currency defined in the contract)""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED: str = Field(
        ...,
        alias="MODIFIED",
        name="",
        description="""Indicate whether this payment is modified after insertion (Ex: for IBTX)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    UNAVAILABLE: Optional[str] = Field(
        None,
        alias="UNAVAILABLE",
        name="",
        description="""NaN""",
        example="""sPzacNRynQdAzcybTaWz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_ORDER_ID: Optional[str] = Field(
        None,
        alias="SALES_ORDER_ID",
        name="",
        description="""NaN""",
        example="""dMxxwnhukokmZksdMSKc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_types: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPES",
        name="",
        description="",
        example="CAR|INS|GEN|HTL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT_ON_COMMISSION: float = Field(
        ...,
        alias="DISCOUNT_ON_COMMISSION",
        name="",
        description="""Discount for the commission of the booking. In Reservation manager > View commision details.""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INSURANCE_DUE: float = Field(
        ...,
        alias="INSURANCE_DUE",
        name="",
        description="""Insurance due amount of the booking""",
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
        example=120.2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_TAX_PRICE: float = Field(
        ...,
        alias="TOTAL_TAX_PRICE",
        name="",
        description="""Total tax price applied for the booking""",
        example=144.76,
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

    REFUND_AUTHORISED: Optional[str] = Field(
        None,
        alias="REFUND_AUTHORISED",
        name="",
        description="""A flag to indicate whether the booking refunds are authorized or not. Refer 'REFUND_AUTHORISED_AMOUNT'""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFUND_AUTHORISED_AMOUNT: Optional[float] = Field(
        None,
        alias="REFUND_AUTHORISED_AMOUNT",
        name="",
        description="""Authorized refund amount. Refer 'REFUND_AUTHORISED'""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_REFUND_ALLOWED_AMT: Optional[float] = Field(
        None,
        alias="COMM_REFUND_ALLOWED_AMT",
        name="",
        description="""Deprecated""",
        example=94282.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROMOTION_ID: Optional[int] = Field(
        None,
        alias="PROMOTION_ID",
        name="",
        description="""Promotion id of the selected promotio for 'Promotion' parameter  in discount scheme setup.""",
        example=1533,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFIT: float = Field(
        ...,
        alias="PROFIT",
        name="",
        description="""Total profit of the booking""",
        example=202.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BROCHURE_ID: Optional[int] = Field(
        None,
        alias="BROCHURE_ID",
        name="",
        description="""Tbx id of the brochure associated with the address""",
        example=265,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCALE: str = Field(
        ...,
        alias="LOCALE",
        name="",
        description="""The TravelBox code of the locale""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LEDGER_DESTINATION: Optional[int] = Field(
        None,
        alias="LEDGER_DESTINATION",
        name="",
        description="""Deprecated""",
        example=3483,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WEBSITE_ID: Optional[str] = Field(
        None,
        alias="WEBSITE_ID",
        name="",
        description="""Id of the website as defined in Setup""",
        example="""jBEMeLnEgpUDMoRnsfCv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VIP_BOOKING: str = Field(
        ...,
        alias="VIP_BOOKING",
        name="",
        description="""A flag to indicate whether the booking is a VIP booking or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADMIN_BOOKING: Optional[str] = Field(
        None,
        alias="ADMIN_BOOKING",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADMIN_BOOKING_AUTHORIZATION: Optional[str] = Field(
        None,
        alias="ADMIN_BOOKING_AUTHORIZATION",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORIZED_USER: Optional[int] = Field(
        None,
        alias="AUTHORIZED_USER",
        name="",
        description="""Deprecated""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_REF: Optional[str] = Field(
        None,
        alias="AGENT_REF",
        name="",
        description="""The agent reference""",
        example="""GAflDzLNCjTCHKVtsAgj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NON_COMMISSIONABLE_PRICE: float = Field(
        ...,
        alias="NON_COMMISSIONABLE_PRICE",
        name="",
        description="""Non commissionable price component of the booking.""",
        example=20.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESTINATION: Optional[str] = Field(
        None,
        alias="DESTINATION",
        name="",
        description="""Destination location code for flight booking items""",
        example="""YwhMMhJJhgwPinUSfGsv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION_ID: Optional[int] = Field(
        None,
        alias="LOCATION_ID",
        name="",
        description="""Location id is saved when the module configuration_x000D_
'STORE_LOCATION_ID' is enabled, otherwise_x000D_
-1""",
        example=849,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SOURCE_ID: Optional[int] = Field(
        None,
        alias="SOURCE_ID",
        name="",
        description="""System generated id of the brochure source""",
        example=9479,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DONT_COLLECT_COMMISSION: Optional[str] = Field(
        None,
        alias="DONT_COLLECT_COMMISSION",
        name="",
        description="""A flag to indicate whether to collect commission from the client or not. In Reservation manager > View commision details but only visible when the trade clients collect payment is selected.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_STYLE: Optional[int] = Field(
        None,
        alias="BOOKING_STYLE",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_NAME: Optional[str] = Field(
        None,
        alias="GROUP_NAME",
        name="",
        description="""Name of the group""",
        example="""omDzSkOFPohweHxUiyFh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIN_DEST_COUNTRY: Optional[str] = Field(
        None,
        alias="MAIN_DEST_COUNTRY",
        name="",
        description="""Main destination country and city code. Format: <country_code>-<city_code>""",
        example="""US-LKBV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_BOOKING_MARGIN: Optional[float] = Field(
        None,
        alias="GROUP_BOOKING_MARGIN",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_BOOKING_ID: Optional[str] = Field(
        None,
        alias="EXT_BOOKING_ID",
        name="",
        description="""Used to keep a reference to an external system (e.g. H2H systems booking reference).""",
        example="""LkOFVXIosLLOsgEBuJxy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_BOOKING_PAX_UPDATED: Optional[str] = Field(
        None,
        alias="GROUP_BOOKING_PAX_UPDATED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATOL_TYPE: Optional[str] = Field(
        None,
        alias="ATOL_TYPE",
        name="",
        description="""ATOL document type, saved when saving the booking and used when generating ATOL document""",
        example="""FiLYHSpkbFMJcyrqLziw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSIGNED_USER: Optional[int] = Field(
        None,
        alias="ASSIGNED_USER",
        name="",
        description="""Not in the disney scope""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ASSIGNED_DATE: Optional[datetime] = Field(
        None,
        alias="ASSIGNED_DATE",
        name="",
        description="""Not in the disney scope""",
        example="""2015-12-27 18:06:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_STATUS: Optional[str] = Field(
        None,
        alias="CLIENT_STATUS",
        name="",
        description="""Flag to indicate the client status associated with the Scheme Rule._x000D_
1 - Active_x000D_
0 - Inactive""",
        example="""qOBedifagbdunBtKOSnp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TC_PAY_GRP: Optional[int] = Field(
        None,
        alias="TC_PAY_GRP",
        name="",
        description="""Trade client pay group id""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RQ_ITEM_INDC: str = Field(
        ...,
        alias="RQ_ITEM_INDC",
        name="",
        description="""flag to denote whether at least one item is ON_REQUEST ( item is done without allocations )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_DEST_CALCULATION: Optional[str] = Field(
        None,
        alias="MANUAL_DEST_CALCULATION",
        name="",
        description="""A flag to indicate whether the destination is calculated manually. if true, destination calculation is skipped.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTO_CANCEL: int = Field(
        ...,
        alias="AUTO_CANCEL",
        name="",
        description="""Flag to indicate whether the booking is auto cancelled, error occured in auto cancellation. Possible values_x000D_
0 = No Change,_x000D_
1 = Auto Cancelled successfully,_x000D_
2 = Error occured while cancelling,_x000D_
3 = Cannot cancel some booking items""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_SOURCE: Optional[str] = Field(
        None,
        alias="BOOKING_SOURCE",
        name="",
        description="""Accounting rule applicable booking source (booking source codes)_x000D_
Ex: TravelBox(0), Bonotel(CAR), Hotelbeds(HTL)""",
        example="""WDPRO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISPATCH_METHOD: Optional[str] = Field(
        None,
        alias="DISPATCH_METHOD",
        name="",
        description="""Notification dispatch method code_x000D_
MET = METRO_MAIL_x000D_
FAX = FAX_x000D_
PST = POST_x000D_
EML = EMAIL_x000D_
UPL = FILE_UPLOAD""",
        example="""ptgbLVZKFvFrnkoVBvhO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISPATCH_ADDRESS: Optional[str] = Field(
        None,
        alias="DISPATCH_ADDRESS",
        name="",
        description="""Dispatch address like email, postal address etc:""",
        example="""QHvGGOGdjcqoaCbJkCDu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INSURANCE_EXCLUDED: Optional[str] = Field(
        None,
        alias="INSURANCE_EXCLUDED",
        name="",
        description="""When the booking is cancelled, value of this column will indicate whether there are insurance items actively remains in the booking which were excluded from the cancellation""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    YOUR_REFERENCE: Optional[str] = Field(
        None,
        alias="YOUR_REFERENCE",
        name="",
        description="""This property is used for store the Your Reference of the Booking.""",
        example="""ASnYjCpxcNMUyDlmpTvE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNSELOR_NAME: Optional[str] = Field(
        None,
        alias="COUNSELOR_NAME",
        name="",
        description="""This property is used for store the Counselor Name of the Booking.""",
        example="""Stephanie Jill Hanen""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNSELOR_REF_KEY: Optional[str] = Field(
        None,
        alias="COUNSELOR_REF_KEY",
        name="",
        description="""This property is used for store the Counselor Guest Reference Key of the Booking.""",
        example="""ouOljvLvzZNJgAXYhQzA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNSELOR_REF_VALUE: Optional[str] = Field(
        None,
        alias="COUNSELOR_REF_VALUE",
        name="",
        description="""This property is used for store the Counselor Guest Reference Value of the Booking.""",
        example="""ZQhwacZQqQfuxdKJTBls""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MOD_SOURCE: Optional[str] = Field(
        None,
        alias="LAST_MOD_SOURCE",
        name="",
        description="""NaN""",
        example="""WDPRO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATA_TYPES: Optional[str] = Field(
        None,
        alias="DATA_TYPES",
        name="",
        description="""List of Classes to Load Data in Bulk Loading""",
        example="""ptEzXJoqahssKCZcaMPp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_DEPOSIT_DUE_DATE: Optional[str] = Field(
        None,
        alias="MANUAL_DEPOSIT_DUE_DATE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BLOCK_CODE: Optional[str] = Field(
        None,
        alias="BLOCK_CODE",
        name="",
        description="""Unique code of the block""",
        example="""01825""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27858693,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=7186204,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPANY: str = Field(
        ...,
        alias="COMPANY",
        name="",
        description="""The TravelBox code of the company for which the limit is defined for""",
        example="""WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIVISION: str = Field(
        ...,
        alias="DIVISION",
        name="",
        description="""The TravelBox code of the division for which the limit is defined for""",
        example="""WDTCWDW""",
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

    BOOKING_PRODUCT: str = Field(
        ...,
        alias="BOOKING_PRODUCT",
        name="",
        description="""Deprecated""",
        example="""CMP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_TYPE: Optional[str] = Field(
        None,
        alias="BOOKING_TYPE",
        name="",
        description="""Deprecated""",
        example="""STD""",
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

    OPTION_STATUS: int = Field(
        ...,
        alias="OPTION_STATUS",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=600,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    QUOTE_DATE: Optional[datetime] = Field(
        None,
        alias="QUOTE_DATE",
        name="",
        description="""If the booking is originally done as a quote then the quote creation date is populated in this field""",
        example="""1989-05-18 07:41:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_DATE: datetime = Field(
        ...,
        alias="BOOKING_DATE",
        name="",
        description="""Contract to selling exchange rate applicable booking date period start date""",
        example="""1992-06-04 04:02:12""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_DATE: datetime = Field(
        ...,
        alias="DEPARTURE_DATE",
        name="",
        description="""Departure date for bookings""",
        example="""2000-08-08 19:11:51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFINITE_DUE_DATE: Optional[datetime] = Field(
        None,
        alias="DEFINITE_DUE_DATE",
        name="",
        description="""System calculated date for a booking to become DEFINITE. The customer has to confirm the booking on or before this date.""",
        example="""1982-03-31 16:17:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFINITE_DATE: Optional[datetime] = Field(
        None,
        alias="DEFINITE_DATE",
        name="",
        description="""The date a booking became DEFINITE.""",
        example="""1990-07-05 02:45:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRM_DUE_DATE: Optional[datetime] = Field(
        None,
        alias="FIRM_DUE_DATE",
        name="",
        description="""System calculated date for a booking to become FIRM""",
        example="""2010-05-12 23:11:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRM_DATE: Optional[datetime] = Field(
        None,
        alias="FIRM_DATE",
        name="",
        description="""Firm date of the booking""",
        example="""1987-07-22 13:54:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BALANCE_DUE_DATE: Optional[datetime] = Field(
        None,
        alias="BALANCE_DUE_DATE",
        name="",
        description="""Balance due date of the firmed booking""",
        example="""1985-05-26 15:19:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULL_PAYMENT_RECEIVED_DATE: Optional[datetime] = Field(
        None,
        alias="FULL_PAYMENT_RECEIVED_DATE",
        name="",
        description="""The date the full payment received for a booking from the client""",
        example="""2009-01-20 19:03:57""",
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

    TOTAL_PRICE: float = Field(
        ...,
        alias="TOTAL_PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=1866.3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_COST: float = Field(
        ...,
        alias="TOTAL_COST",
        name="",
        description="""The total cost of the booking""",
        example=1639.62,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVOICE_TOTAL: float = Field(
        ...,
        alias="INVOICE_TOTAL",
        name="",
        description="""Invoice total of the supplier invoice""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUAL_DEPOSIT: str = Field(
        ...,
        alias="MANUAL_DEPOSIT",
        name="",
        description="""A flag to indicate whether the deposit is calculated manually. if true, deposit calculation is skipped.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPOSIT: float = Field(
        ...,
        alias="DEPOSIT",
        name="",
        description="""Total depoist amount""",
        example=200.0,
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

    BOOKED_USER: Optional[int] = Field(
        None,
        alias="BOOKED_USER",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=20629,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEDIA_CODE: Optional[str] = Field(
        None,
        alias="MEDIA_CODE",
        name="",
        description="""Code of the respective Media Code""",
        example="""gNzzWjYpKuHduPUrxCcZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISTRIBUTION_CHANNEL: str = Field(
        ...,
        alias="DISTRIBUTION_CHANNEL",
        name="",
        description="""The TravelBox code of the distribution channel for which the limit is defined for""",
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELLING_CURRENCY: str = Field(
        ...,
        alias="SELLING_CURRENCY",
        name="",
        description="""Currrency using for selling""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCKED: str = Field(
        ...,
        alias="LOCKED",
        name="",
        description="""THIS FILEDS INDICATE THAT BOOKING IS LOCKED AND NO MODIFICATIONS CAN BE DONE.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION_ADJUSTMENT: float = Field(
        ...,
        alias="COMMISSION_ADJUSTMENT",
        name="",
        description="""ADJUSTMENT DONE TO THE COMMISSION ON REQUEST OF AGENT KEEPING OUR MARGINS CONSTANT""",
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
        example=-1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2002-03-06 21:10:03""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SYSTEM_GENERATED_EXPIRY_DATE: Optional[datetime] = Field(
        None,
        alias="SYSTEM_GENERATED_EXPIRY_DATE",
        name="",
        description="""System generated expire date""",
        example="""2001-07-28 01:18:53""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONSTRAINTS_EXIST: str = Field(
        ...,
        alias="CONSTRAINTS_EXIST",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    JOURNAL_BATCH_NO: int = Field(
        ...,
        alias="JOURNAL_BATCH_NO",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIR_ONLY_BOOKING: str = Field(
        ...,
        alias="AIR_ONLY_BOOKING",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_ID: Optional[int] = Field(
        None,
        alias="AGENT_ID",
        name="",
        description="""Credit agent id of the trade client""",
        example=7648,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: Optional[int] = Field(
        None,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=9837,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS_NO: Optional[int] = Field(
        None,
        alias="ADDRESS_NO",
        name="",
        description="""Address no of the airline""",
        example=6948,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_METHOD: Optional[str] = Field(
        None,
        alias="CONTACT_METHOD",
        name="",
        description="""Preferred contact method mentioned in the booking. Refer CONTACT_NUMBER as well.""",
        example="""IngKIRfpYAZalgXXqsIc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_NUMBER: Optional[str] = Field(
        None,
        alias="CONTACT_NUMBER",
        name="",
        description="""Contact number mentioned in the booking. Refer CONTACT_METHOD as well.""",
        example="""ZPUsYcmLvdFPRxbXDhxE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_CHQ_AUTHORIZED: Optional[str] = Field(
        None,
        alias="COMM_CHQ_AUTHORIZED",
        name="",
        description="""Deprecated""",
        example="""WXTPyNpXokeVHVCzapgh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_CHQ_NOTE: Optional[str] = Field(
        None,
        alias="COMM_CHQ_NOTE",
        name="",
        description="""Deprecated""",
        example="""tYgRGQOcCZehtmGjfbLU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_SELF_BILLING: Optional[str] = Field(
        None,
        alias="CLIENT_SELF_BILLING",
        name="",
        description="""A flag which is related to the trade client's 'self billing' flag""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GSA_JOIN_DATE: Optional[datetime] = Field(
        None,
        alias="GSA_JOIN_DATE",
        name="",
        description="""Grade Client GSA joined date""",
        example="""2017-12-25 17:20:41""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GSA_CLIENT: Optional[str] = Field(
        None,
        alias="GSA_CLIENT",
        name="",
        description="""Flag to indicate if the Trade Client is a GSA Client""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOTAL_COMMISSION: float = Field(
        ...,
        alias="TOTAL_COMMISSION",
        name="",
        description="""Total commission for the trade client""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:35.167129""",
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
        example="""RES_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=21658892212413,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table stores all the to level information related to all the bookings or Quotations made in TravelBox Reservation system."""  # optional
        unique_identifier = ["data.BOOKING_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
