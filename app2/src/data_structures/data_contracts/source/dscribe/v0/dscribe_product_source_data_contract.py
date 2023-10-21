"""Source Data Contract Template for PRODUCT"""


from __future__ import annotations

from typing import List, Optional

from datetime import datetime, date

from pydantic import BaseModel, Field


class AgeType(BaseModel):

    """
    Class For Dscribe PRODUCT AgeType Data
    """

    age_type_name: str = Field(
        ...,
        alias="ageTypeName",
        name="",
        description="",
        example="All Ages",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_type_group: str = Field(
        ...,
        alias="ageTypeGroup",
        name="",
        description="",
        example="Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    minimum_age: int = Field(
        ...,
        alias="minimumAge",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    maximum_age: int = Field(
        ...,
        alias="maximumAge",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PricesItem(BaseModel):

    """
    Class For Dscribe Product PricesItem Data
    """

    price_description: str = Field(
        ...,
        alias="priceDescription",
        name="",
        description="",
        example="Membership (FL Residents)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_type: str = Field(
        ...,
        alias="priceType",
        name="",
        description="",
        example="Retail",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_type: AgeType = Field(
        ...,
        alias="ageType",
        name="",
        description="",
    )

    currency: str = Field(
        ...,
        alias="currency",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2007-01-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2023-08-03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price: float = Field(
        ...,
        alias="price",
        name="",
        description="",
        example=109.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behaviour_quantity: Optional[int] = Field(
        None,
        alias="behaviourQuantity",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_quantity: Optional[int] = Field(
        None,
        alias="frequencyQuantity",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method: Optional[str] = Field(
        None,
        alias="behaviorMethod",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_method: Optional[str] = Field(
        None,
        alias="frequencyMethod",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_amount: float = Field(
        ...,
        alias="taxAmount",
        name="",
        description="",
        example=3.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_price_with_tax: float = Field(
        ...,
        alias="totalPriceWithTax",
        name="",
        description="",
        example=53.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ValidityPeriod(BaseModel):

    """
    Class For Dscribe PRODUCT ValidityPeriod Data
    """

    period_type: Optional[str] = Field(
        None,
        alias="periodType",
        name="",
        description="",
        example="Booking / Sales",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    period_type_id: Optional[str] = Field(
        None,
        alias="periodTypeId",
        name="",
        description="",
        example="80000466",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2007-01-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2023-08-03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Tax(BaseModel):

    """
    Class For Dscribe PRODUCT Tax Data
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
    Class For Dscribe PRODUCT BasePriceItem Data
    """

    base_price_id: str = Field(
        ...,
        alias="basePriceId",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enterprise_id: str = Field(
        ...,
        alias="enterpriseId",
        name="",
        description="",
        example="115470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=79.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: float = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=44.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior: float = Field(
        ...,
        alias="junior",
        name="",
        description="",
        example=44.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="115470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2007-01-01",
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
        example="2022-05-10 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2023-08-03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="Valerie.RuizMateo@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2023-08-04 17:09:31.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class HistoryItem(BaseModel):

    """
    Class For Dscribe PRODUCT HistoryItem Data
    """

    price_id: str = Field(
        ...,
        alias="priceId",
        name="",
        description="",
        example="10985",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    base_price_id: Optional[str] = Field(
        None,
        alias="basePriceId",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_type_id: str = Field(
        ...,
        alias="ageTypeId",
        name="",
        description="",
        example="54729",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_type_name: str = Field(
        ...,
        alias="ageTypeName",
        name="",
        description="",
        example="All Ages",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    currency: Optional[str] = Field(
        None,
        alias="currency",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    internal_name: str = Field(
        ...,
        alias="internalName",
        name="",
        description="",
        example="Alamo Car Rental",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_type_id: str = Field(
        ...,
        alias="priceTypeId",
        name="",
        description="",
        example="80000347",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_type_name: str = Field(
        ...,
        alias="priceTypeName",
        name="",
        description="",
        example="Retail",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method_id: Optional[str] = Field(
        None,
        alias="behaviorMethodId",
        name="",
        description="",
        example="80000094",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method_name: Optional[str] = Field(
        None,
        alias="behaviorMethodName",
        name="",
        description="",
        example="Per Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_quantity: int = Field(
        ...,
        alias="behaviorQuantity",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_method_id: Optional[str] = Field(
        None,
        alias="frequencyMethodId",
        name="",
        description="",
        example="80000088",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_method_name: Optional[str] = Field(
        None,
        alias="frequencyMethodName",
        name="",
        description="",
        example="Per Night",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_quantity: int = Field(
        ...,
        alias="frequencyQuantity",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_fee_type_id: Optional[str] = Field(
        None,
        alias="serviceFeeTypeId",
        name="",
        description="",
        example="80000421",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_fee_value: int = Field(
        ...,
        alias="serviceFeeValue",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity: int = Field(
        ...,
        alias="quantity",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="115470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_amount: float = Field(
        ...,
        alias="taxAmount",
        name="",
        description="",
        example=3.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_price_with_tax: float = Field(
        ...,
        alias="totalPriceWithTax",
        name="",
        description="",
        example=53.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_price_with_tax_override: int = Field(
        ...,
        alias="totalPriceWithTaxOverride",
        name="",
        description="",
        example=0,
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
        example="2022-05-10 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="Valerie.RuizMateo@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2023-08-04 17:09:31.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MembershipAffiliationItem(BaseModel):

    """
    Class For Dscribe PRODUCT MembershipAffiliationItem Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="115470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="11488",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2007-01-01",
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
        example="2022-05-10 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user: str = Field(
        ...,
        alias="user",
        name="",
        description="",
        example="JENNIFER.D.MCCLURE@DISNEY.COM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="Valerie.RuizMateo@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2023-08-04 17:09:31.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PriceItem(BaseModel):

    """
    Class For Dscribe PRODUCT PriceItem Data
    """

    price_id: str = Field(
        ...,
        alias="priceId",
        name="",
        description="",
        example="10985",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enterprise_id: str = Field(
        ...,
        alias="enterpriseId",
        name="",
        description="",
        example="115470",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    history: Optional[List[HistoryItem]] = Field(
        None,
        alias="history",
        name="",
        description="",
    )

    additional_discount_type_id: Optional[str] = Field(
        None,
        alias="additionalDiscountTypeId",
        name="",
        description="",
        example="80000209",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_discount_type_name: Optional[str] = Field(
        None,
        alias="additionalDiscountTypeName",
        name="",
        description="",
        example="Amount",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    additional_discount_value: int = Field(
        ...,
        alias="additionalDiscountValue",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_type_id: str = Field(
        ...,
        alias="discountTypeId",
        name="",
        description="",
        example="80000209",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_type_name: str = Field(
        ...,
        alias="discountTypeName",
        name="",
        description="",
        example="Amount",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_value: float = Field(
        ...,
        alias="discountValue",
        name="",
        description="",
        example=29.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_description: str = Field(
        ...,
        alias="priceDescription",
        name="",
        description="",
        example="Membership (FL Residents)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="1997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="115470",
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
        example="2022-05-10 00:00:00.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="Valerie.RuizMateo@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2023-08-04 17:09:31.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    membership_affiliation: Optional[List[MembershipAffiliationItem]] = Field(
        None,
        alias="membershipAffiliation",
        name="",
        description="",
    )


class Pricing(BaseModel):

    """
    Class For Dscribe PRODUCT Pricing Data
    """

    tax: Tax = Field(
        ...,
        alias="tax",
        name="",
        description="",
    )

    base_price: Optional[List[BasePriceItem]] = Field(
        None,
        alias="basePrice",
        name="",
        description="",
    )

    price: List[PriceItem] = Field(
        ...,
        alias="price",
        name="",
        description="",
    )


class ChannelItem(BaseModel):
    """
    Class For Dscribe PRODUCT ChannelItem Data
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
        example="/Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceItem(BaseModel):

    """
    Class For Dscribe PRODUCT SourceItem Data
    """

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Accovia",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    short_name_id: str = Field(
        ...,
        alias="shortNameId",
        name="",
        description="",
        example="80000074",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    short_name: Optional[str] = Field(
        None,
        alias="shortName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SystemCode(BaseModel):

    """
    Class For Dscribe PRODUCT SystemCode Data
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
        example="Accovia",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_value: Optional[str] = Field(
        None,
        alias="codeValue",
        name="",
        description="",
        example="B6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class FacilityHierarchyItem(BaseModel):

    """
    Class For Dscribe PRODUCT FacilityHierarchyItem Data
    """

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="11488",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Product",
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
        example="Travel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Car Rental",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: str = Field(
        ...,
        alias="nameText",
        name="",
        description="",
        example="Walt Disney World Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: str = Field(
        ...,
        alias="nameHtml",
        name="",
        description="",
        example="<strong>Walt Disney World</strong>\xae Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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


class FacilityAssociationItem(BaseModel):

    """
    Class For Dscribe PRODUCT FacilityAssociationItem Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Travel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="80001079",
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

    resort: List[str] = Field(
        ...,
        alias="Resort",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeProductModel(BaseModel):
    """Payload class for DScribeProductModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Product"
        stream_name = ""
        description = "Contains all information about WDW and DLR contact enterprise metadata"  # optional
        unique_identifier = ["id"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Product"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="11488",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Alamo Rent A Car",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prices: Optional[List[PricesItem]] = Field(
        None,
        alias="prices",
        name="",
        description="",
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
        example="Alamo Car Rental",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: Optional[str] = Field(
        None,
        alias="type",
        name="",
        description="",
        example="Travel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="80001079",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Car Rental",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type_id: Optional[str] = Field(
        None,
        alias="subTypeId",
        name="",
        description="",
        example="80001486",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    level4_type: Optional[str] = Field(
        None,
        alias="level4Type",
        name="",
        description="",
        example="Car Rental",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    level4_type_id: Optional[str] = Field(
        None,
        alias="level4TypeId",
        name="",
        description="",
        example="80001530",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_group: Optional[str] = Field(
        None,
        alias="ageGroup",
        name="",
        description="",
        example="WDTC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_group_id: Optional[str] = Field(
        None,
        alias="ageGroupId",
        name="",
        description="",
        example="6962",
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

    validity_periods: Optional[List[ValidityPeriod]] = Field(
        None,
        alias="validityPeriods",
        name="",
        description="",
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

    pricing: Optional[Pricing] = Field(
        None,
        alias="pricing",
        name="",
        description="",
    )

    merchandise_facility: Optional[List[str]] = Field(
        None,
        alias="MerchandiseFacility",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility: Optional[List[str]] = Field(
        None,
        alias="Facility",
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

    system_codes: Optional[List[SystemCode]] = Field(
        None,
        alias="systemCodes",
        name="",
        description="",
    )

    digital_asset: Optional[List[str]] = Field(
        None,
        alias="DigitalAsset",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schedule_id: Optional[str] = Field(
        None,
        alias="scheduleId",
        name="",
        description="",
        example="411964638",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parent_facility: Optional[str] = Field(
        None,
        alias="parentFacility",
        name="",
        description="",
        example="80008888",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_hierarchy: Optional[List[FacilityHierarchyItem]] = Field(
        None,
        alias="facilityHierarchy",
        name="",
        description="",
    )

    parent_facility_content_type: Optional[str] = Field(
        None,
        alias="parentFacilityContentType",
        name="",
        description="",
        example="Facility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket: Optional[List[str]] = Field(
        None,
        alias="Ticket",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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

    food_beverage_facility: Optional[List[str]] = Field(
        None,
        alias="FoodBeverageFacility",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group: Optional[str] = Field(
        None,
        alias="taxGroup",
        name="",
        description="",
        example="Not Applicable",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_id: Optional[str] = Field(
        None,
        alias="taxGroupId",
        name="",
        description="",
        example="1081",
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

    facility_association: Optional[List[FacilityAssociationItem]] = Field(
        None,
        alias="facilityAssociation",
        name="",
        description="",
    )
