"""Source Data Contract for SnApp Ledger Log"""


from __future__ import annotations
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class EventIdentifier(BaseModel):
    data_id: str = Field(
        ...,
        alias="DataId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE031",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fiscal_date: date = Field(
        ...,
        alias="FiscalDate",
        name="",
        description="",
        example="2023-09-15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LedgerEntryListItem(BaseModel):
    account_code: str = Field(
        ...,
        alias="AccountCode",
        name="",
        description="",
        example="LOC-WWDTI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_id: str = Field(
        ...,
        alias="AccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAA5CCC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    account_name: str = Field(
        ...,
        alias="AccountName",
        name="",
        description="",
        example="DISNEY TICKET INTERFACE (DTI)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cap_coa_categorization: Optional[str] = Field(
        None,
        alias="CAP_COA_Categorization",
        name="",
        description="",
        example="PAYMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    credit: float = Field(
        ...,
        alias="Credit",
        name="",
        description="",
        example=123.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    debit: float = Field(
        ...,
        alias="Debit",
        name="",
        description="",
        example=98.76,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_code: Optional[str] = Field(
        None,
        alias="EntityCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_id: str = Field(
        ...,
        alias="EntityId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE031",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_name: str = Field(
        ...,
        alias="EntityName",
        name="",
        description="",
        example="T:1111.0.000000.45138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_type: int = Field(
        ...,
        alias="EntityType",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entity_type_desc: str = Field(
        ...,
        alias="EntityTypeDesc",
        name="",
        description="",
        example="Transaction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ledger_account_code: str = Field(
        ...,
        alias="LedgerAccountCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ledger_account_id: str = Field(
        ...,
        alias="LedgerAccountId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAD8BB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ledger_account_name: str = Field(
        ...,
        alias="LedgerAccountName",
        name="",
        description="",
        example="VOUCHER (CHARGE CODE)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trigger_type: int = Field(
        ...,
        alias="TriggerType",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trigger_type_desc: str = Field(
        ...,
        alias="TriggerTypeDesc",
        name="",
        description="",
        example="Manual",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Transaction(BaseModel):
    dti_sales_transaction_id: Optional[str] = Field(
        None,
        alias="DTISalesTransactionId",
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
        example="L1241",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    op_area_code: str = Field(
        ...,
        alias="OpAreaCode",
        name="",
        description="",
        example="BACKOFFICE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pnr: str = Field(
        ...,
        alias="PNR",
        name="",
        description="",
        example="CUJABC123",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seller_reservation_code: Optional[str] = Field(
        None,
        alias="SellerReservationCode",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    time_of_payment: Optional[str] = Field(
        None,
        alias="TimeOfPayment",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    total_tax: int = Field(
        ...,
        alias="TotalTax",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction: str = Field(
        ...,
        alias="Transaction",
        name="",
        description="",
        example="T:1111.0.000000.45138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_date_time: datetime = Field(
        ...,
        alias="TransactionDateTime",
        name="",
        description="",
        example="2023-09-15T19:22:58.470+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_fiscal_date: date = Field(
        ...,
        alias="TransactionFiscalDate",
        name="",
        description="",
        example="2023-09-15",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_flags: List[str] = Field(
        ...,
        alias="TransactionFlags",
        name="",
        description="",
        example=[""],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: str = Field(
        ...,
        alias="TransactionId",
        name="",
        description="",
        example="AAAAAAAA-1111-AAAA-1111-AAAAAAAAE031",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_type: int = Field(
        ...,
        alias="TransactionType",
        name="",
        description="",
        example=104,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_type_desc: str = Field(
        ...,
        alias="TransactionTypeDesc",
        name="",
        description="",
        example="Manual entry ledger",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    user_login_alias: str = Field(
        ...,
        alias="UserLoginAlias",
        name="",
        description="",
        example="MOUSM003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_code: str = Field(
        ...,
        alias="WorkstationCode",
        name="",
        description="",
        example="BKOFFICE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    workstation_type: Optional[str] = Field(
        None,
        alias="WorkstationType",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    date_time: datetime = Field(
        ...,
        alias="DateTime",
        name="",
        description="",
        example="2023-09-15T19:23:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_identifier: EventIdentifier = Field(
        ...,
        alias="EventIdentifier",
        name="",
        description="",
    )

    ledger_entry_list: List[LedgerEntryListItem] = Field(
        ...,
        alias="LedgerEntryList",
        name="",
        description="",
    )

    transaction: Transaction = Field(
        ...,
        alias="Transaction",
        name="",
        description="",
    )


class SnAppLedgerLogModel(BaseModel):
    """Payload class for SnAppLedgerLogModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Ledger Log"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = ""
        key_path_value = "SnApp.LedgerLog.Manual"

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
