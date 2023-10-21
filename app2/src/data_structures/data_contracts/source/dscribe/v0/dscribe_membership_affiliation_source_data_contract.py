"""Source Data Contract Template for MEMBERSHIP_AFFILIATION"""

from __future__ import annotations

from typing import List, Optional

from datetime import date

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe MEMBERSHIP_AFFILIATION ChannelItem Data
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
        example="/Membership Affiliation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMembershipAffiliationModel(BaseModel):
    """
    Payload class for DScribeMembershipAffiliationModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Membership Affiliation"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR contact enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "MembershipAffiliation"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="1201",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MembershipAffiliation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Tickets - Corp Alliance and Participants",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Tickets - Corp Alliance and Participants",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Disney Employee",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="1235",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sales_channel_code: Optional[str] = Field(
        None,
        alias="salesChannelCode",
        name="",
        description="",
        example="TKT PARTI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2004-01-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2050-12-31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_type: str = Field(
        ...,
        alias="discountType",
        name="",
        description="",
        example="Percent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_type_id: str = Field(
        ...,
        alias="discountTypeId",
        name="",
        description="",
        example="80000210",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_value: str = Field(
        ...,
        alias="discountValue",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    billing_name: Optional[str] = Field(
        None,
        alias="billingName",
        name="",
        description="",
        example="Aulani - Disney Visa Packages",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    billing_code: Optional[str] = Field(
        None,
        alias="billingCode",
        name="",
        description="",
        example="04250",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    billing_trap_code: Optional[str] = Field(
        None,
        alias="billingTrapCode",
        name="",
        description="",
        example="Walt Disney Travel Company",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    billing_trap_description: Optional[str] = Field(
        None,
        alias="billingTrapDescription",
        name="",
        description="",
        example="04250 provided by John McMenamy ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
