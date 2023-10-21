"""Source Data Contract Template for AMENITY"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class DScribeAmenityModel(BaseModel):
    """
    Payload class for DScribeAmenityModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Amenity"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR amenity enterprise metadata. (such as a blu-ray player in resort rooms)"  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Amenity"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="108114",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Amenity",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Ceiling Fan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    url_friendly_id: str = Field(
        ...,
        alias="urlFriendlyId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        example="Ceiling Fan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Standard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type: Optional[str] = Field(
        None,
        alias="usageType",
        name="",
        description="",
        example="Room/Stateroom",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facet: Optional[List[str]] = Field(
        None,
        alias="Facet",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
