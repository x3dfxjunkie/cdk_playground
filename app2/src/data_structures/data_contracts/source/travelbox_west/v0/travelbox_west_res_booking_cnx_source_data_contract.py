"""Source Data Contract Template for RES_BOOKING_CNX"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_CNX Data
    """

    REVERSIBLE: Optional[str] = Field(
        None,
        alias="REVERSIBLE",
        name="",
        description="""NaN""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=14661814,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_REASON_ID: Optional[int] = Field(
        None,
        alias="CNX_REASON_ID",
        name="",
        description="""The id of the reason for cancelling the booking""",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_USER: int = Field(
        ...,
        alias="CNX_USER",
        name="",
        description="""The id of the user who cancelled the booking""",
        example=16237,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_DATE: datetime = Field(
        ...,
        alias="CNX_DATE",
        name="",
        description="""Booking item cancelled date""",
        example="""2020-05-01 09:39:02""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CHARGE: float = Field(
        ...,
        alias="CNX_CHARGE",
        name="",
        description="""Total booking cancellation charges""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CHARGE_COMMISSIONABLE: str = Field(
        ...,
        alias="CNX_CHARGE_COMMISSIONABLE",
        name="",
        description="""Flag to specify if the cancellation charge is commissionable._x000D_
1 - commissionable_x000D_
0 - not commissionable""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_CONF_DOC_RECEIVED: str = Field(
        ...,
        alias="CLIENT_CONF_DOC_RECEIVED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_CONF_DOC_RECEIVED_DATE: Optional[datetime] = Field(
        None,
        alias="CLIENT_CONF_DOC_RECEIVED_DATE",
        name="",
        description="""Deprecated""",
        example="""1994-11-09 11:27:01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_NO: int = Field(
        ...,
        alias="CNX_NO",
        name="",
        description="""Cancellation No (NULL)""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_NO: Optional[int] = Field(
        None,
        alias="PASSENGER_NO",
        name="",
        description="""Passnger number of the details entered passenger""",
        example=9640,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CALCULATED_DATE: Optional[datetime] = Field(
        None,
        alias="CNX_CALCULATED_DATE",
        name="",
        description="""The date on which cancellation charges calculated""",
        example="""1994-08-25 11:15:36""",
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
        example=960,
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
        example="""C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_CNX Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:27.744734""",
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
        example="""RES_BOOKING_CNX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=39779068507344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResBookingCnxModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_CNX
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Cancellation"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled bookings in TravelBox."""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.CNX_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_CNX"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
