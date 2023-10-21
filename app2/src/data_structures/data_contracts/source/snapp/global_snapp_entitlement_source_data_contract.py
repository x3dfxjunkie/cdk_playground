"""Global SnApp Contract"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppTicketCodeAliasListItem,
    GlobalSnAppExternalReferenceItem,
)


class GlobalSnAppEntitlementOrder(BaseModel):
    """A dataclass that represents the object Order for SnApp"""

    external_reference: List[GlobalSnAppExternalReferenceItem] = Field(
        ...,
        alias="ExternalReference",
        name="External reference",
        description="List of object that represents the guest external reference",
    )
    reservation_code: str = Field(
        ...,
        alias="ReservationCode",
        name="Reservation code",
        description="Code of the reservation",
        example="WPLF12345678",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppEntitlementMetaData(BaseModel):
    """A dataclass that represents the object MetaData for SnApp"""

    ap_season_class: Optional[str] = Field(
        None,
        alias="APSeasonClass",
        name="Annual pass season class",
        description="Class of the annual pass season",
        example="A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    annual_pass_type: Optional[str] = Field(
        None,
        alias="AnnualPassType",
        name="Annual pass type",
        description="Type of the annual pass",
        example="SORCE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    consume: Optional[str] = Field(
        None,
        alias="Consume",
        name="Consume",
        description="Type of consumable",
        example="T",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    memory_maker: Optional[str] = Field(
        None,
        alias="MemoryMaker",
        name="Memory maker",
        description="",
        example="30D-MEM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_entitlement_type: Optional[str] = Field(
        None,
        alias="ProductEntitlementType",
        name="Product entitlement type",
        description="Type of the product entitlement",
        example="AP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppEntitlementProduct(BaseModel):
    """A dataclass that represents the object Product for SnApp"""

    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="Product identifier code",
        example="ZM0DA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    externally_priced: bool = Field(
        ...,
        alias="ExternallyPriced",
        name="Externally priced",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    meta_data: GlobalSnAppEntitlementMetaData = Field(
        ...,
        alias="MetaData",
        name="Meta data",
        description="Object that represents the product meta data",
    )
    name: str = Field(
        ...,
        alias="Name",
        name="Name",
        description="Product name",
        example="10DAY PHP         CH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: int = Field(
        ...,
        alias="Type",
        name="Type",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppEntitlementTicket(BaseModel):
    """A dataclass that represents the object Ticket for SnApp"""

    barcode: str = Field(
        ...,
        alias="Barcode",
        name="Barcode",
        description="Ticket barcode",
        example="ABCD1234ABCD12345",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="Ticket indentifier code",
        example="08011728071300000",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    consumed: Optional[bool] = Field(
        None,
        alias="Consumed",
        name="Consumed",
        description="is the ticket consumed?",
        example=True,
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    create_date: str = Field(
        ...,
        alias="CreateDate",
        name="Create date",
        description="",
        example="020719",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dssn: str = Field(
        ...,
        alias="Dssn",
        name="Date-Site-Station-Number",
        description="Basis of all ticket entitlements: Date Sold, Site, Station Number, Number of Tickets Sold",
        example="020719-ABC-119-00031",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    expired_on_date_time: Optional[datetime] = Field(
        None,
        alias="ExpiredOnDateTime",
        name="Expired on date time",
        description="Date and time when ticket was expired",
        example="2023-04-14T00:00:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_quantity: int = Field(
        ...,
        alias="GroupQuantity",
        name="Group quantity",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="Id",
        name="Id",
        description="Source system ticket id",
        example="44444444-CCCC-4444-CCCC-4444444459000",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    last_usage_date_time: Optional[datetime] = Field(
        None,
        alias="LastUsageDateTime",
        name="Last usage date time",
        description="Date and time when ticket was last used",
        example="2020-12-12T20:20:20.123456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    magnetic_code: str = Field(
        ...,
        alias="MagneticCode",
        name="Magnetic code",
        description="",
        example="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    no_charge: bool = Field(
        ...,
        alias="NoCharge",
        name="No charge",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price: float = Field(
        ...,
        alias="Price",
        name="Price",
        description="Value effectively paid by the customer",
        example=867.15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    purchase_date: date = Field(
        ...,
        alias="PurchaseDate",
        name="Purchase date",
        description="Date when the ticket was purchased",
        example="2023-03-31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_priority_order: int = Field(
        ...,
        alias="RedemptionPriorityOrder",
        name="Redemption priority order",
        description="Order in which the ticket is redeemed",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    remaining_value: float = Field(
        ...,
        alias="RemainingValue",
        name="Remaining value",
        description="",
        example=38.99,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    serial_number: str = Field(
        ...,
        alias="SerialNumber",
        name="Serial number",
        description="",
        example="63706",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site: str = Field(
        ...,
        alias="Site",
        name="Site",
        description="",
        example="DTI",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    station: str = Field(
        ...,
        alias="Station",
        name="Station",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: int = Field(
        ...,
        alias="Status",
        name="Status",
        description="Status code of the ticket",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax: float = Field(
        ...,
        alias="Tax",
        name="Tax",
        description="Amount of tax charged on the ticket",
        example=152.32,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_code: str = Field(
        ...,
        alias="TicketCode",
        name="Ticket code",
        description="Code of the ticket",
        example="P:1001.0.200031.11111",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    upgrade_value: Optional[int] = Field(
        None,
        alias="UpgradeValue",
        name="Upgrade Value",
        description="Upgrade Value of the ticket.  Relates to Delta pricing",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    usages_count: int = Field(
        ...,
        alias="UsagesCount",
        name="Usages count",
        description="Number of times the ticket was used",
        example=9,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    valid_end_date: Optional[date] = Field(
        None,
        alias="ValidEndDate",
        name="Valid end date",
        description="Date that represents the end of the validity period of the ticket",
        example="2023-04-14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    valid_start_date: date = Field(
        ...,
        alias="ValidStartDate",
        name="Valid start date",
        description="Date that represents the start of the validity period of the ticket",
        example="2023-03-31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_code_alias_list: Optional[List[GlobalSnAppTicketCodeAliasListItem]] = Field(
        None,
        alias="TicketCodeAliasList",
        name="Ticket Code Alias List",
        description="",
    )
