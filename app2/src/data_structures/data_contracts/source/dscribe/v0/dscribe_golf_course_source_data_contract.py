"""Source Data Contract Template for GOLF_COURSE"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe GOLF_COURSE ChannelItem Data
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
        example="/FACSVC/All Content/Golf Course",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Types(BaseModel):
    """
    Class For Dscribe GOLF_COURSE Types Data
    """

    enterprise: str = Field(
        ...,
        alias="enterprise",
        name="",
        description="",
        example="Facility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finder: Optional[str] = Field(
        None,
        alias="finder",
        name="",
        description="",
        example="Recreation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finder_list: Optional[List[str]] = Field(
        None,
        alias="finderList",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ExternalSystems(BaseModel):
    """
    Class For Dscribe GOLF_COURSE ExternalSystems Data
    """

    types: Types = Field(
        ...,
        alias="types",
        name="",
        description="",
    )


class FacilityHierarchyItem(BaseModel):
    """
    Class For Dscribe GOLF_COURSE FacilityHierarchyItem Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="90001145",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="GolfCourse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_level: str = Field(
        ...,
        alias="facilityLevel",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Golf Course",
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

    name_text: str = Field(
        ...,
        alias="nameText",
        name="",
        description="",
        example="Walt Disney World Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: str = Field(
        ...,
        alias="nameHtml",
        name="",
        description="",
        example="<strong>Walt Disney World</strong>\xae Resort",
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


class Coordinate(BaseModel):
    """
    Class For Dscribe GOLF_COURSE Coordinate Data
    """

    location_type: str = Field(
        ...,
        alias="locationType",
        name="",
        description="",
        example="Guest Entrance",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    latitude: str = Field(
        ...,
        alias="latitude",
        name="",
        description="",
        example="28.403456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    longitude: str = Field(
        ...,
        alias="longitude",
        name="",
        description="",
        example="-81.592361",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeGolfCourseModel(BaseModel):
    """
    PPayload class for DScribeGolfCourseModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Golf Course"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR golf course facility enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "GolfCourse"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="90001145",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="GolfCourse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Disney's Lake Buena Vista Golf Course",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site_channel: List[str] = Field(
        ...,
        alias="siteChannel",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    channel: List[ChannelItem] = Field(
        ...,
        alias="channel",
        name="",
        description="",
    )

    external_systems: ExternalSystems = Field(
        ...,
        alias="externalSystems",
        name="",
        description="",
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

    contact: Optional[List[str]] = Field(
        None,
        alias="Contact",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Golf Course",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="80001146",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operational_status: Optional[str] = Field(
        None,
        alias="operationalStatus",
        name="",
        description="",
        example="Operating",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operational_status_id: Optional[str] = Field(
        None,
        alias="operationalStatusId",
        name="",
        description="",
        example="80000299",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: Optional[str] = Field(
        None,
        alias="parentFacility",
        name="",
        description="",
        example="114147",
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

    disney_owned_operated: Optional[bool] = Field(
        None,
        alias="disneyOwnedOperated",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schedule_id: Optional[str] = Field(
        None,
        alias="scheduleId",
        name="",
        description="",
        example="411287361",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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

    coordinates: Optional[List[Coordinate]] = Field(
        None,
        alias="coordinates",
        name="",
        description="",
    )
