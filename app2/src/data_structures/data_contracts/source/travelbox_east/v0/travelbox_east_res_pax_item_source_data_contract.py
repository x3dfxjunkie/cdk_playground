"""Source Data Contract Template for RES_PAX_ITEM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_PAX_ITEM Data
    """

    EXTERNAL_BASE_PRICE: Optional[float] = Field(
        None,
        alias="EXTERNAL_BASE_PRICE",
        name="",
        description="""NaN""",
        example=17011.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORDER_LINE_ITEM_ID: Optional[str] = Field(
        None,
        alias="ORDER_LINE_ITEM_ID",
        name="",
        description="""NaN""",
        example="""mIJiRqKFQzshVOjZRDZS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_ORDER_LINE_ITEM_ID: Optional[str] = Field(
        None,
        alias="EXT_ORDER_LINE_ITEM_ID",
        name="",
        description="""NaN""",
        example="""YvBiZXJnwSOMKKFTzkek""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_PRICE_TOKEN_TIME: Optional[str] = Field(
        None,
        alias="EXT_PRICE_TOKEN_TIME",
        name="",
        description="""NaN""",
        example="""cgDVvlfZUINvNJzPIYii""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PLU_CODE: Optional[str] = Field(
        None,
        alias="PLU_CODE",
        name="",
        description="""NaN""",
        example="""pOBbewblbRKWoqPMvxtI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_BASE_CURRENCY: Optional[str] = Field(
        None,
        alias="EXT_BASE_CURRENCY",
        name="",
        description="""NaN""",
        example="""ofNimhwHzOumazpHguQd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=27624765,
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
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAX_ITEM_NO: int = Field(
        ...,
        alias="PAX_ITEM_NO",
        name="",
        description="""Number of the pax that particular car Item""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_NO: int = Field(
        ...,
        alias="PASSENGER_NO",
        name="",
        description="""Passnger number of the details entered passenger""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LEAD: str = Field(
        ...,
        alias="LEAD",
        name="",
        description="""A flag indicating that the passenger is the lead passenger ( value is '1' ) or not ( value is '0' )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: str = Field(
        ...,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_TIME: Optional[int] = Field(
        None,
        alias="DEPARTURE_TIME",
        name="",
        description="""Same column properties as GEN_DEPARTURE_TIME.DEPARTURE_TIME""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ON_REQUEST: str = Field(
        ...,
        alias="ON_REQUEST",
        name="",
        description="""Specifies whether car is On Request or not_x000D_
On Request - 1, Not - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_DATE: Optional[datetime] = Field(
        None,
        alias="DEPARTURE_DATE",
        name="",
        description="""Departure date for bookings""",
        example="""2006-02-12 16:10:27""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_SEAT: Optional[str] = Field(
        None,
        alias="INF_SEAT",
        name="",
        description="""A flag to indicate whether the pax required an infant seat or not.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST: float = Field(
        ...,
        alias="COST",
        name="",
        description="""Debit credit note cost amount_x000D_
- If credit negative value_x000D_
- If debit positive value""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE: float = Field(
        ...,
        alias="PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=1.4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX: float = Field(
        ...,
        alias="TAX",
        name="",
        description="""Total tax for the booking""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DISCOUNT: float = Field(
        ...,
        alias="DISCOUNT",
        name="",
        description="""Invoice line Discount""",
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
        example="""1996-01-14 19:33:12""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRAVEL_WITH_INFANT: Optional[str] = Field(
        None,
        alias="TRAVEL_WITH_INFANT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_PASSENGER_NO: Optional[int] = Field(
        None,
        alias="INF_PASSENGER_NO",
        name="",
        description="""NaN""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION: Optional[float] = Field(
        None,
        alias="COMMISSION",
        name="",
        description="""The commission percentage recieved by the tour operator""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PTC_CODE: Optional[str] = Field(
        None,
        alias="PTC_CODE",
        name="",
        description="""NaN""",
        example="""iMxEhYGOjSJOdUovtKtj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_CARE: Optional[str] = Field(
        None,
        alias="SPECIAL_CARE",
        name="",
        description="""NaN""",
        example="""BsVwXyvIZbSuyrjmgzCA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_PAX_ITEM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:47:42.177127""",
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
        example="""RES_PAX_ITEM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=34240052035824,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResPaxItemModel(BaseModel):
    """
    Payload class for TravelBox RES_PAX_ITEM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Passenger Item"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This Table stores the passenger information at the Booking Item level."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.PRODUCT_CODE",
            "data.ITEM_NO",
            "data.PAX_ITEM_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_PAX_ITEM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
