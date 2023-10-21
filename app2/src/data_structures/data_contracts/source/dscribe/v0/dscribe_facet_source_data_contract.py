"""Source Data Contract Template for FACET"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Icon(BaseModel):

    """
    Class for Dscribe FACET Icon Data
    """

    url: str = Field(
        ...,
        alias="url",
        name="",
        description="",
        example="https://cdn1.parksmedia.wdprapps.disney.com/dam/global/icons/flat-icons/brands/rundisney-shirts.svg?1689783781896",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="wdproInternal",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    alt: Optional[str] = Field(
        None,
        alias="alt",
        name="",
        description="",
        example="A T shirt icon features a contrasting silhouette of Mickey Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Description(BaseModel):

    """
    Class for Dscribe FACET Description Data
    """

    text: str = Field(
        ...,
        alias="text",
        name="",
        description="",
        example="Discount applies to regularly priced merchandise when you purchase $65 or more before tax. Discount does not apply to gift sets, unique services or sale items.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="wdproInternal",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeFacetModel(BaseModel):

    """Payload class for DscribeFacetModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Facet"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR facet enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Facet"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="17938799",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Facet",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Umbrella Recreation WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    url_friendly_id: str = Field(
        ...,
        alias="urlFriendlyId",
        name="",
        description="",
        example="umbrella-recreation-wdw",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        example="Umbrella Recreation WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="wdproInternal",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="ADA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    icon: Optional[Icon] = Field(
        None,
        alias="icon",
        name="",
        description="",
    )

    descriptions: Optional[List[Description]] = Field(
        None,
        alias="descriptions",
        name="",
        description="",
    )
