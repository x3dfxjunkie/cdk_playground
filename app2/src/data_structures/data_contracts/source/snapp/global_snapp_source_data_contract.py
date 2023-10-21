"""Global SnApp source data contract"""

from datetime import datetime, date
from typing import Optional, List

from pydantic import BaseModel, Field


class GlobalSnAppBreadcrumbItem(BaseModel):
    """A dataclass that represents the object Breadcrumb for SnApp Header"""

    system_id: str = Field(
        ...,
        alias="SystemID",
        name="system id",
        description="",
        example="SnApp",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    timestamp: datetime = Field(
        ...,
        alias="Timestamp",
        name="timestamp",
        description="",
        example="2023-04-12T21:36:26.182+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )


class GlobalSnAppHeader(BaseModel):
    """A dataclass that represents the object Header for SnApp"""

    breadcrumb: List[GlobalSnAppBreadcrumbItem] = Field(
        ...,
        alias="Breadcrumb",
        name="breadcrumb",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    correlation_id: str = Field(
        ...,
        alias="CorrelationId",
        name="correlation_id",
        description="Id that correlates the message content to other related messages",
        example="ffffffff-1111-ffff-1111-ffffffff1hce",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    data_commit_timestamp: datetime = Field(
        ...,
        alias="DataCommitTimestamp",
        name="data_commit timestamp",
        description="",
        example="2023-04-12T21:36:26.180+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    data_id: str = Field(
        ...,
        alias="DataId",
        name="data_id",
        description="Source system data id",
        example="CCCCCCC-1111-CCCC-1111-CCCCCCCC0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    dispatch_timestamp: datetime = Field(
        ...,
        alias="DispatchTimestamp",
        name="dispatch timestamp",
        description="",
        example="2023-04-12T21:36:26.140+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    encrypted_random_seed: Optional[str] = Field(
        None,
        alias="EncryptedRandomSeed",
        name="encrypted random seed",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=True,
    )
    message_id: str = Field(
        ...,
        alias="MessageId",
        name="message id",
        description="Source system message id",
        example="CCCCCCC-1111-CCCC-1111-CCCCCCCC0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    message_timestamp: datetime = Field(
        ...,
        alias="MessageTimestamp",
        name="message timestamp",
        description="",
        example="2023-04-12T21:36:26.177+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    namespace: str = Field(
        ...,
        alias="Namespace",
        name="namespace",
        description="Identifies the type of message, reflecting ticket actions",
        example="SnApp.Product",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    operation: str = Field(
        ...,
        alias="Operation",
        name="operation",
        description="",
        example="new",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    payload_encoding: str = Field(
        ...,
        alias="PayloadEncoding",
        name="payload_encoding",
        description="Data type payload, currently only JSON is expected",
        example="JSON",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    recovery: bool = Field(
        ...,
        alias="Recovery",
        name="recovery",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    retransmit: bool = Field(
        ...,
        alias="Retransmit",
        name="retransmit",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=True,
    )
    schema_version: str = Field(
        ...,
        alias="SchemaVersion",
        name="schema_version",
        description="Version of the json schema",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    source_event_date_time: datetime = Field(
        ...,
        alias="SourceEventDateTime",
        name="source event date time",
        description="",
        example="2023-04-12T21:36:26.137+0000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    source_system_name: str = Field(
        ...,
        alias="SourceSystemName",
        name="source system name",
        description="Name of the source system, currently only 'SnApp' is expected",
        example="SnApp",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    source_system_version: str = Field(
        ...,
        alias="SourceSystemVersion",
        name="source system version",
        description="Version of the source system",
        example="28.10.1.0.4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    suppressed: bool = Field(
        ...,
        alias="Suppressed",
        name="suppressed",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )
    version: str = Field(
        ...,
        alias="Version",
        name="version",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
        null=False,
    )


class GlobalSnAppCastAsGuest(BaseModel):
    """A dataclass that represents the object Cast As Guest for SnApp"""

    pernr: str = Field(
        ...,
        alias="Pernr",
        name="PERNR",
        description="Cast Member Personnel Number",
        example="90123456",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    first_name: str = Field(
        ...,
        alias="FirstName",
        name="First Name",
        description="Cast Member as guest's first name",
        example="Donald",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_name: str = Field(
        ...,
        alias="LastName",
        name="Last Name",
        description="Cast Member as guest's last name",
        example="Duck",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppEligibilityMember(BaseModel):
    """A dataclass that represents the object EligibilityMember for SnApp"""

    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="",
        example="3485300",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="first_name",
        description="Guest first name",
        example="Donald",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="Last name",
        description="Guest last name",
        example="Duck",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    birth_date: Optional[date] = Field(
        None,
        alias="BirthDate",
        name="Birth Date",
        description="Guest Birth date",
        example="1921-10-21",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    base_installation: Optional[str] = Field(
        None,
        alias="Base_Installation",
        name="Base Installation",
        description="Military base association for military offer tickets",
        example="Fort Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dvc_member_number: Optional[str] = Field(
        None,
        alias="DVCMemberNumber",
        name="DVC Member Number",
        description="DVC member number",
        example="123456789",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    active: Optional[str] = Field(
        None,
        alias="Active",
        name="Active",
        description="",
        example="Y",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    sales_rep_location: Optional[str] = Field(
        None,
        alias="SalesRep_Location",
        name="Sales Representative Location",
        description="",
        example="123456789",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comment: Optional[str] = Field(
        None,
        alias="Comment",
        name="Comment",
        description="added comments relating to the member",
        example="VARIOUS DATES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: Optional[str] = Field(
        None,
        alias="Name",
        name="Name",
        description="Group or event name relating to member's ticket",
        example="GENERIC CORONADO MEETING/CONVENTION",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    gmr: Optional[str] = Field(
        None,
        alias="GMR",
        name="GMR",
        description="TBD",
        example="G0000001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pernr: Optional[str] = Field(
        None,
        alias="Pernr",
        name="PERNR",
        description="Cast Member Personnel Number",
        example="90123456",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    event_code: Optional[str] = Field(
        None,
        alias="EventCode",
        name="Event Code",
        description="Event Code",
        example="22USGRLSS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_id: Optional[str] = Field(
        None,
        alias="EventID",
        name="Event Identifier",
        description="Event Identifer",
        example="11111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_manager: Optional[str] = Field(
        None,
        alias="EventManager",
        name="Event Manager",
        description="Manager / contact point for the designated event",
        example="Socerer Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_start_validity_date: Optional[date] = Field(
        None,
        alias="TicketStartValidityDate",
        name="Ticket Start Validity Date",
        description="Validity start date for the corresponding ticket",
        example="2023-01-25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ticket_end_validity_date: Optional[date] = Field(
        None,
        alias="TicketEndValidityDate",
        name="Ticket End Validity Date",
        description="Validity end date for the corresponding ticket",
        example="2023-01-29",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    quantity_issued: Optional[date] = Field(
        None,
        alias="QuantityIssued",
        name="Quantity Issued",
        description="Number of tickets issued for this member along with corresponding ticket",
        example="2020-12-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: int = Field(
        ...,
        alias="Status",
        name="Status",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppEligibilityGroup(BaseModel):
    """A dataclass that represents the object EligibilityGroup for SnApp"""

    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="",
        example="25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    eligibility_member: GlobalSnAppEligibilityMember = Field(
        ...,
        alias="EligibilityMember",
        name="Eligibility member",
        description="Object that represents the EligibilityMember",
    )
    group: str = Field(
        ...,
        alias="Group",
        name="Group",
        description="",
        example="CAST AS GUEST (CAST COMPS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: int = Field(
        ...,
        alias="Status",
        name="Status",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppTicketCodeAliasListItem(BaseModel):
    """A dataclass that represents the object TicketCodeAliasList for SnApp"""

    code_alias: str = Field(
        ...,
        alias="CodeAlias",
        name="Code alias",
        description="Alias of the code",
        example="072813-WTS-117-00000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code_alias_type_code: str = Field(
        ...,
        alias="CodeAliasTypeCode",
        name="Code alias type code",
        description="Type of the code alias",
        example="CA03_ATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code_alias_type_name: str = Field(
        ...,
        alias="CodeAliasTypeName",
        name="Code alias type name",
        description="Name of the code alias type",
        example="TICKET ALIAS - TCOD (ATS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppTransactionCodeAliasListItem(BaseModel):
    """A dataclass that represents the object TransactionCodeAliasList for SnApp"""

    code_alias: str = Field(
        ...,
        alias="CodeAlias",
        name="Code alias",
        description="",
        example="072813-WTS-117-00138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code_alias_type_code: str = Field(
        ...,
        alias="CodeAliasTypeCode",
        name="Code alias type code",
        description="",
        example="CA07_ATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code_alias_type_name: str = Field(
        ...,
        alias="CodeAliasTypeName",
        name="Code alias type name",
        description="",
        example="TRANSACTION ALIAS - TRANNID (ATS)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppAccountAddress(BaseModel):
    """a dataclass representing address objects in Account Object"""

    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="First name",
        description="Guest first name",
        example="Donald",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="Last name",
        description="Guest last name",
        example="Duck",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    address_line_1: Optional[str] = Field(
        None,
        alias="AddressLine1",
        name="Address Line 1",
        description="Guest address line 1",
        example="1 Mickey Avenue",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    address_line_2: Optional[str] = Field(
        None,
        alias="AddressLine2",
        name="Address Line 2",
        description="Guest address line 2",
        example="Unit 4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    city: Optional[str] = Field(
        None,
        alias="City",
        name="City",
        description="Guest address's city",
        example="Lake Buena Vista",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    state: Optional[str] = Field(
        None,
        alias="State",
        name="State",
        description="Guest address's state",
        example="FL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    postal_code: Optional[str] = Field(
        None,
        alias="PostalCode",
        name="Postal Code",
        description="Guest address's postal code",
        example="32821",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    country: Optional[str] = Field(
        None,
        alias="Country",
        name="Country",
        description="Guest address's country",
        example="US",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class GlobalSnAppDemographics(BaseModel):
    """A dataclass that represents the object Demographics for SnApp"""

    pernr: Optional[str] = Field(
        None,
        alias="Pernr",
        name="PERNR",
        description="Cast Member Personnel Number",
        example="90123456",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    ok_to_email_offers: Optional[str] = Field(
        None,
        alias="OkToEmailOffers",
        name="Ok to email offers",
        description="Flag to determine if offers should be emailed",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    suffix: Optional[str] = Field(
        None,
        alias="Suffix",
        name="Suffix",
        description="Guest suffix",
        example="JR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    title: Optional[str] = Field(
        None,
        alias="Title",
        name="Tittle",
        description="Guest title",
        example="Mr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="First name",
        description="Guest first name",
        example="LEONARDO",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="MiddleName",
        name="Middle name",
        description="Guest middle name",
        example="Fauntleroy",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="Last name",
        description="Guest last name",
        example="Duck",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    email_1: Optional[str] = Field(
        None,
        alias="Email1",
        name="Email 1",
        description="Guest email address",
        example="donald.duck@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    email_2: Optional[str] = Field(
        None,
        alias="Email2",
        name="Email 2",
        description="alternate guest email address",
        example="angry.duck@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    date_of_birth: Optional[date] = Field(
        None,
        alias="DateOfBirth",
        name="Date of birth",
        description="Guest date of birth",
        example="1934-06-09",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    gender: Optional[str] = Field(
        None,
        alias="Gender",
        name="Gender",
        description="Guest gender",
        example="M",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    home_phone: Optional[str] = Field(
        None,
        alias="HomePhone",
        name="Home phone",
        description="Guest home phone number",
        example="8608361234",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    business_phone: Optional[str] = Field(
        None,
        alias="BusinessPhone",
        name="Business phone",
        description="Guest Business phone number",
        example="8608361234",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    mobile_phone: Optional[str] = Field(
        None,
        alias="MobilePhone",
        name="Mobile phone",
        description="Guest Mobile phone number",
        example="8608361234",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    other_phone_1: Optional[str] = Field(
        None,
        alias="OtherPhone1",
        name="Other phone 1",
        description="Guest other phone number",
        example="8608361234",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    other_phone_2: Optional[str] = Field(
        None,
        alias="OtherPhone2",
        name="Other Phone 2",
        description="Guest other phone number",
        example="8608361234",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    address: Optional[GlobalSnAppAccountAddress] = Field(
        None,
        alias="Address",
        name="Address",
        description="Guest address",
    )
    shipping_address: Optional[GlobalSnAppAccountAddress] = Field(
        None,
        alias="ShippingAddress",
        name="Shipping Address",
        description="Guest shipping address",
    )
    billing_address: Optional[GlobalSnAppAccountAddress] = Field(
        None,
        alias="BillingAddress",
        name="Billing Address",
        description="Guest shipping address",
    )


class GlobalSnAppExternalReferenceItem(BaseModel):
    """A dataclass that represents the object ExternalReference for SnApp"""

    type: Optional[str] = Field(
        None,
        alias="Type",
        name="Type",
        description="Guest external reference type",
        example="SWID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="Value",
        name="Value",
        description="Guest external reference value",
        example="{AAAAAAA-1111-AAAA-1111-11111111DB56}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class GlobalSnAppAccount(BaseModel):
    """A dataclass that represents the object Account for SnApp"""

    id: Optional[str] = Field(
        None,
        alias="Id",
        name="id",
        description="",
        example="BBBBBBBB-2222-BBBB-2222-BBBBBBBB8989",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    code: Optional[str] = Field(
        None,
        alias="Code",
        name="Code",
        description="Guest identifier code",
        example="111111111111111111",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    status: Optional[int] = Field(
        None,
        alias="Status",
        name="Status",
        description="Account status",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    demographics: Optional[GlobalSnAppDemographics] = Field(
        None,
        alias="Demographics",
        name="Demographics",
        description="Object that represents the guest demographics",
    )
    external_reference: Optional[List[GlobalSnAppExternalReferenceItem]] = Field(
        None,
        alias="ExternalReference",
        name="External reference",
        description="List of object that represents the guest external reference",
    )


class GlobalSnAppMediaItem(BaseModel):
    """A dataclass that represents the object MediaList for SnApp"""

    mfr_id: str = Field(
        ...,
        alias="MFRId",
        name="MFR id",
        description="",
        example="33333333333333780",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    secure_id: str = Field(
        ...,
        alias="SecureId",
        name="Secure id",
        description="",
        example="1111111111111215",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: int = Field(
        ...,
        alias="Status",
        name="Status",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: int = Field(
        ...,
        alias="Type",
        name="Type",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visual_id: str = Field(
        ...,
        alias="VisualId",
        name="Visual id",
        description="",
        example="123412348033",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalSnAppTransaction(BaseModel):
    """A dataclass that represents the object Transaction for SnApp"""

    code: str = Field(
        ...,
        alias="Code",
        name="Code",
        description="Transaction identifier code",
        example="00011111111100000",
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
        name="Dssn",
        description="",
        example="020710-ABC-119-00031",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="Id",
        name="Id",
        description="Source system transaction identifier",
        example="CCCCCCC-3333-CCCC-3333-CCCCCCCC83G3",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    serial_number: str = Field(
        ...,
        alias="SerialNumber",
        name="Serial number",
        description="",
        example="00138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    site: str = Field(
        ...,
        alias="Site",
        name="Site",
        description="",
        example="WTS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    station: str = Field(
        ...,
        alias="Station",
        name="station",
        description="",
        example="117",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_code: str = Field(
        ...,
        alias="TransactionCode",
        name="Transaction code",
        description="",
        example="T:1001.0.100728.000",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="",
    )
    transaction_code_alias_list: Optional[List[GlobalSnAppTransactionCodeAliasListItem]] = Field(
        None,
        alias="TransactionCodeAliasList",
        name="Transaction Code Alias List",
        description="alternate transaction codes",
    )


class GlobalSnAppMediaCodeListItem(BaseModel):
    media_code: str = Field(
        ...,
        alias="MediaCode",
        name="",
        description="",
        example="1003112371C2",
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
