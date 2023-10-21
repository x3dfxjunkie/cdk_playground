"""Source Data Contract for SnApp Product"""

from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class MetaDataListItem(BaseModel):
    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="PAC17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type_desc: str = Field(
        ...,
        alias="MetaFieldDataTypeDesc",
        name="",
        description="",
        example="DropDown",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="0624A134-8190-8F75-7507-0163DFF74DD0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_item_name: Optional[str] = Field(
        None,
        alias="MetaFieldItemName",
        name="",
        description="",
        example="Annual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Admission Type",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="ANN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class QuickUpgradeProductListItem(BaseModel):
    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="N1MIA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="F81F5395-953E-F220-07C9-018A955F48E9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="INCRED PASS MIL   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TagListItem(BaseModel):
    tag_name: str = Field(
        ...,
        alias="TagName",
        name="",
        description="",
        example="Grace Period 1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ProductRefundEventListItem(BaseModel):
    entry_amount_type: int = Field(
        ...,
        alias="EntryAmountType",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entry_amount_type_desc: str = Field(
        ...,
        alias="EntryAmountTypeDesc",
        name="",
        description="",
        example="Percentage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entry_amount_value: float = Field(
        ...,
        alias="EntryAmountValue",
        name="",
        description="",
        example=8.33,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_code: str = Field(
        ...,
        alias="EventCode",
        name="",
        description="",
        example="EVT-AKGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_id: str = Field(
        ...,
        alias="EventId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAE8134",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_name: str = Field(
        ...,
        alias="EventName",
        name="",
        description="",
        example="AK Gen Adm",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_entry_amount_type: int = Field(
        ...,
        alias="GuestEntryAmountType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_entry_amount_type_desc: str = Field(
        ...,
        alias="GuestEntryAmountTypeDesc",
        name="",
        description="",
        example="Absolute",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class InstallmentPlanListItem(BaseModel):
    down_payment_type: int = Field(
        ...,
        alias="DownPaymentType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    down_payment_type_desc: str = Field(
        ...,
        alias="DownPaymentTypeDesc",
        name="",
        description="",
        example="Absolute",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    down_payment_value: int = Field(
        ...,
        alias="DownPaymentValue",
        name="",
        description="",
        example=205,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_plan_code: str = Field(
        ...,
        alias="InstallmentPlanCode",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_plan_id: str = Field(
        ...,
        alias="InstallmentPlanId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA392B",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_plan_name: str = Field(
        ...,
        alias="InstallmentPlanName",
        name="",
        description="",
        example="On-Site New Acquisitions",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_fee_type: int = Field(
        ...,
        alias="ProductFeeType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_fee_type_desc: str = Field(
        ...,
        alias="ProductFeeTypeDesc",
        name="",
        description="",
        example="Absolute",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_fee_value: int = Field(
        ...,
        alias="ProductFeeValue",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2020-12-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    allow_cross_location_upg: bool = Field(
        ...,
        alias="AllowCrossLocationUpg",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_redeem_on_sale: bool = Field(
        ...,
        alias="AutoRedeemOnSale",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_check_level: int = Field(
        ...,
        alias="BiometricCheckLevel",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_check_level_desc: str = Field(
        ...,
        alias="BiometricCheckLevelDesc",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_enrollment: int = Field(
        ...,
        alias="BiometricEnrollment",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_enrollment_desc: str = Field(
        ...,
        alias="BiometricEnrollmentDesc",
        name="",
        description="",
        example="Sale",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cm_affiliation: bool = Field(
        ...,
        alias="CMAffiliation",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    category_code: str = Field(
        ...,
        alias="CategoryCode",
        name="",
        description="",
        example="INCRE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    category_id: str = Field(
        ...,
        alias="CategoryId",
        name="",
        description="",
        example="BBBBBBBB-2222-BBBB-2222-BBBBBBBB75FD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    category_name: str = Field(
        ...,
        alias="CategoryName",
        name="",
        description="",
        example="Incredi-Pass",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    category_recursive_name: str = Field(
        ...,
        alias="CategoryRecursiveName",
        name="",
        description="",
        example="Annual Passes \xbb Incredi-Pass",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    consume: str = Field(
        ...,
        alias="Consume",
        name="",
        description="",
        example="T",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    consume_desc: str = Field(
        ...,
        alias="ConsumeDesc",
        name="",
        description="",
        example="Ticket",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    day_class: str = Field(
        ...,
        alias="DayClass",
        name="",
        description="",
        example="CERT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    day_class_desc: str = Field(
        ...,
        alias="DayClassDesc",
        name="",
        description="",
        example="CERT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_price: float = Field(
        ...,
        alias="DefaultPrice",
        name="",
        description="",
        example=1449.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    downgradable: bool = Field(
        ...,
        alias="Downgradable",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrance_area_type: Optional[str] = Field(
        None,
        alias="EntranceAreaType",
        name="",
        description="",
        example="Theme Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrance_area_type_desc: Optional[str] = Field(
        None,
        alias="EntranceAreaTypeDesc",
        name="",
        description="",
        example="Theme Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exchange_type: Optional[str] = Field(
        None,
        alias="ExchangeType",
        name="",
        description="",
        example="PH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exchange_type_desc: Optional[str] = Field(
        None,
        alias="ExchangeTypeDesc",
        name="",
        description="",
        example="Park Hopper",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expiration_usage_type: int = Field(
        ...,
        alias="ExpirationUsageType",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expiration_usage_type_desc: str = Field(
        ...,
        alias="ExpirationUsageTypeDesc",
        name="",
        description="",
        example="As scheduled",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_tag_code: str = Field(
        ...,
        alias="FinanceGroupTagCode",
        name="",
        description="",
        example="FG-APCERTTPO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_tag_name: str = Field(
        ...,
        alias="FinanceGroupTagName",
        name="",
        description="",
        example="AP CERT THEME PARK ONLY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    force_media_generation: bool = Field(
        ...,
        alias="ForceMediaGeneration",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_ticket_option: int = Field(
        ...,
        alias="GroupTicketOption",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_ticket_option_desc: str = Field(
        ...,
        alias="GroupTicketOptionDesc",
        name="",
        description="",
        example="No group",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_type: str = Field(
        ...,
        alias="GuestType",
        name="",
        description="",
        example="A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_type_desc: str = Field(
        ...,
        alias="GuestTypeDesc",
        name="",
        description="",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hide_price_visibility: bool = Field(
        ...,
        alias="HidePriceVisibility",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_update_: datetime = Field(
        ...,
        alias="LastUpdate",
        name="",
        description="",
        example="2023-09-14T20:31:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_exclusive_use: bool = Field(
        ...,
        alias="MediaExclusiveUse",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: List[MetaDataListItem] = Field(
        ...,
        alias="MetaDataList",
        name="",
        description="",
    )

    on_sale_date_from: date = Field(
        ...,
        alias="OnSaleDateFrom",
        name="",
        description="",
        example="2023-10-24",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    on_sale_date_to: date = Field(
        ...,
        alias="OnSaleDateTo",
        name="",
        description="",
        example="2026-12-31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    people_of_determination: bool = Field(
        ...,
        alias="PeopleOfDetermination",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pricing_rule_subtype: Optional[str] = Field(
        None,
        alias="PricingRuleSubtype",
        name="",
        description="",
        example="FULLPRICE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pricing_rule_subtype_desc: Optional[str] = Field(
        None,
        alias="PricingRuleSubtypeDesc",
        name="",
        description="",
        example="Full Price",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pricing_rule_type: str = Field(
        ...,
        alias="PricingRuleType",
        name="",
        description="",
        example="PDREG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pricing_rule_type_desc: str = Field(
        ...,
        alias="PricingRuleTypeDesc",
        name="",
        description="",
        example="Paid-Structural",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="N1MQA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_create_date_time: datetime = Field(
        ...,
        alias="ProductCreateDateTime",
        name="",
        description="",
        example="2023-09-14T20:31:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_category: str = Field(
        ...,
        alias="ProductEntitlementCategory",
        name="",
        description="",
        example="TP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_category_desc: str = Field(
        ...,
        alias="ProductEntitlementCategoryDesc",
        name="",
        description="",
        example="Theme Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration: Optional[str] = Field(
        None,
        alias="ProductEntitlementDuration",
        name="",
        description="",
        example="365",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_desc: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationDesc",
        name="",
        description="",
        example="365 Days",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_expiration_duration: Optional[str] = Field(
        None,
        alias="ProductEntitlementExpirationDuration",
        name="",
        description="",
        example="365",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_expiration_duration_desc: Optional[str] = Field(
        None,
        alias="ProductEntitlementExpirationDurationDesc",
        name="",
        description="",
        example="365 Days",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_event_list: List[str] = Field(
        ...,
        alias="ProductEventList",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="792F11DB-B79A-9FC3-78BD-018A9563E7C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="INCRED PASS MCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name_ext: str = Field(
        ...,
        alias="ProductNameExt",
        name="",
        description="",
        example="INCRED PASS MCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_status: int = Field(
        ...,
        alias="ProductStatus",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_status_desc: str = Field(
        ...,
        alias="ProductStatusDesc",
        name="",
        description="",
        example="On sale (online only)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_type: int = Field(
        ...,
        alias="ProductType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_type_desc: str = Field(
        ...,
        alias="ProductTypeDesc",
        name="",
        description="",
        example="Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_min: int = Field(
        ...,
        alias="QuantityMin",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_step: int = Field(
        ...,
        alias="QuantityStep",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quick_upgrade_product_list: Optional[List[QuickUpgradeProductListItem]] = Field(
        None,
        alias="QuickUpgradeProductList",
        name="",
        description="",
    )

    refundable: bool = Field(
        ...,
        alias="Refundable",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    require_account: bool = Field(
        ...,
        alias="RequireAccount",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    restrict_open_order: bool = Field(
        ...,
        alias="RestrictOpenOrder",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sell_in_a_package: bool = Field(
        ...,
        alias="SellInAPackage",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    shell_type: str = Field(
        ...,
        alias="ShellType",
        name="",
        description="",
        example="CERT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    shell_type_desc: str = Field(
        ...,
        alias="ShellTypeDesc",
        name="",
        description="",
        example="CERT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    show_name_ext: bool = Field(
        ...,
        alias="ShowNameExt",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tag_list: List[TagListItem] = Field(
        ...,
        alias="TagList",
        name="",
        description="",
    )

    tax_calc_type: int = Field(
        ...,
        alias="TaxCalcType",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_calc_type_desc: str = Field(
        ...,
        alias="TaxCalcTypeDesc",
        name="",
        description="",
        example="Tax Exempt",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    test_product_indicator: bool = Field(
        ...,
        alias="TestProductIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgradable: bool = Field(
        ...,
        alias="Upgradable",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_exp_rule: Optional[int] = Field(
        None,
        alias="VarExpRule",
        name="",
        description="",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_exp_rule_desc: Optional[str] = Field(
        None,
        alias="VarExpRuleDesc",
        name="",
        description="",
        example="One year from encoding",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    variable_description: bool = Field(
        ...,
        alias="VariableDescription",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    variable_price: bool = Field(
        ...,
        alias="VariablePrice",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_category_code: Optional[str] = Field(
        None,
        alias="AccountCategoryCode",
        name="",
        description="",
        example="PER-APH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_category_id: Optional[str] = Field(
        None,
        alias="AccountCategoryId",
        name="",
        description="",
        example="9426F88E-7781-17CE-7C07-0175F77654F5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_category_name: Optional[str] = Field(
        None,
        alias="AccountCategoryName",
        name="",
        description="",
        example="Annual/Seasonal Passholder",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_refund_event_list: Optional[List[ProductRefundEventListItem]] = Field(
        None,
        alias="ProductRefundEventList",
        name="",
        description="",
    )

    renew_window_end_days: Optional[int] = Field(
        None,
        alias="RenewWindowEndDays",
        name="",
        description="",
        example=181,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renew_window_start_days: Optional[int] = Field(
        None,
        alias="RenewWindowStartDays",
        name="",
        description="",
        example=-181,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_first_usage_rule: Optional[int] = Field(
        None,
        alias="VarFirstUsageRule",
        name="",
        description="",
        example=8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_first_usage_rule_desc: Optional[str] = Field(
        None,
        alias="VarFirstUsageRuleDesc",
        name="",
        description="",
        example="Specific date",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cag_admission_type: Optional[str] = Field(
        None,
        alias="CAGAdmissionType",
        name="",
        description="",
        example="DISCAST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cag_admission_type_desc: Optional[str] = Field(
        None,
        alias="CAGAdmissionTypeDesc",
        name="",
        description="",
        example="Discounted Cast Ticket",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_plan_list: Optional[List[InstallmentPlanListItem]] = Field(
        None,
        alias="InstallmentPlanList",
        name="",
        description="",
    )

    payment_profile_code: Optional[str] = Field(
        None,
        alias="PaymentProfileCode",
        name="",
        description="",
        example="APMPNEW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_profile_id: Optional[str] = Field(
        None,
        alias="PaymentProfileId",
        name="",
        description="",
        example="1D180A81-8598-4772-4CD4-0175F679D1C2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_profile_name: Optional[str] = Field(
        None,
        alias="PaymentProfileName",
        name="",
        description="",
        example="APMP New Acquisitions",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    restrict_payment_methods: Optional[bool] = Field(
        None,
        alias="RestrictPaymentMethods",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adm_date_from: Optional[date] = Field(
        None,
        alias="AdmDateFrom",
        name="",
        description="",
        example="2023-10-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    adm_date_to: Optional[date] = Field(
        None,
        alias="AdmDateTo",
        name="",
        description="",
        example="2026-06-30",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    var_exp_quantity: Optional[int] = Field(
        None,
        alias="VarExpQuantity",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    market: Optional[str] = Field(
        None,
        alias="Market",
        name="",
        description="",
        example="CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    market_desc: Optional[str] = Field(
        None,
        alias="MarketDesc",
        name="",
        description="",
        example="CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppProductModel(BaseModel):
    """Payload class for SnAppProductModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Product"
        stream_name = ""
        description = """SnApp Product Data"""
        unique_identifier = ["Payload.ProductId"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = "SnApp.Product"

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(
        ...,
        alias="Payload",
        description="Data payload",
    )
