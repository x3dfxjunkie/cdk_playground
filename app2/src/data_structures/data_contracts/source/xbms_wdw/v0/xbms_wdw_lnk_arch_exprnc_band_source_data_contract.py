"""Source Data Contract for XBMS  LNK_ARCH_EXPRNC_BAND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS LNK_ARCH_EXPRNC_BAND Data
    """

    LNK_ARCH_EXPRNC_BAND_ID: int = Field(
        ...,
        alias="lnk_arch_exprnc_band_id",
        name="",
        description="",
        example=1000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ID",
        name="",
        description="",
        example=21669438,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARCH_CREATE_DTS: datetime = Field(
        ...,
        alias="ARCH_CREATE_DTS",
        name="",
        description="",
        example="""1974-01-14 07:48:55""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_EXPRNC_BAND_LNK_ID: Optional[int] = Field(
        None,
        alias="CURR_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=12478683,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIG_EXPRNC_BAND_LNK_ID: Optional[int] = Field(
        None,
        alias="ORIG_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=12478683,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS LNK_ARCH_EXPRNC_BAND Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:43:08.197397""",
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
        example="""LNK_ARCH_EXPRNC_BAND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=47838364865697,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWLnkArchExprncBandModel(BaseModel):
    """
    Payload class for XBMS LNK_ARCH_EXPRNC_BAND
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.lnk_arch_exprnc_band_id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LNK_ARCH_EXPRNC_BAND"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
