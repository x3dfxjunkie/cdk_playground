"""Source Data Contract Template for Pointofinterest"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class FacilityHierarchyItem(BaseModel):
    """Class for Dscribe Pointofinterest FacilityHierarchyItem Data"""

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="80069772",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Facility",
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
        example="Primary Distribution",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Disney's Animal Kingdom Theme Park Resort Area",
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


class ChannelItem(BaseModel):
    """Class For Dscribe Pointofinterest ChannelItem Data"""

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
        example="/Activity Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class FacilityAssociationItem(BaseModel):
    """Class for Dscribe Pointofinterest FacilityAssociationItem Data"""

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Primary Distribution",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80000247",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replacements: List[str] = Field(
        ...,
        alias="Replacements",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility: Optional[List[str]] = Field(
        None,
        alias="Facility",
        name="",
        description="",
        example=["example"],
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

    resort: Optional[List[str]] = Field(
        None,
        alias="Resort",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribePointOfInterestModel(BaseModel):
    """Payload class for Dscribe Pointofinterest"""

    class Config:
        """Payload Level Metadata"""

        title = "Point of Interest"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR contact enterprise metadata"  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "PointOfInterest"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="16886176",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="PointOfInterest",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Animal Kingdom Parade Route 3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Animal Kingdom Parade Route 3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    description_text: str = Field(
        ...,
        alias="descriptionText",
        name="",
        description="",
        example="Animal Kingdom Parade Route 3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Primary Distribution",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    longitude: str = Field(
        ...,
        alias="longitude",
        name="",
        description="",
        example="-81.59149",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    latitude: str = Field(
        ...,
        alias="latitude",
        name="",
        description="",
        example="28.357626",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: Optional[str] = Field(
        None,
        alias="parentFacility",
        name="",
        description="",
        example="80007823",
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
    channel: Optional[List[ChannelItem]] = Field(
        None,
        alias="channel",
        name="",
        description="",
    )

    facility_association: Optional[List[FacilityAssociationItem]] = Field(
        None,
        alias="facilityAssociation",
        name="",
        description="",
    )
