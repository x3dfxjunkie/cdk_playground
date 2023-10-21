"""Source Data Contract for GAM WDW Admissions"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class AssignedGuest(BaseModel):
    """A dataclass that represents the object AssignedGuest"""

    first_name: str = Field(
        ...,
        alias="firstName",
        name="First Name",
        description="First Name of the guest",
        example="Donald",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: str = Field(
        ...,
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
    profile_id: Optional[str] = Field(
        None,
        alias="profileId",
        name="Profile ID",
        description="Profile identifier",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="middleName",
        name="Middle Name",
        description="Middle Name of the guest",
        example="Fauntleroy",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    prefix: Optional[str] = Field(
        None,
        alias="prefix",
        name="Prefix",
        description="Guest prefix",
        example="Mr.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class Category(BaseModel):
    """A dataclass that represents the object Category"""

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
    """A dataclass that represents the object OptionsListItem"""

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
    option_value: List[str] = Field(
        ...,
        alias="optionValue",
        name="Option value",
        description="Option value",
        example=["adult"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Owner(BaseModel):
    """A dataclass that represents the object Owner"""

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


class UsageItem(BaseModel):
    """A dataclass that represents the object UsageItem"""

    acp: str = Field(
        ...,
        alias="acp",
        name="acp",
        description="",
        example="18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acp_name: str = Field(
        ...,
        alias="acpName",
        name="acp name",
        description="",
        example="TURNSTILE 18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    facility: str = Field(
        ...,
        alias="facility",
        name="facility",
        description="Name of the facility",
        example="Disneyland Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="status",
        description="Status of the usage",
        example="Admission",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    use_no: Optional[int] = Field(
        None,
        alias="usageNo",
        name="Usage number",
        description="Number of the usage",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    use_time: Optional[datetime] = Field(
        None,
        alias="usageTime",
        name="Usage time",
        description="Date and time of the usage",
        example="2023-05-08T20:42:16.000-07:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LineageItem(BaseModel):
    """A dataclass that represents the object LineageItem"""

    date_sold: datetime = Field(
        ...,
        alias="dateSold",
        name="Date sold",
        description="Date and time of the sale",
        example="2022-07-01T06:18:02.000-07:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    expiration_date: datetime = Field(
        ...,
        alias="expirationDate",
        name="Expiration date",
        description="Date and time of the expiration",
        example="2022-07-01T06:18:02.000-07:00",
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
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="Status of the entitlement",
        example="TICKET_ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visual_id: str = Field(
        ...,
        alias="visualId",
        name="Visual ID",
        description="Visual identifier of the entitlement",
        example="52564719194252612638",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guest(BaseModel):
    """A dataclass that represents the object Guest"""

    type: Optional[str] = Field(
        None,
        alias="Type",
        name="Type",
        description="Type of the guest identifier",
        example="admission-link-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="Value",
        name="Value",
        description="Guest identifier value",
        example="YKX8UT6317GR79M22BDY",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class TransactionDssn(BaseModel):
    """A dataclass that represents the object Transaction DSSN"""

    site: Optional[str] = Field(
        None,
        alias="site",
        name="Site",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    station: Optional[str] = Field(
        None,
        alias="station",
        name="Station",
        description="",
        example="CXX001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    date: Optional[datetime] = Field(
        None,
        alias="date",
        name="Date",
        description="",
        example="2021-05-26T18:35:41Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_number: Optional[str] = Field(
        None,
        alias="transactionNumber",
        name="Transaction Number",
        description="",
        example="1234",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Transferable(BaseModel):
    """A dataclass that represents the object Transferable"""

    is_transferable: bool = Field(
        ...,
        alias="isTransferable",
        name="Is transferable",
        description="Is the ticket transferable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    reason: Optional[str] = Field(
        None,
        alias="reason",
        name="Reason",
        description="Reason for transferability",
        example="HAS_USAGES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AdmissionEntitlement(BaseModel):
    """A dataclass that represents the object AdmissionEntitlement"""

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
    feature_ids: Optional[List[str]] = Field(
        None,
        alias="featureIds",
        name="Feature IDs",
        description="List of feature IDs",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    genie_plus: Optional[bool] = Field(
        None,
        alias="geniePlus",
        name="Genie Plus",
        description="Is Genie Plus",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    government_id_linked: Optional[bool] = Field(
        None,
        alias="governmentIdLinked",
        name="Government ID Linked",
        description="Is Government ID Linked",
        example=False,
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
    main_entrace_pass: Optional[bool] = Field(
        None,
        alias="mainEntrancePass",
        name="Main Entrance Pass",
        description="Is Main Entrance Pass",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    modifiable: Optional[bool] = Field(
        None,
        alias="modifiable",
        name="Modifiable",
        description="Is Modifiable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
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
    package_entitlement: Optional[bool] = Field(
        None,
        alias="packageEntitlement",
        name="Package Entitlement",
        description="Is Package Entitlement",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    park_hopper: Optional[bool] = Field(
        None,
        alias="parkHopper",
        name="Park Hopper",
        description="Is Park Hopper",
        example=False,
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
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary_guest_linked: Optional[bool] = Field(
        None,
        alias="primaryGuestLinked",
        name="Primary Guest Linked",
        description="Is Primary Guest Linked",
        example=False,
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
    remaining_use: Optional[int] = Field(
        None,
        alias="remainingUse",
        name="Remaining Use",
        description="Days remaining to use the entitlement",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renewable: Optional[bool] = Field(
        None,
        alias="renewable",
        name="Renewable",
        description="Is Renewable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    shared: Optional[bool] = Field(
        None,
        alias="shared",
        name="Shared",
        description="Is Shared",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    skip_renewal: Optional[bool] = Field(
        None,
        alias="skipRenewal",
        name="Skip Renewal",
        description="Is Skip Renewal",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sku: Optional[str] = Field(
        None,
        alias="sku",
        name="SKU",
        description="SKU identifier",
        example="68090",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source_lexvas: Optional[bool] = Field(
        None,
        alias="sourceLexvas",
        name="Source Lexvas",
        description="Is Source Lexvas",
        example=False,
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
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Status",
        description="Status of the entitlement",
        example="ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgradeable: Optional[bool] = Field(
        None,
        alias="upgradeable",
        name="Upgradeable",
        description="Is Upgradeable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    use_count: Optional[int] = Field(
        None,
        alias="useCount",
        name="Use Count",
        description="Number of times the entitlement has been used",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visual_id: Optional[str] = Field(
        None,
        alias="visualId",
        name="Visual ID",
        description="Visual identifier",
        example="1068090990849987010055",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    voidable: Optional[bool] = Field(
        None,
        alias="voidable",
        name="Voidable",
        description="Is Voidable",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    order_confirmation_number: Optional[str] = Field(
        None,
        alias="orderConfirmationNumber",
        name="Order confirmation number",
        description="Order confirmation identifier",
        example="DD429698280114024448",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    shared_with: Optional[List[str]] = Field(
        None,
        alias="sharedWith",
        name="Shared with",
        description="Guests identifiers with whom the entitlement is shared",
        example=["example"],
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    days_remaining: Optional[str] = Field(
        None,
        alias="daysRemaining",
        name="Days remaining",
        description="Days remaining to use the entitlement",
        example="365",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pass_type: Optional[str] = Field(
        None,
        alias="passType",
        name="Pass type",
        description="Pass type identifier",
        example="SIGNTURE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renew_eligibility: Optional[str] = Field(
        None,
        alias="renewEligibility",
        name="Renew eligibility",
        description="Renew eligibility identifier",
        example="INELIGIBLE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renewal_end_date: Optional[float] = Field(
        None,
        alias="renewalEndDate",
        name="Renewal end date",
        description="Renewal end date",
        example=1684220400.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    renewal_start_date: Optional[float] = Field(
        None,
        alias="renewalStartDate",
        name="Renewal start date",
        description="Renewal start date",
        example=1684220400.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement_id: Optional[str] = Field(
        None,
        alias="entitlementId",
        name="Entitlement ID",
        description="Entitlement identifier",
        example="25100000000000000",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    bar_code_number: Optional[str] = Field(
        None,
        alias="barCodeNumber",
        name="Bar code number",
        description="Bar code number identifier",
        example="9PFQRTEL2VJHOKD5A3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    magnetic_code_number: Optional[str] = Field(
        None,
        alias="magneticCodeNumber",
        name="Magnetic code number",
        description="Magnetic code number identifier",
        example=" CJ5FF1T1FZCCT22B3CJT0FFTTFZ2CTMZBCC0FF6F1T9ZC1TMZBC0JTF62TTFZCCTMZBC0JT ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sites: Optional[List[str]] = Field(
        None,
        alias="sites",
        name="Sites",
        description="List of sites",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Source",
        description="Source system that provided the data",
        example="SnApp",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_code: Optional[str] = Field(
        None,
        alias="productCode",
        name="Product code",
        description="Product code identifier",
        example="1JFPA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ats_ticket_type: Optional[str] = Field(
        None,
        alias="atsTicketType",
        name="ATS ticket type",
        description="ATS ticket type identifier",
        example="SNAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    void_code: Optional[int] = Field(
        None,
        alias="voidCode",
        name="Void code",
        description="Void code identifier",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    remaining_value: Optional[float] = Field(
        None,
        alias="remainingValue",
        name="Remaining value",
        description="Remaining value",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    already_used: Optional[bool] = Field(
        None,
        alias="alreadyUsed",
        name="Already used",
        description="Tell if the ticket has already been used",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_void_code_description: Optional[str] = Field(
        None,
        alias="ticketVoidCodeDescription",
        name="Ticket void code description",
        description="Ticket void code description",
        example="Ticket OK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_start_date: Optional[int] = Field(
        None,
        alias="validityStartDate",
        name="Validity start date",
        description="Validity start date",
        example=1614556800000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_end_date: Optional[int] = Field(
        None,
        alias="validityEndDate",
        name="Validity end date",
        description="Validity end date",
        example=1654920000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    purchase_date: Optional[int] = Field(
        None,
        alias="purchaseDate",
        name="Purchase date",
        description="Purchase date",
        example=1654920000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement_type: Optional[int] = Field(
        None,
        alias="entitlementType",
        name="Entitlement type",
        description="Entitlement type identifier",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    complimentary_ticket: Optional[bool] = Field(
        None,
        alias="complimentaryTicket",
        name="Complimentary ticket",
        description="Tell if the ticket is a complimentary ticket",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tdssn: Optional[str] = Field(
        None,
        alias="tdssn",
        name="TDSSN",
        description="TDSSN identifier",
        example="25100011062219632",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tdssn_1: Optional[str] = Field(
        None,
        alias="tdssn_",
        name="TDSSN_",
        description="TDSSN_ identifier",
        example="25100011062219632",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_number: Optional[str] = Field(
        None,
        alias="reservationNumber",
        name="Reservation number",
        description="Reservation number identifier",
        example="UPYA00031134",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    usage: Optional[List[UsageItem]] = Field(None, alias="usage", name="Usage", description="List of usage objects")
    lineage: Optional[List[LineageItem]] = Field(
        None, alias="lineage", name="Lineage", description="List of lineage objects"
    )
    assigned_guest: Optional[AssignedGuest] = Field(
        None, alias="assignedGuest", name="Assigned guest", description="Assigned guest object"
    )
    category: Optional[Category] = Field(None, alias="category", name="Category", description="Category object")
    options: Optional[List[OptionItem]] = Field(
        None, alias="options", name="Options", description="List of option objects"
    )
    owner: Optional[Owner] = Field(None, alias="owner", name="Owner", description="Owner object")
    guest: Optional[Guest] = Field(None, alias="guest", name="Guest", description="Guest object")
    transaction_dssn: Optional[TransactionDssn] = Field(
        None, alias="transactionDSSN", name="Transaction DSSN", description="Transaction Date-Site-Station-Number"
    )
    transferable: Optional[Transferable] = Field(
        None, alias="transferable", name="Transferable", description="Transferable object"
    )


class NativeGuestId(BaseModel):
    """A dataclass that represents the object NativeGuestId"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type identifier",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Value of the identifier",
        example="{B61AA750-E717-405C-BB35-B343E5000000}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class NativeGuestIdItem(BaseModel):
    """A dataclass that represents the object NativeGuestIdItem"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="ID type identifier",
        example="admission-link-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="value",
        description="ID value",
        example="YKX8UT6317GR79M22BDY",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class GAMWDWAdmissionsModel(BaseModel):
    """Payload class for GAMWDWAdmissionsModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM WDW Admissions"
        stream_name = "gam-kinesis-gam-admissions-guest360-wdw"
        description = """WDW Guest admissions as shared from the ticketing source system"""
        unique_identifier = ["admissionEntitlement.entitlementId"]
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
    timestamp: Optional[float] = Field(
        None,
        alias="timestamp",
        name="Timestamp",
        description="Timestamp",
        example=1683321653.3185654,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
