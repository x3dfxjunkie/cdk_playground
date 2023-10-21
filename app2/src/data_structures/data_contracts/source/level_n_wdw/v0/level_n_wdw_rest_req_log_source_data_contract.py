"""Source Data Contract for Level-N REST_REQ_LOG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N REST_REQ_LOG Data
    """

    CORRELATION_ID: str = Field(
        ...,
        alias="CORRELATION_ID",
        name="",
        description="""""",
        example="""00917cbf-9186-4aab-8f8d-9d25323f121a""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REQ_TIMESTAMP_ID: datetime = Field(
        ...,
        alias="REQ_TIMESTAMP_ID",
        name="",
        description="""""",
        example="""1973-02-05 14:07:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REQ_URL: str = Field(
        ...,
        alias="REQ_URL",
        name="",
        description="""""",
        example="""https://stage.leveln.wdprapps.disney.com/nge-leveln/b2b/assign-level-n-entitlement-guest""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REQ_BODY: Optional[str] = Field(
        None,
        alias="REQ_BODY",
        name="",
        description="""""",
        example="""{"entitlement-id-type":"leveln-entitlement-id","entitlement-id-value":"6919662","active-guest":"guest/id;swid={1BCDE2B0-7A78-40C0-A507-6C6F85D2BCB8}/profile","level-n-guest":"2C9180828753376901875657C4B7160B"}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CST_ID: Optional[str] = Field(
        None,
        alias="CST_ID",
        name="",
        description="""""",
        example="""""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_ID: Optional[str] = Field(
        None,
        alias="GST_ID",
        name="",
        description="""""",
        example="""""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CIP: Optional[str] = Field(
        None,
        alias="CIP",
        name="",
        description="""""",
        example="""""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SYS_ID: Optional[str] = Field(
        None,
        alias="SYS_ID",
        name="",
        description="""""",
        example="""""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORGN_SYS_ID: Optional[str] = Field(
        None,
        alias="ORGN_SYS_ID",
        name="",
        description="""""",
        example="""""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REQ_TYP: str = Field(
        ...,
        alias="REQ_TYP",
        name="",
        description="""""",
        example="""POST""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SWID: Optional[str] = Field(
        None,
        alias="SWID",
        name="",
        description="""""",
        example="""{1BCDE2B0-7A78-40C0-A507-6C6F85D2BCB8}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_1: Optional[str] = Field(
        None,
        alias="PL_HLD_1",
        name="",
        description="""""",
        example="""IZLakKoaUjxqmOTQexNR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_2: Optional[str] = Field(
        None,
        alias="PL_HLD_2",
        name="",
        description="""""",
        example="""QnwLHzVvVabEZsLVgoGM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_3: Optional[str] = Field(
        None,
        alias="PL_HLD_3",
        name="",
        description="""""",
        example="""PockWjJkamRjKTzOPXCj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1977-04-08 04:53:03""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2009-01-27 03:53:56""",
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
    Class for Level N REST_REQ_LOG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:31.551260""",
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
        example="""REST_REQ_LOG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=48239097955014,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWRestReqLogModel(BaseModel):
    """
    Payload class for Level N REST_REQ_LOG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Rest Request Log"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Log table for Level N that tracks Restful requests to Level N API."""  # optional
        unique_identifier = ["data.CORRELATION_ID", "data.REQ_TIMESTAMP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "REST_REQ_LOG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
