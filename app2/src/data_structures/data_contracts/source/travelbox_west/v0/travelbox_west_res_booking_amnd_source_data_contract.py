"""Source Data Contract Template for RES_BOOKING_AMND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_AMND Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1988-04-23 03:01:39""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=15007264,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_NO: int = Field(
        ...,
        alias="AMND_NO",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
A system generated id to uniquely identify a booking amendment. """,
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_USER: Optional[int] = Field(
        None,
        alias="AMND_USER",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The TravelBox id of the user who amended the booking.""",
        example=22647,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_DATE: Optional[datetime] = Field(
        None,
        alias="AMND_DATE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The date booking item is amended.""",
        example="""1986-05-21 17:56:35""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CHARGE: Optional[float] = Field(
        None,
        alias="AMND_CHARGE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The amendment charge.""",
        example=35378.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTES: Optional[str] = Field(
        None,
        alias="NOTES",
        name="",
        description="""Notes for the tax invoice""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CHARGE_COMMISSIONABLE: Optional[str] = Field(
        None,
        alias="AMND_CHARGE_COMMISSIONABLE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
Whether the charge is commissionable or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_REASON_ID: Optional[int] = Field(
        None,
        alias="AMND_REASON_ID",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The TravelBox id of the reason for amending the booking""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CAUSE_ID: Optional[int] = Field(
        None,
        alias="CAUSE_ID",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The TravelBox id of the cause for booking amendment""",
        example=961,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REASON_TYPE: Optional[str] = Field(
        None,
        alias="REASON_TYPE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The amendment reason type. Whether it is amendment or cancellation.""",
        example="""vipQkoVBurdIMXStioHO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_AMND Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:27.885399""",
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
        example="""RES_BOOKING_AMND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=41487609279493,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResBookingAmndModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_AMND
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Amendments"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table contains information of booking amendment charges.
These information are visible in Reservation Manager > View Booking Amendment/Cancellation Charges panel."""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.AMND_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_AMND"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
