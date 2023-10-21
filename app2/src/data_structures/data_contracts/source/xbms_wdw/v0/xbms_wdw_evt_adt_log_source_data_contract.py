"""Source Data Contract for XBMS  EVT_ADT_LOG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EVT_ADT_LOG Data
    """

    EVT_ADT_LOG_ID: int = Field(
        ...,
        alias="EVT_ADT_LOG_ID",
        name="",
        description="",
        example=29915803,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_LOC_TX: str = Field(
        ...,
        alias="EVT_LOC_TX",
        name="",
        description="",
        example="""XBMS.XBANDREQUEST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_REF_ID: str = Field(
        ...,
        alias="EVT_REF_ID",
        name="",
        description="",
        example="""AE435126-2941-4A08-9EB6-572A5A85DFA2""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_TYP_TX: Optional[str] = Field(
        None,
        alias="EVT_TYP_TX",
        name="",
        description="",
        example="""BOOK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_GST_ID: Optional[str] = Field(
        None,
        alias="EVT_GST_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_CORRELATION_ID: str = Field(
        ...,
        alias="EVT_CORRELATION_ID",
        name="",
        description="",
        example="""85574f96-37d8-47da-bf27-ba0f25492788""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_PAYLOAD_TX: Optional[str] = Field(
        None,
        alias="evt_payload_tx",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_TIMESTAMP: datetime = Field(
        ...,
        alias="EVT_TIMESTAMP",
        name="",
        description="",
        example="""1992-08-15 06:07:56""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_PRMY_ACKNWL_SYS_NM: Optional[str] = Field(
        None,
        alias="EVT_PRMY_ACKNWL_SYS_NM",
        name="",
        description="",
        example="""WDPR-WDW.MAGICBAND-STAGE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EVT_SEC_ACKNWL_SYS_NM: Optional[str] = Field(
        None,
        alias="EVT_SEC_ACKNWL_SYS_NM",
        name="",
        description="",
        example="""kerSrBKBGMXdfoVFeVLo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1984-10-21 23:28:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1970-03-21 22:13:28""",
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
    Class for XBMS EVT_ADT_LOG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:47:36.637073""",
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
        example="""EVT_ADT_LOG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=14268615740429,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWEvtAdtLogModel(BaseModel):
    """
    Payload class for XBMS EVT_ADT_LOG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Event Audit Log"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EVT_ADT_LOG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EVT_ADT_LOG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
