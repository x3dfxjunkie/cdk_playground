"""Source Data Contract for XBMS  SHIPMT_RCPT_ITEM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS SHIPMT_RCPT_ITEM Data
    """

    SHIPMT_RCPT_ITEM_ID: int = Field(
        ...,
        alias="SHIPMT_RCPT_ITEM_ID",
        name="",
        description="",
        example=501050,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_RCPT_ID: int = Field(
        ...,
        alias="SHIPMT_RCPT_ID",
        name="",
        description="",
        example=502000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_NTC_ID: int = Field(
        ...,
        alias="SHIPMT_NTC_ID",
        name="",
        description="",
        example=529850,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_INVTRY_ITEM_ID: int = Field(
        ...,
        alias="VNDR_INVTRY_ITEM_ID",
        name="",
        description="",
        example=505407,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_PALLET_ID: Optional[int] = Field(
        None,
        alias="SHIPMT_PALLET_ID",
        name="",
        description="",
        example=531850,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_RCPT_ITEM_SEQ_NB: str = Field(
        ...,
        alias="SHIPMT_RCPT_ITEM_SEQ_NB",
        name="",
        description="",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_VNDR_JOB_NB: Optional[str] = Field(
        None,
        alias="FFLMT_VNDR_JOB_NB",
        name="",
        description="",
        example="""67245651006""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_RCPT_ITEM_CN: str = Field(
        ...,
        alias="SHIPMT_RCPT_ITEM_CN",
        name="",
        description="",
        example="""10""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_RCPT_ITEM_DLVR_DT: datetime = Field(
        ...,
        alias="SHIPMT_RCPT_ITEM_DLVR_DT",
        name="",
        description="",
        example="""1990-01-09 05:10:43""",
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
        example="""2003-02-05 12:58:39""",
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
        example="""1978-09-17 08:19:16""",
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

    SAP_UPDT_STS_ID: Optional[int] = Field(
        None,
        alias="SAP_UPDT_STS_ID",
        name="",
        description="",
        example=10003,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MTRL_DOC_NB: Optional[str] = Field(
        None,
        alias="MTRL_DOC_NB",
        name="",
        description="",
        example="""jmhXlYBHujqVsvfSuhik""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS SHIPMT_RCPT_ITEM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:37.106575""",
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
        example="""SHIPMT_RCPT_ITEM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=54912685364645,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWShipmtRcptItemModel(BaseModel):
    """
    Payload class for XBMS SHIPMT_RCPT_ITEM
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.SHIPMT_RCPT_ITEM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "SHIPMT_RCPT_ITEM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
