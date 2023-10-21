"""Source Data Contract for GAM WDW XBand"""
from __future__ import annotations

# from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


"""
class Action(Enum):
    CREATE = "CREATE"
    MODIFY = "MODIFY"
    TRANSFER = "TRANSFER"


class Type(Enum):
    XBAND = "XBAND"
"""


class NativeGuestId(BaseModel):
    """NativeGuestId Class"""

    type: str = Field(
        ...,
        alias="type",
        name="Native Guest ID Type",
        description="Native Guest ID type - swid, xbms-link-id",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Native Guest ID Value",
        description="The value of the Native Guest ID type",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Guest(BaseModel):
    """Guest Class"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Guest Type",
        description="Type of identifier of guest - swid, xbms-link-id",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Guest Value",
        description="Guest Value of swid or xbms-link-id",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class PreviousOwner(BaseModel):
    """PreviousOwner Class"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Previous Owner Type",
        description="Previous Owner type identifier - swid, xbms-link-id",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Previous Owner Value",
        description="Previous Owner Value of swid or xbms-link-id",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Xband(BaseModel):
    """Xband Class"""

    xbandid: str = Field(
        ...,
        alias="xbandid",
        name="XBand Identifier",
        description="The unique identifier assigned by XBMS for each Xband is booked",
        example="A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    xband_external_number: Optional[str] = Field(
        None,
        alias="xband_external_number",
        name="Xband External Number",
        description="A visible Xband ID is printed on the Xband",
        example="00000007139D",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    xband_secure_id: Optional[str] = Field(
        None,
        alias="xband_secure_id",
        name="Xband Secure ID",
        description="A short range ID used for sensitive (financial) transactions",
        example="0009104955250843",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    xband_longrange_tag: Optional[str] = Field(
        None,
        alias="xband_longrange_tag",
        name="Xband Longrange Tag",
        description="RF Disney provided long range read ID",
        example="00051603325905412",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    xband_shortrange_tag: Optional[str] = Field(
        None,
        alias="xband_shortrange_tag",
        name="Xband Shortrange Tag",
        description="HF UID manufacturer supplied short range id (used for door lock)",
        example="00051603325905412",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    xband_shortrange_public_id: Optional[str] = Field(
        None,
        alias="xband_shortrange_public_id",
        name="Xband Shortrange Public ID",
        description="Used for interactions where no sensitive information is exposed",
        example="000785456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    xband_longrange_public_id: Optional[str] = Field(
        None,
        alias="xband_longrange_public_id",
        name="Xband Longrange Public ID",
        description="Used for interactions where no sensitive information is exposed",
        example="000785456",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    secondary_status: Optional[str] = Field(
        None,
        alias="secondary_status",
        name="Secondary Status",
        description="Triggered by the status change of a given Xband ID",
        example="PURCHASED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    category: Optional[str] = Field(
        None,
        alias="category",
        name="Category",
        description="Band category (distinguish between physical and virtual band categories)",
        example="BAND_PLUS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest: Optional[Guest] = Field(
        None,
        alias="guest",
        name="Guest",
        description="Guest identifier - swid, xbms-link-id. Contains type and value",
    )
    previous_owner: Optional[PreviousOwner] = Field(
        None,
        alias="previousOwner",
        name="Previous Owner",
        description="Guest identifier of previous owner - swid, xbms-link-id. Contains type and value",
    )


class GAMWDWMagicbandModel(BaseModel):
    """Payload class for GAMWDWMagicbandModel"""

    class Config:
        """Payload Level Metatags"""

        title = "GAM WDW Magic Band"
        stream_name = "gam-kinesis-gam-magicband-guest360-wdw"
        description = "WDW Guest magic bands as shared from the magic band management system"
        unique_identifier = ["xband.xbandid"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "type"
        key_path_value = "Xband"

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always Xband",
        example="Xband",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the Xband was created, modified, or transferred",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestId] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest IDs",
        description="Native Guest ID type - swid, xbms-link-id",
    )
    xband: Optional[Xband] = Field(
        None,
        alias="xband",
        name="Xband",
        description="Contains guest ID and Xband IDs/information",
    )
