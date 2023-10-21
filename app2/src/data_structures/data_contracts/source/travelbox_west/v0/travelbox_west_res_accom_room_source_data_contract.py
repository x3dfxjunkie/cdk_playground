"""Source Data Contract Template for RES_ACCOM_ROOM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_ACCOM_ROOM Data
    """

    PPPN_INFANT_PRICE: float = Field(
        ...,
        alias="PPPN_INFANT_PRICE",
        name="",
        description="""Per Person Per Night Infant Price""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PPPN_ADULT_COST: float = Field(
        ...,
        alias="PPPN_ADULT_COST",
        name="",
        description="""Per Person Per Night Adult cost (manual item prices are recorded PPPN)""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PPPN_CHILD_COST: float = Field(
        ...,
        alias="PPPN_CHILD_COST",
        name="",
        description="""Per Person Per Night Child cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PPPN_INFANT_COST: float = Field(
        ...,
        alias="PPPN_INFANT_COST",
        name="",
        description="""Per Person Per Night Infant Cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BEDDING: str = Field(
        ...,
        alias="BEDDING",
        name="",
        description="""Bed type in the room eg: Standard Bedding""",
        example="""N/A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OCCUPANCY_CODE: Optional[str] = Field(
        None,
        alias="OCCUPANCY_CODE",
        name="",
        description="""The code specified for the custom occupancy""",
        example="""AD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MARKUP_REF: Optional[str] = Field(
        None,
        alias="MARKUP_REF",
        name="",
        description="""The TravelBox reference of the applied markup for the room""",
        example="""qoBjZjFQaoufJsZetbxt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVAILABILITY_TYPE: int = Field(
        ...,
        alias="AVAILABILITY_TYPE",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NON_PAYING_PAX: Optional[int] = Field(
        None,
        alias="NON_PAYING_PAX",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANCILLARY_PAX: Optional[int] = Field(
        None,
        alias="ANCILLARY_PAX",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MANUALLY_ADDED: Optional[str] = Field(
        None,
        alias="MANUALLY_ADDED",
        name="",
        description="""Flag to check whether manually added or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNIT_COST: Optional[float] = Field(
        None,
        alias="UNIT_COST",
        name="",
        description="""Flag to indicate if the fare is specified per person ( 0 ) or as a unit cost ( 1 ) when fare defined method is selected as 'Amount'""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNIT_PRICE: Optional[float] = Field(
        None,
        alias="UNIT_PRICE",
        name="",
        description="""Unit Price""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_MANUAL_OVERRIDE_PRICE: Optional[float] = Field(
        None,
        alias="ADT_MANUAL_OVERRIDE_PRICE",
        name="",
        description="""Manually added price for adults of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_MANUAL_OVERRIDE_PRICE: Optional[float] = Field(
        None,
        alias="CHD_MANUAL_OVERRIDE_PRICE",
        name="",
        description="""Manually added price for children of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_MANUAL_OVERRIDE_PRICE: Optional[float] = Field(
        None,
        alias="INF_MANUAL_OVERRIDE_PRICE",
        name="",
        description="""Manually added price for infants of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADT_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="ADT_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for adults of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHD_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="CHD_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for children of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INF_MANUAL_OVERRIDE_COST: Optional[float] = Field(
        None,
        alias="INF_MANUAL_OVERRIDE_COST",
        name="",
        description="""Manually added cost for infants of room through TravelBox""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SPECIAL_RATE_APPLIED: str = Field(
        ...,
        alias="SPECIAL_RATE_APPLIED",
        name="",
        description="""Whether it's apply special rate which is setup""",
        example="""0""",
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
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2011-07-17 19:32:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=14698470,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""HTL""",
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

    ROOM_NO: int = Field(
        ...,
        alias="ROOM_NO",
        name="",
        description="""The system generated number for the room of the reservation""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROOM_TYPE: Optional[str] = Field(
        None,
        alias="ROOM_TYPE",
        name="",
        description="""The TravelBox code of the room type of the booking""",
        example="""CS4""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOCATION_CONTRACT: int = Field(
        ...,
        alias="ALLOCATION_CONTRACT",
        name="",
        description="""Deprecated""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT: int = Field(
        ...,
        alias="ADULT",
        name="",
        description="""Number of  Adult passengers of the sharing rule""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD: int = Field(
        ...,
        alias="CHILD",
        name="",
        description="""Number of  Child passengers of the sharing rule""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT: int = Field(
        ...,
        alias="INFANT",
        name="",
        description="""Number of  Infant passengers of the sharing rule""",
        example=0,
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
        example=1817.32,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICE: float = Field(
        ...,
        alias="PRICE",
        name="",
        description="""Oracle managed system tables used for materialised views""",
        example=2138.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROOMS: int = Field(
        ...,
        alias="ROOMS",
        name="",
        description="""Number of rooms reserved""",
        example=1,
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

    ADULT_COST: float = Field(
        ...,
        alias="ADULT_COST",
        name="",
        description="""Reserved for future implementations""",
        example=1817.32,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_COST: float = Field(
        ...,
        alias="CHILD_COST",
        name="",
        description="""Per Child cost for a particuler Other Cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_COST: float = Field(
        ...,
        alias="INFANT_COST",
        name="",
        description="""Infant cost for a particuler Other Cost""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADULT_PRICE: float = Field(
        ...,
        alias="ADULT_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=2138.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_PRICE: float = Field(
        ...,
        alias="CHILD_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_PRICE: float = Field(
        ...,
        alias="INFANT_PRICE",
        name="",
        description="""Reserved for future implementations""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ALLOT_GROUP_NO: int = Field(
        ...,
        alias="ALLOT_GROUP_NO",
        name="",
        description="""The system generated number of the allocation group from which the reservation has been done""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PPPN_ADULT_PRICE: float = Field(
        ...,
        alias="PPPN_ADULT_PRICE",
        name="",
        description="""Per Person Per Night Adult Price""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PPPN_CHILD_PRICE: float = Field(
        ...,
        alias="PPPN_CHILD_PRICE",
        name="",
        description="""Per Person Per Night Child Price""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_ACCOM_ROOM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:07.182048""",
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
        example="""RES_ACCOM_ROOM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=30430878871060,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResAccomRoomModel(BaseModel):
    """
    Payload class for TravelBox RES_ACCOM_ROOM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Accommodation Room"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table holds the Room level information of Accommodation booking items."""  # optional
        unique_identifier = ["data.BOOKING_ID", "data.PRODUCT_CODE", "data.ITEM_NO", "data.ROOM_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_ACCOM_ROOM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
