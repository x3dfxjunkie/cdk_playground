"""Source Data Contract Template for DSCRIBE SERVICE_PRODUCT"""

from __future__ import annotations

from datetime import datetime, date

from typing import List, Optional

from pydantic import BaseModel, Field


class ValidityPeriod(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT ValidityPeriod Data
    """

    period_type: Optional[str] = Field(
        None,
        alias="periodType",
        name="",
        description="",
        example="Regular",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    period_type_id: Optional[str] = Field(
        None,
        alias="periodTypeId",
        name="",
        description="",
        example="15978236",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2021-09-08",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date: Optional[date] = Field(
        None,
        alias="endDate",
        name="",
        description="",
        example="2021-09-30",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class FacilityAssociationItem(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT FacilityAssociationItem Data
    """

    id: Optional[List[str]] = Field(
        None,
        alias="id",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="TEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="411599868",
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


class ProductAssociationItem(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT ProductAssociationItem Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="TEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: Optional[str] = Field(
        None,
        alias="typeId",
        name="",
        description="",
        example="411599868",
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

    accommodation: List[str] = Field(
        ...,
        alias="Accommodation",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ChannelItem(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT ChannelItem Data
    """

    site_name: str = Field(
        ...,
        alias="siteName",
        name="",
        description="",
        example="KnowsMoreOnly",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    channel_name: str = Field(
        ...,
        alias="channelName",
        name="",
        description="",
        example="/",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PriceItem(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT PriceItem Data
    """

    primary_key: str = Field(
        ...,
        alias="primaryKey",
        name="",
        description="",
        example="2775",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    relator_id: str = Field(
        ...,
        alias="relatorId",
        name="",
        description="",
        example="16009896",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult: float = Field(
        ...,
        alias="adult",
        name="",
        description="",
        example=13.24,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_id: str = Field(
        ...,
        alias="adultAgeTypeId",
        name="",
        description="",
        example="7148",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_age_type_name: str = Field(
        ...,
        alias="adultAgeTypeName",
        name="",
        description="",
        example="Resorts Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_tax: int = Field(
        ...,
        alias="adultTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adult_with_tax: float = Field(
        ...,
        alias="adultWithTax",
        name="",
        description="",
        example=13.24,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child: int = Field(
        ...,
        alias="child",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_tax: int = Field(
        ...,
        alias="childTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    child_with_tax: int = Field(
        ...,
        alias="childWithTax",
        name="",
        description="",
        example=0,
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

    junior_tax: int = Field(
        ...,
        alias="juniorTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    junior_with_tax: int = Field(
        ...,
        alias="juniorWithTax",
        name="",
        description="",
        example=0,
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

    infant_tax: int = Field(
        ...,
        alias="infantTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    infant_with_tax: int = Field(
        ...,
        alias="infantWithTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_id: str = Field(
        ...,
        alias="priceId",
        name="",
        description="",
        example="2775",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enterprise_id: str = Field(
        ...,
        alias="enterpriseId",
        name="",
        description="",
        example="16009896",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method_id: str = Field(
        ...,
        alias="behaviorMethodId",
        name="",
        description="",
        example="80000094",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    behavior_method_name: str = Field(
        ...,
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
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    currency_code: str = Field(
        ...,
        alias="currencyCode",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    discount_price_value: int = Field(
        ...,
        alias="discountPriceValue",
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

    end_date: date = Field(
        ...,
        alias="endDate",
        name="",
        description="",
        example="2021-09-30",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_time: str = Field(
        ...,
        alias="endTime",
        name="",
        description="",
        example="00:00:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    facility_req_ind: bool = Field(
        ...,
        alias="facilityReqInd",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_method_id: str = Field(
        ...,
        alias="frequencyMethodId",
        name="",
        description="",
        example="80000088",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    frequency_method_name: str = Field(
        ...,
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
        example=1,
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

    start_date: date = Field(
        ...,
        alias="startDate",
        name="",
        description="",
        example="2021-09-08",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_time: str = Field(
        ...,
        alias="startTime",
        name="",
        description="",
        example="00:00:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_id: str = Field(
        ...,
        alias="taxGroupId",
        name="",
        description="",
        example="4325",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_group_name: str = Field(
        ...,
        alias="taxGroupName",
        name="",
        description="",
        example="Not Applicable",
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
        example="Database Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_by: Optional[str] = Field(
        None,
        alias="updatedBy",
        name="",
        description="",
        example="Rebecca.M.Tomsik@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated: Optional[datetime] = Field(
        None,
        alias="updated",
        name="",
        description="",
        example="2023-01-17 20:29:22.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Pricing(BaseModel):
    """
    Class for Dscribe SERVICE_PRODUCT Pricing Data
    """

    price: List[PriceItem] = Field(
        ...,
        alias="price",
        name="",
        description="",
    )


class DScribeServiceProductModel(BaseModel):
    """Payload class for DScribeServiceProductModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Service Product"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR room category enterprise metadata"  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "ServiceProduct"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="123243",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="ServiceProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="Test Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    category: str = Field(
        ...,
        alias="category",
        name="",
        description="",
        example="Service",
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

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="TEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type_id: str = Field(
        ...,
        alias="typeId",
        name="",
        description="",
        example="411599868",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_group: Optional[str] = Field(
        None,
        alias="ageGroup",
        name="",
        description="",
        example="TEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_group_id: Optional[str] = Field(
        None,
        alias="ageGroupId",
        name="",
        description="",
        example="411550365",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_periods: List[ValidityPeriod] = Field(
        ...,
        alias="validityPeriods",
        name="",
        description="",
    )

    facility_association: Optional[List[FacilityAssociationItem]] = Field(
        None,
        alias="facilityAssociation",
        name="",
        description="",
    )

    product_association: Optional[List[ProductAssociationItem]] = Field(
        None,
        alias="productAssociation",
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

    external_name: Optional[str] = Field(
        None,
        alias="externalName",
        name="",
        description="",
        example="Firewood - Bin - Disn\xe9\ufffdy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    internal_name: Optional[str] = Field(
        None,
        alias="internalName",
        name="",
        description="",
        example="Creekside Meadow - Firewood - Bin - Disn\xe9\ufffdy",
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

    pricing: Optional[Pricing] = Field(
        None,
        alias="pricing",
        name="",
        description="",
    )
