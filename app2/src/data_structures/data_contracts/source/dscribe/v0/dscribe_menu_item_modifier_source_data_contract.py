"""Source Data Contract Template for MENU_ITEM_MODIFIER"""

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1234",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MenuItemModifier",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Test",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="3456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMenuItemModifierModel(BaseModel):
    """
    Payload class for DScribeMenuItemModifierModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Menu Item Modifier"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR contact enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "MenuItemModifier"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1234",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MenuItemModifier",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Test",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="3456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    items: List[Item] = Field(
        ...,
        alias="items",
        name="",
        description="",
    )
