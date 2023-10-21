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
        example="""aFfcjcVDipDIAzGOAHLG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIDE_NNAME: Optional[str] = Field(
        None,
        alias="MAIDE_NNAME",
        name="",
        description="""Deprecated""",
        example="""VEtjvHDtYgGobqXBazRz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REDRESS_NUMBER: Optional[str] = Field(
        None,
        alias="REDRESS_NUMBER",
        name="",
        description="""Redress Number""",
        example="""agZXDfULGqPiODgBngJP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIDEN_NAME: Optional[str] = Field(
        None,
        alias="MAIDEN_NAME",
        name="",
        description="""Maiden Name""",
        example="""wrtVNQJVnshFURHoxwpv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    KNOWN_TRAVELLER_NUMBER: Optional[str] = Field(
        None,
        alias="KNOWN_TRAVELLER_NUMBER",
        name="",
        description="""Known Traveller Number""",
        example="""nUcpcCMbyxXCBMTQaeYH""",
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

    PROFILE_ID: int = Field(
        ...,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=29191,
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
        example="""2000-05-11 05:20:03""",
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
        example="""LaxjRnIAWDynJbMZrPRG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MARITAL_STATUS: Optional[int] = Field(
        None,
        alias="MARITAL_STATUS",
        name="",
        description="""Flag to specify the marital status""",
        example=6589,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SMOKER: Optional[str] = Field(
        None,
        alias="SMOKER",
        name="",
        description="""Flag to specify if the passenger is a smoker (1) or not (0)""",
        example="""YtCCknwROAjoSOuygBHo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITIZANSHIP1: Optional[str] = Field(
        None,
        alias="CITIZANSHIP1",
        name="",
        description="""Deprecated""",
        example="""GtymWvWlSKhhUxlPFDcz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITIZENSHIP2: Optional[str] = Field(
        None,
        alias="CITIZENSHIP2",
        name="",
        description="""Deprecated""",
        example="""iwmnIeuePehNAlvhDozB""",
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
        example="""1986-01-06 23:15:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_EXP_DATE: Optional[datetime] = Field(
        None,
        alias="PRIMARY_PP_EXP_DATE",
        name="",
        description="""Primary Passport Expiry Date""",
        example="""1989-01-31 00:13:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_ISSUE_CITY: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_ISSUE_CITY",
        name="",
        description="""Primary Passport Issued City""",
        example="""UTcLfLuOveGgqbIHkQDG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_ISSUE_COUNTRY: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_ISSUE_COUNTRY",
        name="",
        description="""Primary Passport Issued Country""",
        example="""OkNViYevuTnNDNhWrnyd""",
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
        example="""1988-09-22 00:52:07""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_EXP_DATE: Optional[datetime] = Field(
        None,
        alias="SECONDARY_PP_EXP_DATE",
        name="",
        description="""Secondary Passport Expiry Date""",
        example="""2000-10-20 06:26:25""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_ISSUE_CITY: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_ISSUE_CITY",
        name="",
        description="""Secondary Passport Issued City""",
        example="""axcoahPrOAeqKOvxHHGm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_ISSUE_COUNTRY: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_ISSUE_COUNTRY",
        name="",
        description="""Secondary Passport Issued Country""",
        example="""MXFyHzwCkGuRcCzFneSa""",
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
        example="""jQfnzabevCsbCmaTKfPq""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOME: Optional[str] = Field(
        None,
        alias="INCOME",
        name="",
        description="""Deprecated""",
        example="""hdlLpnJKLkQiJUpnXKhF""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALUTATION: Optional[str] = Field(
        None,
        alias="SALUTATION",
        name="",
        description="""Salutation""",
        example="""lpHxcPeKMLeJbLBkOaFt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CTI_REFERENCE: Optional[int] = Field(
        None,
        alias="CTI_REFERENCE",
        name="",
        description="""Deprecated""",
        example=1614,
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
        example="""TqxmXTQGWNnTsQYxEdBj""",
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
        example="""flskVaEvdhhLLlvROYtw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEAT_REQUEST: Optional[str] = Field(
        None,
        alias="SEAT_REQUEST",
        name="",
        description="""Deprecated""",
        example="""qYVyRQYuvVUWHjWZQeaw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEAL_REQUEST: Optional[str] = Field(
        None,
        alias="MEAL_REQUEST",
        name="",
        description="""Deprecated""",
        example="""iMlMbAGxdCFXsZkXJrmw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OTHER_REQUEST: Optional[str] = Field(
        None,
        alias="OTHER_REQUEST",
        name="",
        description="""Deprecated""",
        example="""ClOkrpddfJjnkBFFoEpd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_CITIZENSHIP: Optional[str] = Field(
        None,
        alias="SECONDARY_CITIZENSHIP",
        name="",
        description="""Country Code of the secondary citizenship country""",
        example="""xypNRwDGShQDZxdThEvD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_ISSUING_OFFICE: Optional[str] = Field(
        None,
        alias="PRIMARY_ISSUING_OFFICE",
        name="",
        description="""Primary Passport Issued Office""",
        example="""aKRrHDeTNIdcWmzRTuMp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_ISSUING_OFFICE: Optional[str] = Field(
        None,
        alias="SECONDARY_ISSUING_OFFICE",
        name="",
        description="""Secondary Passport Issued Office""",
        example="""ZNihaACxcYsnAtecQSrZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREF_HOLIDAY: Optional[str] = Field(
        None,
        alias="PREF_HOLIDAY",
        name="",
        description="""Deprecated""",
        example="""ZiFafVnXCvvpkrsHGBtd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREF_DESTINATION: Optional[int] = Field(
        None,
        alias="PREF_DESTINATION",
        name="",
        description="""Deprecated""",
        example=1694,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VISA_OUTPUT: Optional[str] = Field(
        None,
        alias="VISA_OUTPUT",
        name="",
        description="""Deprecated""",
        example="""WhhJBGDdpMGktnNiIRGM""",
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
        example="""vhreBALhprjWJIXWvylv""",
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
        example="""GJwJxvmHEzJRjcWQAoUk""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRIMARY_PP_MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="PRIMARY_PP_MIDDLE_NAME",
        name="",
        description="""Primary Passport Middle Name""",
        example="""uDPuFYOScuMAlbNsNwCT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECONDARY_PP_MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="SECONDARY_PP_MIDDLE_NAME",
        name="",
        description="""Secondary Passport Middle Name""",
        example="""UjjPnBCViysnJRhjgxiw""",
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
        example="""reVYzhGVVxrYHCvnLDRO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1980-06-07 13:48:23""",
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
        example="""2023-08-16 09:42:30.613078""",
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
        example=92646681613482,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliPassengerProfileModel(BaseModel):
    """
    Payload class for TravelBox CLI_PASSENGER_PROFILE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Passenger Profile"
        stream_name = "prd-use1-guest360-tbxw-stream"
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
