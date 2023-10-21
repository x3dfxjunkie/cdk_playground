"""Source Data Contract Template for MARKETING_MESSAGE"""


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe MARKETING_MESSAGE ChannelItem Data
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
        example="/FACSVC/All Content/Policy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMarketingMessageModel(BaseModel):
    """Payload class for DScribeMarketingMessageModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Marketing Message"
        stream_name = ""
        description = "Contains all information about WDW and DLR marketing message enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "marketing_message"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="100521",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MarketingMessage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="0 Unescorted Minors - Letter",
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

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="0 Unescorted Minors - Letter",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Description",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80000293",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type: str = Field(
        ...,
        alias="usageType",
        name="",
        description="",
        example="Policy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type_id: str = Field(
        ...,
        alias="usageTypeId",
        name="",
        description="",
        example="80000461",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    description_text: Optional[str] = Field(
        None,
        alias="descriptionText",
        name="",
        description="",
        example="a id=Letter name=Letter /Unescorted Minors - Letterp /pNAMEbr /ADDRESSbr /CITY, STATE ZIPbr /br /Re: Parental Agreement (RESERVATION NO.)/pp /pDear PARENT'S NAME,/pp /pWe wish to inform you of our parental consent policy regarding the confirmed reservations for (GUEST NAME) at the WALT DISNEY WORLD Resort Complex. Completion of the enclosed agreement, properly notarized, is required prior to the arrival of a minor Guest who will be unaccompanied by a parent or guardian. Please have your minor child bring the completed form to the Resort, as he/she will be required to present it at check-in./pp /pThank you for your cooperation in this matter./ppWe hope (GUEST NAME) will have a most enjoyable stay in our (RESORT NAME)./pp /pSincerely,/pp /p /p /p /hr /",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
