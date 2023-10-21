"""Source Data Contract for SnApp Entitlement without Redemption"""

from __future__ import annotations
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
    GlobalSnAppCastAsGuest,
    GlobalSnAppEligibilityGroup,
    GlobalSnAppAccount,
    GlobalSnAppTransaction,
)
from app.src.data_structures.data_contracts.source.snapp.global_snapp_entitlement_source_data_contract import (
    GlobalSnAppEntitlementTicket,
    GlobalSnAppEntitlementProduct,
)


class EntitlementTicket(GlobalSnAppEntitlementTicket):
    """A dataclass that represents the object Ticket for SnApp"""

    consumed: bool = Field(
        ...,
        alias="Consumed",
        name="Consumed",
        description="is the ticket consumed?",
        example=True,
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    last_usage_date_time: datetime = Field(
        ...,
        alias="LastUsageDateTime",
        name="Last usage date time",
        description="Date and time when ticket was last used",
        example="2020-12-12T12:12:12.123456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class UsageInfo(BaseModel):
    """A dataclass that represents entitlement.redemption usage info"""

    usage_date_time: datetime = Field(
        ...,
        alias="UsageDateTime",
        name="Usage Date Time",
        description="Ticket Usage Date Timestamp",
        example="2022-09-09T16:57:30.017+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validate_date_time: Optional[datetime] = Field(
        None,
        alias="ValidateDateTime",
        name="Validate Date Time",
        description="Validating Date Timestamp for the ticket usage",
        example="2022-11-10T21:16:00.000+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: int = Field(
        ...,
        alias="Type",
        name="Type",
        description="Type of redemption, correlates with and also described via SnApp.Redemption namespace.  1 - entry, 3 - re-entry, 4 - crossover",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validation_result: int = Field(
        ...,
        alias="Type",
        name="ValidationResult",
        description="Type of redemption, correlates with and also described via SnApp.Redemption namespace.  1 - entry, 3 - re-entry, 4 - crossover",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    access_point_code: str = Field(
        ...,
        alias="AccessPointCode",
        name="Access Point Code",
        description="Ticket usage access point location code",
        example="EC158SM021",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_code: str = Field(
        ...,
        alias="EventCode",
        name="Event Code",
        description="Ticket usage event code",
        example="EVT-ECGA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bio_enrollment_type: int = Field(
        ...,
        alias="BioEnrollmentType",
        name="Bio Enrollment Type",
        description="Bio Enrollment Type",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    biometric_group: bool = Field(
        ...,
        alias="BiometricGroup",
        name="Biometric Group",
        description="Biometric Group",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    biometric_group_ticket_id: Optional[int] = Field(
        None,
        alias="BiometricGroupTicketId",
        name="Biometric Group Ticket Id",
        description="Biometric Group Ticket Id",
        example=0,  # TODO: check if this is the correct example
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    biometric_level: int = Field(
        ...,
        alias="BiometricLevel",
        name="Biometric Level",
        description="Biometric Level",
        example=30,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    biometric_score: Optional[int] = Field(
        None,
        alias="BiometricScore",
        name="biometric_score",
        description="",
        example=58675,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Redemption(BaseModel):
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
    product: GlobalSnAppEntitlementProduct = Field(
        ...,
        alias="Product",
        name="Product",
        description="An object that represents the Product",
    )
    ticket: EntitlementTicket = Field(
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
    usage_info: UsageInfo = Field(
        ...,
        alias="UsageInfo",
        name="Usage Info",
        description="Object that represents the usage info for the ticket",
    )


class Payload(BaseModel):
    """A dataclass that represents the object Payload for SnApp"""

    redemption: Redemption = Field(
        ...,
        alias="Redemption",
        name="Redemption",
        description="Object that represents the Entitlement Redemption",
    )


class SnAppEntitlementRedemptionModel(BaseModel):
    """A dataclass that wraps a representation of SnApp dataclass"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Entitlement Events"
        stream_name = "guest360-snapp-stream"
        description = "SnApp events representing entitlement redemption, which is a part of SnApp Entitlement namespace but has a different schema"
        unique_identifier = ["Payload.Redemption.Ticket.TicketCode", "Payload.Redemption.Transaction.TransactionCode"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "Header.namespace"
        key_path_value = "SnApp.Entitlement.Redemption"

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
