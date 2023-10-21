"""Source Data Contract for XBMS  RES"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS RES Data
    """

    RES_ID: int = Field(
        ...,
        alias="RES_ID",
        name="",
        description="",
        example=708400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TXN_SRC_SYS_NATIVE_ID: str = Field(
        ...,
        alias="TXN_SRC_SYS_NATIVE_ID",
        name="",
        description="",
        example="""442514120667""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_BEGIN_DT: Optional[datetime] = Field(
        None,
        alias="RES_BEGIN_DT",
        name="",
        description="",
        example="""1973-11-22 04:52:48""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ID: Optional[int] = Field(
        None,
        alias="ADDR_ID",
        name="",
        description="",
        example=725550,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RES_UPDT_DT: datetime = Field(
        ...,
        alias="RES_UPDT_DT",
        name="",
        description="",
        example="""1996-07-24 05:10:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1997-03-18 00:34:58""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1996-11-26 14:15:23""",
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

    TXN_SRC_SYS_TX: Optional[str] = Field(
        None,
        alias="TXN_SRC_SYS_TX",
        name="",
        description="",
        example="""travel-plan-id""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALT_TXN_SRC_SYS_ID: Optional[str] = Field(
        None,
        alias="ALT_TXN_SRC_SYS_ID",
        name="",
        description="",
        example="""LWcEEobGCbFAwzJflKho""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALT_TXN_SRC_SYS_TX: Optional[str] = Field(
        None,
        alias="ALT_TXN_SRC_SYS_TX",
        name="",
        description="",
        example="""zfWESdxHhUTGfMiPIiAI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BEGIN_DT: Optional[datetime] = Field(
        None,
        alias="EXPRNC_BEGIN_DT",
        name="",
        description="",
        example="""1985-06-24 14:40:04""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FRST_DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="FRST_DSNY_FAC_ID",
        name="",
        description="",
        example=503279,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FRST_TRVL_PLAN_SEG_ID: Optional[str] = Field(
        None,
        alias="FRST_TRVL_PLAN_SEG_ID",
        name="",
        description="",
        example="""442511722766""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FRST_TRVL_CMPNT_ID: Optional[str] = Field(
        None,
        alias="FRST_TRVL_CMPNT_ID",
        name="",
        description="",
        example="""837396349""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FRST_GRP_MST_REC_TM_ID: Optional[int] = Field(
        None,
        alias="FRST_GRP_MST_REC_TM_ID",
        name="",
        description="",
        example=5826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS RES Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:05.385382""",
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
        example="""RES""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=43581434277208,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWResModel(BaseModel):
    """
    Payload class for XBMS RES
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.RES_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
