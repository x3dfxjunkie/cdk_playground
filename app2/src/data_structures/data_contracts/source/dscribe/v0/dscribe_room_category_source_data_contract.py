"""Source Data Contract Template for Roomcategory"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class DScribeRoomCategoryModel(BaseModel):
    """
    Payload class for Dscribe roomcategory
    """

    class Config:
        """Payload Level Metadata"""

        title = "Room Category"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR room category enterprise metadata"  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "RoomCategory"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="16983815",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="RoomCategory",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Disney's Polynesian Village Resort- Rooms and Suites with Club Level Services - ADA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: str = Field(
        ...,
        alias="nameHtml",
        name="",
        description="",
        example="Accessible Rooms & Suites with Club Level Service",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: str = Field(
        ...,
        alias="nameText",
        name="",
        description="",
        example="Accessible Rooms & Suites with Club Level Service",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accessible: bool = Field(
        ...,
        alias="accessible",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    concierge: bool = Field(
        ...,
        alias="concierge",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type: str = Field(
        ...,
        alias="usageType",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    amenity: List[str] = Field(
        ...,
        alias="Amenity",
        name="",
        description="",
        example=["18667636"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    concierge_amenity: Optional[List[str]] = Field(
        None,
        alias="conciergeAmenity",
        name="",
        description="",
        example=["16894755"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accommodation: Optional[List[str]] = Field(
        None,
        alias="Accommodation",
        name="",
        description="",
        example=["17344346"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
