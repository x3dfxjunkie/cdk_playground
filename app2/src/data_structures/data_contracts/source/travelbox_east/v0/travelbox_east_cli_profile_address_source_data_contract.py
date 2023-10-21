"""Source Data Contract Template for CLI_PROFILE_ADDRESS"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_PROFILE_ADDRESS Data
    """

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1984-12-07 03:22:25""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: int = Field(
        ...,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=848629,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS_NO: int = Field(
        ...,
        alias="ADDRESS_NO",
        name="",
        description="""Address no of the airline""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STREET: Optional[str] = Field(
        None,
        alias="STREET",
        name="",
        description="""Street of the address associated with the contact""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTY: Optional[str] = Field(
        None,
        alias="COUNTY",
        name="",
        description="""Code of the county""",
        example="""HAcAybjyxTsOJcSfnlTj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POSTAL_CODE: Optional[str] = Field(
        None,
        alias="POSTAL_CODE",
        name="",
        description="""Postal code of the address associated with the contact""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: str = Field(
        ...,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIN: str = Field(
        ...,
        alias="MAIN",
        name="",
        description="""Flag to indicate of the address is the main address of the Client (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOUSE_NO: Optional[str] = Field(
        None,
        alias="HOUSE_NO",
        name="",
        description="""House number of the credit card holder for credit card batch payment""",
        example="""XXXXXXXXXX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS_TYPE: Optional[int] = Field(
        None,
        alias="ADDRESS_TYPE",
        name="",
        description="""Deprecated""",
        example=4527,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_CATEGORY: Optional[int] = Field(
        None,
        alias="CONTACT_CATEGORY",
        name="",
        description="""Id of the contact category associated with the Address""",
        example=1897,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_PROFILE_ADDRESS Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:57.486685""",
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
        example="""CLI_PROFILE_ADDRESS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=39933955380125,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliProfileAddressModel(BaseModel):
    """
    Payload class for TravelBox CLI_PROFILE_ADDRESS
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Profile Address"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is to store profile address information that associated with a Direct Client or a Travel Agent.
Profile address are setup in Direct Client, Additional Panel and in Travel Agent, Contacts Panel"""  # optional
        unique_identifier = ["data.PROFILE_ID", "data.ADDRESS_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_PROFILE_ADDRESS"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
