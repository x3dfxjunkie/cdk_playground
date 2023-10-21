"""Source Data Contract for SnApp Entitlement without Redemption"""

from __future__ import annotations
from typing import List, Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
    GlobalSnAppCastAsGuest,
    GlobalSnAppEligibilityGroup,
    GlobalSnAppExternalReferenceItem,
    GlobalSnAppAccount,
    GlobalSnAppMediaItem,
    GlobalSnAppTransaction,
)
from app.src.data_structures.data_contracts.source.snapp.global_snapp_entitlement_source_data_contract import (
    GlobalSnAppEntitlementOrder,
    GlobalSnAppEntitlementTicket,
    GlobalSnAppEntitlementProduct,
)


class SnAppEntitlementOrder(GlobalSnAppEntitlementOrder):
    """A dataclass that represents the object Order for SnApp"""

    reservation_code: Optional[str] = Field(
        None,
        alias="ReservationCode",
        name="Reservation Code",
        description="",
        example="ABCDEFG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_reference: Optional[List[GlobalSnAppExternalReferenceItem]] = Field(
        None,
        alias="ExternalReference",
        name="External reference",
        description="List of object that represents the guest external reference",
    )


class Entitlement(BaseModel):
    """A dataclass that represents the object Entitlement for SnApp"""

    account: GlobalSnAppAccount = Field(
        ...,
        alias="Account",
        name="Account",
        description="Object that represents the Account",
    )
    cast_as_guest: Optional[GlobalSnAppCastAsGuest] = Field(
        None,
        alias="CastAsGuest",
        name="Cast as Guest information",
        description="Object that represents the cast member info as a guest",
    )
    eligibility_group: Optional[GlobalSnAppEligibilityGroup] = Field(
        None,
        alias="EligibilityGroup",
        name="Eligibility group",
        description="Object that represents the EligibilityGroup",
    )

    media_list: Optional[List[GlobalSnAppMediaItem]] = Field(
        None,
        alias="MediaList",
        name="Media list",
        description="A list of objects that represents media",
    )
    order: Optional[SnAppEntitlementOrder] = Field(
        None,
        alias="Order",
        name="Order",
        description="An object that represents order",
    )
    previous_ticket: Optional[GlobalSnAppEntitlementTicket] = Field(
        None,
        alias="PreviousTicket",
        name="Previous ticket",
        description="An object that represents previous ticket if the entitlement is based on a previous ticket, such as upgrade/downgrade",
    )
    product: GlobalSnAppEntitlementProduct = Field(
        ...,
        alias="Product",
        name="Product",
        description="An object that represents the Product",
    )
    ticket: GlobalSnAppEntitlementTicket = Field(
        ...,
        alias="Ticket",
        name="Ticket",
        description="Object that represents the Ticket",
    )
    transaction: GlobalSnAppTransaction = Field(
        ...,
        alias="Transaction",
        name="Transaction",
        description="Object that represents the transaction for the ticket",
    )


class Payload(BaseModel):
    """A dataclass that represents the object Payload for SnApp"""

    entitlement: Entitlement = Field(
        ...,
        alias="Entitlement",
        name="Entitlement",
        description="Object that represents the Entitlement",
    )


class SnAppEntitlementModel(BaseModel):
    """A dataclass that represents SnApp dataclass"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Entitlement Events"
        stream_name = "guest360-snapp-stream"
        description = "SnApp events representing entitlement, except for redemption which is its own data contract"
        unique_identifier = ["Payload.Entitlement.Ticket.TicketCode", "Payload.Entitlement.Transaction.TransactionCode"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = (
            [
                "SnApp.Entitlement.Update, SnApp.Entitlement.PartialRefund, SnApp.Entitlement.Expire, SnApp.Entitlement.Void, SnApp.Entitlement.Renew, SnApp.Entitlement.Blocked, SnApp.Entitlement.TicketSale, SnApp.Entitlement.Unblocked, SnApp.Entitlement.Snapshot, SnApp.Entitlement.PrioritizeRedemptionOrder, SnApp.Entitlement.Transfer, SnApp.Entitlement.UpgradeDowngrade, SnApp.Entitlement.Refund"
            ],
        )

    header: GlobalSnAppHeader = Field(
        ...,
        alias="Header",
        name="Header",
        description="An object that represents header",
    )
    payload: Payload = Field(
        ...,
        alias="Payload",
        name="Payload",
        description="An object that represents payload",
    )
