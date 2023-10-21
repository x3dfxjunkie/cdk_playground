"""Source Data Contract Template for ADM_USER"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ADM_USER Data
    """

    CREATED_TIME: Optional[datetime] = Field(
        None,
        alias="CREATED_TIME",
        name="",
        description="""NaN""",
        example="""1999-09-18 18:05:42""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_USER: Optional[int] = Field(
        None,
        alias="CREATED_USER",
        name="",
        description="""Task created user""",
        example=8971,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_USER: Optional[int] = Field(
        None,
        alias="LAST_MODIFIED_USER",
        name="",
        description="""Queue record last modified user""",
        example=2640,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2017-01-17 08:28:29""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTES: Optional[str] = Field(
        None,
        alias="NOTES",
        name="",
        description="""Notes for the tax invoice""",
        example="""jXKQeYUPzSpwMUBCKiQQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATED_BY_AGENT: str = Field(
        ...,
        alias="CREATED_BY_AGENT",
        name="",
        description="""A flag to indicate whether user was created from TravelBox Agent or OTA flow. 1 for TravelBox Agent and 0 for OTA.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USER_ID: int = Field(
        ...,
        alias="USER_ID",
        name="",
        description="""Deprecated""",
        example=15120,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USERNAME: str = Field(
        ...,
        alias="USERNAME",
        name="",
        description="""The username of the user""",
        example="""seubm001""",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSWORD: str = Field(
        ...,
        alias="PASSWORD",
        name="",
        description="""Hashed value of the user's password""",
        example="""geJ1cqatBnR7zkNHPsNeVe8""",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRSTNAME: Optional[str] = Field(
        None,
        alias="FIRSTNAME",
        name="",
        description="""The first name of the user""",
        example="""Marielos""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LASTNAME: Optional[str] = Field(
        None,
        alias="LASTNAME",
        name="",
        description="""The last name of the user""",
        example="""Seubert""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INITIALS: Optional[str] = Field(
        None,
        alias="INITIALS",
        name="",
        description="""The initials of the user""",
        example="""mxs""",
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
        example="""F""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOB: Optional[datetime] = Field(
        None,
        alias="DOB",
        name="",
        description="""The date of birth of the user""",
        example="""2011-03-21 04:03:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGINS: Optional[int] = Field(
        None,
        alias="LOGINS",
        name="",
        description="""Maximum allowed number of simultaneous logins for the user account""",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_PREFERENCE: Optional[str] = Field(
        None,
        alias="AGENT_PREFERENCE",
        name="",
        description="""Deprecated""",
        example="""IFDcIkSqNpZWwAUFLmXR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TELEPHONE: Optional[str] = Field(
        None,
        alias="TELEPHONE",
        name="",
        description="""The telephone number of the user""",
        example="""tiAUoFLiHAXpDniSwdnA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EMAIL: Optional[str] = Field(
        None,
        alias="EMAIL",
        name="",
        description="""The email address of the user""",
        example="""dummyEmail@codegen.net""",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTENSION: Optional[str] = Field(
        None,
        alias="EXTENSION",
        name="",
        description="""Telephone extension of the user""",
        example="""xqLsucXOaVhmsKjUAZAj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: Optional[str] = Field(
        None,
        alias="STATUS",
        name="",
        description="""The TravelBox code of the status of the contract""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISPLAY_NAME: Optional[str] = Field(
        None,
        alias="DISPLAY_NAME",
        name="",
        description="""The name which will be displayed to other users""",
        example="""Marielos""",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    QUESTION_ID: Optional[int] = Field(
        None,
        alias="QUESTION_ID",
        name="",
        description="""Id of the Security question""",
        example=281,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANSWER: Optional[str] = Field(
        None,
        alias="ANSWER",
        name="",
        description="""Hashed value of the user's security question answer""",
        example="""mCSJs2U5OnLvZlCE+WfdMcrVi2s=""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PWD_CHANGE_DATE: Optional[datetime] = Field(
        None,
        alias="PWD_CHANGE_DATE",
        name="",
        description="""Changed date of the last password""",
        example="""2017-03-03 07:21:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_PASSWORD: Optional[str] = Field(
        None,
        alias="DEFAULT_PASSWORD",
        name="",
        description="""Whether the user use default password or not""",
        example="""0""",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_ANSWER: Optional[str] = Field(
        None,
        alias="DEFAULT_ANSWER",
        name="",
        description="""Whether the user use default security question answer or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_CURRENCY: Optional[str] = Field(
        None,
        alias="DEFAULT_CURRENCY",
        name="",
        description="""Default currency code of the user""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_DIV: Optional[str] = Field(
        None,
        alias="DEFAULT_DIV",
        name="",
        description="""Default division code of the user""",
        example="""WDTCDLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_COM: Optional[str] = Field(
        None,
        alias="DEFAULT_COM",
        name="",
        description="""Default company code of the user""",
        example="""WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_INITIALS: Optional[str] = Field(
        None,
        alias="AGENT_INITIALS",
        name="",
        description="""Deprecated""",
        example="""ekmpzbofyJoQmKMafxDh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGENT_SIGN: Optional[str] = Field(
        None,
        alias="AGENT_SIGN",
        name="",
        description="""Deprecated""",
        example="""wUwTeipOwgLscNHEWYRW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PSUDO_CITY: Optional[str] = Field(
        None,
        alias="PSUDO_CITY",
        name="",
        description="""Deprecated""",
        example="""KmzSrbgIpoKydIrHcjEl""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    B2B_USER: str = Field(
        ...,
        alias="B2B_USER",
        name="",
        description="""whether the user is B2B user or not : 1 or 0 value""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ADM_USER Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:09.233084""",
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
        example="""ADM_USER""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=21933342532392,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAdmUserModel(BaseModel):
    """
    Payload class for TravelBox ADM_USER
    """

    class Config:
        """Payload Level Metadata"""

        title = "User Profiles"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """User profiles for the cast members using Travelbox"""  # optional
        unique_identifier = ["data.USER_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ADM_USER"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
