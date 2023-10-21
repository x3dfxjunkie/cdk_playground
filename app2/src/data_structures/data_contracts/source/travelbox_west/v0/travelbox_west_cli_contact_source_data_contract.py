"""Source Data Contract Template for CLI_CONTACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_CONTACT Data
    """

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=12379,
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

    CONTACT_NO: int = Field(
        ...,
        alias="CONTACT_NO",
        name="",
        description="""System generated index of the Contact""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_NUMBER_TYPE: str = Field(
        ...,
        alias="CONTACT_NUMBER_TYPE",
        name="",
        description="""Contact Number Type""",
        example="""E-mail""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALUE: Optional[str] = Field(
        None,
        alias="VALUE",
        name="",
        description="""The amount/percentage value of the variation""",
        example="""ZuuIkJRoCrdptnuOuefS""",
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

    PREFFERED: str = Field(
        ...,
        alias="PREFFERED",
        name="",
        description="""Flag to indicate if the Contact is the prefered one for the Address (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2006-04-18 06:03:19""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_CONTACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:47:40.167155""",
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
        example="""CLI_CONTACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=31579476390356,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliContactModel(BaseModel):
    """
    Payload class for TravelBox CLI_CONTACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Contact"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store contact information of a client"""  # optional
        unique_identifier = ["data.CLIENT_ID", "data.ADDRESS_NO", "data.CONTACT_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_CONTACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
