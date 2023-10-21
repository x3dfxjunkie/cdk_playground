"""Source Data Contract for GAM Friends & Family - Invitation"""
from __future__ import annotations
from datetime import datetime

# from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

"""
class Action(Enum):
    CREATE = "CREATE"
    MODIFY = "MODIFY"


class Type(Enum):
    INVITATION = "Invitation"
"""


class IssuedGuest(BaseModel):
    """Class for GAM FNF IssuedGuest"""

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="Guest ID Type",
        description="ID type of the Guest that the invitation was sent by/to, often a GUID or a SWID",
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id_value: str = Field(
        ...,
        alias="guestIdValue",
        name="Guest ID Value",
        description="ID value corresponding to the ID type of the Guest that the invitation was sent by/to",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class Invitation(BaseModel):
    """Class for Invitation"""

    id: str = Field(
        ...,
        alias="id",
        name="Invitation ID",
        description="Unique ID assigned by the system for each invitation",
        example="768040",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    invitation_type: str = Field(
        ...,
        alias="invitationType",
        name="Invitation Type",
        description="The form in which the invitation was issued",
        example="qrCode",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Invitation Status",
        description="Current status of the invitation since it was created - Pending, Accepted, Declined, Revoked etc.",
        example="Pending",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    issued_to: IssuedGuest = Field(
        ...,
        alias="issuedTo",
        name="Issued To",
        description="Identifier for the Guest that the invitation was issued to",
    )
    issued_by: IssuedGuest = Field(
        ...,
        alias="issuedBy",
        name="Issued By",
        description="Identifier for the Guest that the invitation was issued by",
    )
    relationship_classification: Optional[str] = Field(
        None,
        alias="relationshipClassification",
        name="Relationship Classification",
        description="Relationship of the Guest that was invited to connect & share",
        example="friend",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    access_classification_code: str = Field(
        ...,
        alias="accessClassificationCode",
        name="Access Classification Code",
        description="Classification code that defines the access level requested for the connected Guests",
        example="PLAN_VIEW_ALL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    access_classification_description: str = Field(
        ...,
        alias="accessClassificationDescription",
        name="Access Classification Description",
        description="Classification description that defines the access level requested for the connected Guests",
        example="Plan and View All",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_classification_code: str = Field(
        ...,
        alias="groupClassificationCode",
        name="Group Classification Code",
        description="Classification code that defines the group of the Guests that are connecting",
        example="TRAVELLING_PARTY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_classification_description: str = Field(
        ...,
        alias="groupClassificationDescription",
        name="Group Classification Description",
        description="Classification description that defines the group of the Guests that are connecting",
        example="Travelling Party",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    share_classification_code: Optional[str] = Field(
        None,
        alias="shareClassificationCode",
        name="Share Classification Code",
        description="Classification code that defines the share level between the Guests",
        example="SHARE_MEDIA_DOWNLOAD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    share_classification_description: Optional[str] = Field(
        None,
        alias="shareClassificationDescription",
        name="Share Classification Description",
        description="Classification description that defines the share level between the Guests",
        example="Share Media Download",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sender_swid: str = Field(
        ...,
        alias="senderSwid",
        name="Starwave Guest Identifier",
        description="SWID of the sender of the invitation; this could be on behalf of another Guest as well",
        example="{A1A1A1A1-A1A1-A1A1-A1A1-A1A1A1A1A1A1}",
        guest_identifier=True,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    invitation_email: Optional[str] = Field(
        None,
        alias="invitationEmail",
        name="Invitation Email",
        description="Email that the invitation was sent to",
        example="mickey.donald@disney.com",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Direct",
    )


class GAMWDWFnfInvitationModel(BaseModel):
    """Payload class for GAMWDWFnfInvitationModel"""

    class Config:
        """Payload Level Metadata"""

        title = "GAM WDW FNF Invitation"
        stream_name = "gam-kinesis-fnf-invitation-guest360-wdw"
        description = """Invitations sent by WDW Guests to connect via Friends & Family in MDX"""
        unique_identifier = ["invitation.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"
        key_path_value = "Invitation"

    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always Invitation",
        example="Invitation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the Friends & Family invitation was created new or modified when accepted/rejected/revoked",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    issued_date_time: datetime = Field(
        ...,
        alias="issuedDateTime",
        name="Issued DateTime",
        description="Datetime that the invitation was issued originally",
        example="2023-04-05T15:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    invitation: Invitation = Field(
        ..., alias="invitation", name="Invitation Details", description="Details of the issued invitation"
    )
