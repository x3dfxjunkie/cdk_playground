"""Source Data Contract Template for MEAL_PERIOD"""

from __future__ import annotations

from typing import List, Optional

from datetime import datetime, date

from pydantic import BaseModel, Field


class ChannelItem(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD ChannelItem Data
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
        example="/D3/Meal Period",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ProductAssociationItem(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD ProductAssociationItem Data
    """

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="411657808",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity: Optional[int] = Field(
        None,
        alias="quantity",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replacements: List[str] = Field(
        ...,
        alias="Replacements",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product: List[str] = Field(
        ...,
        alias="Product",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ValidityPeriod(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD ValidityPeriod Data
    """

    period_type: str = Field(
        ...,
        alias="periodType",
        name="",
        description="",
        example="Validity",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    period_type_id: str = Field(
        ...,
        alias="periodTypeId",
        name="",
        description="",
        example="80000469",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: Optional[date] = Field(
        None,
        alias="startDate",
        name="",
        description="",
        example="2008-10-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2022-10-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Tax(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD Tax Data
    """

    tax_group_id: str = Field(
        ...,
        alias="taxGroupId",
        name="",
        description="",
        example="1081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_name: str = Field(
        ...,
        alias="taxGroupName",
        name="",
        description="",
        example="Orange County Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class BasePriceItem(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD BasePriceItem Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="14613",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="122171",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: str = Field(
        ...,
        alias="prodId",
        name="",
        description="",
        example="285804",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: str = Field(
        ...,
        alias="subTypeId",
        name="",
        description="",
        example="285923",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_indicator: bool = Field(
        ...,
        alias="taxIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=15.98,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_id: str = Field(
        ...,
        alias="adultAgeTypeId",
        name="",
        description="",
        example="7001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_name: str = Field(
        ...,
        alias="adultAgeTypeName",
        name="",
        description="",
        example="F&B Adult 10-100",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_tax: float = Field(
        ...,
        alias="adultTax",
        name="",
        description="",
        example=2.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_with_tax: float = Field(
        ...,
        alias="adultWithTax",
        name="",
        description="",
        example=44.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: float = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=9.59,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_age_type_id: Optional[str] = Field(
        None,
        alias="childAgeTypeId",
        name="",
        description="",
        example="7000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_age_type_name: Optional[str] = Field(
        None,
        alias="childAgeTypeName",
        name="",
        description="",
        example="F&B Child 03-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_tax: float = Field(
        ...,
        alias="childTax",
        name="",
        description="",
        example=1.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_with_tax: float = Field(
        ...,
        alias="childWithTax",
        name="",
        description="",
        example=28.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior: int = Field(
        ...,
        alias="junior",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_tax: float = Field(
        ...,
        alias="juniorTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_with_tax: float = Field(
        ...,
        alias="juniorWithTax",
        name="",
        description="",
        example=15.66,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant: float = Field(
        ...,
        alias="infant",
        name="",
        description="",
        example=152.22,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_age_type_id: Optional[str] = Field(
        None,
        alias="infantAgeTypeId",
        name="",
        description="",
        example="6999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_age_type_name: Optional[str] = Field(
        None,
        alias="infantAgeTypeName",
        name="",
        description="",
        example="F&B Infant 0-2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_tax: float = Field(
        ...,
        alias="infantTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_with_tax: float = Field(
        ...,
        alias="infantWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_by: str = Field(
        ...,
        alias="createdBy",
        name="",
        description="",
        example="Database Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2022-04-27 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="ADELAIDA.JAIMES@DISNEY.COM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2022-07-25 18:21:05.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_age_type_id: Optional[str] = Field(
        None,
        alias="juniorAgeTypeId",
        name="",
        description="",
        example="16124947",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_age_type_name: Optional[str] = Field(
        None,
        alias="juniorAgeTypeName",
        name="",
        description="",
        example="Ages 11-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class BasePriceTotalItem(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD BasePriceTotalItem Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="14613",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="122171",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    base_price: List[BasePriceItem] = Field(
        ...,
        alias="basePrice",
        name="",
        description="",
    )

    end_date: date = Field(
        ...,
        alias="endDate",
        name="",
        description="",
        example="2022-10-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2008-10-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=68.32,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_tax: float = Field(
        ...,
        alias="adultTax",
        name="",
        description="",
        example=2.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_with_tax: float = Field(
        ...,
        alias="adultWithTax",
        name="",
        description="",
        example=44.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: float = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=48.89,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_tax: float = Field(
        ...,
        alias="childTax",
        name="",
        description="",
        example=1.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_with_tax: float = Field(
        ...,
        alias="childWithTax",
        name="",
        description="",
        example=28.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior: int = Field(
        ...,
        alias="junior",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_tax: float = Field(
        ...,
        alias="juniorTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_with_tax: float = Field(
        ...,
        alias="juniorWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant: float = Field(
        ...,
        alias="infant",
        name="",
        description="",
        example=187.62,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_tax: float = Field(
        ...,
        alias="infantTax",
        name="",
        description="",
        example=11.8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_with_tax: float = Field(
        ...,
        alias="infantWithTax",
        name="",
        description="",
        example=202.16,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_id: str = Field(
        ...,
        alias="taxGroupId",
        name="",
        description="",
        example="1081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_name: str = Field(
        ...,
        alias="taxGroupName",
        name="",
        description="",
        example="Orange County Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_by: str = Field(
        ...,
        alias="createdBy",
        name="",
        description="",
        example="Database Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2022-04-27 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="ADELAIDA.JAIMES@DISNEY.COM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2022-07-25 18:21:05.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    currency_code: Optional[str] = Field(
        None,
        alias="currencyCode",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MembershipDiscount(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD MembershipDiscount Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="14613",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="122171",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: str = Field(
        ...,
        alias="prodId",
        name="",
        description="",
        example="285804",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: str = Field(
        ...,
        alias="subTypeId",
        name="",
        description="",
        example="285923",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_indicator: bool = Field(
        ...,
        alias="taxIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=23.22,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_id: str = Field(
        ...,
        alias="adultAgeTypeId",
        name="",
        description="",
        example="7001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_name: str = Field(
        ...,
        alias="adultAgeTypeName",
        name="",
        description="",
        example="F&B Adult 10-100",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_tax: float = Field(
        ...,
        alias="adultTax",
        name="",
        description="",
        example=2.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_with_tax: float = Field(
        ...,
        alias="adultWithTax",
        name="",
        description="",
        example=44.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: float = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=187.62,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_age_type_id: str = Field(
        ...,
        alias="childAgeTypeId",
        name="",
        description="",
        example="7000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_age_type_name: str = Field(
        ...,
        alias="childAgeTypeName",
        name="",
        description="",
        example="F&B Child 03-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_tax: float = Field(
        ...,
        alias="childTax",
        name="",
        description="",
        example=1.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_with_tax: float = Field(
        ...,
        alias="childWithTax",
        name="",
        description="",
        example=28.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior: int = Field(
        ...,
        alias="junior",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_tax: float = Field(
        ...,
        alias="juniorTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_with_tax: float = Field(
        ...,
        alias="juniorWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant: int = Field(
        ...,
        alias="infant",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_age_type_id: str = Field(
        ...,
        alias="infantAgeTypeId",
        name="",
        description="",
        example="6999",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_age_type_name: str = Field(
        ...,
        alias="infantAgeTypeName",
        name="",
        description="",
        example="F&B Infant 0-2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_tax: float = Field(
        ...,
        alias="infantTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_with_tax: float = Field(
        ...,
        alias="infantWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_by: str = Field(
        ...,
        alias="createdBy",
        name="",
        description="",
        example="Database Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2022-04-27 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="ADELAIDA.JAIMES@DISNEY.COM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2022-07-25 18:21:05.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_age_type_id: Optional[str] = Field(
        None,
        alias="juniorAgeTypeId",
        name="",
        description="",
        example="16124947",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_age_type_name: Optional[str] = Field(
        None,
        alias="juniorAgeTypeName",
        name="",
        description="",
        example="Ages 11-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MembershipDiscountsTotalItem(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD MembershipDiscountsTotalItem Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="14613",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="122171",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    membership_discounts: List[MembershipDiscount] = Field(
        ...,
        alias="membershipDiscounts",
        name="",
        description="",
    )

    description: str = Field(
        ...,
        alias="description",
        name="",
        description="",
        example="Food and Beverage - Passholder",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2022-10-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    membership_id: str = Field(
        ...,
        alias="membershipId",
        name="",
        description="",
        example="17492598",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    percent_of_total: int = Field(
        ...,
        alias="percentOfTotal",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    retail_price_indicator: bool = Field(
        ...,
        alias="retailPriceIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2008-10-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=23.22,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_tax: float = Field(
        ...,
        alias="adultTax",
        name="",
        description="",
        example=2.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_with_tax: float = Field(
        ...,
        alias="adultWithTax",
        name="",
        description="",
        example=44.73,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: float = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=48.89,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_tax: float = Field(
        ...,
        alias="childTax",
        name="",
        description="",
        example=1.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_with_tax: float = Field(
        ...,
        alias="childWithTax",
        name="",
        description="",
        example=28.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior: int = Field(
        ...,
        alias="junior",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_tax: float = Field(
        ...,
        alias="juniorTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_with_tax: float = Field(
        ...,
        alias="juniorWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant: int = Field(
        ...,
        alias="infant",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_tax: float = Field(
        ...,
        alias="infantTax",
        name="",
        description="",
        example=1.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_with_tax: float = Field(
        ...,
        alias="infantWithTax",
        name="",
        description="",
        example=31.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_id: str = Field(
        ...,
        alias="taxGroupId",
        name="",
        description="",
        example="1081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_name: str = Field(
        ...,
        alias="taxGroupName",
        name="",
        description="",
        example="Orange County Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_by: str = Field(
        ...,
        alias="createdBy",
        name="",
        description="",
        example="Database Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created: datetime = Field(
        ...,
        alias="created",
        name="",
        description="",
        example="2022-04-27 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: str = Field(
        ...,
        alias="updatedBy",
        name="",
        description="",
        example="ADELAIDA.JAIMES@DISNEY.COM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: datetime = Field(
        ...,
        alias="updated",
        name="",
        description="",
        example="2022-07-25 18:21:05.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Pricing(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD Pricing Data
    """

    tax: Tax = Field(
        ...,
        alias="tax",
        name="",
        description="",
    )

    base_price_total: List[BasePriceTotalItem] = Field(
        ...,
        alias="basePriceTotal",
        name="",
        description="",
    )

    membership_discounts_total: Optional[List[MembershipDiscountsTotalItem]] = Field(
        None,
        alias="membershipDiscountsTotal",
        name="",
        description="",
    )


class Types(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD Types Data
    """

    enterprise: str = Field(
        ...,
        alias="enterprise",
        name="",
        description="",
        example="MealPeriod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ExternalSystems(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD ExternalSystems Data
    """

    types: Types = Field(
        ...,
        alias="types",
        name="",
        description="",
    )


class Experience(BaseModel):
    """
    Class For Dscribe MEAL_PERIOD Experience Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="411657808",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        example="Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeMealPeriodModel(BaseModel):
    """
    Payload class for DscribeMealPeriodModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Meal Period"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR meal period enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "MealPeriod"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="13220",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="MealPeriod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Cape Town Lounge",
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

    schedule_id: Optional[str] = Field(
        None,
        alias="scheduleId",
        name="",
        description="",
        example="19436554",
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

    internal_name: Optional[str] = Field(
        None,
        alias="internalName",
        name="",
        description="",
        example="Cape Town Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_name: Optional[str] = Field(
        None,
        alias="typeName",
        name="",
        description="",
        example="Lounge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    #   Working with GCx to determine what to do with this attribute (it's currently a dupe but potential consumed by other legacy consumers)
    #    name: str = Field(
    #        ...,
    #        alias="name",
    #        name="",
    #        description="",
    #        example="Lounge",
    #        guest_identifier=False,
    #        transaction_identifier=False,
    #        identifier_tag="",
    #    )

    experience_type: Optional[str] = Field(
        None,
        alias="experienceType",
        name="",
        description="",
        example="Lounges",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    experience_type_id: Optional[str] = Field(
        None,
        alias="experienceTypeId",
        name="",
        description="",
        example="80000728",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_legend: Optional[str] = Field(
        None,
        alias="priceLegend",
        name="",
        description="",
        example="$ ($14.99 and under per adult)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    primary_cuisine_type: Optional[str] = Field(
        None,
        alias="primaryCuisineType",
        name="",
        description="",
        example="African",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    secondary_cuisine_type: Optional[str] = Field(
        None,
        alias="secondaryCuisineType",
        name="",
        description="",
        example="American",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_style: Optional[str] = Field(
        None,
        alias="serviceStyle",
        name="",
        description="",
        example="A la Carte",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    average_duration: Optional[str] = Field(
        None,
        alias="averageDuration",
        name="",
        description="",
        example="00:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    reservations_accepted: Optional[bool] = Field(
        None,
        alias="reservationsAccepted",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prepaid: Optional[bool] = Field(
        None,
        alias="prepaid",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sellable_online: Optional[bool] = Field(
        None,
        alias="sellableOnline",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_association: Optional[List[ProductAssociationItem]] = Field(
        None,
        alias="productAssociation",
        name="",
        description="",
    )

    menu_group: Optional[List[str]] = Field(
        None,
        alias="MenuGroup",
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

    name: Optional[List[str]] = Field(
        None,
        alias="Name",
        name="",
        description="",
        example=["example"],
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

    pricing: Optional[Pricing] = Field(
        None,
        alias="pricing",
        name="",
        description="",
    )

    entertainment: Optional[List[str]] = Field(
        None,
        alias="Entertainment",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event: Optional[List[str]] = Field(
        None,
        alias="Event",
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

    external_systems: Optional[ExternalSystems] = Field(
        None,
        alias="externalSystems",
        name="",
        description="",
    )

    experience: Optional[Experience] = Field(
        None,
        alias="experience",
        name="",
        description="",
    )

    character: Optional[List[str]] = Field(
        None,
        alias="Character",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
