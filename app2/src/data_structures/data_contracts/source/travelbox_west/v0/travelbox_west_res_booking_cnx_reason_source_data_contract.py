"""Source Data Contract Template for RES_BOOKING_CNX_REASON"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_CNX_REASON Data
    """

    ID: int = Field(
        ...,
        alias="ID",
        name="",
        description="""System generated - auto incrementing field to uniquqly identify the contract to selling exchange rate""",
        example=41,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REASON: str = Field(
        ...,
        alias="REASON",
        name="",
        description="""Write OFF reason added for the payment""",
        example="""SBC Modification""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONF_DOC_REQUIRED: str = Field(
        ...,
        alias="CONF_DOC_REQUIRED",
        name="",
        description="""Flag to indicate if confirmation is required for the cancellation or amendment from Reservation Manager""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: str = Field(
        ...,
        alias="STATUS",
        name="",
        description="""The TravelBox code of the status of the contract""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APP_FOR_THIRD_PARTY_INS: Optional[str] = Field(
        None,
        alias="APP_FOR_THIRD_PARTY_INS",
        name="",
        description="""Deprecated""",
        example="""piXgKDVrylVPfgRGUTnW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORITY_LEVEL: Optional[int] = Field(
        None,
        alias="AUTHORITY_LEVEL",
        name="",
        description="""Deprecated""",
        example=2508,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REASON_TYPE: str = Field(
        ...,
        alias="REASON_TYPE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The amendment reason type. Whether it is amendment or cancellation.""",
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REPRICING_DATE: str = Field(
        ...,
        alias="REPRICING_DATE",
        name="",
        description="""B-Booking, A-Amendment, N-None""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_PRODUCTS: Optional[str] = Field(
        None,
        alias="APPLICABLE_PRODUCTS",
        name="",
        description="""Applicable products for this cancellation/amendment reason""",
        example="""QVXNHHFkBWKhRaaPEbNE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_CNX_REASON Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:17.444418""",
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
        example="""RES_BOOKING_CNX_REASON""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=23962799601594,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResBookingCnxReasonModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_CNX_REASON
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Cancellation Reason"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This holds setup information on cancellation reasons setup."""  # optional
        unique_identifier = ["data.ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_CNX_REASON"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
