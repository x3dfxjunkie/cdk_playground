"""Source Data Contract Template for PKG_SELLABLE_MEMBERSHIP_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PKG_SELLABLE_MEMBERSHIP_TYPE Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1996-12-03 01:27:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_GROUP_ID: int = Field(
        ...,
        alias="PKG_GROUP_ID",
        name="",
        description="""Id of the Package Group associated with the Scheme Rule.""",
        example=14175,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEMBERSHIP_TYPE: int = Field(
        ...,
        alias="MEMBERSHIP_TYPE",
        name="",
        description="""Frequent membership Type associated with the Scheme Rule""",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MEMBERSHIPID: Optional[str] = Field(
        None,
        alias="MEMBERSHIPID",
        name="",
        description="""This refer the field DESCRIPTION of the CLI_FREQ_MEMBER_TYPE""",
        example="""AoLCHqTfsXEkVRcPmMTx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PKG_SELLABLE_MEMBERSHIP_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:17.176162""",
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
        example="""PKG_SELLABLE_MEMBERSHIP_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=84757264167717,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestPkgSellableMembershipTypeModel(BaseModel):
    """
    Payload class for TravelBox PKG_SELLABLE_MEMBERSHIP_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package Sellable Membership Type"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Setup at the Sales Parameters node of the package tree. Membership types for which this package can be
sold are stored"""  # optional
        unique_identifier = [
            "data.PKG_GROUP_ID",
            "data.MEMBERSHIP_TYPE",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_SELLABLE_MEMBERSHIP_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
