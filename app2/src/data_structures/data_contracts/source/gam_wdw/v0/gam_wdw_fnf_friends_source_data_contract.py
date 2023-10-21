"""Source Data Contract Template for gam_wdw_fnf_friends_source_data_contract_sample"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class From(BaseModel):
    guest_id_type: Optional[str] = Field(
        None,
        alias="guestIdType",
        name="Guest ID Type",
        description="ID type of the Guest that the invitation was sent by/to, often a GUID or a SWID",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id_value: Optional[str] = Field(
        None,
        alias="guestIdValue",
        name="Guest ID Value",
        description="ID value corresponding to the ID type of the Guest that the invitation was sent by/to",
        example="{AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class To(BaseModel):
    guest_id_type: Optional[str] = Field(
        None,
        alias="guestIdType",
        name="Guest ID Type",
        description="ID type of the Guest that the invitation was sent by/to, often a GUID or a SWID",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id_value: Optional[str] = Field(
        None,
        alias="guestIdValue",
        name="Guest ID Value",
        description="ID value corresponding to the ID type of the Guest that the invitation was sent by/to",
        example="{AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Friend(BaseModel):
    from_: From = Field(
        ...,
        alias="from",
        name="Initiated From",
        description="Identifier for the Guest that the friend creation was initiated from",
    )
    to: To = Field(
        ...,
        alias="to",
        name="Initiated To",
        description="Identifier for the Guest that's created as a friend",
    )
    visible: bool = Field(
        ...,
        alias="visible",
        name="Visible Flag",
        description="Visible Flag for friends in linked profile",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    relationship_classification: Optional[str] = Field(
        None,
        alias="relationshipClassification",
        name="Relationship Classification",
        description="Relationship of the Guest - owned, friend, etc.",
        example="friend",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    access_classification_code: Optional[str] = Field(
        None,
        alias="accessClassificationCode",
        name="Access Classification Code",
        description="Classification code that defines the access level requested for the connected Guests",
        example="PLAN_VIEW_ALL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    access_classification_description: Optional[str] = Field(
        None,
        alias="accessClassificationDescription",
        name="Access Classification Description",
        description="Classification description that defines the access level requested for the connected Guests",
        example="Plan and View All",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_classification_code: Optional[str] = Field(
        None,
        alias="groupClassificationCode",
        name="Group Classification Code",
        description="Classification code that defines the group of the Guests that are connecting",
        example="TRAVELLING_PARTY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_classification_description: Optional[str] = Field(
        None,
        alias="groupClassificationDescription",
        name="Group Classification Description",
        description="Classification description that defines the group of the Guests that are connecting",
        example="Travelling Party",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    share_classification_code: Optional[List[str]] = Field(
        None,
        alias="shareClassificationCode",
        name="Share Classification Code",
        description="Classification code that defines the share level between the Guests",
        example=["SHARE_MEDIA_DOWNLOAD"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    share_classification_description: Optional[List[str]] = Field(
        None,
        alias="shareClassificationDescription",
        name="Share Classification Description",
        description="Classification description that defines the share level between the Guests",
        example=["Share Media Download"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GAMWDWFnfFriendsModel(BaseModel):
    class Config:
        """Payload Level Metadata"""

        title = "GAM WDW FNF Friends"
        stream_name = "gam-kinesis-fnf-friends-guest360-wdw"
        description = """WDW Guests connected as friends via Friends and Family in MDX"""
        unique_identifier = [
            "friends.from.guestIdType",
            "friends.from.guestIdValue",
            "friends.to.guestIdType",
            "friends.to.guestIdValue",
        ]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"
        key_path_value = "Friends"

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always Friends",
        example="Friends",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the Friend was created new or modified",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    friends: List[Friend] = Field(
        ...,
        alias="friends",
        name="Friends Details",
        description="Friends and the connection details",
    )
