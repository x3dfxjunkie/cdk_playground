"""Source Data Contract for Dinetime site"""


from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Site(BaseModel):
    """Site Class"""

    address: str = Field(
        ...,
        alias="Address",
        name="Site Adress",
        description="Venue's Address of the record",
        example="201 South S Studio Dr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    brand_uid: str = Field(
        ...,
        alias="BrandUID",
        name="Brand Unique Identifier",
        description="Venue's brand unique identifier",
        example="99999999-9b55-11e4-92f6-22000b510bd7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    city: str = Field(
        ...,
        alias="City",
        name="Site City",
        description="Venue's city where it's placed",
        example="Lake Buena Vista",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    company_uid: str = Field(
        ...,
        alias="CompanyUID",
        name="Company Unique Identifier",
        description="Globally unique identifier for a company - this is provided by QSR",
        example="99999999-9b55-11e4-92f6-22000b510bd7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    contact_number: str = Field(
        ...,
        alias="ContactNumber",
        name="Venue's Contact Number",
        description="Venue's contact number without LADA code",
        example="1234567890",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    country: str = Field(
        ...,
        alias="Country",
        name="Venue's Country",
        description="Venue's site country",
        example="United States",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    county: Optional[str] = Field(
        None,
        alias="County",
        name="Venue's County",
        description="Venue's County",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    creation_time: datetime = Field(
        ...,
        alias="CreationTime",
        name="Record Creation Time",
        description="Creating time of the record in ISO 8601 format",
        example="2015-01-13T18:52:21+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cuisines: Optional[List[str]] = Field(
        None,
        alias="Cuisines",
        name="Venue's cuisine types",
        description="Cuisine types and details inside the venues",
        example=["American"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    customer_site_id: str = Field(
        ...,
        alias="CustomerSiteId",
        name="Customer Site Identifier",
        description="Customizable site identifier",
        example="16",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    display_name: str = Field(
        ...,
        alias="DisplayName",
        name="Display Name",
        description="Venue's display name",
        example="Crown of Corellia Dining Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    hours: str = Field(
        ...,
        alias="Hours",
        name="Venue's Operating Hours",
        description="Venue's daily operating hours",
        example="Sun: 7:00 AM - 10:00 PM\r\nMon: 7:00 AM - 10:00 PM\r\nTue: 7:00 AM - 10:00 PM\r\nWed: 7:00 AM - 10:00 PM\r\nThu: 7:00 AM - 10:00 PM\r\nFri: 7:00 AM - 10:00 PM\r\nSat: 7:00 AM - 10:00 PM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    iid: int = Field(
        ...,
        alias="IID",
        name="Integer Identifier",
        description="Venue's integer identifier",
        example=1234,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Last Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2023-02-05T08:00:40+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    latitude: float = Field(
        ...,
        alias="Latitude",
        name="Latitude",
        description="Venue's latitude",
        example=28.3663784,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    longitude: float = Field(
        ...,
        alias="Longitude",
        name="Longitude",
        description="Venue's longitude",
        example=-81.5559417,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Venue's name",
        example="SWGS Crown of Corellia Dining Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    postal: str = Field(
        ...,
        alias="Postal",
        name="Postal",
        description="Venue's postal zip code",
        example="32830",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary_cuisine: Optional[str] = Field(
        None,
        alias="PrimaryCuisine",
        name="Primary Cusine",
        description="Primary cuisine of the site.",
        example="American",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site_uid: str = Field(
        ...,
        alias="SiteUID",
        name="Site Unique Identifier",
        description="Venue's unique site ID",
        example="99999999-16d1-4a0b-82e9-a98e05be39db",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    state: str = Field(
        ...,
        alias="State",
        name="Venue's State",
        description="Venue's state where is placed.",
        example="Florida",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    time_zone_id: str = Field(
        ...,
        alias="TimeZoneId",
        name="Time Zone Identifier",
        description="Venue's timezone ID",
        example="US/Eastern",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Sites(BaseModel):
    """Sites Class"""

    sites: List[Site] = Field(
        ..., alias="Sites", name="Sites referring to a set sites", description="It refers to the set venue details"
    )


class DineTimeSitesModel(BaseModel):
    """DineTimeSitesModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Sites Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Sites Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    sites: Sites = Field(
        ...,
        alias="Sites",
        name="Sites referring to venues data",
        description="It refers to the venue details",
    )
