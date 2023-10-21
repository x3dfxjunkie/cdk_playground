"""Source Data Contract for GAM Managed Guest"""
from __future__ import annotations
from datetime import date

# from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


"""
class Action(Enum):
    CREATE = "CREATE"
    MODIFY = "MODIFY"
    DELETE = "DELETE"


class Type(Enum):
    MANAGEDGUEST = "MANAGEDGUEST"
"""


class Name(BaseModel):
    """Class for GAM FNF Name"""

    first_name: str = Field(
        ...,
        alias="firstName",
        name="Guest First Name",
        description="Guest first name",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    last_name: str = Field(
        ...,
        alias="lastName",
        name="Guest Last Name",
        description="Guest last name",
        example="Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    middle_name: Optional[str] = Field(
        None,
        alias="middleName",
        name="Guest Middle Name",
        description="Guest middle name",
        example="M",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    title: Optional[str] = Field(
        None,
        alias="title",
        name="Guest Name Title",
        description="Guest name title",
        example="Mr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    suffix: Optional[str] = Field(
        None,
        alias="suffix",
        name="Guest Name Suffix",
        description="Guest name suffix",
        example="Sr.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ManagedGuest(BaseModel):
    """ManagedGuest Class"""

    id: Optional[str] = Field(
        None,
        alias="id",
        name="Managed Guest ID",
        description="Managed Guest ID, which is also called the GUID",
        example="AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    name: Optional[Name] = Field(
        None,
        alias="name",
        name="Name",
        description="Managed Guest name",
    )
    visible: bool = Field(
        ...,
        alias="visible",
        name="Visible Flag",
        description="Visible Flag, often set to False when Managed Guest is deleted",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age: Optional[int] = Field(
        None,
        alias="age",
        name="Age",
        description="Age of the Managed Guest, shows as 18 for all adults",
        example=12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    date_of_birth: Optional[date] = Field(
        None,
        alias="dateOfBirth",
        name="Date of Birth",
        description="Date of birth of the Managed Guest",
        example="1981-09-17",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    avatar_id: Optional[str] = Field(
        None,
        alias="avatarId",
        name="Avatar ID",
        description="ID of the character selected by the Guest as avatar for the online profile",
        example="15655408",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    managing_swid: Optional[str] = Field(
        None,
        alias="managingSwid",
        name="Managing Guest SWID",
        description="Managing Guest ID, which is always the SWID",
        example="{AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class GAMWDWFnfManagedGuestModel(BaseModel):
    """Payload class for GAMWDWFnfManagedGuestModel"""

    class Config:
        """Payload Level Metatags"""

        title = "GAM WDW FNF Managed Guest"
        stream_name = "gam-kinesis-fnf-managedguest-guest360-wdw"
        description = "WDW Guests managed by the primary/managing Guests via MDX"
        unique_identifier = ["managedGuest.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "type"
        key_path_value = "ManagedGuest"

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always ManagedGuest",
        example="ManagedGuest",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the Managed Guest was created new, modified or deleted",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    managed_guest: ManagedGuest = Field(
        ...,
        alias="managedGuest",
        description="Managed Guest details",
    )
