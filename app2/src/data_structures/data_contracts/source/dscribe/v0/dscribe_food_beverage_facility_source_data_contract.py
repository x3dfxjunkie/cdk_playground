"""Source Data Contract Template for FOOD_BEVERAGE_FACILITY"""


from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field


class FacilityHierarchyItem(BaseModel):
    """
    Class For Dscribe FOOD_BEVERAGE_FACILITY FacilityHierarchyItem Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="108856",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="FoodBeverageFacility",
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
        example="Counter",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Epcot Resort Area",
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
    Class For Dscribe FOOD_BEVERAGE_FACILITY Coordinate Data
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
        example="28.36560689",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    longitude: str = Field(
        ...,
        alias="longitude",
        name="",
        description="",
        example="-81.5591418737",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ChannelItem(BaseModel):
    """
    Class For Dscribe FOOD_BEVERAGE_FACILITY ChannelItem Data
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
        example="/D3/Food & Beverage Facility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Types(BaseModel):
    """
    Class For Dscribe FOOD_BEVERAGE_FACILITY Types Data
    """

    enterprise: Optional[str] = Field(
        None,
        alias="enterprise",
        name="",
        description="",
        example="FoodBeverageFacility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finder: Optional[str] = Field(
        None,
        alias="finder",
        name="",
        description="",
        example="restaurant",
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
    Class For Dscribe FOOD_BEVERAGE_FACILITY ExternalSystems Data
    """

    types: Types = Field(
        ...,
        alias="types",
        name="",
        description="",
    )

    url_friendly_id: Optional[str] = Field(
        None,
        alias="urlFriendlyId",
        name="",
        description="",
        example="pym-test-kitchen",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeFoodBeverageFacilityModel(BaseModel):
    """Payload class for DScribeFoodBeverageFacilityModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Food Beverage Facility"
        stream_name = ""
        description = "Contains all information about WDW and DLR food and beverage facility enterprise metadata. This includes quick service and table service locations."  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "FoodBeverageFacility"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="108856",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="FoodBeverageFacility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Kimonos Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Counter",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="80001153",
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
        example="80069789",
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

    coordinates: Optional[List[Coordinate]] = Field(
        None,
        alias="coordinates",
        name="",
        description="",
    )

    reservations_accepted: Optional[bool] = Field(
        None,
        alias="reservationsAccepted",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    admission_required: Optional[bool] = Field(
        None,
        alias="admissionRequired",
        name="",
        description="",
        example=True,
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
        example="18592634",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_systems: Optional[ExternalSystems] = Field(
        None,
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

    meal_period: Optional[List[str]] = Field(
        None,
        alias="MealPeriod",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    services: Optional[List[str]] = Field(
        None,
        alias="Services",
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

    activity_product: Optional[List[str]] = Field(
        None,
        alias="ActivityProduct",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    menu_group: Optional[List[str]] = Field(
        None,
        alias="MenuGroup",
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

    entertainment: Optional[List[str]] = Field(
        None,
        alias="Entertainment",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event: Optional[List[str]] = Field(
        None,
        alias="Event",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
