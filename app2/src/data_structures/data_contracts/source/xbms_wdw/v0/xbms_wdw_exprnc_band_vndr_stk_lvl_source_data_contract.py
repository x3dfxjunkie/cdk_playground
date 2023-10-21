"""Source Data Contract for XBMS  EXPRNC_BAND_VNDR_STK_LVL"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_VNDR_STK_LVL Data
    """

    EXPRNC_BAND_VNDR_STK_LVL_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_VNDR_STK_LVL_ID",
        name="",
        description="",
        example=501550,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_INVTRY_ITEM_ID: int = Field(
        ...,
        alias="VNDR_INVTRY_ITEM_ID",
        name="",
        description="",
        example=505403,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_VNDR_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_VNDR_ID",
        name="",
        description="",
        example=502450,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_ACTL_REORD_PT_CN: int = Field(
        ...,
        alias="VNDR_BAND_ACTL_REORD_PT_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_RCMD_REORD_PT_CN: Optional[int] = Field(
        None,
        alias="VNDR_BAND_RCMD_REORD_PT_CN",
        name="",
        description="",
        example=7623,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_ACTL_SFTY_STK_CN: int = Field(
        ...,
        alias="VNDR_BAND_ACTL_SFTY_STK_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_RCMD_SFTY_STK_CN: Optional[int] = Field(
        None,
        alias="VNDR_BAND_RCMD_SFTY_STK_CN",
        name="",
        description="",
        example=5099,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_ACTL_REORD_QTY_CN: Optional[int] = Field(
        None,
        alias="VNDR_BAND_ACTL_REORD_QTY_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_RCMD_REORD_QTY_CN: Optional[int] = Field(
        None,
        alias="VNDR_BAND_RCMD_REORD_QTY_CN",
        name="",
        description="",
        example=7568,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_AVAIL_FOR_PO_IN: str = Field(
        ...,
        alias="VNDR_BAND_AVAIL_FOR_PO_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""test100.user""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""2009-01-24 13:56:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""test100.user""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2000-07-03 14:38:24""",
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
    Class for XBMS EXPRNC_BAND_VNDR_STK_LVL Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:49:45.926783""",
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
        example="""EXPRNC_BAND_VNDR_STK_LVL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=79462188138201,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandVndrStkLvlModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_VNDR_STK_LVL
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_VNDR_STK_LVL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_VNDR_STK_LVL"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
