"""Source Data Contract Template for PKG_HOLIDAY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PKG_HOLIDAY Data
    """

    TEMPLATE_TYPE: int = Field(
        ...,
        alias="TEMPLATE_TYPE",
        name="",
        description="""Indicate package template type""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1989-01-17 08:22:18""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BLOCK_CODE: Optional[str] = Field(
        None,
        alias="BLOCK_CODE",
        name="",
        description="""Unique code of the block""",
        example="""EFaHllDUwsKoLVGULXHs""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BP_OVERRIDE: str = Field(
        ...,
        alias="BP_OVERRIDE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_ID: Optional[int] = Field(
        None,
        alias="PROD_DEFN_ID",
        name="",
        description="""NaN""",
        example=2270,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_TEMP_GRP_CODE: Optional[str] = Field(
        None,
        alias="PROD_DEFN_TEMP_GRP_CODE",
        name="",
        description="""NaN""",
        example="""eniFOKePJAYaACUOuFAq""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_CATEGORY_CODE: Optional[str] = Field(
        None,
        alias="RATE_CATEGORY_CODE",
        name="",
        description="""Rate category code""",
        example="""xpvnKaTlmucNMJTacfxT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OFFER_GROUP_CODE: Optional[str] = Field(
        None,
        alias="OFFER_GROUP_CODE",
        name="",
        description="""NaN""",
        example="""lYNMAGLtfXBdVaVrcNUj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OFFER_GROUP_NAME: Optional[str] = Field(
        None,
        alias="OFFER_GROUP_NAME",
        name="",
        description="""NaN""",
        example="""rxHYMRmqMsUFAeyJpRjD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TIME_TO_PUBLISH: Optional[datetime] = Field(
        None,
        alias="TIME_TO_PUBLISH",
        name="",
        description="""NaN""",
        example="""1993-07-05 09:32:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_AUDITED_TIME: Optional[datetime] = Field(
        None,
        alias="LAST_AUDITED_TIME",
        name="",
        description="""NaN""",
        example="""2001-08-28 11:35:10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PACKAGE_ID: int = Field(
        ...,
        alias="PACKAGE_ID",
        name="",
        description="""The foreign key which refers the field PACKAGE_ID of the table PKG_HOLIDAY""",
        example=13768,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_GROUP_ID: int = Field(
        ...,
        alias="PKG_GROUP_ID",
        name="",
        description="""Id of the Package Group associated with the Scheme Rule.""",
        example=13857,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VERSION: int = Field(
        ...,
        alias="VERSION",
        name="",
        description="""The version of the contract""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PARENT_VERSION: Optional[int] = Field(
        None,
        alias="PARENT_VERSION",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_TYPE: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPE",
        name="",
        description="""Other Cost applicable Product Type Code""",
        example="""MISC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOLIDAY_TYPE: str = Field(
        ...,
        alias="HOLIDAY_TYPE",
        name="",
        description="""The TravelBox code of the holiday type for which the limit is defined for""",
        example="""RMLS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_FROM: Optional[datetime] = Field(
        None,
        alias="VALID_FROM",
        name="",
        description="""The start date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""2017-11-01 18:04:40""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: Optional[datetime] = Field(
        None,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""2019-06-20 06:22:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: Optional[datetime] = Field(
        None,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""2003-06-28 06:00:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: Optional[datetime] = Field(
        None,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""2015-08-25 05:09:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: int = Field(
        ...,
        alias="STATUS",
        name="",
        description="""The TravelBox code of the status of the contract""",
        example=503,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE: int = Field(
        ...,
        alias="STAGE",
        name="",
        description="""The TravelBox code of the stage of the contract""",
        example=50301,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""TtuxlNzBNOjKbGlGrygn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIGINAL_PACKAGE: str = Field(
        ...,
        alias="ORIGINAL_PACKAGE",
        name="",
        description="""deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVERAGE_MARGIN: Optional[float] = Field(
        None,
        alias="AVERAGE_MARGIN",
        name="",
        description="""Deprecated""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""PLaGQHxAjlLAWhNDbQlJ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15073,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: datetime = Field(
        ...,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2021-12-03 15:58:19""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""2023-05-24 04:54:30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=15873,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COSTING_CURRENCY: str = Field(
        ...,
        alias="COSTING_CURRENCY",
        name="",
        description="""The TravelBox code of the currency which the rates are defined in the package""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_MAIN_PKG_DURATION: int = Field(
        ...,
        alias="EXT_MAIN_PKG_DURATION",
        name="",
        description="""deprecated""",
        example=0,
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

    CALC_CLI_GROUP: Optional[str] = Field(
        None,
        alias="CALC_CLI_GROUP",
        name="",
        description="""The TravelBox code of the client group defined for package cost and prices when pricing method is Markup, Contract markup or Package Markup""",
        example="""DIRECT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_DIST_CHANNEL: Optional[str] = Field(
        None,
        alias="CALC_DIST_CHANNEL",
        name="",
        description="""The TravelBox code of the distribution channel defined for package cost and prices when pricing method is Markup, Contract markup or Package Markup """,
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_TYPE: Optional[str] = Field(
        None,
        alias="CALC_TYPE",
        name="",
        description=""", possible values are_x000D_
C - Cost_x000D_
P - Price_x000D_
CP - Both""",
        example="""CP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_PRICING_METHOD: Optional[int] = Field(
        None,
        alias="CALC_PRICING_METHOD",
        name="",
        description="""The pricing method of the packages, possible values are_x000D_
1 - Margin_x000D_
2 - Markup_x000D_
3 - Contract Markup_x000D_
4 - Package Markup""",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ELEMENT_LEVEL_MARGIN_MARKUP: Optional[str] = Field(
        None,
        alias="ELEMENT_LEVEL_MARGIN_MARKUP",
        name="",
        description="""Flag to indicate whether elements inside an itinerary can have_x000D_
different margins and markups. In Costs and Prices node , Element_x000D_
Markup/Margin checkbox""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_BRAND: Optional[str] = Field(
        None,
        alias="CALC_BRAND",
        name="",
        description="""The TravelBox code of the brand defined for package cost and prices when pricing method is Markup, Contract markup or Package Markup""",
        example="""CORE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MINIMUM_MARGIN: Optional[float] = Field(
        None,
        alias="MINIMUM_MARGIN",
        name="",
        description="""The minimum profit margin percentage of the package""",
        example=77798.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MINIMUM_MARGIN_AMOUNT_TYPE: Optional[str] = Field(
        None,
        alias="MINIMUM_MARGIN_AMOUNT_TYPE",
        name="",
        description="""deprecated""",
        example="""lbeYyhzbWGaGFzOpDLLO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_PAX_BASE: Optional[int] = Field(
        None,
        alias="CALC_PAX_BASE",
        name="",
        description="""Setup at Departure tab of Dates node of the package. Used to determine_x000D_
the group size of the contract for which are defined as group rate contracts.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIVISION: Optional[str] = Field(
        None,
        alias="DIVISION",
        name="",
        description="""The TravelBox code of the division for which the limit is defined for""",
        example="""WDTCDLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEP_DATE_EXIST: Optional[str] = Field(
        None,
        alias="DEP_DATE_EXIST",
        name="",
        description="""deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONSTANT_AIR_TAX: Optional[str] = Field(
        None,
        alias="CONSTANT_AIR_TAX",
        name="",
        description="""deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CMS_CODE: Optional[str] = Field(
        None,
        alias="CMS_CODE",
        name="",
        description="""User defined CMS code which is taken as parameter values for tb_code, tb_itin, tb_pricegrid in package, itinerary and price grid respectively in the CMS URL which refers from travelbox to CMS. If this value is not defined the system will take package code, itinerary code and price grid name as default value of above variables.""",
        example="""bTBMkgRulAEquJqZrIpp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILDREN_AS_ADULT: Optional[str] = Field(
        None,
        alias="CHILDREN_AS_ADULT",
        name="",
        description="""If this flag is selected it is allowed book the package even if in the search criteria number of_x000D_
children are higher than what is mentioned in the sharing rules. But for the number of children_x000D_
exceeding the no of child in sharing rules, adult charge will be applied""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NO_OF_PAX: Optional[int] = Field(
        None,
        alias="NO_OF_PAX",
        name="",
        description="""The Maximum total number of passengers that can be in a booking, in order to apply the Scheme Rule.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEPARATE_ITIN_NO_NEXT_VAL: int = Field(
        ...,
        alias="SEPARATE_ITIN_NO_NEXT_VAL",
        name="",
        description="""When entries are added to pkg_seperate_itinerary table assigned_itinerary_no is given SEPARATE_ITIN_NO_NEXT_VAL + 1""",
        example=500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_BOOKING_DATE: Optional[datetime] = Field(
        None,
        alias="CALC_BOOKING_DATE",
        name="",
        description="""The date which the rates are calculated from contracts for the package""",
        example="""2010-08-04 06:10:36""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALC_COST_DEP_DATE_ONLY: Optional[str] = Field(
        None,
        alias="CALC_COST_DEP_DATE_ONLY",
        name="",
        description="""Boolean value can take 0 or 1_x000D_
If 1 only the departure dates of the element are considered for the package calculation_x000D_
elese calculation happens for the whole valid period of the element""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PKG_HOLIDAY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:21.014193""",
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
        example="""PKG_HOLIDAY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=57994622603191,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestPkgHolidayModel(BaseModel):
    """
    Payload class for TravelBox PKG_HOLIDAY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package Holiday"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Represents a particular version of a package. Primary details such as  of a package
package_id, group_id, version number and valid periods are stored."""  # optional
        unique_identifier = ["data.PACKAGE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_HOLIDAY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
