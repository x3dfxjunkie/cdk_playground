# Sample Data: https://twdc.sharepoint.com/sites/DPPGuest360Team/_layouts/15/download.aspx?UniqueId=3a0550f2bf884cbc8dddd6b3a6210038&e=t7gJYj
"""Source Data Contract Template for PlayApp Quests"""
from __future__ import annotations
from typing import List, Optional
from datetime import datetime

# from enum import Enum
from pydantic import BaseModel, Field

# from app.src.data_structures.data_contracts.source.global_source_data_contract import Swid


# class PlayAppQuestRequestAction(Enum):
#    """Data Class for Request.Action field values"""

#    ABANDON = "ABANDON"
#    ASSIGN = "ASSIGN"
#    CLAIM = "CLAIM"
#    DETECTED = "DETECTED"
#    GESTURE = "GESTURE"


# class PlayAppQuestPayloadMessage(Enum):
#    """Data Class for Payload.Message field values"""

#    SUCCESS = "success"
#    WARN = "warn"


# class PlayAppQuestPayloadStatus(Enum):
#    """Data Class for Payload.Status field values"""

#    ABANDONED = "abandoned"
#    ACTIVE = "active"
#    CLAIMED = "claimed"
#    MARKED = "marked"
#    PENDING = "pending"


class Request(BaseModel):
    """Data Class for Request Object"""

    action: Optional[str] = Field(
        None,
        alias="action",
        name="Action",
        description="",
        example="GESTURE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id: str = Field(
        ...,
        alias="guestId",
        name="Guest ID",
        description="The Identifier associated to the method of the Guest's physical interaction",
        example="306326032",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="Guest ID Type",
        description="The type of Identifier populated in the Guest ID field",
        example="xband-shortrange-public-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location: str = Field(
        ...,
        alias="location",
        name="Location",
        description="",
        example="80007944",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source_id: Optional[str] = Field(
        None,
        alias="source_id",
        name="Source ID",
        description="",
        example="stitch",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Quest Type",
        description="The type of Quest",
        example="STATUE_QUEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    available_destinations: Optional[List[int]] = Field(
        None,
        alias="available_destinations",
        name="Available Destinations",
        description="",
        example=[1, 2, 3],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mark_timeout: Optional[int] = Field(
        None,
        alias="markTimeout",
        name="Mark Timeout",
        description="",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    overall_timeout: Optional[int] = Field(
        None,
        alias="overallTimeout",
        name="Overall Timeout",
        description="",
        example=60,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source_ids: Optional[List[str]] = Field(
        None,
        alias="sourceIds",
        name="Source IDs",
        description="",
        example=["olaf"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    """Data Class for Payload Object"""

    message: Optional[str] = Field(
        None,
        alias="message",
        name="Message",
        description="",
        example="success",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    task_id: Optional[str] = Field(
        None,
        alias="task_id",
        name="Task ID",
        description="",
        example="stitch",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Status",
        description="",
        example="marked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    credits: Optional[int] = Field(
        None,
        alias="credits",
        name="Credits",
        description="",
        example=700,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    number_of_completed_tasks: Optional[int] = Field(
        None,
        alias="number_of_completed_tasks",
        name="Number of Completed Tasks",
        description="",
        example=9,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    total_completed_tasks: Optional[int] = Field(
        None,
        alias="total_completed_tasks",
        name="Total Completed Tasks",
        description="",
        example=9,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    skip_instructions: Optional[bool] = Field(
        None,
        alias="skipInstructions",
        name="Skip Instructions",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Error(BaseModel):
    """Data Class for Error Object"""

    code: int = Field(
        ...,
        alias="code",
        name="Code",
        description="",
        example=404,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    details: Optional[str] = Field(
        None,
        alias="details",
        name="Details",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    message: str = Field(
        ...,
        alias="message",
        name="Message",
        description="",
        example="success",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Response(BaseModel):
    """Data Class for Response Object"""

    payload: Payload = Field(..., alias="payload")
    error: Optional[Error] = Field(None, alias="error")


class PlayAppQuestModel(BaseModel):
    """Payload class for PlayAppQuestModel"""

    class Config:
        """Payload Level Metadata"""

        # All fields are required for Pass 1 except "timezone"

        title = "PlayApp Quests"
        #   Value should spell out the name of the payload
        stream_name = "guest360-playapp-quest-stream"
        #   Value should be the name of the stream minus environment and region designation.
        #   This may be optional given the stream may not be available yet.
        #   Example: CME's kinesis stream name is `prd-use1-guest360-dlr-lightning-lane-stream`,
        #   the stream_name would be `guest360-dlr-lightning-lane-stream` with the environment and region stripped: `prd-use1-`
        description = "PlayApp Quests"
        #   Description of the table or payload
        unique_identifier = ["playId"]
        #   Value should specify an array of attributes that is the unique identifier for each record.
        key_path_name = ""
        #   OPTIONAL - Value should be the attribute key in the payload that can designate the corresponding payload's identity
        key_path_value = ""
        #   OPTIONAL - Value should be the attribute value in the payload that can designate the payload's identity,
        #   so that the ingest process can map a specific payload to this specific data contract
        timezone = "UTC"
        #   Value should be a standard code for the timezone (UTC,ET,PT...)
        pi_category = []
        #   Category of Personal Information contained within the data set
        #       - Biometric Data - Data derived from an individual's physiological, biological, or behavioral characteristics.
        #       Biometric Data is data derived from an individual's physiological, biological, or behavioral characteristics that is often
        #       (but not necessarily) used to identify an individual.  It includes fingerprints, iris or retina scans, face scans, and voiceprints.
        #
        #       - Data from Children - Personal Information from children under 13.  Personal Information collected from children under 13 can be
        #       subject to various legal and regulatory schemes, including (but not limited to) the Children's Online Privacy Protection Act ("COPPA").
        #
        #       - Cross-Segment Data - Personal Information obtained from a TWDC affiliate outside of DPEP. Examples include data from Disney+ or the Studios.
        #
        #       - Financial Product Data - Personal Information regarding financial products or services, such as loans. Companies offering certain
        #       financial products and services (e.g. consumer loans) may be subject to legal and regulatory schemes, including (but not limited to)
        #       the Gramm-Leach-Bliley Act ("GLBA"), which imposes data privacy and security requirements on the Personal Information collected in
        #       connection with those financial products and services."
        #
        #       - Genetic Data - Genetic Data is considered Sensitive Personal Information and is therefore subject to various legal and regulatory schemes.
        #       When tagging a table as containing Genetic Data, reach out to Privacy Legal to confirm this designation.
        #
        #       - Health Data - Health Data is Personal Information concerning an individual's past, present, or future mental or physical health or diagnosis.
        #       Health Data is considered Sensitive Personal Information and is therefore subject to various legal and regulatory schemes.
        #
        #       - Payment Card Data - Payment card data (e.g. data concerning credit and debit cards). Payment Card Data is subject to the Payment
        #       Card Industry Data Security Standard ("PCI DSS" or "PCI").
        #
        #       - Personal Information from Third Parties - Personal Information obtained from a source outside of Disney. Personal Information from
        #       Third Parties includes data obtained from data brokers (e.g. Neustar and Epsilon) to append to guest profile.
        #
        #       - Photo and Video Data - Photo and Video Data of guests. Examples include photos associated tickets and passes for theme park entry,
        #       PhotoPass photos, surveillance footage, and ride operation footage.
        #
        #       - Precise Geolocation - Data that can identify an individual's location within a 1750 ft radius. Precise Geolocation is data derived
        #       from a device that is used or is intended to be used to identify an individual's location within a geographic area equal to or less
        #       than the area of a circle with a radius of 1750 ft.
        #
        #       - Private Communications - Data containing a consumer's private communications. Private communications are consumer communications that
        #       the consumer does not intend for anyone to see other than the recipient, e.g. guest-to-guest chat transmissions.  Private communications
        #       do not include messages that the consumer sends to (or receives from) Disney, e.g. calls or emails to customer service.
        #
        #       - Video Consumption Data - Personal Information regarding video viewing, streaming, and purchases. Personal Information regarding a
        #       consumer's consumption of videos (e.g. viewing, streaming, and purchases) can be subject to various legal and regulatory schemes, including
        #       (but not limited to) the Video Privacy Protection Act ("VPPA").
        #
        #       - Data from Minors - Personal Information from individuals under 18.
        #
        #       - Personal Identifying Information - First Name/Last Name
        isps = "Internal Use"
        #   TWDC Information Security Policies and Standards (ISPS) Classification
        #   Confidential (Financial Info, Children Information, Attendance, Revenue); Internal Use (Most things would sit here); Public (Calendars, Weather)
        #   Additional details:  https://confluence.disney.com/display/TWDCISPS/Information+Classification
        financial_data = "false"
        #   True/False/NULL indicator designating if financial data is included in the table/payload
        version = "0.0.1"

    #   The version of the data contract (Default to 0.0.1).  Modifications/updates to the data contract should be considered Minor releases.
    #   The criteria for incrementing Major release is limited to the addition of a Required field.
    play_id: str = Field(
        ...,
        alias="playId",
        name="PlayID",
        description="The PlayApp Guest Identifier",
        example="AaAAaaaaa1aa1aaaAaaAaa",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    request: Request = Field(..., alias="request")
    response: Response = Field(..., alias="response")
    swid: str = Field(
        ...,
        alias="swid",
        name="SWID",
        description="Registered Guest Starwave ID",
        example="",
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Timestamp",
        description="Event Timestamp",
        example="2023-06-01T21:35:28.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cast_id: Optional[str] = Field(
        None,
        alias="castId",
        name="Cast ID",
        description="The Portal/HUB/SAP ID of the Cast Member manually making an update.",
        example="MOUSM001",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
