"""Source Data Contract Template for MENU_OFFERING"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Name(BaseModel):
    """
    Class For Dscribe MENU_OFFERING Name Data
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Bagel with Cream Cheese",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: List[str] = Field(
        ...,
        alias="type",
        name="",
        description="",
        example=["Mobile Long"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PriceSpecification(BaseModel):
    """
    Class For Dscribe MENU_OFFERING PriceSpecification Data
    """

    price_qualifier: str = Field(
        ...,
        alias="priceQualifier",
        name="",
        description="",
        example="Per Serving",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_without_tax: Optional[float] = Field(
        None,
        alias="priceWithoutTax",
        name="",
        description="",
        example=2.99,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Description(BaseModel):
    """
    Class For Dscribe MENU_OFFERING Description Data
    """

    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        example="Bagel with Cream Cheese",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: List[str] = Field(
        ...,
        alias="type",
        name="",
        description="",
        example=["Mobile Long"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MediaItem(BaseModel):
    """
    Class For Dscribe MENU_OFFERING MediaItem Data
    """

    url: str = Field(
        ...,
        alias="url",
        name="",
        description="",
        example="https://cdn1.parksmedia.wdprapps.disney.com/dam/Ops-Comm/mobile-order/wdw/parks/dak/flame-tree/FT_Cart_KidsChickenSandwich.jpg",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Single",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMenuOfferingModel(BaseModel):
    """Payload class for DScribeMenuOfferingModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Menu Offering"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR menu offering enterprise metadata. Used at food and beverage locations."  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "MenuOffering"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="16240253",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MenuOffering",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Bagel with Cream Cheese (2.99)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Single",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    names: List[Name] = Field(
        ...,
        alias="names",
        name="",
        description="",
    )

    price_type: str = Field(
        ...,
        alias="priceType",
        name="",
        description="",
        example="Retail",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_specifications: Optional[List[PriceSpecification]] = Field(
        None,
        alias="priceSpecifications",
        name="",
        description="",
    )

    currency: str = Field(
        ...,
        alias="currency",
        name="",
        description="",
        example="US dollar",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    descriptions: Optional[List[Description]] = Field(
        None,
        alias="descriptions",
        name="",
        description="",
    )

    classification: Optional[List[str]] = Field(
        None,
        alias="Classification",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media: Optional[List[MediaItem]] = Field(
        None,
        alias="media",
        name="",
        description="",
    )
