# Sample Data: https://twdc.sharepoint.com/sites/DPPGuest360Team/_layouts/15/download.aspx?UniqueId=78670ddfc5b24be0bd505cc29b1ae53d&e=1bVgPj
"""Source Data Contract Template for PlayApp Achievements"""
from __future__ import annotations

# from typing import List
# from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime

# from app.src.data_structures.data_contracts.source.global_source_data_contract import (Swid)


# class PlayAppAchievementEnvironment(Enum):
#    """Data Class for Environment field values"""

#    PROD = "prod"
#    LOAD = "load"
#    STAGE = "stage"
#    LATEST = "latest"


# class PlayAppAchievementType(Enum):
#    """Data Class for Type field values"""

#    INGAME = "ingame"  # issued through a game played on the device
#    INQUEUE = "inqueue"  # a platform achievement earned in an attraction queue, for instance a ride achievement
#    TRIVIA = "trivia"  # issued through the trivia game
#    SPECIAL = "special"  # issued by the platform for “special actions” e.g. creating a play file with an avatar
#    RIDECOUNT = "rideCount"  # issued by the Ride Count Service for seeing a ride counting beacon
#    CASTAPP = "CastApp"  # issued by the CastApp usually for remediation of a guest not being awarded an achievement.


class Award(BaseModel):
    """Class for Achievement Awards"""

    environment: str = Field(
        ...,
        alias="environment",
        name="Environment",
        description="The Source Application's environment that produced the record.",
        example="prod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    issued_by: str = Field(
        ...,
        alias="issuedBy",
        name="Issued By",
        description="Metadata about what issued the achievement.",
        example="platform",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    issued_date: datetime = Field(
        ...,
        alias="issuedDate",
        name="Issued Date",
        description="The date the achievement was awarded.",
        example="2023-06-01T22:10:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location: str = Field(
        ...,
        alias="location",
        name="Achievement Location",
        description="The location associated with the Achievement.",
        example="starWarsRiseOfTheResistanceRideCountWDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="name",
        name="Achievement Name",
        description="The name of Achievement that has been awarded.",
        example="heroOfTheResistance",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Achievement Type",
        description="The type of Achievement that has been awarded.",
        example="inqueue",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PlayAppAchievementModel(BaseModel):
    """Payload class for PlayAppAchievementModel"""

    class Config:
        """Payload Level Metadata"""

        # All fields are required for Pass 1 except "timezone"

        title = "PlayApp Achievements"
        #   Value should spell out the name of the payload
        stream_name = "guest360-playapp-achievement-stream"
        #   Value should be the name of the stream minus environment and region designation.
        #   This may be optional given the stream may not be available yet.
        #   Example: CME's kinesis stream name is `prd-use1-guest360-dlr-lightning-lane-stream`,
        #   the stream_name would be `guest360-dlr-lightning-lane-stream` with the environment and region stripped: `prd-use1-`
        description = "PlayApp Achievements"
        #   Description of the table or payload
        unique_identifier = ["award.environment", "award.name", "award.location", "guestId"]
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
        #       connection with those financial products and services.
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
        #       Confidential -
        #           The information utilized by TWDC and only intended for individuals with a business need.
        #           Loss or unauthorized use of this information could, as determined by TWDC, result in severe
        #           adverse effects on the Company brand, operations, or compliance.
        #           Examples: Attendance, any revenue data, PCI Data, children data, health data, genetic data, biometric data, cross segment data,
        #       Internal Use -
        #           The information utilized by TWDC and not intended to be shared with the public. Loss or unauthorized use of this information could,
        #           as determined by TWDC, result in profound adverse effects on the Company brand, finance, operations, or compliance.
        #           Examples: Most things would sit here
        #       Public -
        #           Information types that are lawfully made available to the general public or are made available for public distribution through
        #           authorized TWDC channels.
        #           Examples: Calendars, Weather, School schedules, Venue schedules
        #   Additional details:  https://confluence.disney.com/display/TWDCISPS/Information+Classification
        financial_data = "false"
        #   True/False/NULL indicator designating if financial data is included in the table/payload
        version = "0.0.1"

    #   The version of the data contract (Default to 0.0.1).  Modifications/updates to the data contract should be considered Minor releases.
    #   The criteria for incrementing Major release is limited to the addition of a Required field.
    award: Award = Field(..., alias="award")
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
        example="swid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
