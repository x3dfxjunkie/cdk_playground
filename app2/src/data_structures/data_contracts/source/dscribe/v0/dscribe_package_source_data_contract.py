"""Source Data Contract Template for PACKAGE"""

from __future__ import annotations

from typing import List, Optional

from datetime import date

from pydantic import BaseModel, Field


class ValidityPeriod(BaseModel):
    """
    Class For Dscribe PACKAGE ValidityPeriod Data
    """

    period_type: str = Field(
        ...,
        alias="periodType",
        name="",
        description="",
        example="Travel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    period_type_id: str = Field(
        ...,
        alias="periodTypeId",
        name="",
        description="",
        example="1102",
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
        example="2021-12-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SalesChannelItem(BaseModel):
    """
    Class For Dscribe PACKAGE SalesChannelItem Data
    """

    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        example="Sales Center - LACD All Other Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replacements: Optional[List[str]] = Field(
        None,
        alias="Replacements",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    distribution_channel: Optional[List[str]] = Field(
        None,
        alias="DistributionChannel",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    membership_affiliation: Optional[List[str]] = Field(
        None,
        alias="MembershipAffiliation",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sales_zone: Optional[List[str]] = Field(
        None,
        alias="SalesZone",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceItem(BaseModel):

    """
    Class For Dscribe PACKAGE SourceItem Data
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Sales Center - LACD All Other Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    short_name_id: str = Field(
        ...,
        alias="shortNameId",
        name="",
        description="",
        example="80000071",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SystemCode(BaseModel):

    """
    Class For Dscribe PACKAGE SystemCode Data
    """

    source: List[SourceItem] = Field(
        ...,
        alias="source",
        name="",
        description="",
    )

    code_name: Optional[str] = Field(
        None,
        alias="codeName",
        name="",
        description="",
        example="Package Code",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_value: str = Field(
        ...,
        alias="codeValue",
        name="",
        description="",
        example="PX6R7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ComponentItem(BaseModel):

    """
    Class For Dscribe PACKAGE ComponentItem Data
    """

    quantity: Optional[str] = Field(
        None,
        alias="quantity",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method: str = Field(
        ...,
        alias="behaviorMethod",
        name="",
        description="",
        example="Per Individual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method_id: str = Field(
        ...,
        alias="behaviorMethodId",
        name="",
        description="",
        example="80000095",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_frequency: str = Field(
        ...,
        alias="behaviorFrequency",
        name="",
        description="",
        example="One Time",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fullfillment: str = Field(
        ...,
        alias="fullfillment",
        name="",
        description="",
        example="Electronic Coupons (KTTW)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replacements: Optional[List[str]] = Field(
        None,
        alias="Replacements",
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

    product: Optional[List[str]] = Field(
        None,
        alias="Product",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketPortfolio(BaseModel):

    """
    Class For Dscribe PACKAGE TicketPortfolio Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="19384706",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Package",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribePackageModel(BaseModel):
    """
    Payload class for DscribePackageModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR contact enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Package"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="19384706",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Package",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="21 LACD AO RO RO Room Only-PX6R7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    long_name: str = Field(
        ...,
        alias="longName",
        name="",
        description="",
        example="Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    internal_name: str = Field(
        ...,
        alias="internalName",
        name="",
        description="",
        example="21 LACD AO RO RO Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Annual Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80001188",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: str = Field(
        ...,
        alias="subType",
        name="",
        description="",
        example="Core Packages",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: str = Field(
        ...,
        alias="subTypeId",
        name="",
        description="",
        example="80001482",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    package_group: str = Field(
        ...,
        alias="packageGroup",
        name="",
        description="",
        example="Annual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plan_type: str = Field(
        ...,
        alias="planType",
        name="",
        description="",
        example="Room Only",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plan_type_id: str = Field(
        ...,
        alias="planTypeId",
        name="",
        description="",
        example="80000330",
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

    minimum_night_count: str = Field(
        ...,
        alias="minimumNightCount",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    maximum_night_count: str = Field(
        ...,
        alias="maximumNightCount",
        name="",
        description="",
        example="30",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    advance_booking_day: Optional[str] = Field(
        None,
        alias="advanceBookingDay",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_periods: Optional[List[ValidityPeriod]] = Field(
        None,
        alias="validityPeriods",
        name="",
        description="",
    )

    sales_channel: List[SalesChannelItem] = Field(
        ...,
        alias="salesChannel",
        name="",
        description="",
    )

    system_codes: List[SystemCode] = Field(
        ...,
        alias="systemCodes",
        name="",
        description="",
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

    accommodation: Optional[List[str]] = Field(
        None,
        alias="Accommodation",
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

    component: Optional[List[ComponentItem]] = Field(
        None,
        alias="component",
        name="",
        description="",
    )

    ticket_portfolio: Optional[TicketPortfolio] = Field(
        None,
        alias="ticketPortfolio",
        name="",
        description="",
    )

    package: Optional[List[str]] = Field(
        None,
        alias="Package",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product: Optional[List[str]] = Field(
        None,
        alias="Product",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
