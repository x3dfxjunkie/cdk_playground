"""Source Data Contract Template for GEN_CONTRACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_CONTRACT Data
    """

    ACCOM_ID: Optional[int] = Field(
        None,
        alias="ACCOM_ID",
        name="",
        description="""The system generated id of the Accom Supplier""",
        example=6223,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCLUDE_INF_BOOK_COUNT: str = Field(
        ...,
        alias="INCLUDE_INF_BOOK_COUNT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNAL_PRICING: str = Field(
        ...,
        alias="EXTERNAL_PRICING",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICING_ENGINE: Optional[str] = Field(
        None,
        alias="PRICING_ENGINE",
        name="",
        description="""NaN""",
        example="""MpIsMHogNnsziBGWPPKi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_AVAIL: str = Field(
        ...,
        alias="EXT_AVAIL",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""GXYCONT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1993-07-04 15:42:05""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_PRICING: str = Field(
        ...,
        alias="SPECIAL_PRICING",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_PRICING_METHOD: Optional[str] = Field(
        None,
        alias="SPECIAL_PRICING_METHOD",
        name="",
        description="""NaN""",
        example="""JtthWZNdVQurAbqiKCGH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICING_OVERRIDE: Optional[str] = Field(
        None,
        alias="PRICING_OVERRIDE",
        name="",
        description="""NaN""",
        example="""vPfFDfFnohXVjBCyzrqG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USAGE_OVERRIDE: Optional[str] = Field(
        None,
        alias="USAGE_OVERRIDE",
        name="",
        description="""NaN""",
        example="""cPkZkrgubKEDBucaaWiH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BUNDLE_PRODUCT: str = Field(
        ...,
        alias="BUNDLE_PRODUCT",
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
        example=5588,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_TEMP_GRP_CODE: Optional[str] = Field(
        None,
        alias="PROD_DEFN_TEMP_GRP_CODE",
        name="",
        description="""NaN""",
        example="""oQqIdDtHUXAxPFgfyDle""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_AVAIL_SOURCE: int = Field(
        ...,
        alias="EXT_AVAIL_SOURCE",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=11343,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_GROUP_ID: int = Field(
        ...,
        alias="CONTRACT_GROUP_ID",
        name="",
        description="""The system generated id of the contract group""",
        example=61455,
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
        example=-1,
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

    VALID_FROM: datetime = Field(
        ...,
        alias="VALID_FROM",
        name="",
        description="""The start date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""1985-08-12 11:42:31""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: datetime = Field(
        ...,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""2015-12-28 21:38:39""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: datetime = Field(
        ...,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""1987-12-03 20:45:21""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: datetime = Field(
        ...,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""1985-06-13 12:51:02""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15873,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: datetime = Field(
        ...,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""1976-05-23 06:04:53""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=16178,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1993-11-21 15:18:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_CURRENCY: Optional[str] = Field(
        None,
        alias="NETT_CURRENCY",
        name="",
        description="""If the contract is a nett contract, this field holds the TravelBox code of the currency in which the costs are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_TYPE: str = Field(
        ...,
        alias="RATE_TYPE",
        name="",
        description="""NM = NETT AND MARKUP, GC = GROSS AND COMMISSION, NG = GROSS OEM_sqlplus_input_finished, GO = GROSS ONLY""",
        example="""NG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_GROSS_CURRENCY: Optional[str] = Field(
        None,
        alias="DEFAULT_GROSS_CURRENCY",
        name="",
        description="""If the contract rate type is CM / GC / GM / GO or NG, this field holds the TravelBox code of the default currency in which prices are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRORATA: Optional[str] = Field(
        None,
        alias="PRORATA",
        name="",
        description="""A string representating respectively cost,markup,discount,supplement are on/off for prorata. On is denoted by character 't' while Off is denoted by character 'f''._x000D_
Example :- If cost, discount and supplement are On and markup is Off for prorata, the value is tftt.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELL_ALONE: str = Field(
        ...,
        alias="SELL_ALONE",
        name="",
        description="""SELLABLE ALONE (USED INTOURS WHEN LOADING TOUR ACCOM CONTRACT VIA TOUR BUILDER)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SUPPLIER_GROSS: str = Field(
        ...,
        alias="PAY_SUPPLIER_GROSS",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CUSTOMER_PAY_SUPPLIER: str = Field(
        ...,
        alias="CUSTOMER_PAY_SUPPLIER",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ERRATA_GROUP: Optional[int] = Field(
        None,
        alias="ERRATA_GROUP",
        name="",
        description="""Refers to the errata_group_id of errata_group table when user adds Free Text Conditions in contract level.  The option is available in 'Free Text Conditions' node in contract.""",
        example=282903,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GEN_PRODUCT: int = Field(
        ...,
        alias="GEN_PRODUCT",
        name="",
        description="""The system generated id of the product group of the generic contract""",
        example=3829,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STARTING_DAYS: Optional[str] = Field(
        None,
        alias="STARTING_DAYS",
        name="",
        description="""Deprecated""",
        example="""HPodTczvWpOLdFwKPmRz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE_GUARANTEED: str = Field(
        ...,
        alias="PRICE_GUARANTEED",
        name="",
        description="""If the product is to  be sold for a pre-defined price irrespective of the markup scheme , make this as 1 otherwise 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: Optional[str] = Field(
        None,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOURIST_REGION: Optional[str] = Field(
        None,
        alias="TOURIST_REGION",
        name="",
        description="""The TravelBox code of the destination tourist region for which the contract is applicable""",
        example="""AzOMPtbaXIZZHXDitdWs""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""ANA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESORT: Optional[str] = Field(
        None,
        alias="RESORT",
        name="",
        description="""The foreign Key which refers the field CODE of the ACT_ABSORPTION table""",
        example="""ByPJsVwBwIoPaYyTFskl""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""GndgYrfUDsITXwjspZaI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: str = Field(
        ...,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: str = Field(
        ...,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRPORT: Optional[str] = Field(
        None,
        alias="AIRPORT",
        name="",
        description="""Departure airport's code""",
        example="""suRcCYvlvbCoCIYzoXzW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DURATION_TYPE: str = Field(
        ...,
        alias="DURATION_TYPE",
        name="",
        description="""Generic item valid duration type_x000D_
Days = 'D' (Default)_x000D_
Nights = 'N'_x000D_
Hours = 'H'""",
        example="""D""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_WISE: str = Field(
        ...,
        alias="ITEM_WISE",
        name="",
        description="""if the duration of the Generic item is one day this field mark as 1 : 1 or 0 value""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TERM_AND_CONDITION: Optional[str] = Field(
        None,
        alias="TERM_AND_CONDITION",
        name="",
        description="""Text for terms and conditions of the generic contract.""",
        example="""EcSeeSfBJjwHMTkSHFCq""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""CA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCOM_CODE: Optional[str] = Field(
        None,
        alias="ACCOM_CODE",
        name="",
        description="""Accommodation""",
        example="""NDbCYBQgpZWgqfBPhfbH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCOM_NAME: Optional[str] = Field(
        None,
        alias="ACCOM_NAME",
        name="",
        description="""The Name of the Accom Supplier""",
        example="""wpfYEJJdIcZbLiCzkBeW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTENT_SUPPLIER_ID: Optional[int] = Field(
        None,
        alias="CONTENT_SUPPLIER_ID",
        name="",
        description="""The system generated id of the Content Supplier""",
        example=9159,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTENT_SUPPLIER_CODE: Optional[str] = Field(
        None,
        alias="CONTENT_SUPPLIER_CODE",
        name="",
        description="""The code of the Content Supplier""",
        example="""XKFVcjZCYRVscyJziEOY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTENT_SUPPLIER_NAME: Optional[str] = Field(
        None,
        alias="CONTENT_SUPPLIER_NAME",
        name="",
        description="""The Name of the Content Supplier""",
        example="""QXHUnYFoLngQXhumqrKs""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEND_DOCUMENTS_TO_SUPPLIER: Optional[str] = Field(
        None,
        alias="SEND_DOCUMENTS_TO_SUPPLIER",
        name="",
        description="""Deprecated""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROUP_RATES: Optional[str] = Field(
        None,
        alias="GROUP_RATES",
        name="",
        description="""A flag indicating the group rates are enabled for the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_WISE_SUPPLIER: Optional[str] = Field(
        None,
        alias="DATE_WISE_SUPPLIER",
        name="",
        description="""Flag for Date wise Suplier Enable (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRACKABLE: Optional[str] = Field(
        None,
        alias="TRACKABLE",
        name="",
        description="""Whether the voucher code is trackable or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_CONTRACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:31.392116""",
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
        example="""GEN_CONTRACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=69724821576285,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestGenContractModel(BaseModel):
    """
    Payload class for TravelBox GEN_CONTRACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Pass Through Generic Contracts"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Pass through view of generic contracts"""  # optional
        unique_identifier = ["data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_CONTRACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
