"""Source Data Contract Template for MENU_GROUP"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Name(BaseModel):
    """
    Class For Dscribe MENU_GROUP Name Data
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Kids' Meals",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: List[str] = Field(
        ...,
        alias="type",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Description(BaseModel):
    """
    Class For Dscribe MENU_GROUP Description Data
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Kids' Meals",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: List[str] = Field(
        ...,
        alias="type",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMenuGroupModel(BaseModel):
    """
    Payload class for DscribeMenuGroupModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Menu Group"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR menu group enterprise metadata. Used at food and beverage locations."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "MenuGroup"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="16603775",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MenuGroup",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="#BOG - Lunch - Kids' Meals",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    types: List[str] = Field(
        ...,
        alias="types",
        name="",
        description="",
        example=["example"],
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

    descriptions: Optional[List[Description]] = Field(
        None,
        alias="descriptions",
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

    menu_offering: Optional[List[str]] = Field(
        None,
        alias="MenuOffering",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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
