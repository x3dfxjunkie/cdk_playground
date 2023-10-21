"""Source Data Contract for GAM DLR Tickets"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class NativeGuestIdItem(BaseModel):
    """Data class that represents various Guest Identifier types and values"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Identifier type",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Value",
        description="Identifier value",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Owner(BaseModel):
    """Data class that represents the object Owner"""

    owner_type: str = Field(
        ...,
        alias="ownerType",
        name="Owner type",
        description="Owner type identifier",
        example="B2C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    profile_id: Optional[str] = Field(
        None,
        alias="profileId",
        name="Profile ID",
        description="Profile ID",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    partner_id: Optional[str] = Field(
        None,
        alias="partnerId",
        name="Partner ID",
        description="Partner ID",
        example="05744314",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AssignedGuest(BaseModel):
    """Data class that represents the object AssignedGuest"""

    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="First Name",
        description="First Name of the guest",
        example="Donald",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="lastName",
        name="Last Name",
        description="Last Name of the guest",
        example="Duck",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    nickname: str = Field(
        ...,
        alias="nickname",
        name="Nickname",
        description="Nickname of the guest",
        example="Donald Duck",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class Category(BaseModel):
    """Data class that represents the object Category"""

    id: str = Field(
        ...,
        alias="id",
        name="Category ID",
        description="Category ID",
        example="admission-link-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="name",
        name="Name",
        description="Category Name",
        example="Theme Park Tickets",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class OptionItem(BaseModel):
    """Data class that represents the object OptionsListItem"""

    option_type: str = Field(
        ...,
        alias="optionType",
        name="Option type",
        description="Option type identifier",
        example="addOns",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    option_value: Optional[List[str]] = Field(
        None,
        alias="optionValue",
        name="Option value",
        description="Option value",
        example=["adult"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AdmissionEntitlement(BaseModel):
    """Data class that represents the object AdmissionEntitlement"""

    visual_id: str = Field(
        ...,
        alias="visualId",
        name="Visual ID",
        description="Visual identifier",
        example="1068090990849987010055",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    name: Optional[str] = Field(
        None,
        alias="name",
        name="Name",
        description="Name of the entitlement",
        example="1-Day Magic Kingdom Park Ticket",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    government_id_linked: bool = Field(
        ...,
        alias="governmentIdLinked",
        name="Government ID Linked",
        description="Is Government ID Linked",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    genie_plus: Optional[bool] = Field(
        None,
        alias="geniePlus",
        name="Genie Plus",
        description="Is Genie Plus",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sku: str = Field(
        ...,
        alias="sku",
        name="SKU",
        description="SKU identifier",
        example="68090",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_instance_id: Optional[str] = Field(
        None,
        alias="productInstanceId",
        name="Product Instance ID",
        description="Product Instance identifier",
        example="dlrThemePark_2_A_0_0_RF_AF_SOF_dlr_nonsellable_68090",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="status",
        description="Status of the entitlement",
        example="ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exchange_status: Optional[str] = Field(
        None,
        alias="exchangeStatus",
        name="Exchange status",
        description="If the entitlement is exchangeable",
        example="NOT_ELIGIBLE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary_guest: Optional[str] = Field(
        None,
        alias="primaryGuest",
        name="Primary Guest",
        description="Primary guest identifier",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    shared: bool = Field(
        ...,
        alias="shared",
        name="Shared",
        description="Is Shared",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_type_id: Optional[str] = Field(
        None,
        alias="productTypeId",
        name="Product Type ID",
        description="Product Type identifier",
        example="dlrThemePark",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feature_ids: Optional[List[str]] = Field(
        None,
        alias="featureIds",
        name="Feature IDs",
        description="List of feature IDs",
        example=["tier-0"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    voidable: bool = Field(
        ...,
        alias="voidable",
        name="Voidable",
        description="Is Voidable",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_age_group: Optional[str] = Field(
        None,
        alias="guestAgeGroup",
        name="Guest Age Group",
        description="Group of the guest age",
        example="Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    remaining_use: int = Field(
        ...,
        alias="remainingUse",
        name="Remaining use",
        description="Remaining use",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    use_count: int = Field(
        ...,
        alias="useCount",
        name="Use Count",
        description="Number of times the entitlement has been used",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary_guest_linked: bool = Field(
        ...,
        alias="primaryGuestLinked",
        name="Primary Guest Linked",
        description="Is Primary Guest Linked",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renewable: bool = Field(
        ...,
        alias="renewable",
        name="Renewable",
        description="Is Renewable",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    modifiable: bool = Field(
        ...,
        alias="modifiable",
        name="Modifiable",
        description="Is Modifiable",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgradeable: bool = Field(
        ...,
        alias="upgradeable",
        name="Upgradeable",
        description="Is Upgradeable",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    skip_renewal: bool = Field(
        ...,
        alias="skipRenewal",
        name="Skip Renewal",
        description="Is Skip Renewal",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    park_hopper: Optional[bool] = Field(
        None,
        alias="parkHopper",
        name="Park Hopper",
        description="Is Park Hopper",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source_lexvas: bool = Field(
        ...,
        alias="sourceLexvas",
        name="Source Lexvas",
        description="Is Source Lexvas",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    package_entitlement: bool = Field(
        ...,
        alias="packageEntitlement",
        name="Package Entitlement",
        description="Is Package Entitlement",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    main_entrance_pass: bool = Field(
        ...,
        alias="mainEntrancePass",
        name="Main Entrance Pass",
        description="Is Main Entrance Pass",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: Optional[datetime] = Field(
        None,
        alias="startDateTime",
        name="Start date time",
        description="Date and time of the start of the entitlement",
        example="2022-07-29T09:40:10.000-07:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time: Optional[datetime] = Field(
        None,
        alias="endDateTime",
        name="End date time",
        description="Date and time of the end of the entitlement",
        example="2022-07-29T09:40:10.000-07:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    owner: Owner = Field(..., alias="owner", name="Owner", description="Owner object")
    assigned_guest: Optional[AssignedGuest] = Field(
        None, alias="assignedGuest", name="Assigned guest", description="Assigned guest object"
    )
    category: Optional[Category] = Field(None, alias="category", name="Category", description="Category object")
    options: Optional[List[OptionItem]] = Field(
        None, alias="options", name="Options", description="List of option objects"
    )


class GAMDLRTicketsModel(BaseModel):
    """Payload class for GAMDLRTicketsModel"""

    class Config:
        """Payload Level Metadata"""

        name = "Tickets for DLR from GAM"
        stream_name = "gam-kinesis-gam-tickets-guest360-dlr"
        description = """DLR Guest tickets as shared from the ticketing source system"""
        unique_identifier = ["admissionEntitlement.visualId"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "ADMISSION"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type identifier",
        example="ADMISSION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Action",
        description="Action identifier",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ..., alias="nativeGuestIds", name="Native guest IDs", description="List of native guest identifiers"
    )
    admission_entitlement: AdmissionEntitlement = Field(
        ..., alias="admissionEntitlement", name="Admission entitlement", description="Admission entitlement object"
    )
