"""Source Data Contract Template for ENTERTAINMENT"""


from __future__ import annotations

from typing import List, Optional

from datetime import date

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe ENTERTAINMENT ChannelItem Data
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
        example="/D3/Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class FacilityHierarchyItem(BaseModel):
    """
    Class For Dscribe ENTERTAINMENT FacilityHierarchyItem Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="12248",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_level: Optional[str] = Field(
        None,
        alias="facilityLevel",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Nighttime Spectacular",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Magic Kingdom Resort Area",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: Optional[str] = Field(
        None,
        alias="nameText",
        name="",
        description="",
        example="Walt Disney World Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: Optional[str] = Field(
        None,
        alias="nameHtml",
        name="",
        description="",
        example="<strong>Walt Disney World</strong>\xae Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    destination: Optional[str] = Field(
        None,
        alias="destination",
        name="",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeEntertainmentModel(BaseModel):
    """
    Payload class for DScribeEntertainmentModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entertainment"
        stream_name = ""
        description = (
            "Contains all enterprise reference data for entertainment shows at WDW and DLR from Dscribe."  # optional
        )
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Entertainment"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="12248",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Entertainment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Fantasy In The Sky Fireworks",
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

    schedule_id: Optional[str] = Field(
        None,
        alias="scheduleId",
        name="",
        description="",
        example="19322691",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    destination: str = Field(
        ...,
        alias="destination",
        name="",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Nighttime Spectacular",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="44852",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: Optional[str] = Field(
        None,
        alias="parentFacility",
        name="",
        description="",
        example="80007958",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_hierarchy: Optional[List[FacilityHierarchyItem]] = Field(
        None,
        alias="facilityHierarchy",
        name="",
        description="",
    )

    parent_facility_content_type: Optional[str] = Field(
        None,
        alias="parentFacilityContentType",
        name="",
        description="",
        example="Facility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operating_status: str = Field(
        ...,
        alias="operatingStatus",
        name="",
        description="",
        example="Operates Seasonally",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operating_status_id: Optional[str] = Field(
        None,
        alias="operatingStatusId",
        name="",
        description="",
        example="80000300",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    duration: str = Field(
        ...,
        alias="duration",
        name="",
        description="",
        example="00:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sellable_online: Optional[bool] = Field(
        None,
        alias="sellableOnline",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_locations: Optional[List[str]] = Field(
        None,
        alias="serviceLocations",
        name="",
        description="",
        example=["example"],
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

    character: Optional[List[str]] = Field(
        None,
        alias="Character",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    open_date: Optional[date] = Field(
        None,
        alias="openDate",
        name="",
        description="",
        example="1998-04-22",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    policy: Optional[List[str]] = Field(
        None,
        alias="Policy",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
