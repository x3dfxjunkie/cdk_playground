"""Source Data Contract for XBMS  LNK_ARCH_RES_GST"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS LNK_ARCH_RES_GST Data
    """

    RES_GST_ARCHIVE_ID: int = Field(
        ...,
        alias="RES_GST_ARCHIVE_ID",
        name="",
        description="",
        example=1000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_ID: int = Field(
        ...,
        alias="GST_ID",
        name="",
        description="",
        example=1222961,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=1276717,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_ID: Optional[int] = Field(
        None,
        alias="RES_ID",
        name="",
        description="",
        example=811,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2022-01-20 17:30:05""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARCHIVE_CREATE_DTS: datetime = Field(
        ...,
        alias="ARCHIVE_CREATE_DTS",
        name="",
        description="",
        example="""1987-09-10 02:14:12""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS LNK_ARCH_RES_GST Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:54.169395""",
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
        example="""XBANDMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""LNK_ARCH_RES_GST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=74391815458573,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWLnkArchResGstModel(BaseModel):
    """
    Payload class for XBMS LNK_ARCH_RES_GST
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.RES_GST_ARCHIVE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LNK_ARCH_RES_GST"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
