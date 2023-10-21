"""Source Data Contract for Level-N INBOUND_REST_RESP_LOG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N INBOUND_REST_RESP_LOG Data
    """

    CORRELATION_ID: str = Field(
        ...,
        alias="CORRELATION_ID",
        name="",
        description="""""",
        example="""dc55c52f-d733-49b4-b8d0-822b5051a3a0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESP_TIMESTAMP: datetime = Field(
        ...,
        alias="RESP_TIMESTAMP",
        name="",
        description="""""",
        example="""2016-07-13 19:47:12""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESP_CD: int = Field(
        ...,
        alias="RESP_CD",
        name="",
        description="""""",
        example=200,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESP_ERR_CD: Optional[int] = Field(
        None,
        alias="RESP_ERR_CD",
        name="",
        description="""""",
        example=5074,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESP_BODY: Optional[str] = Field(
        None,
        alias="RESP_BODY",
        name="",
        description="""""",
        example="""{"entitlementId":"21300024012307692","alternateEntitlementIdentifiers":[{"value":"012423-BTI-000-07692","type":"TDSSN"},{"value":"NFGGZLELJQHMR9KSU2","type":"BARCODE"},{"value":"39174336583109483679","type":"BARCODE"},{"value":" CT1FF3C4FTCBF23M9CTB0FFCLFT2BFKZMCC0FF1F0L7TC2FKZMC0TBF62CLFTCBFKZMC0TB ","type":"MAGCODE"}],"productCode":"WHE63","productName":"MEM MAKER 1D  MOBILE","redemptionPoint":"MM101AM011","bioRequired":false,"simulateBio":false,"newEnrollmentRequired":false,"decremented":false,"biometricCheckLevel":1,"isFirstUsageAtLocation":true,"guestName":"JOSHUA","usages":[],"childFlag":false,"securityNotes":[],"resultCode":"001","resultDescription":"OK","entitlementNotes":[],"lastUsage":{"usageDate":null,"usageTime":null},"performance":{"performanceStartTime":"2023-01-24T03:00:00.000","performanceEndTime":"2023-01-25T03:00:00.000","eventCode":"EVT-MMMM","eventName":"MM+ Mem Maker"}}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_1: Optional[str] = Field(
        None,
        alias="PL_HLD_1",
        name="",
        description="""""",
        example="""zClmraUCbIMjJOKQaNHj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_2: Optional[str] = Field(
        None,
        alias="PL_HLD_2",
        name="",
        description="""""",
        example="""JpGJDWmqbgmjTfgFEfUk""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PL_HLD_3: Optional[str] = Field(
        None,
        alias="PL_HLD_3",
        name="",
        description="""""",
        example="""dZArzGPSmctIGyspOGfP""",
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
        example="""2023-08-03 18:18:53""",
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
        example="""2008-12-08 04:08:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N INBOUND_REST_RESP_LOG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:50.062773""",
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
        example="""INBOUND_REST_RESP_LOG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=31020813116196,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWInboundRestRespLogModel(BaseModel):
    """
    Payload class for Level N INBOUND_REST_RESP_LOG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Inbound Rest Response Log"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Log table that captures API responses from Level N to external systems."""  # optional
        unique_identifier = ["data.RESP_TIMESTAMP", "data.CORRELATION_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "INBOUND_REST_RESP_LOG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
