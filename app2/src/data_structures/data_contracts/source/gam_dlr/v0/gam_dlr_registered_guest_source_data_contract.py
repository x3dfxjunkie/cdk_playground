"""Source Data Contract for GAM DLR Registered Guest"""
from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class NativeGuestIdItem(BaseModel):
    """Data class that represents the Guest ID Type/Value pairs"""

    type: str = Field(
        ...,
        alias="type",
        name="Registered Guest ID Type",
        description="The Guest ID type for the registered Guest. Could be any ID type which locates a Guest uniquely.",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Registered Guest ID Value",
        description="The Guest ID value corresponding to the Guest ID type for the registered Guest",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Name(BaseModel):
    """Data class for the Guest name components"""

    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="First Name",
        description="Registered Guest first name",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: Optional[str] = Field(
        None,
        alias="lastName",
        name="Last Name",
        description="Registered Guest last name",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="middleName",
        name="Middle Name",
        description="Registered Guest middle name",
        example="M",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    title: Optional[str] = Field(
        None,
        alias="title",
        name="Name Title",
        description="Registered Guest name title",
        example="Ms.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    suffix: Optional[str] = Field(
        None,
        alias="suffix",
        name="Name Suffix",
        description="Registered Guest name suffix",
        example="Sr.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class AddressListItem(BaseModel):
    """Data class for the Guest mailing address components"""

    id: str = Field(
        ...,
        alias="id",
        name="Address ID",
        description="Unique address ID, assigned by OneID",
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    line1: Optional[str] = Field(
        None,
        alias="line1",
        name="Address Line1",
        description="Address Line1 of the registered Guest",
        example="123 Main St.",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    line2: Optional[str] = Field(
        None,
        alias="line2",
        name="Address Line2",
        description="Address Line2 of the registered Guest",
        example="Apt A",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    line3: Optional[str] = Field(
        None,
        alias="line3",
        name="Address Line3",
        description="Address Line3 of the registered Guest",
        example="Building1",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    city: Optional[str] = Field(
        None,
        alias="city",
        name="Address City",
        description="City name from the registered Guest address",
        example="Orlando",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    state_or_province: Optional[str] = Field(
        None,
        alias="stateOrProvince",
        name="Address State or Province",
        description="State or Province name from the registered Guest address",
        example="FL",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    country: Optional[str] = Field(
        None,
        alias="country",
        name="Address Country",
        description="Country code from the registered Guest address",
        example="US",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    postal_code: str = Field(
        ...,
        alias="postalCode",
        name="Address Postal Code",
        description="Postal code from the registered Guest address",
        example="06520",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Address Type",
        description="Type of the registered Guest address - Home, Shipping, Billing etc.",
        example="HOME",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PhoneListItem(BaseModel):
    """Data class for the Guest phone components"""

    id: str = Field(
        ...,
        alias="id",
        name="Phone ID",
        description="Unique Phone ID, assigned by OneID",
        example="a1a1a1a1-a1a1-a1a1-a1a1-a1a1a1a1a1a1",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    number: str = Field(
        ...,
        alias="number",
        name="Phone Number",
        description="Phone number of the registered Guest",
        example="(407) 899-5090",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    extension: Optional[str] = Field(
        None,
        alias="extension",
        name="Phone Extension",
        description="Phone number extension of the registered Guest",
        example="4781",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    country_code: Optional[str] = Field(
        None,
        alias="countryCode",
        name="Phone Country",
        description="Country code from the registered Guest phone",
        example="US",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Phone Type",
        description="Type of the registered Guest phone",
        example="MOBILE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CommunicationPreferences(BaseModel):
    """Data class for communication language preferences of Guests"""

    preferred_language: Optional[str] = Field(
        None,
        alias="preferredLanguage",
        name="Preferred Language",
        description="Preferred language of the registered Guest",
        example="en",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class OptionItem(BaseModel):
    """Data class for communication options for Guests"""

    text: str = Field(
        ...,
        alias="text",
        name="Text",
        description="Indicates communication channel",
        example="Phone Message",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="Value",
        description="Indicates communication type",
        example="SMS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    checked: bool = Field(
        ...,
        alias="checked",
        name="Checked",
        description="Indicates opt-in vs opt-out",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Offers(BaseModel):
    """Data class for messaging channel preferences for communicating offers"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class DisneyFamilyOfBusinessNews(BaseModel):
    """Data class for messaging channel preferences for Disney FOB news"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class ItineraryReminders(BaseModel):
    """Data class for messaging channel preferences for itinerary reminders"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class WeeklyDisneyInsiderNewsletter(BaseModel):
    """Data class for messaging channel preferences for Disney insider newsletters"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class MediaAlerts(BaseModel):
    """Data class for messaging channel preferences for media alerts"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class FamilyAndFriendsNotifications(BaseModel):
    """Data class for messaging channel preferences for family and friends notifications"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class ItineraryChanges(BaseModel):
    """Data class for messaging channel preferences for itinerary changes"""

    type: str = Field(
        ...,
        alias="type",
        name="Type",
        description="",
        example="select",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    required: bool = Field(
        ...,
        alias="required",
        name="Required",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    multi: bool = Field(
        ...,
        alias="multi",
        name="Multi",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    options: List[OptionItem] = Field(
        ...,
        alias="options",
        name="Options",
        description="Messaging options",
    )


class MessagingPreferencesForm(BaseModel):
    """Data class for messaging preferences for various communication types"""

    offers: Optional[Offers] = Field(
        None,
        alias="offers",
        name="Offers",
        description="Messaging channel preferences for communicating offers",
    )
    disney_family_of_business_news: Optional[DisneyFamilyOfBusinessNews] = Field(
        None,
        alias="disneyFamilyOfBusinessNews",
        name="Disney Family of Business News",
        description="Messaging channel preferences for Disney FOB news",
    )
    itinerary_reminders: Optional[ItineraryReminders] = Field(
        None,
        alias="itineraryReminders",
        name="Itinerary Reminders",
        description="Messaging channel preferences for communicating itinerary reminders",
    )
    weekly_disney_insider_newsletter: Optional[WeeklyDisneyInsiderNewsletter] = Field(
        None,
        alias="weeklyDisneyInsiderNewsletter",
        name="Weekly Disney Insider Newsletter",
        description="Messaging channel preferences for weekly Disney insider newsletter",
    )
    media_alerts: Optional[MediaAlerts] = Field(
        None,
        alias="mediaAlerts",
        name="Media Alerts",
        description="Messaging channel preferences for communicating media alerts",
    )
    family_and_friends_notifications: Optional[FamilyAndFriendsNotifications] = Field(
        None,
        alias="familyAndFriendsNotifications",
        name="Family and Friends Notifications",
        description="Messaging channel preferences for family & friends notifications",
    )
    itinerary_changes: Optional[ItineraryChanges] = Field(
        None,
        alias="itineraryChanges",
        name="Itinerary Changes",
        description="Messaging channel preferences for itinerary changes",
    )


class MessagingPreferences(BaseModel):
    """Data class for messaging preferences"""

    messaging_preferences_form: Optional[MessagingPreferencesForm] = Field(
        None,
        alias="messagingPreferencesForm",
        name="Messaging Preferences Form",
        description="Messaging Preferences of the registered Guest",
    )


class Preferences(BaseModel):
    """Data class for other Guest preferences"""

    favorite_character_id: str = Field(
        ...,
        alias="favoriteCharacterId",
        name="Favorite Character ID",
        description="D-Scribe Enterprise ID of the favorite character of the Guest",
        example="411822047",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    avatar_id: str = Field(
        ...,
        alias="avatarId",
        name="Avatar ID",
        description="D-Scribe Enterprise ID of the character selected by the Guest as avatar for the online profile",
        example="15655408",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class RegisteredGuest(BaseModel):
    """Data class that represents the registered Guest details"""

    swid: str = Field(
        ...,
        alias="swid",
        name="Starwave Guest Identifier",
        description="Unique identifier for the registered Guest's online account",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    name: Optional[Name] = Field(
        None,
        alias="name",
        name="Name",
        description="Name components of the registered Guest",
    )
    date_of_birth: Optional[List[int]] = Field(
        None,
        alias="DateOfBirth",
        name="Date of Birth",
        description="DOB components, as available, for the registered Guest",
        example=[1980, 1970],
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    gender: Optional[str] = Field(
        None,
        alias="gender",
        name="Gender",
        description="Gender of the registered Guest",
        example="MALE",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    user_name: Optional[str] = Field(
        None,
        alias="UserName",
        name="User Name",
        description="User name for the online account",
        example="Mickeym876",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    email: Optional[str] = Field(
        None,
        alias="email",
        name="Email Address",
        description="Guest Email address used for the registration",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    country_code: Optional[str] = Field(
        None,
        alias="countryCode",
        name="Country Code",
        description="Guest approved legal country code of the registered account",
        example="US",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    language_code: Optional[str] = Field(
        None,
        alias="languageCode",
        name="Language Code",
        description="Language code associated with the registered account",
        example="en-US",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Status",
        description="Current status of the registered account",
        example="ACTIVE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    email_validation_status: Optional[str] = Field(
        None,
        alias="emailValidationStatus",
        name="Email Validation Status",
        description="Indiates if the email was verified or not",
        example="UNVALIDATED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    registration_date: Optional[datetime] = Field(
        None,
        alias="registrationDate",
        name="Registartion Date",
        description="Date that the account was originally registered",
        example="2021-11-28T02:05:20.499Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    test_profile_flag: Optional[str] = Field(
        None,
        alias="testProfileFlag",
        name="Test Profile Flag",
        description="Indicates if the profile was created as a test account",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reference_id: Optional[str] = Field(
        None,
        alias="referenceId",
        name="Reference ID",
        description="Unique ID for the account - this carries the SWID and is a redundant field now",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    client_id: Optional[str] = Field(
        None,
        alias="clientId",
        name="Client ID",
        description="Client ID associated with the website at the time of registration",
        example="TPR-WDW-LBSDK.AND-PROD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    affiliate_name: Optional[str] = Field(
        None,
        alias="affiliateName",
        name="Affiliate Name",
        description="Affiliate associated with the website at the time of registration",
        example="disneyid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_band: Optional[str] = Field(
        None,
        alias="ageBand",
        name="Age Band",
        description="Age group of the registered Guest - ADULT, CHILD, TEEN",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    profile_context: Optional[str] = Field(
        None,
        alias="profileContext",
        name="Profile Context",
        description="Profile Context",
        example="templateName=,siteID=1,sourceName=",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    address_list: Optional[List[AddressListItem]] = Field(
        None,
        alias="AddressList",
        name="Address List",
        description="Address details of the registered Guest",
    )
    phone_list: Optional[List[PhoneListItem]] = Field(
        None,
        alias="phoneList",
        name="Phone List",
        description="Phone number details of the registered Guest",
    )
    communication_preferences: Optional[CommunicationPreferences] = Field(
        None,
        alias="communicationPreferences",
        name="Communication Preferences",
        description="Communication languange preference of the registered Guest",
    )
    messaging_preferences: Optional[MessagingPreferences] = Field(
        None,
        alias="messagingPreferences",
        name="Messaging Preferences",
        description="Messaging channel preferences of the registered Guest for offers, reminders etc.",
    )
    preferences: Optional[Preferences] = Field(
        None,
        alias="preferences",
        name="Preferences",
        description="Other preferences of the registered Guest on characters, avatars etc.",
    )


class GAMDLRRegisteredGuestModel(BaseModel):
    """Payload class for GAMDLRRegisteredGuestModel"""

    class Config:
        """Payload Level Metadata"""

        name = "GAM DLR Registered Guest"
        stream_name = "gam-kinesis-gam-registeredguest-guest360-dlr"
        description = """DLR Registered Guest account details as shared by OneID"""
        unique_identifier = ["registeredGuest.swid"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"  # optional
        key_path_value = "RegisteredGuest"  # optional

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always RegisteredGuest",
        example="RegisteredGuest",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the registered Guest was created new, modified or deleted",
        example="MODIFY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestIdItem] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Details of Guest IDs from source systems for the registered Guest",
    )
    registered_guest: RegisteredGuest = Field(
        ...,
        alias="registeredGuest",
        name="Registered Guest Details",
        description="Registered Guest PII, contact information and account preferences",
    )
