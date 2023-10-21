"""Source Data Contract for Level-N CNTNT_CACHE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N CNTNT_CACHE Data
    """

    CNTNT_CACHE_ID: int = Field(
        ...,
        alias="CNTNT_CACHE_ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTRPRS_CNTNT_TYP_NM: str = Field(
        ...,
        alias="ENTRPRS_CNTNT_TYP_NM",
        name="",
        description="""""",
        example="""ticket""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTRPRS_CNTNT_ID: str = Field(
        ...,
        alias="ENTRPRS_CNTNT_ID",
        name="",
        description="""""",
        example="""16024628""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTNT_ATTR_NM: str = Field(
        ...,
        alias="CNTNT_ATTR_NM",
        name="",
        description="""""",
        example="""ticket.internalName""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTNT_ATTR_TX: Optional[str] = Field(
        None,
        alias="CNTNT_ATTR_TX",
        name="",
        description="""""",
        example="""Personal Magic""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""admin""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1985-08-22 13:56:57""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""admin""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""1996-11-10 15:14:36""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LGCL_DEL_IN: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N CNTNT_CACHE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:20.664534""",
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
        example="""SFLNSMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""CNTNT_CACHE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=19185019024291,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWCntntCacheModel(BaseModel):
    """
    Payload class for Level N CNTNT_CACHE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Content Cache"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Product information from the content management system."""  # optional
        unique_identifier = ["data.CNTNT_CACHE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CNTNT_CACHE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
