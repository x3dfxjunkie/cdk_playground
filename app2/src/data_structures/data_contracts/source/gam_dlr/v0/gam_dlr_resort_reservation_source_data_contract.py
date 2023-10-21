"""Source Data Contract for GAM DLR Resort Reservations"""

from __future__ import annotations
from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class Code(BaseModel):
    """Data class that represents codes from various sources"""

    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Code Value",
        example="5C38J",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Source",
        description="Source system for the code value",
        example="TBX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Period(BaseModel):
    """Data class that represents validity period"""

    start_date: date = Field(
        ...,
        alias="startDate",
        name="Start Date",
        description="Start date",
        example="2023-05-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date: date = Field(
        ...,
        alias="endDate",
        name="End Date",
        description="End Date",
        example="2023-05-06",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Name(BaseModel):
    """Data class that represents the product name"""

    long_name: Optional[str] = Field(
        None,
        alias="longName",
        name="Long Name",
        description="Product name for additional selected option",
        example="2 Day Base Ticket",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SelectedOptionItem(BaseModel):
    """Data class that represents the additional options selected with accommodation"""

    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Code for additional selected options",
    )
    name: Name = Field(
        ...,
        alias="name",
        name="Name",
        description="Product name for additional selected options",
    )
    period: Period = Field(
        ...,
        alias="period",
        name="Period",
        description="Validity period for additional selected options",
    )


class AuditDetails(BaseModel):
    """Data class that represents the Cast ID and datetime of the updates made on the booking"""

    created_by: str = Field(
        ...,
        alias="createdBy",
        name="Created By",
        description="ID of the cast member that created the update",
        example="75436",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updated_date_time: Optional[datetime] = Field(
        None,
        alias="updatedDateTime",
        name="Updated Datetime",
        description="Datetime when the update was made",
        example="2022-12-10T18:13:59.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_date_time: Optional[datetime] = Field(
        None,
        alias="createdDateTime",
        name="Created Datetime",
        description="Datetime when the change was originally created",
        example="2022-12-10T18:13:59.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PersonName(BaseModel):
    """Data class that represents the name components of the Guests"""

    full_legal_name: Optional[str] = Field(
        None,
        alias="fullLegalName",
        name="Full Legal Name",
        description="Full legal name of Guest",
        example="Minnie Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    first_name: Optional[str] = Field(
        None,
        alias="FirstName",
        name="Full Legal Name",
        description="Full legal name of Guest",
        example="Minnie",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="LastName",
        name="Last Name",
        description="Last name of Guest",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    title: Optional[str] = Field(
        None,
        alias="title",
        name="Name Title",
        description="Name tile of Guest",
        example="Mr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    suffix: Optional[str] = Field(
        None,
        alias="suffix",
        name="Name Suffix",
        description="Name suffix of Guest",
        example="Jr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class NativeGuestIdItem(BaseModel):
    """Data class that represents various Guest Identifier types and values"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Guest ID Type",
        description="The Guest ID type for the resort Guest",
        example="transactional-guest-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the resort Guest",
        example="750854738",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class ContactPerson(BaseModel):
    """Data class that represents individual contact details"""

    person_name: PersonName = Field(
        ...,
        alias="personName",
        name="Person Name",
        description="Full name of contact person",
    )
    subscribe_market_info: bool = Field(
        ...,
        alias="subscribeMarketInfo",
        name="Subscriber Market Information",
        description="Subscriber market information",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AlternateIdentifierItem(BaseModel):
    """Data class that represents alternate source identifiers types and values"""

    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="ID value",
        example="15252534",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="ID type",
        example="RESERVATION_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Source",
        description="Source system for the id value",
        example="TBX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Id(BaseModel):
    """Data class that represents various source identifiers types and values"""

    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="ID value",
        example="15252534",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="ID type",
        example="RESERVATION_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Source",
        description="Source system for the id value",
        example="TBX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    alternate_identifiers: Optional[List[AlternateIdentifierItem]] = Field(
        None,
        alias="alternateIdentifiers",
        name="Alternate Identifiers",
        description="Alternate identifiers from different source",
    )


class Country(BaseModel):
    """Data class that represents the country code of Guests"""

    iso2_country_code: str = Field(
        ...,
        alias="iso2CountryCode",
        name="ISO 2-Char Country Code",
        description="2-character ISO country code",
        example="US",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ContactNumberItem(BaseModel):
    """Data class that represents the contact phone details of individuals"""

    number: Optional[str] = Field(
        None,
        alias="number",
        name="Number",
        description="Phone number of Guest",
        example="4045125678",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    primary: bool = Field(
        ...,
        alias="primary",
        name="Primary",
        description="Indicates if the phone number of the Guest is primary",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LanguagePref(BaseModel):
    """Data class that represents the language preferences of Guests"""

    code: str = Field(
        ...,
        alias="code",
        name="Code",
        description="Language code",
        example="eng",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AffiliationItem(BaseModel):
    """Data class that represents affiliations and membership details of Guests"""

    membership_type: str = Field(
        ...,
        alias="membershipType",
        name="Membership Type",
        description="Membership of the Guest that is applied towards discount etc. on the reservation",
        example="COSTCO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelDocumentItem(BaseModel):
    """Data class that represents the Guest details in travel documents"""

    person_name: PersonName = Field(
        ...,
        alias="personName",
        name="Person Name",
        description="Guest name details from travel documents",
    )


class AddressItem(BaseModel):
    """Data class that represents the addresses of Guests"""

    address_line1: str = Field(
        ...,
        alias="addressLine1",
        name="Address",
        description="Guest address line1",
        example="123 Main St",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    city: Optional[str] = Field(
        None,
        alias="city",
        name="Address City",
        description="City name from the Guest address",
        example="Orlando",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    country: Country = Field(
        ...,
        alias="country",
        name="Address Country",
        description="Country code from the Guest address",
    )
    zip_code: str = Field(
        ...,
        alias="zipCode",
        name="Address Zipcode",
        description="Postal code from the Guest address",
        example="06520",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary: bool = Field(
        ...,
        alias="primary",
        name="Primary",
        description="Indicates if the address is primary for the Guest",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    state: Optional[str] = Field(
        None,
        alias="state",
        name="Address State",
        description="State name from the dining Guest address",
        example="FL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EmailItem(BaseModel):
    """Data class that represents the email addresses"""

    primary: Optional[bool] = Field(
        None,
        alias="primary",
        name="Primary",
        description="Indicates if the email address is primary",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Value",
        description="Email address",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class Guest(BaseModel):
    """Data class that represents the details of individual Guests"""

    id: Id = Field(
        ...,
        alias="id",
        name="ID",
        description="Guest ID details from booking system",
    )
    addresses: Optional[List[AddressItem]] = Field(
        None,
        alias="addresses",
        name="Addresses",
        description="Addresses of the Guest",
    )
    age: int = Field(
        ...,
        alias="age",
        name="Age",
        description="Age of the Guest",
        example=18,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_group: str = Field(
        ...,
        alias="ageGroup",
        name="Age Group",
        description="Age group of the Guest - ADULT, CHILD, INFANT etc.",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    contact_numbers: Optional[List[ContactNumberItem]] = Field(
        None,
        alias="contactNumbers",
        name="Contact Numbers",
        description="Contact phone numbers for Guests",
    )
    do_not_mail_indicator: bool = Field(
        ...,
        alias="doNotMailIndicator",
        name="Do Not Mail Indicator",
        description="Permissions provided by Guest for receiving marketing communications at address",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    do_not_phone_indicator: bool = Field(
        ...,
        alias="doNotPhoneIndicator",
        name="Do Not Phone Indicator",
        description="Permissions provided by Guest for receiving marketing communications on the phone",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gender: str = Field(
        ...,
        alias="gender",
        name="Gender",
        description="Gender of the Guest",
        example="MALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    person_name: PersonName = Field(
        ...,
        alias="personName",
        name="Person Name",
        description="Guest name details",
    )
    traveling_with_infant: bool = Field(
        ...,
        alias="travelingWithInfant",
        name="Traveling With Infant",
        description="Indicates if the reservation party has an infant",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    primary: bool = Field(
        ...,
        alias="primary",
        name="Primary",
        description="Indicates if the Guest references is the primary",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    emails: Optional[List[EmailItem]] = Field(
        None,
        alias="emails",
        name="Emails",
        description="Guest email addresses",
    )
    language_pref: Optional[LanguagePref] = Field(
        None,
        alias="languagePref",
        name="Language Preference",
        description="Language preferences of Guests",
    )
    affiliations: Optional[List[AffiliationItem]] = Field(
        None,
        alias="affiliations",
        name="Affiliations",
        description="Affiliations and memberships of Guests",
    )
    travel_documents: Optional[List[TravelDocumentItem]] = Field(
        None,
        alias="travelDocuments",
        name="Travel Documents",
        description="Guest details in travel documents",
    )
    birth_date: Optional[date] = Field(
        None,
        alias="birthDate",
        name="Birth Date",
        description="Date of birth of Guests",
        example="1993-04-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guests(BaseModel):
    """Data class that represents the details of the reservation Guests"""

    guest_1: Optional[Guest] = Field(
        None,
        alias="1",
        name="Guest1",
        description="Details of Guest on reservation",
    )
    guest_2: Optional[Guest] = Field(
        None,
        alias="2",
        name="Guest2",
        description="Details of Guest on reservation",
    )
    guest_3: Optional[Guest] = Field(
        None,
        alias="3",
        name="Guest3",
        description="Details of Guest on reservation",
    )
    guest_4: Optional[Guest] = Field(
        None,
        alias="4",
        name="Guest4",
        description="Details of Guest on reservation",
    )
    guest_5: Optional[Guest] = Field(
        None,
        alias="5",
        name="Guest5",
        description="Details of Guest on reservation",
    )
    guest_6: Optional[Guest] = Field(
        None,
        alias="6",
        name="Guest6",
        description="Details of Guest on reservation",
    )
    guest_7: Optional[Guest] = Field(
        None,
        alias="7",
        name="Guest7",
        description="Details of Guest on reservation",
    )
    guest_8: Optional[Guest] = Field(
        None,
        alias="8",
        name="Guest8",
        description="Details of Guest on reservation",
    )
    guest_9: Optional[Guest] = Field(
        None,
        alias="9",
        name="Guest9",
        description="Details of Guest on reservation",
    )
    guest_10: Optional[Guest] = Field(
        None,
        alias="10",
        name="Guest6",
        description="Details of Guest on reservation",
    )
    guest_11: Optional[Guest] = Field(
        None,
        alias="11",
        name="Guest11",
        description="Details of Guest on reservation",
    )
    guest_12: Optional[Guest] = Field(
        None,
        alias="12",
        name="Guest12",
        description="Details of Guest on reservation",
    )
    guest_13: Optional[Guest] = Field(
        None,
        alias="13",
        name="Guest13",
        description="Details of Guest on reservation",
    )
    guest_14: Optional[Guest] = Field(
        None,
        alias="14",
        name="Guest14",
        description="Details of Guest on reservation",
    )


class AreaPeriod(BaseModel):
    """Data class that represents the start date of the visit"""

    start_date: date = Field(
        ...,
        alias="startDate",
        name="Start Date",
        description="Start date of the stay",
        example="2023-07-18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Currency(BaseModel):
    """Data class that represents the currency code on prices and payments"""

    code: str = Field(
        ...,
        alias="code",
        name="Code",
        description="Curreny code",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Prices(BaseModel):
    """Data class that represents the breakdown of the prices"""

    additional_charge: float = Field(
        ...,
        alias="additionalCharge",
        name="Additional Charge",
        description="Additional charge for nightly stay",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    additional_adult_charge: float = Field(
        ...,
        alias="additionalAdultCharge",
        name="Additional Adult Charge",
        description="Charge for additional adult per nightly stay",
        example=99.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price: float = Field(
        ...,
        alias="price",
        name="Price",
        description="Price per night",
        example=344.1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    commission: float = Field(
        ...,
        alias="commission",
        name="Commission",
        description="Commission paid towards the booking per night",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    net: float = Field(
        ...,
        alias="net",
        name="Net",
        description="Net price for the night before tax",
        example=344.1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax: float = Field(
        ...,
        alias="tax",
        name="Tax",
        description="Tax for the nightly price",
        example=34.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    total: float = Field(
        ...,
        alias="total",
        name="Total",
        description="Total price for the night",
        example=378.6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Deposit(BaseModel):
    """Data class that represents the details of the deposits made"""

    amount_due: float = Field(
        ...,
        alias="amountDue",
        name="Amount Due",
        description="Amount due as deposit",
        example=250.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    due_date: date = Field(
        ...,
        alias="dueDate",
        name="Due Date",
        description="Due date for deposit payment",
        example="2023-04-28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    paid_amount: float = Field(
        ...,
        alias="paidAmount",
        name="Paid Amount",
        description="Amount paid towards deposit",
        example=100.12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    due_number_of_days: int = Field(
        ...,
        alias="dueNumberOfDays",
        name="Due Number of Days",
        description="Due number of days; always seen to be 0",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Balance(BaseModel):
    """Data class that represents the balance due on the booking"""

    amount_due: float = Field(
        ...,
        alias="amountDue",
        name="Amount Due",
        description="Balance amount due; total price minus deposit paid",
        example=150.2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    due_date: date = Field(
        ...,
        alias="dueDate",
        name="Due Date",
        description="Due date for balance payment",
        example="2023-05-28",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    paid_amount: float = Field(
        ...,
        alias="paidAmount",
        name="Paid Amount",
        description="Amount paid towards balance",
        example=50.2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    due_number_of_days: int = Field(
        ...,
        alias="dueNumberOfDays",
        name="Due Number of Days",
        description="Due number of days; always seen to be 0",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ReservationPropertyItem(BaseModel):
    """Data class that represents the source of business associated with the booking"""

    key: str = Field(
        ...,
        alias="key",
        name="Key",
        description="Reservation property key",
        example="Source of Business",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    values: List[str] = Field(
        ...,
        alias="values",
        name="Values",
        description="Reservation property key value",
        example=["TW"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class HistoryItem(BaseModel):
    """Data class that represents history of updates on the booking"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of historical update",
        example="OPTION_STATUS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notes: str = Field(
        ...,
        alias="notes",
        name="Notes",
        description="Historical update notes",
        example="Option Changed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    modified_by: str = Field(
        ...,
        alias="modifiedBy",
        name="Modified By",
        description="ID of the cast member that made the update",
        example="24128",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    audit_details: AuditDetails = Field(
        ...,
        alias="auditDetails",
        name="Audit Details",
        description="Cast member ID and datetime of the original updates made",
    )


class ComponentId(BaseModel):
    """Data class that represents component IDs from various sources"""

    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Component ID value",
        example="15421314#HTL#2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Component type",
        example="COMPONENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: str = Field(
        ...,
        alias="source",
        name="Source",
        description="Component source",
        example="TBX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CommentItem(BaseModel):
    """Data class that represents the comments and notes added by Cast on the booking"""

    code: Optional[Code] = Field(
        None,
        alias="code",
        name="Code",
        description="Comment code",
    )
    notes: str = Field(
        ...,
        alias="notes",
        name="Notes",
        description="Comment notes",
        example="Adv Parking Fee P/NT- 1 Car Max",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    audit_details: AuditDetails = Field(
        ...,
        alias="auditDetails",
        name="Audit Details",
        description="Cast member ID and datetime of the updates made",
    )


class StayPeriod(BaseModel):
    """Data class that represents the stay period of the accommodation"""

    start_date: date = Field(
        ...,
        alias="startDate",
        name="Start Date",
        description="Start date of the stay",
        example="2023-07-18",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date: date = Field(
        ...,
        alias="endDate",
        name="End Date",
        description="End date of the stay",
        example="2023-07-21",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Facility(BaseModel):
    """Data class that represents the facility ID, code and name details"""

    id: Id = Field(
        ...,
        alias="id",
        name="Facility ID",
        description="Facility ID",
    )
    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Facility code",
    )
    name: Name = Field(
        ...,
        alias="name",
        name="Name",
        description="Facility name",
    )


class TypeCode(BaseModel):
    """Data class that represents the accommodation type code"""

    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Accommodation type code value",
        example="D5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class NightlyPriceItem(BaseModel):
    """Data class that represents the nightly price details of the accommodation product"""

    additional_charge: float = Field(
        ...,
        alias="additionalCharge",
        name="Additional Charge",
        description="Additional charge for nightly stay",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    additional_adult_charge: float = Field(
        ...,
        alias="additionalAdultCharge",
        name="Additional Adult Charge",
        description="Charge for additional adult per nightly stay",
        example=99.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    price: float = Field(
        ...,
        alias="price",
        name="Price",
        description="Price per night",
        example=344.1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    commission: float = Field(
        ...,
        alias="commission",
        name="Commission",
        description="Commission paid towards the booking per night",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    net: float = Field(
        ...,
        alias="net",
        name="Net",
        description="Net price for the night before tax",
        example=344.1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax: float = Field(
        ...,
        alias="tax",
        name="Tax",
        description="Tax for the nightly price",
        example=34.5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    total: float = Field(
        ...,
        alias="total",
        name="Total",
        description="Total price for the night",
        example=378.6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    date_for_nightly_price: date = Field(
        ...,
        alias="date",
        name="Date",
        description="Date for nightly price",
        example="2023-05-22",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AccommodationOption(BaseModel):
    """Data class that represents the option codes and prices of the accommodation component"""

    type_code: TypeCode = Field(
        ...,
        alias="typeCode",
        name="Type Code",
        description="Accommodation type code",
    )
    nightly_prices: Optional[List[NightlyPriceItem]] = Field(
        None,
        alias="nightlyPrices",
        name="Nightly Prices",
        description="Nightly price details of the accommodation product",
    )


class AccommodationProductItem(BaseModel):
    """Data class that represents the details of the accommodation component"""

    component_id: ComponentId = Field(
        ...,
        alias="componentId",
        name="Component ID",
        description="Component ID, source details",
    )
    guest_refs: List[str] = Field(
        ...,
        alias="guestRefs",
        name="Guest References",
        description="Guest references, often in sequential numbers",
        example=["1"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Accommodation product code",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of the product",
        example="ACCOMMODATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comments: Optional[List[CommentItem]] = Field(
        None,
        alias="comments",
        name="Comments",
        description="Freeform comments put in as notes, requests etc., along with the ID of the Cast that put in the comment",
    )
    stay_period: StayPeriod = Field(
        ...,
        alias="stayPeriod",
        name="Stay Period",
        description="Stay period for the accommodation components",
    )
    facility: Facility = Field(
        ...,
        alias="facility",
        name="Facility",
        description="Facility ID, code and name",
    )
    accommodation_option: AccommodationOption = Field(
        ...,
        alias="accommodationOption",
        name="Accommodation Option",
        description="Option codes and prices associated with accommodation component",
    )
    special_needs_requested: bool = Field(
        ...,
        alias="specialNeedsRequested",
        name="Special Needs Requested",
        description="Indicator for special needs requested",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    audit_details: AuditDetails = Field(
        ...,
        alias="auditDetails",
        name="Audit Details",
        description="Cast member ID and datetime of the updates made",
    )
    voucher_issue_date: Optional[date] = Field(
        None,
        alias="voucherIssueDate",
        name="Voucher Issue Date",
        description="Issue date of voucher, if used",
        example="2022-02-02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class OtherProductItem(BaseModel):
    """Data class that represents the details of the non-accommodation and non-admission components"""

    guest_refs: List[str] = Field(
        ...,
        alias="guestRefs",
        name="Guest References",
        description="Guest references, often in sequential numbers",
        example=["1"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Other product code",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of the product",
        example="MAGXPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sub_type: str = Field(
        ...,
        alias="subType",
        name="Subtype",
        description="Subtype of the product",
        example="MAGXPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: Name = Field(
        ...,
        alias="name",
        name="Name",
        description="Other product name",
    )
    product_family: Optional[str] = Field(
        None,
        alias="productFamily",
        name="Product Family",
        description="Product family",
        example="Extra",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    min_option_count: int = Field(
        ...,
        alias="minOptionCount",
        name="Minimum Option Count",
        description="Mininum option count",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_option_count: int = Field(
        ...,
        alias="maxOptionCount",
        name="Maximum Option Count",
        description="Maximum option count",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    selected_options: List[SelectedOptionItem] = Field(
        ...,
        alias="selectedOptions",
        name="Selected Options",
        description="Additional options selected with the other products",
    )


class VoucherItem(BaseModel):
    """Data class that represents the voucher details"""

    id: Id = Field(
        ...,
        alias="id",
        name="Voucher ID",
        description="Voucher ID",
    )
    code: str = Field(
        ...,
        alias="code",
        name="Code",
        description="Voucher code",
        example="GXYCATA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="Voucher status - Processed etc.",
        example="Processed",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    issued_date_time: datetime = Field(
        ...,
        alias="issuedDateTime",
        name="Issued Datetime",
        description="Datetime when the voucher was issued",
        example="2023-02-20T17:13:50",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_ref: str = Field(
        ...,
        alias="guestRef",
        name="Guest Reference",
        description="Sequential number assigned to reservation Guests",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AdmissionProduct(BaseModel):
    """Data class that represents the details of the admission component of the booking"""

    component_id: ComponentId = Field(
        ...,
        alias="componentId",
        name="Component ID",
        description="Admission component ID from original source",
    )
    guest_refs: List[str] = Field(
        ...,
        alias="guestRefs",
        name="Guest References",
        description="Guest references, often in sequential numbers",
        example=["1"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Admission product code",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="Type of the admission product",
        example="GENIEPLUS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    min_option_count: int = Field(
        ...,
        alias="minOptionCount",
        name="Minimum Option Count",
        description="Mininum option count",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_option_count: int = Field(
        ...,
        alias="maxOptionCount",
        name="Maximum Option Count",
        description="Maximum option count",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vouchers: List[VoucherItem] = Field(
        ...,
        alias="vouchers",
        name="Voucher",
        description="Voucher details, if applicable",
    )
    selected_options: List[SelectedOptionItem] = Field(
        ...,
        alias="selectedOptions",
        name="Selected Options",
        description="Additional options selected with the admission product",
    )


class PriceSummary(BaseModel):
    """Data class that represents the price details"""

    currency: Currency = Field(
        ...,
        alias="currency",
        name="Currency",
        description="Currency that the prices are denoted in",
    )
    prices: Prices = Field(
        ...,
        alias="prices",
        name="Prices",
        description="Breakdown of the prices associated",
    )
    deposit: Optional[Deposit] = Field(
        None,
        alias="deposit",
        name="Deposit",
        description="Details of the deposits made",
    )
    balance: Optional[Balance] = Field(
        None,
        alias="balance",
        name="Balance",
        description="Details of the balances to be paid",
    )


class Group(BaseModel):
    """Data class that represents the details of the group booking"""

    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Code of the group booking, if applicable",
    )
    wholesaler: bool = Field(
        ...,
        alias="wholesaler",
        name="Wholesaler",
        description="Indicates if the package is a wholesale group booking",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AccommodationPackage(BaseModel):
    """Data class that represents the details of the accommodation package"""

    code: Code = Field(
        ...,
        alias="code",
        name="Code",
        description="Code of the accommodation package",
    )
    name: Name = Field(
        ...,
        alias="name",
        name="Name",
        description="Name",
    )
    price_summary: PriceSummary = Field(
        ...,
        alias="priceSummary",
        name="Price Summary",
        description="Price summary for the accommodation package",
    )
    room_only: bool = Field(
        ...,
        alias="roomOnly",
        name="Room Only",
        description="Indicates if it is a room only booking",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_requests: Optional[List[str]] = Field(
        None,
        alias="guestRequests",
        name="Guest Requests",
        description="Special requests from Guests",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    accommodation_products: List[AccommodationProductItem] = Field(
        ...,
        alias="accommodationProducts",
        name="Accommodation Products",
        description="Details of the accommodation components of the booking",
    )
    admission_product: Optional[AdmissionProduct] = Field(
        None,
        alias="admissionProduct",
        name="Admission Product",
        description="Details of the admission component of the booking",
    )
    other_products: List[OtherProductItem] = Field(
        ...,
        alias="otherProducts",
        name="Other Products",
        description="Details of other non-accommodation and non-admission components of the booking",
    )


class AccommodationPackageOrderItem(BaseModel):
    """Data class that represents the details of the accommodation package"""

    id: Id = Field(
        ...,
        alias="id",
        name="Source ID",
        description="ID from the package reservation system",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="Status of the accommodation package - Booked etc.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    booking_date: date = Field(
        ...,
        alias="bookingDate",
        name="Booking Date",
        description="Booking date of the accommodation package",
        example="2023-02-05",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vip: bool = Field(
        ...,
        alias="vip",
        name="VIP",
        description="Indicates if the booking was made for a VIP",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr: bool = Field(
        ...,
        alias="rsr",
        name="rsr",
        description="rsr",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dtc: bool = Field(
        ...,
        alias="dtc",
        name="Direct to Consumer",
        description="Indicates if the booking was made in a direct-to-consumer channel",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group: Optional[Group] = Field(
        None,
        alias="group",
        name="Group",
        description="Details of the group booking, if applicable",
    )
    accommodation_package: AccommodationPackage = Field(
        ...,
        alias="accommodationPackage",
        name="Accommodation Package",
        description="Accommodation package details",
    )


class AgencyId(BaseModel):
    """Data class that represents the Travel Agency ID"""

    value: Optional[str] = Field(
        None,
        alias="value",
        name="Value",
        description="Travel agency ID",
        example="00568674",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelAgency(BaseModel):
    """Data class that represents the details of the travel agency through which booking was made"""

    agency_id: AgencyId = Field(
        ...,
        alias="agencyId",
        name="Agency ID",
        description="Unique ID for travel agency",
    )
    agency_name: str = Field(
        ...,
        alias="agencyName",
        name="Agency Name",
        description="Travel agency name",
        example="AAA TRAVEL AGENCY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chain_name: Optional[str] = Field(
        None,
        alias="chainName",
        name="Chain Name",
        description="Name of the travel agency chain, if applicable",
        example="AAA Washington",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    commission_code: Optional[str] = Field(
        None,
        alias="commissionCode",
        name="Commission Code",
        description="Travel agency commission details",
        example="10percent Flat Commission",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelAgent(BaseModel):
    """Data class that represents the details of the Travel Agent through with booking was made"""

    email: List[EmailItem] = Field(
        ...,
        alias="email",
        name="Email",
        description="Travel agent email",
    )


class TravelBoxResortReservationEventDetails(BaseModel):
    """Data class that represents the details around resort booking, Guest PII, pricing etc."""

    status: str = Field(
        ...,
        alias="status",
        name="Reservation Status",
        description="Status of the resort reservation - Booked etc.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    booking_date: date = Field(
        ...,
        alias="bookingDate",
        name="Booking Date",
        description="Booking date of the resort reservation",
        example="2023-02-05",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    contact_person: Optional[ContactPerson] = Field(
        None,
        alias="contactPerson",
        name="Contact Person",
        description="Contact person name and details",
    )
    travel_agency: Optional[TravelAgency] = Field(
        None,
        alias="travelAgency",
        name="Travel Agency",
        description="Details of the travel agency through which booking was made",
    )
    travel_agent: Optional[TravelAgent] = Field(
        None,
        alias="travelAgent",
        name="Travel Agent",
        description="Details of the travel agent through which booking was made",
    )
    primary_guest_ref: str = Field(
        ...,
        alias="primaryGuestRef",
        name="Primary Guest Reference",
        description="Number that denotes the primary Guest",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guests: Guests = Field(
        ...,
        alias="guests",
        name="Guests",
        description="Details of all the Guests in the reservation, including name, locators etc. A DLR reservation from TBX could have up to 14 Guests",
    )
    comments: Optional[List[CommentItem]] = Field(
        None,
        alias="comments",
        name="Comments",
        description="Freeform comments put in as notes, requests etc., along with the ID of the Cast that put in the comment",
    )
    area_period: AreaPeriod = Field(
        ...,
        alias="areaPeriod",
        name="Area Period",
        description="Start date of the visit",
    )
    price_summary: PriceSummary = Field(
        ...,
        alias="priceSummary",
        name="Price Summary",
        description="Summary of total price, deposits paid and balance due",
    )
    guaranteed: bool = Field(
        ...,
        alias="guaranteed",
        name="Guaranteed",
        description="Indicator for guaranteed reservation",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_properties: List[ReservationPropertyItem] = Field(
        ...,
        alias="reservationProperties",
        name="Reservation Properties",
        description="Indicates the source of business associated with the reservation",
    )
    history: List[HistoryItem] = Field(
        ...,
        alias="history",
        name="History",
        description="Shows summarized history of updates on the reservation",
    )
    audit_details: AuditDetails = Field(
        ...,
        alias="auditDetails",
        name="Audit Details",
        description="Cast member ID and datetime of the updates made",
    )
    id: Id = Field(
        ...,
        alias="id",
        name="ID",
        description="Travelbox Reservation ID",
    )
    accommodation_package_order_items: List[AccommodationPackageOrderItem] = Field(
        ...,
        alias="accommodationPackageOrderItems",
        name="Accommodation Package Order Items",
        description="Details, price summary etc., of the accommodation package that includes products beyond rooms",
    )
    booking_reference: Optional[str] = Field(
        None,
        alias="bookingReference",
        name="Booking Reference",
        description="Booking reference number",
        example="0000ADB800",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )


class ReservationLinkItem(BaseModel):
    """Data class that represents the reservation links pointing to the Guest details"""

    dob: Optional[date] = Field(
        None,
        alias="dob",
        name="Date of Birth",
        description="Date of Birth of the reservation Guest in yyyy-mm-dd",
        example="1999-09-09",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    email_id: Optional[str] = Field(
        None,
        alias="emailId",
        name="Email Address",
        description="Guest email address",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="Guest First Name",
        description="Guest last name",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="lastName",
        name="Guest Last Name",
        description="Guest last name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    reservation_num: Optional[str] = Field(
        None,
        alias="reservationNum",
        name="Reservation Number",
        description="Resort reservation number",
        example="353116564535",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    swid: Optional[str] = Field(
        None,
        alias="swid",
        name="Starwave Guest Identifier",
        description="Unique identifier for the Guest's online account",
        example="{EC42B76E-1054-4CCE-9406-4CBFD707B818}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    passenger_num: Optional[int] = Field(
        None,
        alias="passengerNum",
        name="Passenger Number",
        description="Passenger number from the reservation party",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_primary_guest: Optional[bool] = Field(
        None,
        alias="isPrimaryGuest",
        name="Primary Guest Indicator",
        description="Indicator for the primary Guest in the reservation party",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_reservation_manager: Optional[bool] = Field(
        None,
        alias="isReservationManager",
        name="Reservation Manager Indicator",
        description="Indicator for the reservation manager in the reservation party",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketItem(BaseModel):
    """Data class that represents the tickets associated with the Guests"""

    park_hopper: Optional[bool] = Field(
        None,
        alias="parkHopper",
        name="Park Hopper Indicator",
        description="Indicator for the park-hopper ticket",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    passenger_no: Optional[int] = Field(
        None,
        alias="passengerNo",
        name="Passenger Number",
        description="Passenger number from the reservation party",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pseudo_visual_id: Optional[str] = Field(
        None,
        alias="pseudoVisualId",
        name="Psuedo Visual ID",
        description="Initially assigned ticket Visual ID",
        example="01V7B4B20436AE84C00A17C05460E046DB1REB4AB0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_num: Optional[str] = Field(
        None,
        alias="reservationNum",
        name="Reservation Number",
        description="Resort reservation number",
        example="353116564535",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    num_days: Optional[int] = Field(
        None,
        alias="numDays",
        name="Number of Days",
        description="Number of days associated with the tickets",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_start_date: Optional[date] = Field(
        None,
        alias="validityStartDate",
        name="Validity Start Date",
        description="Ticket validity start date",
        example="2023-05-22",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_end_date: Optional[date] = Field(
        None,
        alias="validityEndDate",
        name="Validity End Date",
        description="Ticket validity end date",
        example="2024-01-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_activated: Optional[bool] = Field(
        None,
        alias="isActivated",
        name="Is Activated",
        description="Indicator for whether the ticket is activated",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pbp: Optional[int] = Field(
        None,
        alias="pbp",
        name="pbp",
        description="pbp",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    visual_id: Optional[str] = Field(
        None,
        alias="visualId",
        name="Visual ID",
        description="Ticket visual ID",
        example="7099941215197044699",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    voucher_id: Optional[str] = Field(
        None,
        alias="VoucherId",
        name="Voucher ID",
        description="Ticket voucher ID",
        example="KRWT1J",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )


class RocketResortReservationDetails(BaseModel):
    """Data class that represents the rocket resort reservation details"""

    reservation_num: str = Field(
        ...,
        alias="reservationNum",
        name="Reservation Number",
        description="Resort reservation Number",
        example="15293754",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    brand: str = Field(
        ...,
        alias="brand",
        name="Brand Name",
        description="Brand Name",
        example="CORE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ext_reference_id: Optional[str] = Field(
        None,
        alias="extReferenceId",
        description="External Reference ID",
        example="NUXZQFJU",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reservation_links: List[ReservationLinkItem] = Field(
        ...,
        alias="reservationLinks",
        name="Reservation Links",
        description="Reservation links pointing to Guest details",
    )
    tickets: List[TicketItem] = Field(
        ...,
        alias="tickets",
        name="Tickets",
        description="Tickets associated with the Guests",
    )
    is_direct_booking: bool = Field(
        ...,
        alias="isDirectBooking",
        name="Is Direct Booking",
        description="Direct booking indicator",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_wholesale_booking: bool = Field(
        ...,
        alias="isWholesaleBooking",
        name="Is Wholesale Booking",
        description="Wholesale booking indicator",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_travel_agent_booking: bool = Field(
        ...,
        alias="isTravelAgentBooking",
        name="Is Travel Agent Booking",
        description="Travel Agent booking indicator",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_disney_vacation_club: bool = Field(
        ...,
        alias="isDisneyVacationClub",
        name="Is Disney Vacation Club Booking",
        description="DVC booking indicator",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_package: bool = Field(
        ...,
        alias="isPackage",
        name="Is Package Booking",
        description="Package booking indicator",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TicketEntitlementItem(BaseModel):
    """Data class that represents the ticket entitlements associated with the reservation"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Ticket ID Type",
        description="Ticket entitlement ID type",
        example="package-admission-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Ticket ID Value",
        description="The ticket entitlement ID value corresponding to the ID type",
        example="15421488::TBX::15421488#GEN#1::11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ResortReservation(BaseModel):
    """Data class that represents the resort reservation details"""

    travel_box_resort_reservation_event_details: Optional[TravelBoxResortReservationEventDetails] = Field(
        None,
        alias="travelBoxResortReservationEventDetails",
        name="TravelBox Resort Reservation Event Details",
        description="Details around resort booking, Guest PII, pricing etc.",
    )
    rocket_resort_reservation_details: Optional[RocketResortReservationDetails] = Field(
        None,
        alias="rocketResortReservationDetails",
        name="Resort Reservation Details",
        description="Details associated with the booking around channel, package etc.",
    )
    ticket_entitlements: Optional[List[TicketEntitlementItem]] = Field(
        None,
        alias="ticketEntitlements",
        name="Ticket Entitlements",
        description="Ticket entitlements associated with the reservation",
    )
    reservation_number: Optional[str] = Field(
        None,
        alias="reservationNumber",
        name="Reservation Number",
        description="Resort reservation Number, populated only for DELETEs",
        example="15293754",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )


class GAMDLRResortReservationModel(BaseModel):
    """Payload class for GAMDLRResortReservationModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM DLR Resort Reservation"
        stream_name = "gam-kinesis-gam-resortreservation-guest360-dlr"
        description = """DLR Guest resort reservations as shared by the reservation source system"""
        unique_identifier = [
            "resort-reservation.rocketResortReservationDetails.reservationNum",
            "resort-reservation.reservationNumber",
        ]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = ""  # optional
        key_path_value = ""  # optional

    type_: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always RESORT RESERVATION",
        example="Resort Reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the resort reservation was created new, modified or deleted",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Details of Guest IDs from source systems for the resort Guests",
    )
    resort_reservation: Optional[ResortReservation] = Field(
        None,
        alias="resort-reservation",
        name="Resort Reservation",
        description="Resort reservation details",
    )
