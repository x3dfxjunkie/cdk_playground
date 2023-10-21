"""Source Data Contract Template for SERVICES"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):

    """
    Class for Dscribe SERVICES ChannelItem Data
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
        example="/D3/Services",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeServicesModel(BaseModel):

    """Payload class for DscribeServicesModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Services"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR services enterprise metadata. "  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Services"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="19610173",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Services",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Happy Birthday, Walt Disney!",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schedule_id: Optional[str] = Field(
        None,
        alias="scheduleId",
        name="",
        description="",
        example="62307",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    destination: Optional[str] = Field(
        None,
        alias="destination",
        name="",
        description="",
        example="DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="MDX Overview",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="16892586",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Guest Services",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: Optional[str] = Field(
        None,
        alias="subTypeId",
        name="",
        description="",
        example="16892584",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: List[str] = Field(
        ...,
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

    point_of_interest: Optional[List[str]] = Field(
        None,
        alias="PointOfInterest",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
