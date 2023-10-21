"""Source Data Contract Template for RESORT"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class FacilityHierarchyItem(BaseModel):

    """
    Payload class for DScribe RESORT FacilityHierarchyItem
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Resort",
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
        example="Walt Disney World Owned & Operated",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Deluxe Villa",
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
    Payload class for DScribe Resort Coordinate
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
        example="28.4164047147",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    longitude: str = Field(
        ...,
        alias="longitude",
        name="",
        description="",
        example="-81.5737873865",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Address(BaseModel):

    """
    Payload class for DScribe Resort Address
    """

    address1: str = Field(
        ...,
        alias="address1",
        name="",
        description="",
        example="4600 North World Drive",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    address2: Optional[str] = Field(
        None,
        alias="address2",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    city: str = Field(
        ...,
        alias="city",
        name="",
        description="",
        example="Lake Buena Vista",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    state: str = Field(
        ...,
        alias="state",
        name="",
        description="",
        example="Florida",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    state_code: str = Field(
        ...,
        alias="stateCode",
        name="",
        description="",
        example="FL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    postal_code: str = Field(
        ...,
        alias="postalCode",
        name="",
        description="",
        example="32830-8413",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    country: str = Field(
        ...,
        alias="country",
        name="",
        description="",
        example="United States",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    country_code: str = Field(
        ...,
        alias="countryCode",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceItem(BaseModel):

    """
    Payload class for DScribe Resort SourceItem
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Disney Property Management System",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_id: Optional[str] = Field(
        None,
        alias="nameId",
        name="",
        description="",
        example="80000071",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    short_name: str = Field(
        ...,
        alias="shortName",
        name="",
        description="",
        example="DPMS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    short_name_id: Optional[str] = Field(
        None,
        alias="shortNameId",
        name="",
        description="",
        example="336474",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SystemCode(BaseModel):

    """
    Payload class for DScribe RESORT SystemCode
    """

    source: List[SourceItem] = Field(
        ...,
        alias="source",
        name="",
        description="",
    )

    code_name: str = Field(
        ...,
        alias="codeName",
        name="",
        description="",
        example="5xID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_value: str = Field(
        ...,
        alias="codeValue",
        name="",
        description="",
        example="BLT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Flags(BaseModel):

    """
    Payload class for DScribe Resort Flags
    """

    dvc_resort: Optional[bool] = Field(
        None,
        alias="dvcResort",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    on_property: Optional[bool] = Field(
        None,
        alias="On Property",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wdpro_sellable: Optional[bool] = Field(
        None,
        alias="WDPROSellable",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ChannelItem(BaseModel):

    """
    Payload class for DScribe Resort ChannelItem
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
        example="/D3/Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Types(BaseModel):

    """
    Payload class for DScribe RESORT Types
    """

    enterprise: str = Field(
        ...,
        alias="enterprise",
        name="",
        description="",
        example="Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finder: Optional[str] = Field(
        None,
        alias="finder",
        name="",
        description="",
        example="resort",
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
    Payload class for DScribe Resort ExternalSystems
    """

    types: Types = Field(
        ...,
        alias="types",
        name="",
        description="",
    )


class DScribeResortModel(BaseModel):

    """Payload class for DScribeResortModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR resort facility enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Resort"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Bay Lake Tower",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Walt Disney World Owned & Operated",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80001061",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: str = Field(
        ...,
        alias="subType",
        name="",
        description="",
        example="Deluxe Villa",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: str = Field(
        ...,
        alias="subTypeId",
        name="",
        description="",
        example="80001206",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    area: Optional[str] = Field(
        None,
        alias="area",
        name="",
        description="",
        example="Magic Kingdom Resort Area",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    area_id: Optional[str] = Field(
        None,
        alias="areaId",
        name="",
        description="",
        example="10406",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    resort_campus: Optional[List[str]] = Field(
        None,
        alias="resortCampus",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operational_status: str = Field(
        ...,
        alias="operationalStatus",
        name="",
        description="",
        example="Operating",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operational_status_id: str = Field(
        ...,
        alias="operationalStatusId",
        name="",
        description="",
        example="80000299",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: str = Field(
        ...,
        alias="parentFacility",
        name="",
        description="",
        example="324159",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_hierarchy: List[FacilityHierarchyItem] = Field(
        ...,
        alias="facilityHierarchy",
        name="",
        description="",
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

    disney_owned_operated: bool = Field(
        ...,
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

    check_in: Optional[str] = Field(
        None,
        alias="checkIn",
        name="",
        description="",
        example="4:00:00 PM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    check_out: Optional[str] = Field(
        None,
        alias="checkOut",
        name="",
        description="",
        example="11:00:00 AM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    address: Address = Field(
        ...,
        alias="address",
        name="",
        description="",
    )

    phone_number: Optional[str] = Field(
        None,
        alias="phoneNumber",
        name="",
        description="",
        example="407-824-1000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    system_codes: Optional[List[SystemCode]] = Field(
        None,
        alias="systemCodes",
        name="",
        description="",
    )

    flags: Optional[Flags] = Field(
        None,
        alias="flags",
        name="",
        description="",
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

    room_category: Optional[List[str]] = Field(
        None,
        alias="RoomCategory",
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
