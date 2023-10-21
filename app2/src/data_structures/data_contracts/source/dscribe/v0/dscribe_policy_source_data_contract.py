"""Source Data Contract Template for POLICY"""

from __future__ import annotations

from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):

    """
    Payload class for DScribe POLICY ChannelItem
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
        example="/FACSVC/All Content/Policy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ActionablePlanItem(BaseModel):

    """
    Payload class for DScribe POLICY ActionablePlanItem
    """

    value: Optional[str] = Field(
        None,
        alias="value",
        name="",
        description="",
        example="50",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value_type: Optional[str] = Field(
        None,
        alias="valueType",
        name="",
        description="",
        example="Amount",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value_type_id: Optional[str] = Field(
        None,
        alias="valueTypeId",
        name="",
        description="",
        example="80000261",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_count: Optional[str] = Field(
        None,
        alias="startCount",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_count: Optional[str] = Field(
        None,
        alias="endCount",
        name="",
        description="",
        example="44",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    duration_count_unit: Optional[str] = Field(
        None,
        alias="durationCountUnit",
        name="",
        description="",
        example="Days",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    duration_count_unit_id: Optional[str] = Field(
        None,
        alias="durationCountUnitId",
        name="",
        description="",
        example="80000257",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    booking_type: Optional[str] = Field(
        None,
        alias="bookingType",
        name="",
        description="",
        example="Prior to Arrival",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    booking_type_id: Optional[str] = Field(
        None,
        alias="bookingTypeId",
        name="",
        description="",
        example="80000258",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accounting_type: Optional[str] = Field(
        None,
        alias="accountingType",
        name="",
        description="",
        example="Per Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accounting_type_id: Optional[str] = Field(
        None,
        alias="accountingTypeId",
        name="",
        description="",
        example="281779",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    effective_start_time: Optional[str] = Field(
        None,
        alias="effectiveStartTime",
        name="",
        description="",
        example="00:00:00:0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    effective_end_time: Optional[str] = Field(
        None,
        alias="effectiveEndTime",
        name="",
        description="",
        example="00:00:00:0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribePolicyModel(BaseModel):

    """Payload class for DScribePolicyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Policy"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR policy enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Policy"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="100577",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Policy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Unescorted Minors",
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

    name_html: str = Field(
        ...,
        alias="nameHtml",
        name="",
        description="",
        example="Unescorted Minors",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: str = Field(
        ...,
        alias="nameText",
        name="",
        description="",
        example="Unescorted Minors",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Cast Member Procedure",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80000333",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    restriction_type: Optional[str] = Field(
        None,
        alias="restrictionType",
        name="",
        description="",
        example="Age Restriction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    marketing_message: Optional[List[str]] = Field(
        None,
        alias="MarketingMessage",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Restriction / Requirement",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: Optional[str] = Field(
        None,
        alias="subTypeId",
        name="",
        description="",
        example="80001062",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    actionable_plan: Optional[List[ActionablePlanItem]] = Field(
        None,
        alias="actionablePlan",
        name="",
        description="",
    )
