"""Source Data Contract Template for GEN_SUPPLEMENT_CATEGORY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_SUPPLEMENT_CATEGORY Data
    """

    REF_CODE: Optional[str] = Field(
        None,
        alias="REF_CODE",
        name="",
        description="""NaN""",
        example="""37DCA64C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_ID: int = Field(
        ...,
        alias="CATEGORY_ID",
        name="",
        description="""The system generated id of the supplement type""",
        example=1093,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""ePQYHwSCtytrzfiVETyI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""EUyqsYOxvbWwYOviOEFK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_SUPPLEMENT_CATEGORY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:30.388766""",
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
        example="""GEN_SUPPLEMENT_CATEGORY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=30464826828686,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestGenSupplementCategoryModel(BaseModel):
    """
    Payload class for TravelBox GEN_SUPPLEMENT_CATEGORY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic Supplement Category"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Generic Supplement categories list which is used to categorize the supplement of a Generic contract. Setup under 'Supplement Categories' of 'Setup' menu in Generic Loading Client"""  # optional
        unique_identifier = ["data.CATEGORY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_SUPPLEMENT_CATEGORY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
