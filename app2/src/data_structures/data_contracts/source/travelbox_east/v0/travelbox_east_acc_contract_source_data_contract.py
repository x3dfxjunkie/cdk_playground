"""Source Data Contract Template for ACC_CONTRACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACC_CONTRACT Data
    """

    ALLOCATION_CONTRACT_ID: Optional[int] = Field(
        None,
        alias="ALLOCATION_CONTRACT_ID",
        name="",
        description="""Deprecated""",
        example=4604,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""WHUxqxbeyZWGEOwrRMPI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: str = Field(
        ...,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
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

    ROOM_WISE_OR_PAX_WISE: str = Field(
        ...,
        alias="ROOM_WISE_OR_PAX_WISE",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALCULATION_WEIGHT: Optional[int] = Field(
        None,
        alias="CALCULATION_WEIGHT",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOCUMENT_SEND_TO_ACCOM: Optional[str] = Field(
        None,
        alias="DOCUMENT_SEND_TO_ACCOM",
        name="",
        description="""A flag indicating whether the supplier documents needs to be send to the hotel ( value is 1 ) or to the supplier ( value is 0 )""",
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

    RATE_PLAN_CODE: Optional[str] = Field(
        None,
        alias="RATE_PLAN_CODE",
        name="",
        description="""Deprecated""",
        example="""FdYxETAQpRNSRitRDRmO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_PLAN_NAME: Optional[str] = Field(
        None,
        alias="RATE_PLAN_NAME",
        name="",
        description="""Deprecated""",
        example="""aVuotqkQCCiBGiZlOTaO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DELETED: Optional[str] = Field(
        None,
        alias="DELETED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPP_COMM: Optional[float] = Field(
        None,
        alias="SUPP_COMM",
        name="",
        description="""Deprecated""",
        example=0.0,
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

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""RRD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2001-08-31 01:38:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_AVAIL_SOURCE: int = Field(
        ...,
        alias="EXT_AVAIL_SOURCE",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OVERRIDE_PRICE: int = Field(
        ...,
        alias="OVERRIDE_PRICE",
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
        example=55552,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_GROUP_ID: int = Field(
        ...,
        alias="CONTRACT_GROUP_ID",
        name="",
        description="""The system generated id of the contract group""",
        example=55513,
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
        example="""2002-06-11 16:22:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: datetime = Field(
        ...,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""1998-11-30 19:02:14""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: datetime = Field(
        ...,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""1977-02-12 09:57:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: datetime = Field(
        ...,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""1970-11-29 18:07:19""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: datetime = Field(
        ...,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2020-03-15 00:12:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15078,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1996-10-22 01:07:24""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=20839,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRORATA: str = Field(
        ...,
        alias="PRORATA",
        name="",
        description="""A string representating respectively cost,markup,discount,supplement are on/off for prorata. On is denoted by character 't' while Off is denoted by character 'f''._x000D_
Example :- If cost, discount and supplement are On and markup is Off for prorata, the value is tftt.""",
        example="""tttt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ECLC_ALLOWED: str = Field(
        ...,
        alias="ECLC_ALLOWED",
        name="",
        description="""A flag indicating early checkin - late checkout is allowed ( value is 1 ) or not ( value is 0 ) for this hotel""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ECLC_GURANTEED: Optional[str] = Field(
        None,
        alias="ECLC_GURANTEED",
        name="",
        description="""A flag indicating early checkin - late checkout is guaranteed by hotel ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHECKIN_TIME: Optional[int] = Field(
        None,
        alias="CHECKIN_TIME",
        name="",
        description="""The early check-in/ late check-out time""",
        example=1500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHECKOUT_TIME: Optional[int] = Field(
        None,
        alias="CHECKOUT_TIME",
        name="",
        description="""Checkout time of the hotel in 24 hours""",
        example=1100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELL_ALONE: Optional[str] = Field(
        None,
        alias="SELL_ALONE",
        name="",
        description="""SELLABLE ALONE (USED INTOURS WHEN LOADING TOUR ACCOM CONTRACT VIA TOUR BUILDER)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_CURRENCY: Optional[str] = Field(
        None,
        alias="NETT_CURRENCY",
        name="",
        description="""If the contract is a nett contract, this field holds the TravelBox code of the currency in which the costs are defined""",
        example="""SCKaAldkIdTCFmZaTOjW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_TYPE: str = Field(
        ...,
        alias="RATE_TYPE",
        name="",
        description="""NM = NETT AND MARKUP, GC = GROSS AND COMMISSION, NG = GROSS OEM_sqlplus_input_finished, GO = GROSS ONLY""",
        example="""GC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_DEFAULT_CURRENCY: Optional[str] = Field(
        None,
        alias="GROSS_DEFAULT_CURRENCY",
        name="",
        description="""If the contract is a gross contract, this field holds the TravelBox code of the currency in which the prices are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CUSTOMER_PAY_HOTEL: str = Field(
        ...,
        alias="CUSTOMER_PAY_HOTEL",
        name="",
        description="""CUSTOMER PAY THE HOTEL AND RECEIVE THE COMMISSION FROM HOTEL""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_HOTEL_GROSS: str = Field(
        ...,
        alias="PAY_HOTEL_GROSS",
        name="",
        description="""GROSS IS PAID TO THE HOTEL, AND EXPECT THE COMMISION""",
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
        example=275431,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREFFERED_BOARD_BASIS: Optional[str] = Field(
        None,
        alias="PREFFERED_BOARD_BASIS",
        name="",
        description="""THIS WILL BE SELECTED BY DEFAULT IN SEARCH RESULTS. THIS IS USUALLY SPECIFIED BY THE SUPPLIER IN THE CONTRACT.""",
        example="""kBlWAukmHfRSPpxiPjpI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACC_CONTRACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:47:26.672495""",
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
        example="""ACC_CONTRACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=98033639936063,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastAccContractModel(BaseModel):
    """
    Payload class for TravelBox ACC_CONTRACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Pass Through Accommodation ContrAccounts"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store Accommodaion contract information. The values are setup in root node in Accommodation Manager"""  # optional
        unique_identifier = ["data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACC_CONTRACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
