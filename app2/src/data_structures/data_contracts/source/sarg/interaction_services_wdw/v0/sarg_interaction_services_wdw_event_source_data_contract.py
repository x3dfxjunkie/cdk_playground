"""Source Data Contract Template for SARG WDW Interaction Services Events"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    rule_id: str = Field(
        ...,
        alias="ruleId",
        name="",
        description="",
        example="dak-generic-rode-attraction",
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

    facility_name: Optional[str] = Field(
        None,
        alias="facilityName",
        name="",
        description="",
        example="it's a small world",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SARGInteractionServicesWDWEventModel(BaseModel):
    """Payload class for SARGInteractionServicesWDWEventModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Interaction Services WDW Event"
        stream_name = ""
        description = """Guest Interaction events for WDW"""
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
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: str = Field(
        ...,
        alias="guestId",
        name="",
        description="",
        example="111111155",
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
        example="bbbbbbbb-2222-bbbb-2222-222222226be7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    interaction_id: str = Field(
        ...,
        alias="interactionId",
        name="",
        description="",
        example="dak-generic-rode-attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    interaction_per_facility: str = Field(
        ...,
        alias="interactionPerFacility",
        name="",
        description="",
        example="RODE_ATTRACTION#18665186",
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
        example="avatar-flight-of-passage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_id: str = Field(
        ...,
        alias="sourceId",
        name="",
        description="",
        example="18665186",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_type: Optional[str] = Field(
        None,
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
        example=1653757952000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ttl: int = Field(
        ...,
        alias="ttl",
        name="",
        description="",
        example=1653758433,
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
