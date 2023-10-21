"""Source Data Contract Template for Categoryadmin"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """Class For Dscribe Categoryadmin ChannelItem Data"""

    site_name: str = Field(
        ...,
        alias="siteName",
        name="",
        description="",
        example="Campus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    channel_name: str = Field(
        ...,
        alias="channelName",
        name="",
        description="",
        example="/Category Admin",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeCategoryAdminModel(BaseModel):
    """Payload class for DscribeCategoryAdminModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Category Admin"
        stream_name = ""
        description = "Contains all information about WDW and DLR category admin enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "CategoryAdmin"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1434",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="CategoryAdmin",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Ticket + Disney Dining Plan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Ticket + Disney Dining Plan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Plan Type",
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
