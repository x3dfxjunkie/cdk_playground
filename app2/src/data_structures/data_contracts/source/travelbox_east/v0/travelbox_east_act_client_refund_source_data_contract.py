"""Source Data Contract Template for ACT_CLIENT_REFUND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_REFUND Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1992-07-26 03:39:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=26013651,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_INDEX: int = Field(
        ...,
        alias="RECEIPT_INDEX",
        name="",
        description="""A foreign key which refers to the field RECEIPT_INDEX of the ACT_CLIENT_ACCOUNT_RECEIPT table""",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFUND_TYPE: str = Field(
        ...,
        alias="REFUND_TYPE",
        name="",
        description="""Refund type mapping for the PAYMENT_TYPE""",
        example="""283""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORISED: str = Field(
        ...,
        alias="AUTHORISED",
        name="",
        description="""Whether this is an authorized payment or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSFER_RECEIPT_INDEX: Optional[int] = Field(
        None,
        alias="TRANSFER_RECEIPT_INDEX",
        name="",
        description="""If this payment is a refund from other payment then receipt index of original payment""",
        example=9,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFUND_BATCH_NO: int = Field(
        ...,
        alias="REFUND_BATCH_NO",
        name="",
        description="""THIS WILL BE GEENRATED  AFTER SAING THE REFUNDS""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTO_REFUND: Optional[str] = Field(
        None,
        alias="AUTO_REFUND",
        name="",
        description="""Flag to chek the auto refund""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_PAYMENT_AS_REFUND: Optional[str] = Field(
        None,
        alias="COMM_PAYMENT_AS_REFUND",
        name="",
        description="""Deprecated""",
        example="""MlVBahyPRqmpJVFDWgje""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_PAYMENT_PRINTED: Optional[str] = Field(
        None,
        alias="COMM_PAYMENT_PRINTED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TEMP_USER: Optional[str] = Field(
        None,
        alias="TEMP_USER",
        name="",
        description="""Deprecated""",
        example="""OPcpYMeThmHuBYAEIuRU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORISED_USER: Optional[int] = Field(
        None,
        alias="AUTHORISED_USER",
        name="",
        description="""Payment authorized user id""",
        example=15297,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHEQUE_REFUND_INDEX: Optional[int] = Field(
        None,
        alias="CHEQUE_REFUND_INDEX",
        name="",
        description="""Refund index of the cheque refund summary (only for cheque refunds)""",
        example=3315,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_REFUND Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:15.899912""",
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
        example="""ACT_CLIENT_REFUND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=89601121466266,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastActClientRefundModel(BaseModel):
    """
    Payload class for TravelBox ACT_CLIENT_REFUND
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Client Refund"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store information of  Refund details . The values are setup in
'Refunds->Refunds' in Accounts Client"""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.RECEIPT_INDEX",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACT_CLIENT_REFUND"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
