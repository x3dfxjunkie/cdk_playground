"""Source Data Contract for SnApp Transaction"""

from __future__ import annotations

from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
)


class MultiLanguageText(BaseModel):
    default: str = Field(
        ...,
        alias="Default",
        name="",
        description="",
        example="00568461",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC32",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA3317",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="IATA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[str] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="00568461",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="Will Call ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PaymentListItem(BaseModel):
    auth_code: Optional[str] = Field(
        None,
        alias="AuthCode",
        name="",
        description="",
        example="111111832",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    capture_method: Optional[str] = Field(
        None,
        alias="CaptureMethod",
        name="",
        description="",
        example="keyed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_class: Optional[str] = Field(
        None,
        alias="CardClass",
        name="",
        description="",
        example="0118",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_token: Optional[str] = Field(
        None,
        alias="CardToken",
        name="",
        description="",
        example="1000AAAAAAA0FNS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    card_type: Optional[int] = Field(
        None,
        alias="CardType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    change: bool = Field(
        ...,
        alias="Change",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    charge_id: Optional[str] = Field(
        None,
        alias="ChargeId",
        name="",
        description="",
        example="1577015983",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    currency_iso: Optional[str] = Field(
        None,
        alias="CurrencyISO",
        name="",
        description="",
        example="EUR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    data_auth_code: Optional[str] = Field(
        None,
        alias="DataAuthCode",
        name="",
        description="",
        example="000AAA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    device_tran_id: Optional[str] = Field(
        None,
        alias="DeviceTranID",
        name="",
        description="",
        example="0000250000812330068941 6895767109132023070626124",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expiration_date: Optional[str] = Field(
        None,
        alias="ExpirationDate",
        name="",
        description="",
        example="0125",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_contract_code: Optional[str] = Field(
        None,
        alias="InstallmentContractCode",
        name="",
        description="",
        example="34998431",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    installment_contract_id: Optional[str] = Field(
        None,
        alias="InstallmentContractId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA2180",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    intercompany_cost_center_code: Optional[str] = Field(
        None,
        alias="IntercompanyCostCenterCode",
        name="",
        description="",
        example="7767",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    intercompany_cost_center_name: Optional[str] = Field(
        None,
        alias="IntercompanyCostCenterName",
        name="",
        description="",
        example="7767 DTI - TTC7767 - RESERVE AMERICA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invoice_number: Optional[str] = Field(
        None,
        alias="InvoiceNumber",
        name="",
        description="",
        example="2330068941",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    issuer_name: Optional[str] = Field(
        None,
        alias="IssuerName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kttw_id_resp: Optional[str] = Field(
        None,
        alias="KttwIdResp",
        name="",
        description="",
        example="991553046836330101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    offline: Optional[str] = Field(
        None,
        alias="Offline",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_amount: float = Field(
        ...,
        alias="PaymentAmount",
        name="",
        description="",
        example=201.29,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_gateway: Optional[str] = Field(
        None,
        alias="PaymentGateway",
        name="",
        description="",
        example="APP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_id: str = Field(
        ...,
        alias="PaymentId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0B29",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_method_code: str = Field(
        ...,
        alias="PaymentMethodCode",
        name="",
        description="",
        example="PMT-02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_method_id: str = Field(
        ...,
        alias="PaymentMethodId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA28BF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_method_last_update: datetime = Field(
        ...,
        alias="PaymentMethodLastUpdate",
        name="",
        description="",
        example="2021-05-19T10:05:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_method_name: str = Field(
        ...,
        alias="PaymentMethodName",
        name="",
        description="",
        example="Credit Card",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_status: int = Field(
        ...,
        alias="PaymentStatus",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_status_desc: str = Field(
        ...,
        alias="PaymentStatusDesc",
        name="",
        description="",
        example="Failed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_type: int = Field(
        ...,
        alias="PaymentType",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_type_desc: str = Field(
        ...,
        alias="PaymentTypeDesc",
        name="",
        description="",
        example="Credit card",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pms_transaction_id: Optional[str] = Field(
        None,
        alias="PmsTransactionId",
        name="",
        description="",
        example="8440291533",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rrn: Optional[str] = Field(
        None,
        alias="RRN",
        name="",
        description="",
        example="244685038832",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    reservation_end_date: Optional[datetime] = Field(
        None,
        alias="ReservationEndDate",
        name="",
        description="",
        example="2023-09-14T00:00:00-04:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sap_customer_number: Optional[str] = Field(
        None,
        alias="SAPCustomerNumber",
        name="",
        description="",
        example="80191213",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status_code: Optional[str] = Field(
        None,
        alias="StatusCode",
        name="",
        description="",
        example="A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem1(BaseModel):
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
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA4DD0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_item_name: Optional[str] = Field(
        None,
        alias="MetaFieldItemName",
        name="",
        description="",
        example="Multi Day",
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

    meta_field_type: Optional[str] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="MULTI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TaxListItem(BaseModel):
    tax_amount: float = Field(
        ...,
        alias="TaxAmount",
        name="",
        description="",
        example=33.74,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_code: str = Field(
        ...,
        alias="TaxCode",
        name="",
        description="",
        example="TAX5010501",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_id: str = Field(
        ...,
        alias="TaxId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA90DA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_last_update: datetime = Field(
        ...,
        alias="TaxLastUpdate",
        name="",
        description="",
        example="2022-02-15T05:31:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_name: str = Field(
        ...,
        alias="TaxName",
        name="",
        description="",
        example="Florida/Orange County Tax AA01 TP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ItemListItem(BaseModel):
    commission_code: Optional[str] = Field(
        None,
        alias="CommissionCode",
        name="",
        description="",
        example="COMMTA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    commission_name: Optional[str] = Field(
        None,
        alias="CommissionName",
        name="",
        description="",
        example="Travel Agent Commission",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    commissionable_quantity: Optional[int] = Field(
        None,
        alias="CommissionableQuantity",
        name="",
        description="",
        example=-2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_code: Optional[str] = Field(
        None,
        alias="EventCode",
        name="",
        description="",
        example="ADM_DATEBP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_id: Optional[str] = Field(
        None,
        alias="EventId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA11A1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_last_update: Optional[datetime] = Field(
        None,
        alias="EventLastUpdate",
        name="",
        description="",
        example="2020-12-17T19:32:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_name: Optional[str] = Field(
        None,
        alias="EventName",
        name="",
        description="",
        example="For calendar Date Based Pricing Calendar (Delta)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_code: str = Field(
        ...,
        alias="FinanceGroupCode",
        name="",
        description="",
        example="FG-TP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_id: str = Field(
        ...,
        alias="FinanceGroupId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAADCAD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_name: str = Field(
        ...,
        alias="FinanceGroupName",
        name="",
        description="",
        example="THEME PARK ONLY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: List[MetaDataListItem1] = Field(
        ...,
        alias="MetaDataList",
        name="",
        description="",
    )

    performance_date_time: Optional[datetime] = Field(
        None,
        alias="PerformanceDateTime",
        name="",
        description="",
        example="2023-09-23T03:00:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_id: Optional[str] = Field(
        None,
        alias="PerformanceId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE250",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_last_update: Optional[datetime] = Field(
        None,
        alias="PerformanceLastUpdate",
        name="",
        description="",
        example="2020-12-17T20:55:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="6J0RE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="Assigned To (TS OE)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA1AC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-05-19T01:35:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="6DAY 1P IA 24     AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity: int = Field(
        ...,
        alias="Quantity",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_unit: int = Field(
        ...,
        alias="QuantityUnit",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCCF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    stat_amount: float = Field(
        ...,
        alias="StatAmount",
        name="",
        description="",
        example=552.79,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_calc_type: int = Field(
        ...,
        alias="TaxCalcType",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_calc_type_desc: str = Field(
        ...,
        alias="TaxCalcTypeDesc",
        name="",
        description="",
        example="Tax Excluded",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_list: Optional[List[TaxListItem]] = Field(
        None,
        alias="TaxList",
        name="",
        description="",
    )

    total_amount: float = Field(
        ...,
        alias="TotalAmount",
        name="",
        description="",
        example=2763.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_net_full: float = Field(
        ...,
        alias="TotalNetFull",
        name="",
        description="",
        example=2595.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_tax: float = Field(
        ...,
        alias="TotalTax",
        name="",
        description="",
        example=168.7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=552.79,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_full: float = Field(
        ...,
        alias="UnitNetFull",
        name="",
        description="",
        example=519.05,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_raw_price: float = Field(
        ...,
        alias="UnitRawPrice",
        name="",
        description="",
        example=519.05,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=33.74,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    commission_amount: Optional[float] = Field(
        None,
        alias="CommissionAmount",
        name="",
        description="",
        example=-28.64,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EligibilityMember(BaseModel):
    code: str = Field(
        ...,
        alias="Code",
        name="",
        description="",
        example="6210656",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="",
        description="",
        example="MIKE INTERFACE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="",
        description="",
        example="MIKE INTERFACE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: int = Field(
        ...,
        alias="Status",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gmr: Optional[str] = Field(
        None,
        alias="GMR",
        name="",
        description="",
        example="G0805589",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    base_installation: Optional[str] = Field(
        None,
        alias="Base_Installation",
        name="",
        description="",
        example="NAVY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    birth_date: Optional[date] = Field(
        None,
        alias="BirthDate",
        name="",
        description="",
        example="2001-09-04",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_issued: Optional[str] = Field(
        None,
        alias="QuantityIssued",
        name="",
        description="",
        example="3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pernr: Optional[str] = Field(
        None,
        alias="Pernr",
        name="",
        description="",
        example="11111449",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EligibilityGroup(BaseModel):
    code: str = Field(
        ...,
        alias="Code",
        name="",
        description="",
        example="12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    eligibility_member: EligibilityMember = Field(
        ...,
        alias="EligibilityMember",
        name="",
        description="",
    )

    group: str = Field(
        ...,
        alias="Group",
        name="",
        description="",
        example="EXECUTIVE COMPLIMENTARY AUTHORIZATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: int = Field(
        ...,
        alias="Status",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Order(BaseModel):
    approved: bool = Field(
        ...,
        alias="Approved",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_purge: bool = Field(
        ...,
        alias="AutoPurge",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    completed: bool = Field(
        ...,
        alias="Completed",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encoded: bool = Field(
        ...,
        alias="Encoded",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item_count: int = Field(
        ...,
        alias="ItemCount",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_code: str = Field(
        ...,
        alias="LocationCode",
        name="",
        description="",
        example="LOC-WTKSV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_id: str = Field(
        ...,
        alias="LocationId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF2C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_last_update: datetime = Field(
        ...,
        alias="LocationLastUpdate",
        name="",
        description="",
        example="2023-05-11T03:01:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_name: str = Field(
        ...,
        alias="LocationName",
        name="",
        description="",
        example="TICKET SERVICES / FULFILLMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_code: str = Field(
        ...,
        alias="OpAreaCode",
        name="",
        description="",
        example="STSAD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_id: str = Field(
        ...,
        alias="OpAreaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAB4C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_last_update: datetime = Field(
        ...,
        alias="OpAreaLastUpdate",
        name="",
        description="",
        example="2022-06-20T19:14:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_name: str = Field(
        ...,
        alias="OpAreaName",
        name="",
        description="",
        example="Ticket Administration",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    owner_account_code: Optional[str] = Field(
        None,
        alias="OwnerAccountCode",
        name="",
        description="",
        example="ORG-DRC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    owner_account_id: Optional[str] = Field(
        None,
        alias="OwnerAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA745",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    owner_account_last_update: Optional[datetime] = Field(
        None,
        alias="OwnerAccountLastUpdate",
        name="",
        description="",
        example="2020-11-30T11:44:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    owner_account_name: Optional[str] = Field(
        None,
        alias="OwnerAccountName",
        name="",
        description="",
        example="DRC - COMMISSION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    paid: bool = Field(
        ...,
        alias="Paid",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    paid_amount: float = Field(
        ...,
        alias="PaidAmount",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_channel_code: Optional[str] = Field(
        None,
        alias="SaleChannelCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_channel_id: Optional[str] = Field(
        None,
        alias="SaleChannelId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_channel_last_update: Optional[datetime] = Field(
        None,
        alias="SaleChannelLastUpdate",
        name="",
        description="",
        example="2023-09-13T00:11:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_channel_name: Optional[str] = Field(
        None,
        alias="SaleChannelName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="ZDPZ4JBJ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_date_time: datetime = Field(
        ...,
        alias="SaleDateTime",
        name="",
        description="",
        example="2023-09-13T00:11:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_fiscal_date: date = Field(
        ...,
        alias="SaleFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_flow_type: int = Field(
        ...,
        alias="SaleFlowType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_flow_type_desc: str = Field(
        ...,
        alias="SaleFlowTypeDesc",
        name="",
        description="",
        example="Traditional",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA55D7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_status: int = Field(
        ...,
        alias="SaleStatus",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_status_desc: str = Field(
        ...,
        alias="SaleStatusDesc",
        name="",
        description="",
        example="Normal",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sales_tax_exempt_flag: bool = Field(
        ...,
        alias="SalesTaxExemptFlag",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_amount: float = Field(
        ...,
        alias="TotalAmount",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_code: Optional[str] = Field(
        None,
        alias="UserAccountCode",
        name="",
        description="",
        example="AAAAAAAABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_id: Optional[str] = Field(
        None,
        alias="UserAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0B6F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_last_update: Optional[datetime] = Field(
        None,
        alias="UserAccountLastUpdate",
        name="",
        description="",
        example="2023-06-07T16:10:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_name: Optional[str] = Field(
        None,
        alias="UserAccountName",
        name="",
        description="",
        example="Mouse, Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_login_alias: Optional[str] = Field(
        None,
        alias="UserLoginAlias",
        name="",
        description="",
        example="MOUSM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validated: bool = Field(
        ...,
        alias="Validated",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_code: str = Field(
        ...,
        alias="WorkstationCode",
        name="",
        description="",
        example="ENTTL-ACC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_id: str = Field(
        ...,
        alias="WorkstationId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA6AFE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_last_update: datetime = Field(
        ...,
        alias="WorkstationLastUpdate",
        name="",
        description="",
        example="2020-12-29T01:35:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_name: str = Field(
        ...,
        alias="WorkstationName",
        name="",
        description="",
        example="Guest Account API",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    payment_list: Optional[List[PaymentListItem]] = Field(
        None,
        alias="PaymentList",
        name="",
        description="",
    )

    item_list: Optional[List[ItemListItem]] = Field(
        None,
        alias="ItemList",
        name="",
        description="",
    )

    eligibility_group: Optional[EligibilityGroup] = Field(
        None,
        alias="EligibilityGroup",
        name="",
        description="",
    )


class MediaCodeListItem(BaseModel):
    media_code: str = Field(
        ...,
        alias="MediaCode",
        name="",
        description="",
        example="00A34C06514F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_type: int = Field(
        ...,
        alias="MediaCodeType",
        name="",
        description="",
        example=101,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_type_desc: str = Field(
        ...,
        alias="MediaCodeTypeDesc",
        name="",
        description="",
        example="Visual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class UpdateStatusMediaListItem(BaseModel):
    media_calc_code: str = Field(
        ...,
        alias="MediaCalcCode",
        name="",
        description="",
        example="M:1000.0.123123.6354",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_list: List[MediaCodeListItem] = Field(
        ...,
        alias="MediaCodeList",
        name="",
        description="",
    )

    media_id: str = Field(
        ...,
        alias="MediaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA9B03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_status: int = Field(
        ...,
        alias="MediaStatus",
        name="",
        description="",
        example=1012,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_status_desc: str = Field(
        ...,
        alias="MediaStatusDesc",
        name="",
        description="",
        example="Lost",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_code: str = Field(
        ...,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: str = Field(
        ...,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA9997",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: Optional[datetime] = Field(
        None,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-04-04T21:17:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: str = Field(
        ...,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA9A28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MultiLanguageText1(BaseModel):
    default: str = Field(
        ...,
        alias="Default",
        name="",
        description="",
        example="MOUSE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem2(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA904E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Last Name Note",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[str] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText1] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="MOUSE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DiscountListItem(BaseModel):
    promo_product_code: Optional[str] = Field(
        None,
        alias="PromoProductCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    promo_product_id: Optional[str] = Field(
        None,
        alias="PromoProductId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    promo_product_last_update: Optional[datetime] = Field(
        None,
        alias="PromoProductLastUpdate",
        name="",
        description="",
        example="2020-12-17T19:32:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    promo_product_name: Optional[str] = Field(
        None,
        alias="PromoProductName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ItemListItem1(BaseModel):
    discount_list: List[DiscountListItem] = Field(
        ...,
        alias="DiscountList",
        name="",
        description="",
    )

    event_code: Optional[str] = Field(
        None,
        alias="EventCode",
        name="",
        description="",
        example="ADM_DATEBP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_id: Optional[str] = Field(
        None,
        alias="EventId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA11A1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_last_update: Optional[datetime] = Field(
        None,
        alias="EventLastUpdate",
        name="",
        description="",
        example="2020-12-17T19:32:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_name: Optional[str] = Field(
        None,
        alias="EventName",
        name="",
        description="",
        example="For calendar Date Based Pricing Calendar (Delta)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_code: str = Field(
        ...,
        alias="FinanceGroupCode",
        name="",
        description="",
        example="FG-TP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_id: str = Field(
        ...,
        alias="FinanceGroupId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAADCAD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    finance_group_name: str = Field(
        ...,
        alias="FinanceGroupName",
        name="",
        description="",
        example="THEME PARK ONLY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_date_time: Optional[datetime] = Field(
        None,
        alias="PerformanceDateTime",
        name="",
        description="",
        example="2023-09-23T03:00:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_id: Optional[str] = Field(
        None,
        alias="PerformanceId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE250",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_last_update: Optional[datetime] = Field(
        None,
        alias="PerformanceLastUpdate",
        name="",
        description="",
        example="2020-12-17T20:55:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="6J0RE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="Assigned To (TS OE)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA1AC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-05-19T03:34:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="6DAY 1P IA 24     AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity: int = Field(
        ...,
        alias="Quantity",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_paid: int = Field(
        ...,
        alias="QuantityPaid",
        name="",
        description="",
        example=-5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_unit: int = Field(
        ...,
        alias="QuantityUnit",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCCF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    stat_amount: float = Field(
        ...,
        alias="StatAmount",
        name="",
        description="",
        example=552.79,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_calc_type: int = Field(
        ...,
        alias="TaxCalcType",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_calc_type_desc: str = Field(
        ...,
        alias="TaxCalcTypeDesc",
        name="",
        description="",
        example="Tax Excluded",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_list: Optional[List[TaxListItem]] = Field(
        None,
        alias="TaxList",
        name="",
        description="",
    )

    total_amount: float = Field(
        ...,
        alias="TotalAmount",
        name="",
        description="",
        example=2763.95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_net_full: float = Field(
        ...,
        alias="TotalNetFull",
        name="",
        description="",
        example=2595.25,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_tax: float = Field(
        ...,
        alias="TotalTax",
        name="",
        description="",
        example=168.7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=552.79,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_full: float = Field(
        ...,
        alias="UnitNetFull",
        name="",
        description="",
        example=519.05,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_raw_price: float = Field(
        ...,
        alias="UnitRawPrice",
        name="",
        description="",
        example=519.05,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=33.74,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MultiLanguageText2(BaseModel):
    default: str = Field(
        ...,
        alias="Default",
        name="",
        description="",
        example="1610",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem3(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC48",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA73D5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Additional Pricing Information",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="( + 152.0 + 149.0 + 149.0 + 118.0 + 119.0 + 118.0 + 154.0 + 161.0 + 154.0 )/9 * 6 - 272.64(32.1%) - 57.67 (10.0%) = 519.05",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText2] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="CONNECTICUT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketCodeAliasListItem(BaseModel):
    code_alias: str = Field(
        ...,
        alias="CodeAlias",
        name="",
        description="",
        example="020117-WDI-018-00008",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_code: str = Field(
        ...,
        alias="CodeAliasTypeCode",
        name="",
        description="",
        example="CA04_ATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_name: str = Field(
        ...,
        alias="CodeAliasTypeName",
        name="",
        description="",
        example="TICKET ALIAS - DSSN (ATS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class VoidedTicketListItem(BaseModel):
    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGHA5Y3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="091223-DTI-1-11622",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-09-12T23:57:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="",
        description="",
        example=1,
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

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example="ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBTTZCC0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem3]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    portfolio_account_code: Optional[str] = Field(
        None,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123ABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: Optional[str] = Field(
        None,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC9AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: Optional[datetime] = Field(
        None,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-12T23:57:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: Optional[str] = Field(
        None,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACC8D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="6J0RE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="Assigned To (TS OE)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA1AC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-05-19T03:34:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="6DAY 1P IA 24     AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_from_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0E2E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_root_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA30C9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0E2E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="AHBJ70181818",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACAF1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detail_id: str = Field(
        ...,
        alias="SaleItemDetailId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCF1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCCF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000622",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.1622",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCFC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_serial: str = Field(
        ...,
        alias="TicketSerial",
        name="",
        description="",
        example="111622",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status: int = Field(
        ...,
        alias="TicketStatus",
        name="",
        description="",
        example=102,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status_desc: str = Field(
        ...,
        alias="TicketStatusDesc",
        name="",
        description="",
        example="Void",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.81710",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACBE8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="181710",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=552.79,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_amount: float = Field(
        ...,
        alias="UnitFaceAmount",
        name="",
        description="",
        example=614.21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_net_amount: float = Field(
        ...,
        alias="UnitFaceNetAmount",
        name="",
        description="",
        example=576.72,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_tax: float = Field(
        ...,
        alias="UnitFaceTax",
        name="",
        description="",
        example=37.49,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_amount: float = Field(
        ...,
        alias="UnitNetAmount",
        name="",
        description="",
        example=519.05,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=33.74,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="ZM0PG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE8D8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="10DAY PHP G+      AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2022-03-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_id: str = Field(
        ...,
        alias="UpgradeFromSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACAF1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCCF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCFC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_transaction_id: str = Field(
        ...,
        alias="UpgradeFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACBE8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="ZM0PG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE8D8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="10DAY PHP G+      AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2022-02-18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACAF1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCCF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACCFC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_transaction_id: str = Field(
        ...,
        alias="UpgradeRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACBE8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2023-09-23",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_to: date = Field(
        ...,
        alias="ValidDateTo",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code_alias_list: Optional[List[TicketCodeAliasListItem]] = Field(
        None,
        alias="TicketCodeAliasList",
        name="",
        description="",
    )


class MultiLanguageText3(BaseModel):
    default: str = Field(
        ...,
        alias="Default",
        name="",
        description="",
        example="MICKEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem4(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="FT1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA2603",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="First Name",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText3] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="MICKEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="FLORIDA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EncodedTicketListItem(BaseModel):
    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGHA5Y3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="091223-DTI-1-12455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-09-13T00:15:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="",
        description="",
        example=1,
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

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example="ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBTCLJJ0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem4]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    portfolio_account_code: Optional[str] = Field(
        None,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123077",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: Optional[str] = Field(
        None,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA1111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: Optional[datetime] = Field(
        None,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2022-10-31T20:24:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: Optional[str] = Field(
        None,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA7559",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="N1FJ3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="365",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="365 Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA9C96",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-07-25T04:04:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="FL INCRED WS REN  AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_from_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAAFE4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_root_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0524",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAAFE4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="S67WYWAJ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE71F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detail_id: str = Field(
        ...,
        alias="SaleItemDetailId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE7B6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE79A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.2455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE7C3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_serial: str = Field(
        ...,
        alias="TicketSerial",
        name="",
        description="",
        example="112455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status: int = Field(
        ...,
        alias="TicketStatus",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status_desc: str = Field(
        ...,
        alias="TicketStatusDesc",
        name="",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.84374",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE725",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="184374",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=1355.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_amount: float = Field(
        ...,
        alias="UnitFaceAmount",
        name="",
        description="",
        example=1355.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_net_amount: float = Field(
        ...,
        alias="UnitFaceNetAmount",
        name="",
        description="",
        example=1273.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_tax: float = Field(
        ...,
        alias="UnitFaceTax",
        name="",
        description="",
        example=82.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_amount: float = Field(
        ...,
        alias="UnitNetAmount",
        name="",
        description="",
        example=1273.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=82.75,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_id: str = Field(
        ...,
        alias="UpgradeFromSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE71F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE79A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE7C3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_transaction_id: str = Field(
        ...,
        alias="UpgradeFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE725",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE71F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE79A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE7C3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_transaction_id: str = Field(
        ...,
        alias="UpgradeRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE725",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2023-09-14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_to: date = Field(
        ...,
        alias="ValidDateTo",
        name="",
        description="",
        example="2024-09-13",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem5(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC48",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA73D5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Additional Pricing Information",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="( + 177.0 + 177.0 + 177.0 + 173.0 + 166.0 + 156.0 + 156.0 )/7 * 4 - 72.27(10.7%) = 603.17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText3] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="FLORIDA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketCodeAliasListItem1(BaseModel):
    code_alias: str = Field(
        ...,
        alias="CodeAlias",
        name="",
        description="",
        example="031905-WDR-014-01010",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_code: str = Field(
        ...,
        alias="CodeAliasTypeCode",
        name="",
        description="",
        example="CA04_ATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_name: str = Field(
        ...,
        alias="CodeAliasTypeName",
        name="",
        description="",
        example="TICKET ALIAS - DSSN (ATS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TransferTicketListItem(BaseModel):
    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGH65A3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="042723-DTI-1-66867",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-04-28T03:23:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-04-27",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="",
        description="",
        example=1,
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

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example="ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBZZDZK0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem5]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    portfolio_account_code: str = Field(
        ...,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123ABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: str = Field(
        ...,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA036",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: datetime = Field(
        ...,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-13T00:14:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: str = Field(
        ...,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA45E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="4J0RC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: str = Field(
        ...,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: str = Field(
        ...,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: str = Field(
        ...,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="4 Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA4536",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-06-16T03:45:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="4DAY 1P           AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_from_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_root_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAADA50",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="LTGU66181818",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA349",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detail_id: str = Field(
        ...,
        alias="SaleItemDetailId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA507",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA49E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000867",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.6867",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA50E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_serial: str = Field(
        ...,
        alias="TicketSerial",
        name="",
        description="",
        example="166867",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status: int = Field(
        ...,
        alias="TicketStatus",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status_desc: str = Field(
        ...,
        alias="TicketStatusDesc",
        name="",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.95455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA3E2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="395455",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=642.38,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_amount: float = Field(
        ...,
        alias="UnitFaceAmount",
        name="",
        description="",
        example=642.38,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_net_amount: float = Field(
        ...,
        alias="UnitFaceNetAmount",
        name="",
        description="",
        example=603.17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_tax: float = Field(
        ...,
        alias="UnitFaceTax",
        name="",
        description="",
        example=39.21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_amount: float = Field(
        ...,
        alias="UnitNetAmount",
        name="",
        description="",
        example=603.17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=39.21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_id: str = Field(
        ...,
        alias="UpgradeFromSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA349",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA49E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA50E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_transaction_id: str = Field(
        ...,
        alias="UpgradeFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA3E2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA349",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA49E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA50E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_transaction_id: str = Field(
        ...,
        alias="UpgradeRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA3E2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2023-12-29",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_to: date = Field(
        ...,
        alias="ValidDateTo",
        name="",
        description="",
        example="2024-01-04",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code_alias_list: Optional[List[TicketCodeAliasListItem1]] = Field(
        None,
        alias="TicketCodeAliasList",
        name="",
        description="",
    )


class MultiLanguageText5(BaseModel):
    default: str = Field(
        ...,
        alias="Default",
        name="",
        description="",
        example="2061666060",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem6(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC48",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA73D5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Additional Pricing Information",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="(85.0 + 135.0 + 129.0 + 124.0 + 104.0 + 104.0 + 104.0 + 129.0 + 139.0 )/8 * 5 - 140.97(23.3%) - 131.77 (24.0%) = 417.26",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText5] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="NEW HAMPSHIRE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class BiometricResetTicketListItem(BaseModel):
    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGHS5Y3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="090923-DTI-1-23578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-09-09T22:29:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="",
        description="",
        example=1,
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

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example="ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBCBJKD0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem6]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    portfolio_account_code: str = Field(
        ...,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123ABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: str = Field(
        ...,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: datetime = Field(
        ...,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-09T22:28:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: str = Field(
        ...,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA5F8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="5KWPB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: str = Field(
        ...,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: str = Field(
        ...,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: str = Field(
        ...,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="5 Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAFA4A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-01-04T05:29:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="5DAY PH TC 23     CH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_from_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF44C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_root_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA1C3F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF44C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="1FQ9SUR3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detail_id: str = Field(
        ...,
        alias="SaleItemDetailId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA62C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.3578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_serial: str = Field(
        ...,
        alias="TicketSerial",
        name="",
        description="",
        example="123578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status: int = Field(
        ...,
        alias="TicketStatus",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status_desc: str = Field(
        ...,
        alias="TicketStatusDesc",
        name="",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.89594",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="189594",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=444.38,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_amount: float = Field(
        ...,
        alias="UnitFaceAmount",
        name="",
        description="",
        example=584.72,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_net_amount: float = Field(
        ...,
        alias="UnitFaceNetAmount",
        name="",
        description="",
        example=549.03,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_tax: float = Field(
        ...,
        alias="UnitFaceTax",
        name="",
        description="",
        example=35.69,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_amount: float = Field(
        ...,
        alias="UnitNetAmount",
        name="",
        description="",
        example=417.26,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=27.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_id: str = Field(
        ...,
        alias="UpgradeFromSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_transaction_id: str = Field(
        ...,
        alias="UpgradeFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_transaction_id: str = Field(
        ...,
        alias="UpgradeRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_to: date = Field(
        ...,
        alias="ValidDateTo",
        name="",
        description="",
        example="2023-09-16",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class MetaDataListItem7(BaseModel):
    auto_populate: bool = Field(
        ...,
        alias="AutoPopulate",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_code: str = Field(
        ...,
        alias="MetaFieldCode",
        name="",
        description="",
        example="MISC48",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_format: Optional[int] = Field(
        None,
        alias="MetaFieldDataFormat",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_data_type: int = Field(
        ...,
        alias="MetaFieldDataType",
        name="",
        description="",
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_id: str = Field(
        ...,
        alias="MetaFieldId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA73D5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_name: str = Field(
        ...,
        alias="MetaFieldName",
        name="",
        description="",
        example="Additional Pricing Information",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_purge_option: Optional[str] = Field(
        None,
        alias="MetaFieldPurgeOption",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_field_type: Optional[int] = Field(
        None,
        alias="MetaFieldType",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: str = Field(
        ...,
        alias="Value",
        name="",
        description="",
        example="(85.0 + 135.0 + 129.0 + 124.0 + 104.0 + 104.0 + 104.0 + 129.0 + 139.0 )/8 * 5 - 140.97(23.3%) - 131.77 (24.0%) = 417.26",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_language_text: Optional[MultiLanguageText5] = Field(
        None,
        alias="MultiLanguageText",
        name="",
        description="",
    )

    item_name: Optional[str] = Field(
        None,
        alias="ItemName",
        name="",
        description="",
        example="NEW HAMPSHIRE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketCodeAliasListItem2(BaseModel):
    code_alias: str = Field(
        ...,
        alias="CodeAlias",
        name="",
        description="",
        example="022415-WTS-043-12104",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_code: str = Field(
        ...,
        alias="CodeAliasTypeCode",
        name="",
        description="",
        example="CA04_ATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code_alias_type_name: str = Field(
        ...,
        alias="CodeAliasTypeName",
        name="",
        description="",
        example="TICKET ALIAS - DSSN (ATS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketNoteListItem(BaseModel):
    note: str = Field(
        ...,
        alias="Note",
        name="",
        description="",
        example="TICKET LOCKED 06/07/22",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    note_date_time: datetime = Field(
        ...,
        alias="NoteDateTime",
        name="",
        description="",
        example="2022-06-08T03:00:22.487+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    note_id: str = Field(
        ...,
        alias="NoteId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA8755",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class UpdateTicketListItem(BaseModel):
    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGHS5Y3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="090923-DTI-1-23578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-09-09T22:29:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="",
        description="",
        example=1,
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

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example="ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBCBJKD0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meta_data_list: Optional[List[MetaDataListItem7]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    portfolio_account_code: str = Field(
        ...,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123ABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: str = Field(
        ...,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: datetime = Field(
        ...,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-09T22:28:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: str = Field(
        ...,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA5F8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="5KWPB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_code: str = Field(
        ...,
        alias="ProductEntitlementDurationCode",
        name="",
        description="",
        example="PAC14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: str = Field(
        ...,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_name: str = Field(
        ...,
        alias="ProductEntitlementDurationName",
        name="",
        description="",
        example="5 Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAFA4A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: datetime = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-01-04T05:29:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="5DAY PH TC 23     CH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_from_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF44C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_root_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA1C3F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_transaction_id: Optional[str] = Field(
        None,
        alias="RenewalTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF44C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_code: str = Field(
        ...,
        alias="SaleCode",
        name="",
        description="",
        example="1FQ9SUR3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detail_id: str = Field(
        ...,
        alias="SaleItemDetailId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA62C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.3578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_serial: str = Field(
        ...,
        alias="TicketSerial",
        name="",
        description="",
        example="123578",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status: int = Field(
        ...,
        alias="TicketStatus",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_status_desc: str = Field(
        ...,
        alias="TicketStatusDesc",
        name="",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.89594",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="189594",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=444.38,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_amount: float = Field(
        ...,
        alias="UnitFaceAmount",
        name="",
        description="",
        example=584.72,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_net_amount: float = Field(
        ...,
        alias="UnitFaceNetAmount",
        name="",
        description="",
        example=549.03,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_face_tax: float = Field(
        ...,
        alias="UnitFaceTax",
        name="",
        description="",
        example=35.69,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_net_amount: float = Field(
        ...,
        alias="UnitNetAmount",
        name="",
        description="",
        example=417.26,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_tax: float = Field(
        ...,
        alias="UnitTax",
        name="",
        description="",
        example=27.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_id: str = Field(
        ...,
        alias="UpgradeFromSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_transaction_id: str = Field(
        ...,
        alias="UpgradeFromTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="N10AH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA76E4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="INCRED PASS WCT   AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: Optional[date] = Field(
        None,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2023-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA4FB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA60D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA635",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_transaction_id: str = Field(
        ...,
        alias="UpgradeRootTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAA550",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_from: date = Field(
        ...,
        alias="ValidDateFrom",
        name="",
        description="",
        example="2023-09-09",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_date_to: date = Field(
        ...,
        alias="ValidDateTo",
        name="",
        description="",
        example="2023-09-16",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code_alias_list: Optional[List[TicketCodeAliasListItem2]] = Field(
        None,
        alias="TicketCodeAliasList",
        name="",
        description="",
    )

    ticket_note_list: Optional[List[TicketNoteListItem]] = Field(
        None,
        alias="TicketNoteList",
        name="",
        description="",
    )


class MediaCodeListItem1(BaseModel):
    media_code: str = Field(
        ...,
        alias="MediaCode",
        name="",
        description="",
        example="1094879507108234",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_type: int = Field(
        ...,
        alias="MediaCodeType",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_type_desc: str = Field(
        ...,
        alias="MediaCodeTypeDesc",
        name="",
        description="",
        example="Secure",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EncodedMediaListItem(BaseModel):
    media_calc_code: str = Field(
        ...,
        alias="MediaCalcCode",
        name="",
        description="",
        example="M:1000.0.123123.5057",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_list: List[MediaCodeListItem1] = Field(
        ...,
        alias="MediaCodeList",
        name="",
        description="",
    )

    media_id: str = Field(
        ...,
        alias="MediaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAEADA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_status: int = Field(
        ...,
        alias="MediaStatus",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_status_desc: str = Field(
        ...,
        alias="MediaStatusDesc",
        name="",
        description="",
        example="Active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_code: str = Field(
        ...,
        alias="PortfolioAccountCode",
        name="",
        description="",
        example="000123123ABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_id: str = Field(
        ...,
        alias="PortfolioAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE342",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: datetime = Field(
        ...,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-13T00:12:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_name: str = Field(
        ...,
        alias="PortfolioAccountName",
        name="",
        description="",
        example="MOUSE, MINNIE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: str = Field(
        ...,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE552",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Transaction(BaseModel):
    approved: bool = Field(
        ...,
        alias="Approved",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    box_code: Optional[str] = Field(
        None,
        alias="BoxCode",
        name="",
        description="",
        example="230912-0710",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    box_id: Optional[str] = Field(
        None,
        alias="BoxId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAADBE8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    box_last_update: Optional[datetime] = Field(
        None,
        alias="BoxLastUpdate",
        name="",
        description="",
        example="2023-09-12T22:23:15.940+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    box_status: Optional[int] = Field(
        None,
        alias="BoxStatus",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    box_status_desc: Optional[str] = Field(
        None,
        alias="BoxStatusDesc",
        name="",
        description="",
        example="In use",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="091223-DTI-1-83699",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encoded: bool = Field(
        ...,
        alias="Encoded",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item_count: int = Field(
        ...,
        alias="ItemCount",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_code: str = Field(
        ...,
        alias="LocationCode",
        name="",
        description="",
        example="LOC-WTKSV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_id: str = Field(
        ...,
        alias="LocationId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAF2C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_last_update: datetime = Field(
        ...,
        alias="LocationLastUpdate",
        name="",
        description="",
        example="2023-05-11T03:01:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_name: str = Field(
        ...,
        alias="LocationName",
        name="",
        description="",
        example="TICKET SERVICES / FULFILLMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_code: str = Field(
        ...,
        alias="OpAreaCode",
        name="",
        description="",
        example="STSAD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_id: str = Field(
        ...,
        alias="OpAreaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAB4C0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_last_update: datetime = Field(
        ...,
        alias="OpAreaLastUpdate",
        name="",
        description="",
        example="2022-06-20T19:14:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_name: str = Field(
        ...,
        alias="OpAreaName",
        name="",
        description="",
        example="Ticket Administration",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    paid: bool = Field(
        ...,
        alias="Paid",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    paid_amount: float = Field(
        ...,
        alias="PaidAmount",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    paid_tax_amount: float = Field(
        ...,
        alias="PaidTaxAmount",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_count: int = Field(
        ...,
        alias="PaymentCount",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    printed: bool = Field(
        ...,
        alias="Printed",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    serial_date_time: datetime = Field(
        ...,
        alias="SerialDateTime",
        name="",
        description="",
        example="2023-09-13T00:10:49.690+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    serial_fiscal_date: date = Field(
        ...,
        alias="SerialFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    station_serial: str = Field(
        ...,
        alias="StationSerial",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000699",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_amount: float = Field(
        ...,
        alias="TotalAmount",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_tax: float = Field(
        ...,
        alias="TotalTax",
        name="",
        description="",
        example=0.00,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="",
        description="",
        example="T:1111.0.000000.83699",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_date_time: datetime = Field(
        ...,
        alias="TransactionDateTime",
        name="",
        description="",
        example="2023-09-13T00:10:49.690+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_fiscal_date: date = Field(
        ...,
        alias="TransactionFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA55D9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_license_id: int = Field(
        ...,
        alias="TransactionLicenseId",
        name="",
        description="",
        example=1241,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_serial: str = Field(
        ...,
        alias="TransactionSerial",
        name="",
        description="",
        example="183699",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_type: int = Field(
        ...,
        alias="TransactionType",
        name="",
        description="",
        example=82,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_type_desc: str = Field(
        ...,
        alias="TransactionTypeDesc",
        name="",
        description="",
        example="Change media status",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_warn: Optional[int] = Field(
        None,
        alias="TransactionWarn",
        name="",
        description="",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_warn_desc: Optional[str] = Field(
        None,
        alias="TransactionWarnDesc",
        name="",
        description="",
        example="Payment failure",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    update_status_media_list: Optional[List[UpdateStatusMediaListItem]] = Field(
        None,
        alias="UpdateStatusMediaList",
        name="",
        description="",
    )

    user_account_code: Optional[str] = Field(
        None,
        alias="UserAccountCode",
        name="",
        description="",
        example="AAAAAAAABB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_id: Optional[str] = Field(
        None,
        alias="UserAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0B6F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_last_update: Optional[datetime] = Field(
        None,
        alias="UserAccountLastUpdate",
        name="",
        description="",
        example="2023-06-07T16:10:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_account_name: Optional[str] = Field(
        None,
        alias="UserAccountName",
        name="",
        description="",
        example="Mouse, Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_login_alias: Optional[str] = Field(
        None,
        alias="UserLoginAlias",
        name="",
        description="",
        example="MOUSM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validated: bool = Field(
        ...,
        alias="Validated",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_code: str = Field(
        ...,
        alias="WorkstationCode",
        name="",
        description="",
        example="ENTTL-ACC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_id: str = Field(
        ...,
        alias="WorkstationId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA6AFE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_last_update: datetime = Field(
        ...,
        alias="WorkstationLastUpdate",
        name="",
        description="",
        example="2020-12-29T01:35:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_name: str = Field(
        ...,
        alias="WorkstationName",
        name="",
        description="",
        example="Guest Account API",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    payment_list: Optional[List[PaymentListItem]] = Field(
        None,
        alias="PaymentList",
        name="",
        description="",
    )

    meta_data_list: Optional[List[MetaDataListItem2]] = Field(
        None,
        alias="MetaDataList",
        name="",
        description="",
    )

    item_list: Optional[List[ItemListItem1]] = Field(
        None,
        alias="ItemList",
        name="",
        description="",
    )

    voided_ticket_list: Optional[List[VoidedTicketListItem]] = Field(
        None,
        alias="VoidedTicketList",
        name="",
        description="",
    )

    encoded_ticket_list: Optional[List[EncodedTicketListItem]] = Field(
        None,
        alias="EncodedTicketList",
        name="",
        description="",
    )

    transfer_ticket_list: Optional[List[TransferTicketListItem]] = Field(
        None,
        alias="TransferTicketList",
        name="",
        description="",
    )

    biometric_reset_ticket_list: Optional[List[BiometricResetTicketListItem]] = Field(
        None,
        alias="BiometricResetTicketList",
        name="",
        description="",
    )

    update_ticket_list: Optional[List[UpdateTicketListItem]] = Field(
        None,
        alias="UpdateTicketList",
        name="",
        description="",
    )

    encoded_media_list: Optional[List[EncodedMediaListItem]] = Field(
        None,
        alias="EncodedMediaList",
        name="",
        description="",
    )


class Payload(BaseModel):
    order: Order = Field(
        ...,
        alias="Order",
        name="",
        description="",
    )

    transaction: Transaction = Field(
        ...,
        alias="Transaction",
        name="",
        description="",
    )


class SnAppTransactionModel(BaseModel):
    """Payload class for SnAppTransactionModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Transaction"
        stream_name = ""
        description = """"""
        unique_identifier = ["Payload.Transaction.TransactionId"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = [
            "SnApp.Transaction.AccountChangeStatus",
            "SnApp.Transaction.ChangePerformance",
            "SnApp.Transaction.FailedSaleVoidCancellation",
            "SnApp.Transaction.ForeignCurrencyExchange",
            "SnApp.Transaction.GiftCardActivation",
            "SnApp.Transaction.GiftCardCashout",
            "SnApp.Transaction.GiftCardReload",
            "SnApp.Transaction.InstallmentContractVoid",
            "SnApp.Transaction.ManualRedemption",
            "SnApp.Transaction.MediaAssign",
            "SnApp.Transaction.MediaChangeStatus",
            "SnApp.Transaction.NegativeTransaction",
            "SnApp.Transaction.Normal",
            "SnApp.Transaction.OrderAbort",
            "SnApp.Transaction.OrderVoid",
            "SnApp.Transaction.PortfolioMerge",
            "SnApp.Transaction.ProductRefund",
            "SnApp.Transaction.RecycleMedia",
            "SnApp.Transaction.RedemptionVoid",
            "SnApp.Transaction.Renewal",
            "SnApp.Transaction.TicketChangePriority",
            "SnApp.Transaction.TicketTransfer",
            "SnApp.Transaction.TicketUpdate",
            "SnApp.Transaction.UpgradeDowngrade",
        ]

    header: GlobalSnAppHeader = Field(
        ...,
        alias="Header",
        name="",
        description="",
    )

    payload: Payload = Field(
        ...,
        alias="Payload",
        name="",
        description="",
    )
