"""Source Data Contract Template for CHARACTER"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe CHARACTER ChannelItem Data
    """

    site_name: str = Field(
        ...,
        alias="siteName",
        name="",
        description="",
        example="Additional Integrations",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    channel_name: str = Field(
        ...,
        alias="channelName",
        name="",
        description="",
        example="/D3/Character",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeCharacterModel(BaseModel):
    """
    Payload class for DScribeCharacterModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Character"
        stream_name = ""
        description = "Contains all information about WDW and DLR character enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Character"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="123456789111111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Character",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="test-jer-solo",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: Optional[str] = Field(
        None,
        alias="nameHtml",
        name="",
        description="",
        example="Jer-Solo",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: Optional[str] = Field(
        None,
        alias="nameText",
        name="",
        description="",
        example="Jer-Solo",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Costumed Character",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_channel: Optional[List[str]] = Field(
        None,
        alias="siteChannel",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    channel: Optional[List[ChannelItem]] = Field(
        None,
        alias="channel",
        name="",
        description="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="80000833",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Entertainment Character",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: Optional[List[str]] = Field(
        None,
        alias="Name",
        name="",
        description="",
        example=["example"],
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
