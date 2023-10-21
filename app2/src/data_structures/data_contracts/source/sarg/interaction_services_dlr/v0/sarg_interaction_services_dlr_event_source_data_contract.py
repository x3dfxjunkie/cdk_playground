"""Source Data Contract Template for SARG DLR Interaction Services Events """

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    facility_name: str = Field(
        ...,
        alias="facilityName",
        name="",
        description="",
        example="Soarin' Around the World",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rule_id: str = Field(
        ...,
        alias="ruleId",
        name="",
        description="",
        example="dca-generic-rode-attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expiring_ttl: Optional[str] = Field(
        None,
        alias="expiringTtl",
        name="",
        description="",
        example="true",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SARGInteractionServicesDLREventModel(BaseModel):
    """Payload class for SARGInteractionServicesDLREventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Interaction Services DLR Event"
        stream_name = ""
        description = """Guest Interaction events for DLR"""
        unique_identifier = ["id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    confidence: str = Field(
        ...,
        alias="confidence",
        name="",
        description="",
        example="HIGH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cooldown_timeout: int = Field(
        ...,
        alias="cooldownTimeout",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="111111196112",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="",
        description="",
        example="xband-longrange-public-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="bbbbbbbb-2222-bbbb-2222-2222222211ef",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    interaction_id: str = Field(
        ...,
        alias="interactionId",
        name="",
        description="",
        example="dca-generic-rode-attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    interaction_per_facility: str = Field(
        ...,
        alias="interactionPerFacility",
        name="",
        description="",
        example="RODE_ATTRACTION#353431",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    metadata: Metadata = Field(
        ...,
        alias="metadata",
        name="",
        description="",
    )

    region_id: Optional[str] = Field(
        None,
        alias="regionId",
        name="",
        description="",
        example="soarin-around-the-world",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_id: str = Field(
        ...,
        alias="sourceId",
        name="",
        description="",
        example="353431",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_type: str = Field(
        ...,
        alias="sourceType",
        name="",
        description="",
        example="RIDE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="SUCCESS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    timestamp: int = Field(
        ...,
        alias="timestamp",
        name="",
        description="",
        example=1683504583000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ttl: int = Field(
        ...,
        alias="ttl",
        name="",
        description="",
        example=1683509217215,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="RODE_ATTRACTION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
