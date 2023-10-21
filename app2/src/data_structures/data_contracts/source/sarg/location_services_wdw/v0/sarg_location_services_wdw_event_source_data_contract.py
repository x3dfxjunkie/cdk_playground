"""Source Data Contract Template for SARG Location Services WDW Data"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class RegionDetails(BaseModel):
    region_id: str = Field(
        ...,
        alias="regionId",
        name="",
        description="",
        example="mk-monorail",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_seen: int = Field(
        ...,
        alias="lastSeen",
        name="",
        description="",
        example=1686083242,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_id: Optional[str] = Field(
        None,
        alias="sourceId",
        name="",
        description="",
        example="90002656",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_source_ids: Optional[str] = Field(
        None,
        alias="additionalSourceIds",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ActiveRegions(BaseModel):
    destination: Optional[RegionDetails] = Field(
        None,
        alias="DESTINATION",
        name="",
        description="",
    )

    territory: Optional[RegionDetails] = Field(
        None,
        alias="TERRITORY",
        name="",
        description="",
    )

    area: Optional[RegionDetails] = Field(
        None,
        alias="AREA",
        name="",
        description="",
    )

    land: Optional[RegionDetails] = Field(
        None,
        alias="LAND",
        name="",
        description="",
    )

    location: Optional[RegionDetails] = Field(
        None,
        alias="LOCATION",
        name="",
        description="",
    )


class ThirdPartyIdentifiers(BaseModel):
    adobe_places: Optional[str] = Field(
        None,
        alias="adobe_places",
        name="",
        description="",
        example="bbbbbbbb-2222-bbbb-2222-22222222b469",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SARGLocationServicesWDWEventModel(BaseModel):
    """Payload class for SARGLocationServicesWDWEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Location Services WDW Event"
        stream_name = ""
        description = """Guest Location events for WDW"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="",
        description="",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="{AAAAAAAA-1111-AAAA-1111-1111111119F6}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region_id: str = Field(
        ...,
        alias="regionId",
        name="",
        description="",
        example="magic-kingdom-parking",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region_level: str = Field(
        ...,
        alias="regionLevel",
        name="",
        description="",
        example="LAND",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region_tags: Optional[List[str]] = Field(
        None,
        alias="regionTags",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_id: Optional[str] = Field(
        None,
        alias="sourceId",
        name="",
        description="",
        example="400656",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_source_ids: Optional[str] = Field(
        None,
        alias="additionalSourceIds",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="ABANDONED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_seen: int = Field(
        ...,
        alias="firstSeen",
        name="",
        description="",
        example=1686089357,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_seen: int = Field(
        ...,
        alias="lastSeen",
        name="",
        description="",
        example=1686089357,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    process_timestamp: int = Field(
        ...,
        alias="processTimestamp",
        name="",
        description="",
        example=1690639680036,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    publish_timestamp: int = Field(
        ...,
        alias="publishTimestamp",
        name="",
        description="",
        example=1690639887843,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    active_regions: ActiveRegions = Field(
        ...,
        alias="activeRegions",
        name="",
        description="",
    )

    third_party_identifiers: Optional[ThirdPartyIdentifiers] = Field(
        None,
        alias="thirdPartyIdentifiers",
        name="",
        description="",
    )

    subscriptions: List[str] = Field(
        ...,
        alias="subscriptions",
        name="",
        description="",
        example=["shuri"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
