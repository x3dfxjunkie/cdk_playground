"""Source Data Contract for Level-N REVENUE_RECOGNITION_AUDIT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N REVENUE_RECOGNITION_AUDIT Data
    """

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

    CORRELATIONID: str = Field(
        ...,
        alias="correlationId",
        name="",
        description="""""",
        example="""01071013-f085-4fba-acff-eaaeabe720e5""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REVENUE_TOTAL: Optional[float] = Field(
        None,
        alias="revenue_total",
        name="",
        description="""""",
        example=6043.96,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SITE: str = Field(
        ...,
        alias="site",
        name="",
        description="""""",
        example="""DLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEF_REVENUE_TOTAL: Optional[float] = Field(
        None,
        alias="def_revenue_total",
        name="",
        description="""""",
        example=-6043.96,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: str = Field(
        ...,
        alias="status",
        name="",
        description="""""",
        example="""SUCCESS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESPONSE_CODE: Optional[str] = Field(
        None,
        alias="response_code",
        name="",
        description="""""",
        example="""200""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYLOAD: str = Field(
        ...,
        alias="payload",
        name="",
        description="""""",
        example="""{"sellingSystem":{"key":"LNS","transactionId":"LNS-01071013-f085-4fba-acff-eaaeabe720e5"},"createdDateTime":"2023-06-17T08:00:05.266Z","salesChannel":"back-office","type":"generalLedger","businessDate":"2023-06-17","ledgerAllotments":[{"ledgerTransmissions":[{"ledgerTypeId":"LNSREV","ledgerType":"LNS","quantity":1,"extended":{"amount":-6043.96,"currency":"USD"},"ledgerContextId":"DLRLNS02","extendedInTransactionCurrency":{"amount":-6043.96,"currency":"USD"}},{"ledgerTypeId":"LNSDEFREV","ledgerType":"LNS","quantity":1,"extended":{"amount":6043.96,"currency":"USD"},"ledgerContextId":"DLRLNS02","extendedInTransactionCurrency":{"amount":6043.96,"currency":"USD"}}],"allotmentType":"LNS-REVREC","allotmentId":"08GL"}]}""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESPONSE_PAYLOAD: Optional[str] = Field(
        None,
        alias="response_payload",
        name="",
        description="""""",
        example="""EGdzhgdLapNqnhSKPbUy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="create_dts",
        name="",
        description="""""",
        example="""2004-01-24 15:29:14""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="updt_dts",
        name="",
        description="""""",
        example="""2000-01-27 10:09:44""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N REVENUE_RECOGNITION_AUDIT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:35.892175""",
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
        example="""REVENUE_RECOGNITION_AUDIT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=41203439370214,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWRevenueRecognitionAuditModel(BaseModel):
    """
    Payload class for Level N REVENUE_RECOGNITION_AUDIT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Revenue Recognition Audit"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Audit table that contains Level N recognized revenue."""  # optional
        unique_identifier = ["data.transactionId"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "REVENUE_RECOGNITION_AUDIT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
