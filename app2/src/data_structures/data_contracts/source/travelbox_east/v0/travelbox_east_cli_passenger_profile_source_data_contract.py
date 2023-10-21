"""Source Data Contract Template for CLI_PASSENGER_PROFILE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_PASSENGER_PROFILE Data
    """

    UNAVAILABLE: Optional[str] = Field(
        None,
        alias="UNAVAILABLE",
        name="",
        description="""NaN""",
        example="""vVohndibnyJVSsHgAzBc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_ISSUE_CITY: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_ISSUE_CITY",
        name="",
        description="""Secondary Passport Issued City""",
        example="""ITuWhtIIdCaBEtSbQPlT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_ISSUE_COUNTRY: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_ISSUE_COUNTRY",
        name="",
        description="""Secondary Passport Issued Country""",
        example="""QspWWlcAPNmPendzJMwu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELF_EMPLOYED: Optional[str] = Field(
        None,
        alias="SELF_EMPLOYED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPANY_NAME: Optional[str] = Field(
        None,
        alias="COMPANY_NAME",
        name="",
        description="""Deprecated""",
        example="""ZyGqnLgwDglCdKIdBRlM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOME: Optional[str] = Field(
        None,
        alias="INCOME",
        name="",
        description="""Deprecated""",
        example="""VtARmGqjRtECAaTpomBi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALUTATION: Optional[str] = Field(
        None,
        alias="SALUTATION",
        name="",
        description="""Salutation""",
        example="""GkKJNrPNlMYLRpVXssXH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CTI_REFERENCE: Optional[int] = Field(
        None,
        alias="CTI_REFERENCE",
        name="",
        description="""Deprecated""",
        example=7473,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLUB_MEMBER: str = Field(
        ...,
        alias="CLUB_MEMBER",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_CITIZENSHIP: Optional[str] = Field(
        None,
        alias="PRIMARY_CITIZENSHIP",
        name="",
        description="""Country Code of the primary citizenship country""",
        example="""bScMrUVhBWKGsAsOuyAi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_FIRST_NAME: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_FIRST_NAME",
        name="",
        description="""Secondary Passport First Name""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_LAST_NAME: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_LAST_NAME",
        name="",
        description="""Secondary Passport Last Name""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_FIRST_NAME: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_FIRST_NAME",
        name="",
        description="""Primary Passport First Name""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_LAST_NAME: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_LAST_NAME",
        name="",
        description="""Primary Passport Last Name""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALIEN_REG_NO: Optional[str] = Field(
        None,
        alias="ALIEN_REG_NO",
        name="",
        description="""Deprecated""",
        example="""ObJnoMSJMoGiTKToSIMj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEAT_REQUEST: Optional[str] = Field(
        None,
        alias="SEAT_REQUEST",
        name="",
        description="""Deprecated""",
        example="""bIvPuitGZXWeerIutEyD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEAL_REQUEST: Optional[str] = Field(
        None,
        alias="MEAL_REQUEST",
        name="",
        description="""Deprecated""",
        example="""AkZaCtyEpTXidUxeTVLY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OTHER_REQUEST: Optional[str] = Field(
        None,
        alias="OTHER_REQUEST",
        name="",
        description="""Deprecated""",
        example="""gPyiAflhnunEGdhwQSJJ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_CITIZENSHIP: Optional[str] = Field(
        None,
        alias="SECONDARY_CITIZENSHIP",
        name="",
        description="""Country Code of the secondary citizenship country""",
        example="""iAPRqFqlVRRWUAehkFuT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_ISSUING_OFFICE: Optional[str] = Field(
        None,
        alias="PRIMARY_ISSUING_OFFICE",
        name="",
        description="""Primary Passport Issued Office""",
        example="""MxvBBDYptvjCWxOAzFWP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_ISSUING_OFFICE: Optional[str] = Field(
        None,
        alias="SECONDARY_ISSUING_OFFICE",
        name="",
        description="""Secondary Passport Issued Office""",
        example="""vQoPJSsRLOYKXPxDEWCX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREF_HOLIDAY: Optional[str] = Field(
        None,
        alias="PREF_HOLIDAY",
        name="",
        description="""Deprecated""",
        example="""dLYXsFXpaladeqFuzBQN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREF_DESTINATION: Optional[int] = Field(
        None,
        alias="PREF_DESTINATION",
        name="",
        description="""Deprecated""",
        example=8086,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VISA_OUTPUT: Optional[str] = Field(
        None,
        alias="VISA_OUTPUT",
        name="",
        description="""Deprecated""",
        example="""tsIoxyLBErpOYqxTNqGX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_OF_BIRTH_UNKNOWN: Optional[str] = Field(
        None,
        alias="DATE_OF_BIRTH_UNKNOWN",
        name="",
        description="""Flag to indicate if the passenger's birthday is unknown (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCALE: Optional[str] = Field(
        None,
        alias="LOCALE",
        name="",
        description="""The TravelBox code of the locale""",
        example="""zGzCcvGzGypYBvPnBvdV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USER_SET_DOB: Optional[str] = Field(
        None,
        alias="USER_SET_DOB",
        name="",
        description="""Flag to specify if the user set the Date of Birth (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="MIDDLE_NAME",
        name="",
        description="""Middle Name of the person associated with the contact""",
        example="""JScCaBNLmoXrUWJsKEhN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_MIDDLE_NAME",
        name="",
        description="""Primary Passport Middle Name""",
        example="""cRmmiySxEBnzlGXPEOLa""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_MIDDLE_NAME",
        name="",
        description="""Secondary Passport Middle Name""",
        example="""QIAcMjYcQIKYtkafcWiV""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DUMMYPASENGER: Optional[str] = Field(
        None,
        alias="DUMMYPASENGER",
        name="",
        description="""Flag to indicate if the passenger is a Dummy Passenger (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARE_OF: Optional[str] = Field(
        None,
        alias="CARE_OF",
        name="",
        description="""Deprecated""",
        example="""UsFUCAJsaWGerVuMMaKt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIDE_NNAME: Optional[str] = Field(
        None,
        alias="MAIDE_NNAME",
        name="",
        description="""Deprecated""",
        example="""WCkhcRDXbwsmuAeReLmN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REDRESS_NUMBER: Optional[str] = Field(
        None,
        alias="REDRESS_NUMBER",
        name="",
        description="""Redress Number""",
        example="""CUhOowUOAHWMVhVNWUFC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIDEN_NAME: Optional[str] = Field(
        None,
        alias="MAIDEN_NAME",
        name="",
        description="""Maiden Name""",
        example="""TrnQuBPDQotEGamZWgRM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    KNOWN_TRAVELLER_NUMBER: Optional[str] = Field(
        None,
        alias="KNOWN_TRAVELLER_NUMBER",
        name="",
        description="""Known Traveller Number""",
        example="""OMdGXVzhjtUrtXFPRLWJ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PTOI_INFO: Optional[int] = Field(
        None,
        alias="PTOI_INFO",
        name="",
        description="""NaN""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SANITIZE: str = Field(
        ...,
        alias="SANITIZE",
        name="",
        description="""NaN""",
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
        example="""2007-01-24 19:36:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: int = Field(
        ...,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=492710,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TITLE: str = Field(
        ...,
        alias="TITLE",
        name="",
        description="""The title of the accommodation image""",
        example="""Mstr.""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NAME: str = Field(
        ...,
        alias="FIRST_NAME",
        name="",
        description="""First Name of the person associated with the contact""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_NAME: str = Field(
        ...,
        alias="LAST_NAME",
        name="",
        description="""Last Name of the person associated with the contact""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_OF_BIRTH: Optional[datetime] = Field(
        None,
        alias="DATE_OF_BIRTH",
        name="",
        description="""Date of Birth""",
        example="""1972-12-16 18:20:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEX: Optional[str] = Field(
        None,
        alias="SEX",
        name="",
        description="""Sex of the user  M or F_x000D_
""",
        example="""M""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: Optional[str] = Field(
        None,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example="""N/A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFESSION: Optional[str] = Field(
        None,
        alias="PROFESSION",
        name="",
        description="""Deprecated""",
        example="""nsnkdNRVYtGDyPvSnKjm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MARITAL_STATUS: Optional[int] = Field(
        None,
        alias="MARITAL_STATUS",
        name="",
        description="""Flag to specify the marital status""",
        example=2073,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SMOKER: Optional[str] = Field(
        None,
        alias="SMOKER",
        name="",
        description="""Flag to specify if the passenger is a smoker (1) or not (0)""",
        example="""yEYNKoyljUZJIhMSogzv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITIZANSHIP1: Optional[str] = Field(
        None,
        alias="CITIZANSHIP1",
        name="",
        description="""Deprecated""",
        example="""iYsakyAFQFCBgWLCgeiR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITIZENSHIP2: Optional[str] = Field(
        None,
        alias="CITIZENSHIP2",
        name="",
        description="""Deprecated""",
        example="""hXpqZywPKApsecMeEKQt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_NO: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_NO",
        name="",
        description="""Primary Passport Number""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_ISUE_DATE: Optional[datetime] = Field(
        None,
        alias="PRIMARY_PP_ISUE_DATE",
        name="",
        description="""Primary Passport Issued Date""",
        example="""2009-09-12 10:56:28""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_EXP_DATE: Optional[datetime] = Field(
        None,
        alias="PRIMARY_PP_EXP_DATE",
        name="",
        description="""Primary Passport Expiry Date""",
        example="""2009-09-08 22:07:56""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_ISSUE_CITY: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_ISSUE_CITY",
        name="",
        description="""Primary Passport Issued City""",
        example="""UqtscISdfzmymBepgpoX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_ISSUE_COUNTRY: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_ISSUE_COUNTRY",
        name="",
        description="""Primary Passport Issued Country""",
        example="""mrpYglATkYPdHxjkOCYZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_NO: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_NO",
        name="",
        description="""Secondary Passport Number""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_ISSUE_DATE: Optional[datetime] = Field(
        None,
        alias="SECONDARY_PP_ISSUE_DATE",
        name="",
        description="""Secondary Passport Issued Date""",
        example="""1998-04-24 22:36:53""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_EXP_DATE: Optional[datetime] = Field(
        None,
        alias="SECONDARY_PP_EXP_DATE",
        name="",
        description="""Secondary Passport Expiry Date""",
        example="""2001-06-20 17:23:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_PASSENGER_PROFILE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:50.003057""",
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
        example="""CLI_PASSENGER_PROFILE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=13505057841118,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliPassengerProfileModel(BaseModel):
    """
    Payload class for TravelBox CLI_PASSENGER_PROFILE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Passenger Profile"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Guest profiles including PI"""  # optional
        unique_identifier = ["data.PROFILE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_PASSENGER_PROFILE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
