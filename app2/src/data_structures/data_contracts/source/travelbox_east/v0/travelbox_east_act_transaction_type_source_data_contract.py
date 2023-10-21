"""Source Data Contract Template for ACT_TRANSACTION_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_TRANSACTION_TYPE Data
    """

    APM_TYPE: Optional[str] = Field(
        None,
        alias="APM_TYPE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    API_ENABLED: Optional[str] = Field(
        None,
        alias="API_ENABLED",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_REFUNDABLE: Optional[str] = Field(
        None,
        alias="MANUALLY_REFUNDABLE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""CHEQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Cheque """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT: str = Field(
        ...,
        alias="RECEIPT",
        name="",
        description="""Whether transaction type can be considered as receipts""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT: str = Field(
        ...,
        alias="PAYMENT",
        name="",
        description="""Whether transaction type can be considered for payments""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFUND_ORDER: int = Field(
        ...,
        alias="REFUND_ORDER",
        name="",
        description="""Deprecated""",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SYS_DEFINED: Optional[str] = Field(
        None,
        alias="SYS_DEFINED",
        name="",
        description="""Whether this is a system defined refund type or user created refund type""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BANKABLE: Optional[str] = Field(
        None,
        alias="BANKABLE",
        name="",
        description="""Transaction type (receipts/ payments) is bankable or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPENSE: Optional[str] = Field(
        None,
        alias="EXPENSE",
        name="",
        description="""Transaction type (receipts/ payments) is expensable or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_TRANSACTION_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:16.483089""",
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
        example="""TBX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""ACT_TRANSACTION_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=71543039915828,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastActTransactionTypeModel(BaseModel):
    """
    Payload class for TravelBox ACT_TRANSACTION_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Transaction Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store information of Payment/ReceiptTypes. The values are setup in
'Setup->Receivable->Payment/Receipt Types' in Accounts Client."""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACT_TRANSACTION_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
