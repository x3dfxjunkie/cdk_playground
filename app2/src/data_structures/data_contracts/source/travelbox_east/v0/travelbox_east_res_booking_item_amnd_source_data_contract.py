"""Source Data Contract Template for RES_BOOKING_ITEM_AMND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM_AMND Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27517669,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""GEN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: int = Field(
        ...,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=1,
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

    AMND_DATE: datetime = Field(
        ...,
        alias="AMND_DATE",
        name="",
        description="""Booking amendment charges: Reservation Manager > View Booking Amendment/Cancellation Charges._x000D_
The date booking item is amended.""",
        example="""2019-12-14 21:06:02""",
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
        example=17899,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_COST: float = Field(
        ...,
        alias="AMND_COST",
        name="",
        description="""Cost applied for the booking item amendment""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTES: str = Field(
        ...,
        alias="NOTES",
        name="",
        description="""Notes for the tax invoice""",
        example=""" """,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_NOTIFICATION_SENT: Optional[str] = Field(
        None,
        alias="AMND_NOTIFICATION_SENT",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_NOTIFICATION_SENT_DATE: Optional[datetime] = Field(
        None,
        alias="AMND_NOTIFICATION_SENT_DATE",
        name="",
        description="""Deprecated""",
        example="""2000-07-29 08:50:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_NOTIFICATION_SENT_USER: Optional[int] = Field(
        None,
        alias="AMND_NOTIFICATION_SENT_USER",
        name="",
        description="""Deprecated""",
        example=259,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_NOTIFICATION_SENT_METHOD: Optional[str] = Field(
        None,
        alias="AMND_NOTIFICATION_SENT_METHOD",
        name="",
        description="""Deprecated""",
        example="""BfPdVeqbmqWcxKfYDJOB""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CONF_RECEIVED: Optional[str] = Field(
        None,
        alias="AMND_CONF_RECEIVED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CONF_RECEIVED_DATE: Optional[datetime] = Field(
        None,
        alias="AMND_CONF_RECEIVED_DATE",
        name="",
        description="""Deprecated""",
        example="""2010-07-24 00:54:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CONF_RECEIVED_USER: Optional[int] = Field(
        None,
        alias="AMND_CONF_RECEIVED_USER",
        name="",
        description="""Deprecated""",
        example=127,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CONF_RECEIVED_METHOD: Optional[str] = Field(
        None,
        alias="AMND_CONF_RECEIVED_METHOD",
        name="",
        description="""Deprecated""",
        example="""aOYdGEJgTZXaRbVDBALb""",
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
        example=14,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_PRICE: float = Field(
        ...,
        alias="AMND_PRICE",
        name="",
        description="""Price applied for the booking item amendment""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_IN_CONTRACT: float = Field(
        ...,
        alias="COST_IN_CONTRACT",
        name="",
        description="""Cost of the booking item in contract currency""",
        example=0.0,
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

    AMND_ADT_COST: float = Field(
        ...,
        alias="AMND_ADT_COST",
        name="",
        description="""The amendment cost of adults of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CHD_COST: float = Field(
        ...,
        alias="AMND_CHD_COST",
        name="",
        description="""The amendment cost of children of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_INF_COST: float = Field(
        ...,
        alias="AMND_INF_COST",
        name="",
        description="""Amendment cost of infants of the booking item""",
        example=0.0,
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

    CHARGE_TYPE: Optional[str] = Field(
        None,
        alias="CHARGE_TYPE",
        name="",
        description="""P = PERCENTAGE, A = AMOUNT""",
        example="""FIXED""",
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
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_ADT_PRICE: Optional[float] = Field(
        None,
        alias="AMND_ADT_PRICE",
        name="",
        description="""The amendment price of adults of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_CHD_PRICE: Optional[float] = Field(
        None,
        alias="AMND_CHD_PRICE",
        name="",
        description="""The amendment price of children of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMND_INF_PRICE: Optional[float] = Field(
        None,
        alias="AMND_INF_PRICE",
        name="",
        description="""Amendment price of infants of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2008-05-15 07:27:11""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM_AMND Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:48:33.122555""",
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
        example="""RES_BOOKING_ITEM_AMND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=75156322698605,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResBookingItemAmndModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_ITEM_AMND
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Booking Item Amendment"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table contains information related to amendments made to booking items."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
            "data.AMND_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_ITEM_AMND"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
