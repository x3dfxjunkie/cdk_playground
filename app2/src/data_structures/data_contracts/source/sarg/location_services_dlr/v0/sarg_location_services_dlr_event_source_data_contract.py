"""Source Data Contract Template for SARG Location Services DLR Data"""

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
    area: Optional[RegionDetails] = Field(
        None,
        alias="AREA",
        name="",
        description="",
    )

    destination: Optional[RegionDetails] = Field(
        None,
        alias="DESTINATION",
        name="",
        description="",
    )

    zone: Optional[RegionDetails] = Field(
        None,
        alias="ZONE",
        name="",
        description="",
    )

    territory: Optional[RegionDetails] = Field(
        None,
        alias="TERRITORY",
        name="",
        description="",
    )

    land: Optional[RegionDetails] = Field(
        None,
        alias="LAND",
        name="",
        description="",
    )


class ThirdPartyIdentifiers(BaseModel):
    adobe_places: Optional[str] = Field(
        None,
        alias="adobe_places",
        name="",
        description="",
        example="bbbbbbbb-2222-bbbb-2222-22222222d939",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SARGLocationServicesDLREventModel(BaseModel):
    """Payload class for SARGLocationServicesDLREventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Location Services DLR Event"
        stream_name = ""
        description = """Guest Location events for DLR"""
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
        example="{AAAAAAAA-1111-AAAA-1111-11111111773B}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region_id: str = Field(
        ...,
        alias="regionId",
        name="",
        description="",
        example="disneyland-park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region_level: str = Field(
        ...,
        alias="regionLevel",
        name="",
        description="",
        example="AREA",
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

    source_id: str = Field(
        ...,
        alias="sourceId",
        name="",
        description="",
        example="330339",
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
        example=1686087445,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_seen: int = Field(
        ...,
        alias="lastSeen",
        name="",
        description="",
        example=1686087584,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    process_timestamp: int = Field(
        ...,
        alias="processTimestamp",
        name="",
        description="",
        example=1686087985257,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    publish_timestamp: int = Field(
        ...,
        alias="publishTimestamp",
        name="",
        description="",
        example=1686087985681,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    active_regions: Optional[ActiveRegions] = Field(
        None,
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
