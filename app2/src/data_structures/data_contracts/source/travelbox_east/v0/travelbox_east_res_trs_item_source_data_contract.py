"""Source Data Contract Template for RES_TRS_ITEM"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox RES_TRS_ITEM Data
    """

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=10132011,
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

    PRODUCT_CODE: str = Field(
        ...,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""TRS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRS_ITEM_NO: int = Field(
        ...,
        alias="TRS_ITEM_NO",
        name="",
        description="""NaN""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITINERARY_ORDER: Optional[int] = Field(
        None,
        alias="ITINERARY_ORDER",
        name="",
        description="""position in the itinerary order of all items within the booking. By Clicking on Reservation Client 'Itinerary' node will show the itinerary in this order. User can change the order (position) manually. This is -1 for Transfer items""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EMBARKATION_TIME: int = Field(
        ...,
        alias="EMBARKATION_TIME",
        name="",
        description="""THIS IS USED FOR DAY CRUISES. EMBARKATION TIMES SHOULD BE DISPLAYED ALONG WITH DEPARTURE TIME IN RES BOOKING. DO NOT DISPLAY ANYTHING IF NOT DEFINED.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_ITEM_ORDER: Optional[int] = Field(
        None,
        alias="PKG_ITEM_ORDER",
        name="",
        description="""If the booking item belongs to a package, the order number of the booking item within the package.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    START_TIME: Optional[datetime] = Field(
        None,
        alias="START_TIME",
        name="",
        description="""Start timestamp of the booking item""",
        example="""2005-01-31 14:42:48""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    END_TIME: Optional[datetime] = Field(
        None,
        alias="END_TIME",
        name="",
        description="""End timestamp of the booking item""",
        example="""2020-04-26 04:33:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2000-05-02 04:25:39""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox RES_TRS_ITEM Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:48:49.055463""",
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
        example="""RES_TRS_ITEM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=90435103741839,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastResTrsItemModel(BaseModel):
    """
    Payload class for TravelBox RES_TRS_ITEM
    """

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Transfer Item"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table holds itinerary level information related to Transfer bookings."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.ITEM_NO",
            "data.PRODUCT_CODE",
            "data.TRS_ITEM_NO",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "RES_TRS_ITEM"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
