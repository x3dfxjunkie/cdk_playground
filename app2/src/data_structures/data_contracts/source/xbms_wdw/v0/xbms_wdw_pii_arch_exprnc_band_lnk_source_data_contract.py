"""Source Data Contract for XBMS  PII_ARCH_EXPRNC_BAND_LNK"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PII_ARCH_EXPRNC_BAND_LNK Data
    """

    EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_PRFL_FRST_NM: Optional[str] = Field(
        None,
        alias="GST_PRFL_FRST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_PRFL_LST_NM: Optional[str] = Field(
        None,
        alias="GST_PRFL_LST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: Optional[str] = Field(
        None,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: Optional[datetime] = Field(
        None,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2018-10-01 14:45:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2021-01-17 20:23:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGICAL_DEL_IN: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS PII_ARCH_EXPRNC_BAND_LNK Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:45:54.260436""",
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
        example="""PII_ARCH_EXPRNC_BAND_LNK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=50930435048923,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPiiArchExprncBandLnkModel(BaseModel):
    """
    Payload class for XBMS PII_ARCH_EXPRNC_BAND_LNK
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_LNK_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PII_ARCH_EXPRNC_BAND_LNK"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
