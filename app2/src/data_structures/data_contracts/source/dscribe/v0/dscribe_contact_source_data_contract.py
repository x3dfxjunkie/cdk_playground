"""Source Data Contract Template for CONTACT"""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class PhoneItem(BaseModel):
    """
    Class For Dscribe CONTACT PhoneItem Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Non-Disney Contacts",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    number: str = Field(
        ...,
        alias="number",
        name="",
        description="",
        example="(949) 632-4694",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    share_with_guest: bool = Field(
        ...,
        alias="shareWithGuest",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Addres(BaseModel):
    """
    Class For Dscribe CONTACT Addres Data
    """

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Non-Disney Contacts",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    address1: Optional[str] = Field(
        None,
        alias="address1",
        name="",
        description="",
        example="Attn: Mike Hogan",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    address2: Optional[str] = Field(
        None,
        alias="address2",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    city: Optional[str] = Field(
        None,
        alias="city",
        name="",
        description="",
        example="Balboa",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    zip: Optional[str] = Field(
        None,
        alias="zip",
        name="",
        description="",
        example="92261",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    share_with_guest: bool = Field(
        ...,
        alias="shareWithGuest",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    state: Optional[str] = Field(
        None,
        alias="state",
        name="",
        description="",
        example="Florida",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    country: Optional[str] = Field(
        None,
        alias="country",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Website(BaseModel):
    """
    Class For Dscribe CONTACT Website Data
    """

    url: Optional[str] = Field(
        None,
        alias="url",
        name="",
        description="",
        example="http://www.chinacovekayakadventures.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    share_with_guest: bool = Field(
        ...,
        alias="shareWithGuest",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Email(BaseModel):
    """
    Class For Dscribe CONTACT Email Data
    """

    email_address: Optional[str] = Field(
        None,
        alias="emailAddress",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    share_with_guest: bool = Field(
        ...,
        alias="shareWithGuest",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DScribeContactModel(BaseModel):
    """
    Payload class for DscribeContactModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Contact"
        stream_name = "prd-use1-guest360-dscribe-stream"
        description = "Contains all information about WDW and DLR contact enterprise metadata."  # optional
        unique_identifier = ["id"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "contentType"
        key_path_value = "Contact"

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="10620431",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    content_type: str = Field(
        ...,
        alias="contentType",
        name="",
        description="",
        example="Contact",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    title: str = Field(
        ...,
        alias="title",
        name="",
        description="",
        example="China Cove Kayak Adventures",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_html: str = Field(
        ...,
        alias="nameHtml",
        name="",
        description="",
        example="China Cove Kayak Adventures",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name_text: str = Field(
        ...,
        alias="nameText",
        name="",
        description="",
        example="China Cove Kayak Adventures",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    destination: str = Field(
        ...,
        alias="destination",
        name="",
        description="",
        example="DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    type: str = Field(
        ...,
        alias="type",
        name="",
        description="",
        example="Non-Disney Contacts",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    share_with_guest: bool = Field(
        ...,
        alias="shareWithGuest",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phone: Optional[List[PhoneItem]] = Field(
        None,
        alias="phone",
        name="",
        description="",
    )

    address: List[Addres] = Field(
        ...,
        alias="address",
        name="",
        description="",
    )

    website: Website = Field(
        ...,
        alias="website",
        name="",
        description="",
    )

    email: Email = Field(
        ...,
        alias="email",
        name="",
        description="",
    )

    description: Optional[str] = Field(
        None,
        alias="description",
        name="",
        description="",
        example=" Notes: Kayak tours on the ocean for all ages and skill levels. Guided tours customized to include Newport Beach Bay, Orange County's best surf spots, and local beaches. Hotel pick-up suggested at 7:00am. ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sub_type: Optional[str] = Field(
        None,
        alias="subType",
        name="",
        description="",
        example="Transportation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
