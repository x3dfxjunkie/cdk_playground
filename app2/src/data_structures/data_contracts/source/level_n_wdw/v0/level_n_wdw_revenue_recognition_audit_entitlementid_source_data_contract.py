"""Source Data Contract for Level-N REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID Data
    """

    ENTITLEMENTID: int = Field(
        ...,
        alias="entitlementId",
        name="",
        description="""""",
        example=7083862,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTIONID: str = Field(
        ...,
        alias="transactionId",
        name="",
        description="""""",
        example="""LNS-01071013-f085-4fba-acff-eaaeabe720e5""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="create_dts",
        name="",
        description="""""",
        example="""2001-03-16 02:00:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="updt_dts",
        name="",
        description="""""",
        example="""2021-02-23 05:09:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:21.334674""",
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
        example="""REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=87759558527181,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWRevenueRecognitionAuditEntitlementidModel(BaseModel):
    """
    Payload class for Level N REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID
    """

    class Config:
        """Payload Level Metadata"""

        title = "Revenue Recognition Audit Entitlement ID"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Table containing the recognized revenue and the corresponding entitlement id and transaction id."""  # optional
        unique_identifier = ["data.transactionId", "data.entitlementId"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "REVENUE_RECOGNITION_AUDIT_ENTITLEMENTID"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
