"""Source Data Contract for SnApp Redemption"""

from __future__ import annotations

from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
    GlobalSnAppEligibilityGroup,
    GlobalSnAppTicketCodeAliasListItem,
    GlobalSnAppTransactionCodeAliasListItem,
    GlobalSnAppMediaCodeListItem,
)


class Media(BaseModel):
    """Redemption Media payload"""

    entity_alias: Optional[str] = Field(
        None,
        alias="EntityAlias",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_calc_code: Optional[str] = Field(
        None,
        alias="MediaCalcCode",
        name="",
        description="",
        example="M:1000.0.123123.1606",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_code_list: Optional[List[GlobalSnAppMediaCodeListItem]] = Field(
        None,
        alias="MediaCodeList",
        name="",
        description="",
    )

    media_id: Optional[str] = Field(
        None,
        alias="MediaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAACA7D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_type: int = Field(
        ...,
        alias="MediaType",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_type_desc: str = Field(
        ...,
        alias="MediaTypeDesc",
        name="",
        description="",
        example="Card",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Portfolio(BaseModel):
    """Portfolio payload"""

    account_code: Optional[str] = Field(
        None,
        alias="AccountCode",
        name="",
        description="",
        example="AAAAAAAAAAAAABBBBBBB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_id: Optional[str] = Field(
        None,
        alias="AccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC75F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_name: Optional[str] = Field(
        None,
        alias="AccountName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ats_account_alias: Optional[str] = Field(
        None,
        alias="AtsAccountAlias",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_id: Optional[str] = Field(
        None,
        alias="PortfolioId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC80C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Ticket(BaseModel):
    """Redemption ticket payload"""

    ats_ticket_barcode: Optional[str] = Field(
        None,
        alias="AtsTicketBarcode",
        name="",
        description="",
        example="SILVER PASS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ats_ticket_tcod: Optional[str] = Field(
        None,
        alias="AtsTicketTCOD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    barcode18: str = Field(
        ...,
        alias="Barcode18",
        name="",
        description="",
        example="12345678ABCDEFGHD5A3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cumulative_theme_park_usage_day_count: int = Field(
        ...,
        alias="CumulativeThemeParkUsageDayCount",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cumulative_usage_day_count: int = Field(
        ...,
        alias="CumulativeUsageDayCount",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dssn: str = Field(
        ...,
        alias="Dssn",
        name="",
        description="",
        example="091123-DTI-0-43801",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_date_time: datetime = Field(
        ...,
        alias="EncodeDateTime",
        name="",
        description="",
        example="2023-09-11T16:48:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encode_fiscal_date: date = Field(
        ...,
        alias="EncodeFiscalDate",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_alias: Optional[str] = Field(
        None,
        alias="EntityAlias",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expired_on_date_time: Optional[datetime] = Field(
        None,
        alias="ExpiredOnDateTime",
        name="",
        description="",
        example="2023-09-11T18:16:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_usage_date_time: datetime = Field(
        ...,
        alias="FirstUsageDateTime",
        name="",
        description="",
        example="2023-09-11T18:16:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    magcode: str = Field(
        ...,
        alias="Magcode",
        name="",
        description="",
        example=" ABCDABCDABCDABCDABCDABCDABABCDABCDABCDABCDABCDABCDABABCDABCDCBLBDFT0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio_account_last_update: Optional[date] = Field(
        None,
        alias="PortfolioAccountLastUpdate",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_code: str = Field(
        ...,
        alias="ProductCode",
        name="",
        description="",
        example="4JWRA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_entitlement_duration_count: Optional[str] = Field(
        None,
        alias="ProductEntitlementDurationCount",
        name="",
        description="",
        example="4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="ProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA5AAA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_last_update: date = Field(
        ...,
        alias="ProductLastUpdate",
        name="",
        description="",
        example="2023-05-19",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_name: str = Field(
        ...,
        alias="ProductName",
        name="",
        description="",
        example="4DAY 1P TC 24     AD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    renewal_date: Optional[date] = Field(
        None,
        alias="RenewalDate",
        name="",
        description="",
        example="2022-10-03",
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
        example="Q42J7V76",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_fiscal_date: date = Field(
        ...,
        alias="SaleFiscalDate",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_id: str = Field(
        ...,
        alias="SaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC784",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_detailed_id: str = Field(
        ...,
        alias="SaleItemDetailedId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC833",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_item_id: str = Field(
        ...,
        alias="SaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC81D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_operating_area_code: str = Field(
        ...,
        alias="SaleOperatingAreaCode",
        name="",
        description="",
        example="SDIAA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_operating_area_id: str = Field(
        ...,
        alias="SaleOperatingAreaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA0CA3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_operating_area_name: str = Field(
        ...,
        alias="SaleOperatingAreaName",
        name="",
        description="",
        example="Art of Animation Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sale_transaction_id: str = Field(
        ...,
        alias="SaleTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC7AF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    t_cod: str = Field(
        ...,
        alias="TCod",
        name="",
        description="",
        example="11100000000000801",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="",
        description="",
        example="1000.0.123123.3801",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_id: str = Field(
        ...,
        alias="TicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC839",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_validity_end: Optional[date] = Field(
        None,
        alias="TicketValidityEnd",
        name="",
        description="",
        example="2023-09-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_validity_start: date = Field(
        ...,
        alias="TicketValidityStart",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_amount: float = Field(
        ...,
        alias="UnitAmount",
        name="",
        description="",
        example=384.67,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_encode_transaction_id: str = Field(
        ...,
        alias="UpgradeFromEncodeTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC7AF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_code: Optional[str] = Field(
        None,
        alias="UpgradeFromProductCode",
        name="",
        description="",
        example="4A0A3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_id: Optional[str] = Field(
        None,
        alias="UpgradeFromProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAD55F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_product_name: Optional[str] = Field(
        None,
        alias="UpgradeFromProductName",
        name="",
        description="",
        example="4 PARK MAGIC      CH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_channel_code: Optional[str] = Field(
        None,
        alias="UpgradeFromSaleChannelCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_channel_id: Optional[str] = Field(
        None,
        alias="UpgradeFromSaleChannelId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_channel_name: Optional[str] = Field(
        None,
        alias="UpgradeFromSaleChannelName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_fiscal_date: date = Field(
        ...,
        alias="UpgradeFromSaleFiscalDate",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_item_id: str = Field(
        ...,
        alias="UpgradeFromSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC81D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_sale_transaction_id: str = Field(
        ...,
        alias="UpgradeFromSaleTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC7AF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_from_ticket_id: str = Field(
        ...,
        alias="UpgradeFromTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC839",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_encode_transaction_id: str = Field(
        ...,
        alias="UpgradeRootEncodeTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC7AF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_code: Optional[str] = Field(
        None,
        alias="UpgradeRootProductCode",
        name="",
        description="",
        example="4A0A3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_id: Optional[str] = Field(
        None,
        alias="UpgradeRootProductId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAD55F",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_product_name: Optional[str] = Field(
        None,
        alias="UpgradeRootProductName",
        name="",
        description="",
        example="4 PARK MAGIC      CH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_channel_code: Optional[str] = Field(
        None,
        alias="UpgradeRootSaleChannelCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_channel_id: Optional[str] = Field(
        None,
        alias="UpgradeRootSaleChannelId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_channel_name: Optional[str] = Field(
        None,
        alias="UpgradeRootSaleChannelName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_fiscal_date: date = Field(
        ...,
        alias="UpgradeRootSaleFiscalDate",
        name="",
        description="",
        example="2023-09-11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_id: str = Field(
        ...,
        alias="UpgradeRootSaleId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC784",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_item_id: str = Field(
        ...,
        alias="UpgradeRootSaleItemId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC81D",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_sale_transaction_id: str = Field(
        ...,
        alias="UpgradeRootSaleTransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC7AF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrade_root_ticket_id: str = Field(
        ...,
        alias="UpgradeRootTicketId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAC839",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_after_upgrade: bool = Field(
        ...,
        alias="UsageAfterUpgrade",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_code_alias_list: Optional[List[GlobalSnAppTicketCodeAliasListItem]] = Field(
        None,
        alias="TicketCodeAliasList",
        name="",
        description="",
    )

    transaction_code_alias_list: Optional[List[GlobalSnAppTransactionCodeAliasListItem]] = Field(
        None,
        alias="TransactionCodeAliasList",
        name="",
        description="",
    )


class RedemptionPayload(BaseModel):
    """Actual Redemption payload"""

    access_area_code: str = Field(
        ...,
        alias="AccessAreaCode",
        name="",
        description="",
        example="ACC-WSTGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_area_id: str = Field(
        ...,
        alias="AccessAreaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA6944",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_area_name: str = Field(
        ...,
        alias="AccessAreaName",
        name="",
        description="",
        example="HS GA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_point_code: str = Field(
        ...,
        alias="AccessPointCode",
        name="",
        description="",
        example="ST114VM054",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_point_id: str = Field(
        ...,
        alias="AccessPointId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA7A80",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    access_point_name: str = Field(
        ...,
        alias="AccessPointName",
        name="",
        description="",
        example="Hollywood Studios DAP 114",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bio_enrollment_type: int = Field(
        ...,
        alias="BioEnrollmentType",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_group: bool = Field(
        ...,
        alias="BiometricGroup",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_group_ticket_id: Optional[str] = Field(
        None,
        alias="BiometricGroupTicketId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    biometric_match_number: Optional[int] = Field(
        None,
        alias="BiometricMatchNumber",
        name="",
        description="",
        example=28332,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_code: str = Field(
        ...,
        alias="EventCode",
        name="",
        description="",
        example="EVT-STGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_id: str = Field(
        ...,
        alias="EventId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA7B35",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_name: str = Field(
        ...,
        alias="EventName",
        name="",
        description="",
        example="HS Gen Adm",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_usage_access_point_code: str = Field(
        ...,
        alias="FirstUsageAccessPointCode",
        name="",
        description="",
        example="AK136VM102",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_usage_indicator: bool = Field(
        ...,
        alias="FirstUsageIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    group_usage_quantity: int = Field(
        ...,
        alias="GroupUsageQuantity",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inc_product_code: Optional[str] = Field(
        None,
        alias="IncProductCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inc_product_id: Optional[str] = Field(
        None,
        alias="IncProductId",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inc_product_name: Optional[str] = Field(
        None,
        alias="IncProductName",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_code: str = Field(
        ...,
        alias="LocationCode",
        name="",
        description="",
        example="LOC-WSTTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_id: str = Field(
        ...,
        alias="LocationId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA492C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_name: str = Field(
        ...,
        alias="LocationName",
        name="",
        description="",
        example="HOLLYWOOD STUDIOS THEME PARK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media: Media = Field(
        ...,
        alias="Media",
        name="",
        description="",
    )

    performance_date_time: datetime = Field(
        ...,
        alias="PerformanceDateTime",
        name="",
        description="",
        example="2023-09-12T03:00:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    performance_id: str = Field(
        ...,
        alias="PerformanceId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAEB35",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    portfolio: Portfolio = Field(
        ...,
        alias="Portfolio",
        name="",
        description="",
    )

    previous_usage_access_point_code: Optional[str] = Field(
        None,
        alias="PreviousUsageAccessPointCode",
        name="",
        description="",
        example="ST132VM102",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket: Ticket = Field(
        ...,
        alias="Ticket",
        name="",
        description="",
    )

    ticket_usage_id: str = Field(
        ...,
        alias="TicketUsageId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA22DA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ticket_usage_user_account_id: Optional[str] = Field(
        None,
        alias="TicketUsageUserAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA6000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_after_renewal_indicator: bool = Field(
        ...,
        alias="UsageAfterRenewalIndicator",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_date_time: datetime = Field(
        ...,
        alias="UsageDateTime",
        name="",
        description="",
        example="2023-09-12T22:26:50.680+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_fiscal_date: date = Field(
        ...,
        alias="UsageFiscalDate",
        name="",
        description="",
        example="2023-09-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_operating_area_code: str = Field(
        ...,
        alias="UsageOperatingAreaCode",
        name="",
        description="",
        example="SSTAC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_operating_area_id: str = Field(
        ...,
        alias="UsageOperatingAreaId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA901A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_operating_area_name: str = Field(
        ...,
        alias="UsageOperatingAreaName",
        name="",
        description="",
        example="Hollywood Studios Access Control",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type: int = Field(
        ...,
        alias="UsageType",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usage_type_desc: str = Field(
        ...,
        alias="UsageTypeDesc",
        name="",
        description="",
        example="Re-entry",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validate_result: int = Field(
        ...,
        alias="ValidateResult",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validate_result_desc: str = Field(
        ...,
        alias="ValidateResultDesc",
        name="",
        description="",
        example="Reentry",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    eligibility_group: Optional[GlobalSnAppEligibilityGroup] = Field(
        None,
        alias="EligibilityGroup",
        name="",
        description="",
    )


class Payload(RedemptionPayload):
    """actual Redemption Payload with an optional previous redemption object that uses the same fields"""

    previous_redemption: Optional[RedemptionPayload] = Field(
        None,
        alias="PreviousRedemption",
        name="",
        description="",
    )


class SnAppRedemptionModel(BaseModel):
    """Payload class for SnAppRedemptionModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Redemption"
        stream_name = ""
        description = """Ticket redemption information relating to Park entry"""
        unique_identifier = ["Payload.TicketUsageId"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = ["SnApp.Redemption.Crossover", "SnApp.Redemption.Entry", "SnApp.Redemption.ReEntry"]

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(
        ...,
        alias="Payload",
        description="Data payload",
    )
