"""Source Data Contract for XBMS  ARCH_EXPRNC_BAND_LNK_LNK"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS ARCH_EXPRNC_BAND_LNK_LNK Data
    """

    EXPRNC_BAND_LNK_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_LNK_ID",
        name="",
        description="",
        example=537132,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRMY_EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="PRMY_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=1348347,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRR_EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="PRR_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=1348348,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LNK_RSN_TX: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_LNK_RSN_TX",
        name="",
        description="",
        example="""zZwTlqJDDempkmfmOLYA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""{70CD9445-C26D-4B93-9050-9855BAC1835A}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2020-05-11 06:55:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""{70CD9445-C26D-4B93-9050-9855BAC1835A}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2001-03-19 12:46:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGICAL_DEL_IN: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ARCHIVED_DTS: datetime = Field(
        ...,
        alias="ARCHIVED_DTS",
        name="",
        description="",
        example="""2008-08-30 04:14:36""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS ARCH_EXPRNC_BAND_LNK_LNK Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:55.851000""",
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
        example="""ARCH_EXPRNC_BAND_LNK_LNK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=40191113506373,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWArchExprncBandLnkLnkModel(BaseModel):
    """
    Payload class for XBMS ARCH_EXPRNC_BAND_LNK_LNK
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_LNK_LNK_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ARCH_EXPRNC_BAND_LNK_LNK"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
