"""Source Data Contract Template for SUPPLIER"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox SUPPLIER Data
    """

    PAYMENT_TYPE: Optional[str] = Field(
        None,
        alias="PAYMENT_TYPE",
        name="",
        description="""PAYMENT_TYPE of the receipt""",
        example="""ARC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=16180,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1987-10-20 13:47:30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: Optional[int] = Field(
        None,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15075,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: Optional[datetime] = Field(
        None,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2017-04-07 14:15:31""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTOMATIC_NOTIFICATION: Optional[str] = Field(
        None,
        alias="AUTOMATIC_NOTIFICATION",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXCEMPT: Optional[str] = Field(
        None,
        alias="TAX_EXCEMPT",
        name="",
        description="""Specifies whether to disable any taxes from being applied to the contract_x000D_
Disable - 1, Not disable - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_NUMBER: Optional[str] = Field(
        None,
        alias="TAX_NUMBER",
        name="",
        description="""The supplier?s Tax number, string value, applied only for Supplier, Accomadation and Cruise Line""",
        example="""sDXbdSQDVHBsmhMKoGdZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: Optional[str] = Field(
        None,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANCEL_BEFORE: Optional[str] = Field(
        None,
        alias="CANCEL_BEFORE",
        name="",
        description="""A time string field which defines the exact time on the booking cancellation date, from when the cancellation charges should apply. Default is 12:00.""",
        example="""12:00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHAIN: str = Field(
        ...,
        alias="CHAIN",
        name="",
        description="""A flag indicating the supplier is an accommodation chain ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCALE: Optional[str] = Field(
        None,
        alias="LOCALE",
        name="",
        description="""The TravelBox code of the locale""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_CONCURRENT_USER_COUNT: int = Field(
        ...,
        alias="MAX_CONCURRENT_USER_COUNT",
        name="",
        description="""Deprecated""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEDUP_ORDER: Optional[str] = Field(
        None,
        alias="DEDUP_ORDER",
        name="",
        description="""The deduplication order for the search results. This is stored as a string consist of pipe '|' separated codes in the order of sorting principle of the results.""",
        example="""BizDAcMYfPQFepbFCDZM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENABLE: Optional[str] = Field(
        None,
        alias="ENABLE",
        name="",
        description="""Flag to indicate if the Additional Attribute is enable_x000D_
1 - enable_x000D_
0 - not enable""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2005-11-09 13:54:40""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: int = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=29965,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""AA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IDENTITY: Optional[str] = Field(
        None,
        alias="IDENTITY",
        name="",
        description="""A char to identify whether it is a Supplier profile(S), Accomadation(A), Flight(F), Cruise(C), Rail(R), All(I), Chain Supplier(N). Determined by the TBX panel.""",
        example="""F""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""American Airlines""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS: Optional[str] = Field(
        None,
        alias="ADDRESS",
        name="",
        description="""Address of the credit card holder for credit card batch payment""",
        example="""MBYRrfnvAAuUUlhbwPVL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""OsuaSWcOnKFbLQwBotpV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESORT: Optional[str] = Field(
        None,
        alias="RESORT",
        name="",
        description="""The foreign Key which refers the field CODE of the ACT_ABSORPTION table""",
        example="""okPkwvJyArnXGguHERYp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOURIST_REGION: Optional[str] = Field(
        None,
        alias="TOURIST_REGION",
        name="",
        description="""The TravelBox code of the destination tourist region for which the contract is applicable""",
        example="""XCfLKtDPYFBEEmCvWwHa""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_CODE: Optional[str] = Field(
        None,
        alias="POST_CODE",
        name="",
        description="""Postal code of the credit card holder for credit card batch payment""",
        example="""RuqKCBOfXcjSRxahWdWC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: str = Field(
        ...,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTES: Optional[str] = Field(
        None,
        alias="NOTES",
        name="",
        description="""Notes for the tax invoice""",
        example="""jINDBQyKxXzsfhTCMSPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SCHEME: Optional[int] = Field(
        None,
        alias="PAY_SCHEME",
        name="",
        description="""The TravelBox id of the supplier payment scheme""",
        example=2753,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANCEL_SCHEME: Optional[int] = Field(
        None,
        alias="CANCEL_SCHEME",
        name="",
        description="""The TravelBox id of the supplier cancellation scheme""",
        example=4460,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION: Optional[float] = Field(
        None,
        alias="COMMISSION",
        name="",
        description="""The commission percentage recieved by the tour operator""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTENDED_PERSON: Optional[str] = Field(
        None,
        alias="ATTENDED_PERSON",
        name="",
        description="""Deprecated""",
        example="""vTpVrATIADSagnfpCDrP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EMAIL: Optional[str] = Field(
        None,
        alias="EMAIL",
        name="",
        description="""The email address of the user""",
        example="""dummyEmail@codegen.net""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAX: Optional[str] = Field(
        None,
        alias="FAX",
        name="",
        description="""Fax number associated with the location""",
        example="""otoGJLaxilcJKmDsJHqp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TELEPHONE: Optional[str] = Field(
        None,
        alias="TELEPHONE",
        name="",
        description="""The telephone number of the user""",
        example="""zJFbADGKzmkmlywzaBaY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_CONTACT_METHOD: Optional[str] = Field(
        None,
        alias="DEFAULT_CONTACT_METHOD",
        name="",
        description="""Deprecated""",
        example="""EMAIL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEND_IMMEDIATELY: Optional[str] = Field(
        None,
        alias="SEND_IMMEDIATELY",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WEB_URL: Optional[str] = Field(
        None,
        alias="WEB_URL",
        name="",
        description="""Web site of the Airline  supplier  can be specified_x000D_
for information purposes""",
        example="""sCwMOSsmhvFJlgkIsitb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREFERENCE: Optional[int] = Field(
        None,
        alias="PREFERENCE",
        name="",
        description="""Preference priority of the GDS""",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox SUPPLIER Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:39.106769""",
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
        example="""SUPPLIER""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=34797098210073,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestSupplierModel(BaseModel):
    """
    Payload class for TravelBox SUPPLIER
    """

    class Config:
        """Payload Level Metadata"""

        title = "Pass Through Supplier"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Pass through view of supplier information which contains resorts"""  # optional
        unique_identifier = ["data.SUPPLIER_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "SUPPLIER"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
