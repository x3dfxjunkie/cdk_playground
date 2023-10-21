"""Source Data Contract for XBMS  PII_ARCH_ADDR"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PII_ARCH_ADDR Data
    """

    ADDR_ID: int = Field(
        ...,
        alias="ADDR_ID",
        name="",
        description="",
        example=1197636,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_1_TX: Optional[str] = Field(
        None,
        alias="ADDR_1_TX",
        name="",
        description="",
        example="""326 oXiioY fXueiYa eiaYYi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_2_TX: Optional[str] = Field(
        None,
        alias="ADDR_2_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_3_TX: Optional[str] = Field(
        None,
        alias="ADDR_3_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_4_TX: Optional[str] = Field(
        None,
        alias="ADDR_4_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTRY_ID: Optional[int] = Field(
        None,
        alias="CNTRY_ID",
        name="",
        description="",
        example=10374,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_CTY_NM: Optional[str] = Field(
        None,
        alias="ADDR_CTY_NM",
        name="",
        description="",
        example="""Cedartown""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ST_NM: Optional[str] = Field(
        None,
        alias="ADDR_ST_NM",
        name="",
        description="",
        example="""SZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_PSTL_CD: Optional[str] = Field(
        None,
        alias="ADDR_PSTL_CD",
        name="",
        description="",
        example="""82659""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RCPNT_PHN_NB: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_PHN_NB",
        name="",
        description="",
        example="""7705550125""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RCPNT_NM: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_NM",
        name="",
        description="",
        example="""PZBmRFGgulgimckrbAgE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RCPNT_PHN_EXT_NB: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_RCPNT_PHN_EXT_NB",
        name="",
        description="",
        example="""nxyzWxZpgizgChdTqDdf""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: Optional[str] = Field(
        None,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: Optional[datetime] = Field(
        None,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2013-05-01 09:35:42""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1977-10-19 00:40:14""",
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


class Metadata(BaseModel):
    """
    Class for XBMS PII_ARCH_ADDR Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:47:18.414026""",
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
        example="""PII_ARCH_ADDR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=87112476543538,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPiiArchAddrModel(BaseModel):
    """
    Payload class for XBMS PII_ARCH_ADDR
    """

    class Config:
        """Payload Level Metadata"""

        title = "If the magicband is older than 5 years, guest data is removed. After 30 days, the data is purged from the table. Batch process runs everyday."
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.ADDR_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PII_ARCH_ADDR"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
