"""Source Data Contract for SnApp Payment Method"""

from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class Payload(BaseModel):
    """Class for Snapp PaymentMethod Payload"""

    auto_fill: bool = Field(
        ...,
        alias="AutoFill",
        name="Auto Fill",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    credit_ledger_account_code: str = Field(
        ...,
        alias="CreditLedgerAccountCode",
        name="Credit Ledger AccountCode",
        description="",
        example="#.#.#.#",  # nosec
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    credit_ledger_account_id: str = Field(
        ...,
        alias="CreditLedgerAccountId",
        name="Credit Ledger Account Id",
        description="F0A9D6EA-FEF3-FE17-0007-01630845FD0B",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    credit_ledger_account_name: Optional[str] = Field(
        None,
        alias="Credit Ledger Account Name",
        name="",
        description="",
        example="SNAPP CLEARING ACCOUNT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    custom_icon_name: Optional[str] = Field(
        None,
        alias="CustomIconName",
        name="Custom Icon Name",
        description="",
        example="Null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    debit_ledger_account_code: str = Field(
        ...,
        alias="DebitLedgerAccountCode",
        name="Debit Ledger Account Code",
        description="",
        example="#.#.#.#",  # nosec
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    debit_ledger_account_id: str = Field(
        ...,
        alias="DebitLedgerAccountId",
        name="Debit Ledger Account Id",
        description="",
        example="DE364459-B49E-7D4D-36EC-016308B57645",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    debit_ledger_account_name: str = Field(
        ...,
        alias="DebitLedgerAccountName",
        name="Debit Ledger Account Name",
        description="",
        example="VOUCHER (CHARGE CODE)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mask_ids: str = Field(
        ...,
        alias="MaskIDs",
        name="Mask IDs",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_change_amount: int = Field(
        ...,
        alias="MaxChangeAmount",
        name="Max Change Amount",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    payment_count_message: Optional[str] = Field(
        None,
        alias="PaymentCountMessage",
        name="Payment Count Message",
        description="",
        example="Null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    payment_group_tag_id: str = Field(
        ...,
        alias="PaymentGroupTagId",
        name="Payment Group Tag Id",
        description="",
        example="AC8186BA-DC07-528B-7A76-0178CB9F8532",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    payment_method_code: str = Field(
        ...,
        alias="PaymentMethodCode",
        name="Payment Method Code",
        description="",
        example="PMT-26",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plugin_default: bool = Field(
        ...,
        alias="PluginDefault",
        name="Plugin Default",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plugin_enabled: bool = Field(
        ...,
        alias="PluginEnabled",
        name="Plugin Enabled",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plugin_id: str = Field(
        ...,
        alias="PluginId",
        name="Plugin Id",
        description="",
        example="9BAB3003-E331-F820-548C-01711D099953",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plugin_name: str = Field(
        ...,
        alias="PluginName",
        name="Plugin Name",
        description="",
        example="Voucher (Billable)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    plugin_settings: Optional[str] = Field(
        None,
        alias="PluginSettings",
        name="Plugin Settings",
        description="",
        example="null",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    priority_order: int = Field(
        ...,
        alias="PriorityOrder",
        name="Priority Order",
        description="",
        example=8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppPaymentMethodModel(BaseModel):
    """SnAppPaymentMethodModel"""

    class Config:
        """Config for SnAppPaymentMethodModel"""

        title = "SnApp Payment Method"
        stream_name = "prd-use1-guest360-snapp-stream"
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = "SnApp.PaymentMethod"

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(..., alias="Payload", description="Data payload")
