"""Source Data Contract Template for RES_BOOKING_ITEM_CNX"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM_CNX Data
    """

    CNX_USER: Optional[int] = Field(
        None,
        alias="CNX_USER",
        name="",
        description="""The id of the user who cancelled the booking""",
        example=20629,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_NOTIFICATION_SENT_USER: Optional[int] = Field(
        None,
        alias="CNX_NOTIFICATION_SENT_USER",
        name="",
        description="""Deprecated""",
        example=2073,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONFIRMATION_RECEIVED_USER: Optional[int] = Field(
        None,
        alias="CNX_CONFIRMATION_RECEIVED_USER",
        name="",
        description="""Deprecated""",
        example=879,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONF_RECEIVED_USER: Optional[int] = Field(
        None,
        alias="CNX_CONF_RECEIVED_USER",
        name="",
        description="""Deprecated""",
        example=1843,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_ADT_COST: float = Field(
        ...,
        alias="CNX_ADT_COST",
        name="",
        description="""Cancellation cost of Adults of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CHD_COST: float = Field(
        ...,
        alias="CNX_CHD_COST",
        name="",
        description="""Cancellation cost of children of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_INF_COST: float = Field(
        ...,
        alias="CNX_INF_COST",
        name="",
        description="""Cancellation cost of infants of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CALCULATED_DATE: Optional[datetime] = Field(
        None,
        alias="CNX_CALCULATED_DATE",
        name="",
        description="""The date on which cancellation charges calculated""",
        example="""1971-03-07 22:42:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TBX_ONLY: Optional[str] = Field(
        None,
        alias="TBX_ONLY",
        name="",
        description="""Constant value 1""",
        example="""0""",
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

    CHARGE_TYPE: Optional[str] = Field(
        None,
        alias="CHARGE_TYPE",
        name="",
        description="""P = PERCENTAGE, A = AMOUNT""",
        example="""CEitMVOQAlrIQyDJfqgC""",
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
        example="""qlnDFNoOFdQWvpfvDjlI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27740227,
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
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INDEX_NO: int = Field(
        ...,
        alias="INDEX_NO",
        name="",
        description="""The system generated number for the discount rate""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_REASON_ID: Optional[int] = Field(
        None,
        alias="CNX_REASON_ID",
        name="",
        description="""The id of the reason for cancelling the booking""",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_DATE: datetime = Field(
        ...,
        alias="CNX_DATE",
        name="",
        description="""Booking item cancelled date""",
        example="""2006-12-04 06:00:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_COST: float = Field(
        ...,
        alias="CNX_COST",
        name="",
        description="""Total cancellation cost of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_PRICE: float = Field(
        ...,
        alias="CNX_PRICE",
        name="",
        description="""Total cancellation price of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_NOTIFICATION_SENT: str = Field(
        ...,
        alias="CNX_NOTIFICATION_SENT",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_NOTIFICATION_SENT_METHOD: Optional[str] = Field(
        None,
        alias="CNX_NOTIFICATION_SENT_METHOD",
        name="",
        description="""Deprecated""",
        example="""oRUzLYPZAJHLwfFeSdfj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_NOTIFICATION_SENT_DATE: Optional[datetime] = Field(
        None,
        alias="CNX_NOTIFICATION_SENT_DATE",
        name="",
        description="""Deprecated""",
        example="""1990-06-06 21:55:40""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONFIRMATION_RECEIVED: Optional[str] = Field(
        None,
        alias="CNX_CONFIRMATION_RECEIVED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONFIRMATION_RECEIVED_DATE: Optional[datetime] = Field(
        None,
        alias="CNX_CONFIRMATION_RECEIVED_DATE",
        name="",
        description="""Deprecated""",
        example="""2006-08-07 17:20:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONFIRMATION_RECEIVED_METH: Optional[str] = Field(
        None,
        alias="CNX_CONFIRMATION_RECEIVED_METH",
        name="",
        description="""Deprecated""",
        example="""awHFtoyzXehHotyRyAAx""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example="""DBrfrciCMriJqiESFeXy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONF_RECEIVED: Optional[str] = Field(
        None,
        alias="CNX_CONF_RECEIVED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONF_RECEIVED_DATE: Optional[datetime] = Field(
        None,
        alias="CNX_CONF_RECEIVED_DATE",
        name="",
        description="""Deprecated""",
        example="""2002-04-25 00:02:25""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNX_CONF_RECEIVED_METHOD: Optional[str] = Field(
        None,
        alias="CNX_CONF_RECEIVED_METHOD",
        name="",
        description="""Deprecated""",
        example="""uBBOZeMgfAuDnaFkNSDc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_NO: Optional[int] = Field(
        None,
        alias="PASSENGER_NO",
        name="",
        description="""Passnger number of the details entered passenger""",
        example=8597,
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

    CNX_CHARGE_COMMISSIONABLE: Optional[str] = Field(
        None,
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

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2001-07-17 15:27:48""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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


class Metadata(BaseModel):
    """
    Class for TravelBox RES_BOOKING_ITEM_CNX Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:41.174451""",
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
        example="""RES_BOOKING_ITEM_CNX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=52043188525321,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResBookingItemCnxModel(BaseModel):
    """
    Payload class for TravelBox RES_BOOKING_ITEM_CNX
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Item Cancellation"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table holds the Cancellation information (cancalation cause  / reason, cancelation charges, etc) for all the cancelled booking items in TravelBox."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
            "data.INDEX_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_BOOKING_ITEM_CNX"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
