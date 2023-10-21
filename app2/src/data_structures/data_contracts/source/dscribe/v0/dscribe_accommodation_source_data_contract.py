"""Source Data Contract Template for ACCOMMODATION"""

from __future__ import annotations

from typing import List, Optional

from datetime import date

from pydantic import BaseModel, Field


class FacilityHierarchyItem(BaseModel):

    """
    Class For Dscribe ACCOMMODATION FacilityHierarchyItem Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="109702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Accommodation",
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
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Standard",
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


class SourceItem(BaseModel):

    """
    Class For Dscribe ACCOMMODATION SourceItem Data
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

    name_id: str = Field(
        ...,
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

    short_name_id: str = Field(
        ...,
        alias="shortNameId",
        name="",
        description="",
        example="336474",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ParentFacilitySystemCode(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ParentFacilitySystemCode Data
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
        example="Q",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceItem1(BaseModel):

    """
    Class For Dscribe ACCOMMODATION SourceItem1 Data
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
    Class For Dscribe ACCOMMODATION SystemCode Data
    """

    source: List[SourceItem1] = Field(
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
        example="Q",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Flags(BaseModel):

    """
    Class For Dscribe ACCOMMODATION Flags Data
    """

    ada: bool = Field(
        ...,
        alias="ADA",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    concierge_flag: Optional[bool] = Field(
        None,
        alias="conciergeFlag",
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

    suite_flag: Optional[bool] = Field(
        None,
        alias="suiteFlag",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kitchen: Optional[bool] = Field(
        None,
        alias="Kitchen",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lock_off: Optional[bool] = Field(
        None,
        alias="Lock-Off",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ValidityDate(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ValidityDate Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80001082",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2021-01-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: date = Field(
        ...,
        alias="endDate",
        name="",
        description="",
        example="2022-04-30",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Component(BaseModel):

    """
    Class For Dscribe ACCOMMODATION Component Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="109702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    product_year: str = Field(
        ...,
        alias="productYear",
        name="",
        description="",
        example="Product Year 2021",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_year_id: str = Field(
        ...,
        alias="productYearId",
        name="",
        description="",
        example="15487346",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_adult_threshold: str = Field(
        ...,
        alias="additionalAdultThreshold",
        name="",
        description="",
        example="3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_dates: List[ValidityDate] = Field(
        ...,
        alias="validityDates",
        name="",
        description="",
    )


class ChannelItem(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ChannelItem Data
    """

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
        example="/Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Types(BaseModel):

    """
    Class For Dscribe ACCOMMODATION Types Data
    """

    enterprise: str = Field(
        ...,
        alias="enterprise",
        name="",
        description="",
        example="Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ExternalSystems(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ExternalSystems Data
    """

    types: Types = Field(
        ...,
        alias="types",
        name="",
        description="",
    )


class ConfigurationItem(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ConfigurationItem Data
    """

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="DAKL - Savanna View - Club Level Access - QG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity: int = Field(
        ...,
        alias="quantity",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class BeddingItem(BaseModel):

    """
    Class For Dscribe ACCOMMODATION BeddingItem Data
    """

    category: str = Field(
        ...,
        alias="category",
        name="",
        description="",
        example="varies",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    configuration: List[ConfigurationItem] = Field(
        ...,
        alias="configuration",
        name="",
        description="",
    )


class ParentAccommodation(BaseModel):

    """
    Class For Dscribe ACCOMMODATION ParentAccommodation Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="109702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeAccommodationModel(BaseModel):

    """Payload class for DScribeAccommodationModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR attraction enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Accommodation"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="109702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Accommodation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="DAKL - Savanna View - Club Level Access - QG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group: Optional[str] = Field(
        None,
        alias="taxGroup",
        name="",
        description="",
        example="WDW Orange County Resorts",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_id: Optional[str] = Field(
        None,
        alias="taxGroupId",
        name="",
        description="",
        example="80007254",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="80001082",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Standard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: Optional[str] = Field(
        None,
        alias="subTypeId",
        name="",
        description="",
        example="80001240",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    view_type: Optional[str] = Field(
        None,
        alias="viewType",
        name="",
        description="",
        example="Savanna View",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    view_type_id: Optional[str] = Field(
        None,
        alias="viewTypeId",
        name="",
        description="",
        example="80000413",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: Optional[str] = Field(
        None,
        alias="parentFacility",
        name="",
        description="",
        example="80010395",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_hierarchy: Optional[List[FacilityHierarchyItem]] = Field(
        None,
        alias="facilityHierarchy",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility_system_codes: Optional[List[ParentFacilitySystemCode]] = Field(
        None,
        alias="parentFacilitySystemCodes",
        name="",
        description="",
    )

    description: Optional[str] = Field(
        None,
        alias="description",
        name="",
        description="",
        example="Savanna View - Club Level Access",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_adult_occupancy: Optional[str] = Field(
        None,
        alias="maxAdultOccupancy",
        name="",
        description="",
        example="4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_non_adult_occupancy: Optional[str] = Field(
        None,
        alias="maxNonAdultOccupancy",
        name="",
        description="",
        example="3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_non_infant_occupancy: Optional[str] = Field(
        None,
        alias="maxNonInfantOccupancy",
        name="",
        description="",
        example="4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_occupancy: Optional[str] = Field(
        None,
        alias="maxOccupancy",
        name="",
        description="",
        example="4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_adult_threshold: Optional[str] = Field(
        None,
        alias="additionalAdultThreshold",
        name="",
        description="",
        example="3",
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

    components: Optional[List[Component]] = Field(
        None,
        alias="components",
        name="",
        description="",
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

    external_systems: Optional[ExternalSystems] = Field(
        None,
        alias="externalSystems",
        name="",
        description="",
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

    bedding: Optional[List[BeddingItem]] = Field(
        None,
        alias="bedding",
        name="",
        description="",
    )

    revenue_classification: Optional[List[str]] = Field(
        None,
        alias="RevenueClassification",
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

    amenity: Optional[List[str]] = Field(
        None,
        alias="Amenity",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_accommodation: Optional[ParentAccommodation] = Field(
        None,
        alias="parentAccommodation",
        name="",
        description="",
    )

    parent_facility_content_type: Optional[str] = Field(
        None,
        alias="parentFacilityContentType",
        name="",
        description="",
        example="Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    target_audience: Optional[List[str]] = Field(
        None,
        alias="targetAudience",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
