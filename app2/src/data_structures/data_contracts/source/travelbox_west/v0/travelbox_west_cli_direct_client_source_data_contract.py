"""Source Data Contract Template for CLI_DIRECT_CLIENT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_DIRECT_CLIENT Data
    """

    EXCLUDE_ARCHIVING: str = Field(
        ...,
        alias="EXCLUDE_ARCHIVING",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=15073,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_ID: int = Field(
        ...,
        alias="PROFILE_ID",
        name="",
        description="""The system  generated id of the H2H profile""",
        example=32700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRADE: Optional[int] = Field(
        None,
        alias="GRADE",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DO_NOT_CONTACT: str = Field(
        ...,
        alias="DO_NOT_CONTACT",
        name="",
        description="""Flag to indicate if the direct client is Excluded from E-mailings_x000D_
1 - Excluded_x000D_
0 - Not Excluded""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOC_USER_ID: Optional[int] = Field(
        None,
        alias="ALLOC_USER_ID",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXCLUDE_FROM_MAILINGS: str = Field(
        ...,
        alias="EXCLUDE_FROM_MAILINGS",
        name="",
        description="""Flag to indicate if the direct client is Excluded from Mailings_x000D_
1 - Excluded_x000D_
0 - Not Excluded""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VIP: Optional[str] = Field(
        None,
        alias="VIP",
        name="",
        description="""Flag to indicate if the client is VIP (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_ALLOWED: Optional[str] = Field(
        None,
        alias="SALES_ALLOWED",
        name="",
        description="""Flag to indicate if sales are allowed for the specific client (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOCUMENTS_ALLOWED: Optional[str] = Field(
        None,
        alias="DOCUMENTS_ALLOWED",
        name="",
        description="""Flag to indicate if documents are allowed for the specific client (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXCLUDE_PARTNER_EMAILING: str = Field(
        ...,
        alias="EXCLUDE_PARTNER_EMAILING",
        name="",
        description="""Flag to indicate if the direct client is Excluded from Partner E-mailings_x000D_
1 - Excluded_x000D_
0 - Not Excluded""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE_ID: Optional[int] = Field(
        None,
        alias="TYPE_ID",
        name="",
        description="""The TravelBox id of the generic product type for which the scheme is applicable""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1995-07-05 06:22:10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_DIRECT_CLIENT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:13.389155""",
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
        example="""CLI_DIRECT_CLIENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=42020157117828,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliDirectClientModel(BaseModel):
    """
    Payload class for TravelBox CLI_DIRECT_CLIENT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Direct Client"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store information associated with a Direct Client"""  # optional
        unique_identifier = ["data.CLIENT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_DIRECT_CLIENT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
