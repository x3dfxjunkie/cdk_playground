"""Source Data Contract Template for RES_GENERIC_BOOKING"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_GENERIC_BOOKING Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=15505886,
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
        example=9,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DURATION: float = Field(
        ...,
        alias="DURATION",
        name="",
        description="""Duration of the booking item""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTURE_TIME: str = Field(
        ...,
        alias="DEPARTURE_TIME",
        name="",
        description="""Same column properties as GEN_DEPARTURE_TIME.DEPARTURE_TIME""",
        example="""00""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNIT_COST: str = Field(
        ...,
        alias="UNIT_COST",
        name="",
        description="""Flag to indicate if the fare is specified per person ( 0 ) or as a unit cost ( 1 ) when fare defined method is selected as 'Amount'""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNITS: int = Field(
        ...,
        alias="UNITS",
        name="",
        description="""The number of allocations""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAX_UNIT: str = Field(
        ...,
        alias="PAX_UNIT",
        name="",
        description="""Pax unit which is defined  under manual property edit in gen summary tab""",
        example="""N/A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_ID: int = Field(
        ...,
        alias="CATEGORY_ID",
        name="",
        description="""The system generated id of the supplement type""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RESERVATION_ID: int = Field(
        ...,
        alias="RESERVATION_ID",
        name="",
        description="""The system generated id of the reservation""",
        example=8362149,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DURATION_TYPE: str = Field(
        ...,
        alias="DURATION_TYPE",
        name="",
        description="""Generic item valid duration type_x000D_
Days = 'D' (Default)_x000D_
Nights = 'N'_x000D_
Hours = 'H'""",
        example="""U""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_TYPE_ID: int = Field(
        ...,
        alias="CATEGORY_TYPE_ID",
        name="",
        description="""Category type foreign key""",
        example=6587,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ELEMENT_GROUP_ID: int = Field(
        ...,
        alias="ELEMENT_GROUP_ID",
        name="",
        description="""The generic element group for which the mentioned permutation is valid""",
        example=3829,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_USED: Optional[str] = Field(
        None,
        alias="VOUCHER_USED",
        name="",
        description="""whether a voucher used or not for  particular item : 1 or 0 value ( if it is not used , cancellation will charge Before voucher use value which is defined under supplier cancellation schema setup)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKETING_DEAD_LINE: Optional[datetime] = Field(
        None,
        alias="TICKETING_DEAD_LINE",
        name="",
        description="""Ticketing deadline date for generic bookings (used for bus ticket implementation)""",
        example="""2009-10-21 14:56:13""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_RELEASE_DAY: Optional[int] = Field(
        None,
        alias="MAX_RELEASE_DAY",
        name="",
        description="""Maximum day of release allocation  within allocations period of the booking""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_CODE: Optional[str] = Field(
        None,
        alias="CATEGORY_CODE",
        name="",
        description="""Refer to CODE in GEN_CATEGORY table""",
        example="""COGC1851""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_NAME: Optional[str] = Field(
        None,
        alias="CATEGORY_NAME",
        name="",
        description="""The name of the car supplement category""",
        example="""$185 Disney Gift Card RST CO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_GROUP_CODE: Optional[str] = Field(
        None,
        alias="PRODUCT_GROUP_CODE",
        name="",
        description="""The TravelBox Code of the Product Group""",
        example="""COSTCO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_GROUP_NAME: Optional[str] = Field(
        None,
        alias="PRODUCT_GROUP_NAME",
        name="",
        description="""The TravelBox Name of the Product Group""",
        example="""Costco Package Inclusions""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_TYPE_CODE: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPE_CODE",
        name="",
        description="""Comma seperated product type codes""",
        example="""GIFTCARD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_TYPE_NAME: Optional[str] = Field(
        None,
        alias="PRODUCT_TYPE_NAME",
        name="",
        description="""The TravelBox Name of the Product Type""",
        example="""Disney Gift Card""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTENT_SUPPLIER: Optional[int] = Field(
        None,
        alias="CONTENT_SUPPLIER",
        name="",
        description="""The TravelBox id of the supplier who provides content for the contract""",
        example=29940,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKETED: Optional[str] = Field(
        None,
        alias="TICKETED",
        name="",
        description="""Specifies whether the tickets have been issued for flight booking item Ticketed - 1, Not ticketed - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEARCHED_AS_FC: Optional[str] = Field(
        None,
        alias="SEARCHED_AS_FC",
        name="",
        description="""whether this item add as a forced component (value 1) or not (value 0)""",
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
        example="""1977-04-15 19:49:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_FREQ: Optional[str] = Field(
        None,
        alias="FULFILLMENT_FREQ",
        name="",
        description="""Specify the frequency type of gategory, P: per Person, I: Per Item""",
        example="""I""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USAGE_LOV_FROM: Optional[datetime] = Field(
        None,
        alias="USAGE_LOV_FROM",
        name="",
        description="""NaN""",
        example="""2015-06-16 16:41:43""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    USAGE_LOV_TO: Optional[datetime] = Field(
        None,
        alias="USAGE_LOV_TO",
        name="",
        description="""NaN""",
        example="""1984-03-29 07:40:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICING_LOV_FROM: Optional[datetime] = Field(
        None,
        alias="PRICING_LOV_FROM",
        name="",
        description="""NaN""",
        example="""2007-07-13 04:49:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRICING_LOV_TO: Optional[datetime] = Field(
        None,
        alias="PRICING_LOV_TO",
        name="",
        description="""NaN""",
        example="""1984-07-29 10:58:41""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_GENERIC_BOOKING Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:46:59.899484""",
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
        example="""RES_GENERIC_BOOKING""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=77952207946848,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestResGenericBookingModel(BaseModel):
    """
    Payload class for TravelBox RES_GENERIC_BOOKING
    """

    class Config:
        """Payload Level Metadata"""

        title = "Booking Generic"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = (
            """This table contains all the Booking Item level information specif for generic bookings."""  # optional
        )
        unique_identifier = ["data.BOOKING_ID", "data.PRODUCT_CODE", "data.ITEM_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_GENERIC_BOOKING"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
