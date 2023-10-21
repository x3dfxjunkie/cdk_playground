"""Source Data Contract for ED Redemption REDEMPTION_ATTEMPT"""
from __future__ import annotations

from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel, Field


class EaRedemptionDetails(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT EaRedemptionDetails Data
    """

    cache_appointment_id: str = Field(
        ...,
        alias="cacheAppointmentId",
        name="",
        description="FUll EA entitlement ID.  The UUID is the third section",
        example="2327549",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    das_entitlement_locked: bool = Field(
        ...,
        alias="dasEntitlementLocked",
        name="",
        description=" Was das entitlement locked.  Default is false.",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entitlement_type: str = Field(
        ...,
        alias="entitlementType",
        name="",
        description="The entitlement type.  Values: STD,NON,NOI,DAS,LRT,RDS,OVR,FDS",
        example="DAS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_name: str = Field(
        ...,
        alias="firstName",
        name="",
        description="Optional first name of guest associated to tapped media.",
        example="Submissive",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gwd_first_name: Optional[str] = Field(
        None,
        alias="gwdFirstName",
        name="",
        description="",
        example="Submissive",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gwd_tap: bool = Field(
        ...,
        alias="gwdTap",
        name="",
        description="Is the guest who tapped a Guest with disabilities for DAS purposes",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_link: Optional[str] = Field(
        None,
        alias="mediaLink",
        name="",
        description="",
        example="https://wdpr-gam-selfie-us-east-1-stage.s3.amazonaws.com/",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    party_size: int = Field(
        ...,
        alias="partySize",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_date_time: Optional[datetime] = Field(
        None,
        alias="endDateTime",
        name="",
        description="The end date time of the entitlement redemption window",
        example="2023-07-17T21:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    start_date_time: Optional[datetime] = Field(
        None,
        alias="startDateTime",
        name="",
        description="The start date time of the entitlement redemption window",
        example="2023-07-17T20:20:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ErrorData(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT ErrorData Data
    """

    current_queue_ids: List[str] = Field(
        ...,
        alias="currentQueueIds",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    minutes_late: int = Field(
        ...,
        alias="minutesLate",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    override_reasons: List[str] = Field(
        ...,
        alias="overrideReasons",
        name="",
        description="",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GuestId(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT GuestId Data
    """

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="",
        description="",
        example="VIRTUALQ_LINK_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id_value: str = Field(
        ...,
        alias="guestIdValue",
        name="",
        description="",
        example="c22ffd82-84f4-47a7-81c6-448ae1c605d7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guest(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT Guest Data
    """

    first_name: Optional[str] = Field(
        None,
        alias="firstName",
        name="",
        description="",
        example="Submissive",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_ids: List[GuestId] = Field(
        ...,
        alias="guestIds",
        name="",
        description="",
    )

    is_valid_ticket: bool = Field(
        ...,
        alias="isValidTicket",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PartyGuestId(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT PartyGuestId Data
    """

    guest_id_type: str = Field(
        ...,
        alias="guestIdType",
        name="",
        description="",
        example="VIRTUALQ_LINK_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id_value: str = Field(
        ...,
        alias="guestIdValue",
        name="",
        description="",
        example="c22ffd82-84f4-47a7-81c6-448ae1c605d7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Position(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT Position Data
    """

    anonymous_party_size: int = Field(
        ...,
        alias="anonymousPartySize",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group: int = Field(
        ...,
        alias="boardingGroup",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    boarding_group_type: str = Field(
        ...,
        alias="boardingGroupType",
        name="",
        description="",
        example="PRIMARY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expires_at: Optional[datetime] = Field(
        None,
        alias="expiresAt",
        name="",
        description="",
        example="2023-07-14T10:40:02-04:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_id: GuestId = Field(
        ...,
        alias="guestId",
        name="",
        description="",
    )

    is_released: bool = Field(
        ...,
        alias="isReleased",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    original_estimated_wait: str = Field(
        ...,
        alias="originalEstimatedWait",
        name="",
        description="",
        example="20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    party_guest_ids: Optional[List[PartyGuestId]] = Field(
        None,
        alias="partyGuestIds",
        name="",
        description="",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="The id of the located queue",
        example="91c23f11-5cc5-4840-9792-5f6d1c556770",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queued_at: datetime = Field(
        ...,
        alias="queuedAt",
        name="",
        description="",
        example="2023-07-14T10:41:37-04:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    summoned_at: Optional[datetime] = Field(
        None,
        alias="summonedAt",
        name="",
        description="",
        example="2023-07-14T10:42:02-04:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redeemed_at: Optional[datetime] = Field(
        None,
        alias="redeemedAt",
        name="",
        description="",
        example="2023-08-02T15:26:38-04:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Queue(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT Queue Data
    """

    backup_group_start: int = Field(
        ...,
        alias="backupGroupStart",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    current_arriving_group_end: int = Field(
        ...,
        alias="currentArrivingGroupEnd",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    current_arriving_group_start: int = Field(
        ...,
        alias="currentArrivingGroupStart",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    currently_filling_group: int = Field(
        ...,
        alias="currentlyFillingGroup",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    day_phase: str = Field(
        ...,
        alias="dayPhase",
        name="",
        description="",
        example="IN_USE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    is_accepting_joins: bool = Field(
        ...,
        alias="isAcceptingJoins",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    is_autovalidating: bool = Field(
        ...,
        alias="isAutovalidating",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modify_group_max: int = Field(
        ...,
        alias="modifyGroupMax",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    modify_group_min: int = Field(
        ...,
        alias="modifyGroupMin",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Z REF (Space Mountain)",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    physical_wait_time: int = Field(
        ...,
        alias="physicalWaitTime",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="",
        example="91c23f11-5cc5-4840-9792-5f6d1c556770",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    requires_cast_login: bool = Field(
        ...,
        alias="requiresCastLogin",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validate_queue_state_on_redemption_add_to_queue: bool = Field(
        ...,
        alias="validateQueueStateOnRedemptionAddToQueue",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wait_time: int = Field(
        ...,
        alias="waitTime",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_definition_id: Optional[str] = Field(
        None,
        alias="externalDefinitionId",
        name="",
        description="",
        example="411499845;entityType=Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    next_scheduled_open_time: Optional[str] = Field(
        None,
        alias="nextScheduledOpenTime",
        name="",
        description="",
        example="17:30:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    symbolic_identifier: Optional[str] = Field(
        None,
        alias="symbolicIdentifier",
        name="",
        description="",
        example="tron-lr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class VQRedemptionDetails(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT VQRedemptionDetails Data
    """

    error_data: Optional[ErrorData] = Field(
        None,
        alias="errorData",
        name="",
        description="",
    )

    guests: List[Guest] = Field(
        ...,
        alias="guests",
        name="",
        description="",
    )

    line_mode: str = Field(
        ...,
        alias="lineMode",
        name="",
        description="The type of line: FP, VQ, DUAL",
        example="VQ",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    positions: List[Position] = Field(
        ...,
        alias="positions",
        name="",
        description="Set of queue positions",
    )

    queue_id: str = Field(
        ...,
        alias="queueId",
        name="",
        description="",
        example="91c23f11-5cc5-4840-9792-5f6d1c556770",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queue_id_type: str = Field(
        ...,
        alias="queueIdType",
        name="",
        description="The type of queueId:  QUEUE_ID, SYMBOLIC_IDENTIFIER",
        example="QUEUE_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    queues: List[Queue] = Field(
        ...,
        alias="queues",
        name="",
        description="",
    )

    vq_link_id: str = Field(
        ...,
        alias="vqLinkId",
        name="",
        description="The VQ link Id",
        example="c22ffd82-84f4-47a7-81c6-448ae1c605d7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Redemption(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT Redemption Data
    """

    media_id: str = Field(
        ...,
        alias="mediaId",
        name="",
        description="The id of the media that was used to attempt the redemption",
        example="666055071",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    media_id_type: str = Field(
        ...,
        alias="mediaIdType",
        name="",
        description="The type of the media ID (Possible Values: BAND_PUBLIC, BAND_SECURE, TICKET_VISUAL, BAND_VISUAL)",
        example="BAND_PUBLIC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_mode: str = Field(
        ...,
        alias="productMode",
        name="",
        description="The product mode of that experience (Possible values: DUAL, FP)",
        example="FP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_type: str = Field(
        ...,
        alias="productType",
        name="",
        description="Which type of redemption occurred: FP/VQ",
        example="FP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    status: str = Field(
        ...,
        alias="status",
        name="",
        description="The status of this attempted redemption",
        example="OK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tap_date_time: datetime = Field(
        ...,
        alias="tapDateTime",
        name="",
        description="Time when tap occurred",
        example="2023-07-04T10:15:51",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_type: str = Field(
        ...,
        alias="unitType",
        name="",
        description="Optional value for the type of reader used (Possible values: ENTRANCE, MERGE, COMBO)",
        example="ENTRANCE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    valid_park_admission: bool = Field(
        ...,
        alias="validParkAdmission",
        name="",
        description="Was there valid park admission",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ea_redemption_details: Optional[EaRedemptionDetails] = Field(
        None,
        alias="eaRedemptionDetails",
        name="",
        description="",
    )

    v_q_redemption_details: Optional[VQRedemptionDetails] = Field(
        None,
        alias="vQRedemptionDetails",
        name="",
        description="",
    )


class Item(BaseModel):
    """
    Class For EA REDEMPTION_ATTEMPT Item Data
    """

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="",
        description="",
        example="4ec0335f-8994-46bd-a067-243f26e5cd68",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    experience_id: str = Field(
        ...,
        alias="experienceId",
        name="",
        description="The experience id  where the redemption attempt occured.",
        example="16491297",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_id: str = Field(
        ...,
        alias="locationId",
        name="",
        description="The location id  where the redemption attempt occured.",
        example="16491297",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    publish_key: str = Field(
        ...,
        alias="publishKey",
        name="",
        description="",
        example="16491297",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redemption: Redemption = Field(
        ...,
        alias="redemption",
        name="",
        description="",
    )

    redemption_event_type: str = Field(
        ...,
        alias="redemptionEventType",
        name="",
        description="Redemption event type.",
        example="REDEMPTION_ATTEMPT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EARedemptionWDWRedemptionAttemptModel(BaseModel):
    """
    Payload class for EARedemptionWDWRedemptionAttemptModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Redemption Attempt"
        stream_name = "prd-use1-guest360-ea-stream"
        description = "Provides all redemption attempt messages from EA. Even errors such as a blue lane (errors at touch point for early arrival, late arrival, no entitlement, etc.)."  # optional
        unique_identifier = ["correlationId"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "item.redemptionEventType"
        key_path_value = "REDEMPTION_ATTEMPT"

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="",
        description="",
        example="4ec0335f-8994-46bd-a067-243f26e5cd68",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_type: str = Field(
        ...,
        alias="eventType",
        name="",
        description="",
        example="REDEMPTION_REPORTING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item: Item = Field(
        ...,
        alias="item",
        name="",
        description="",
    )

    key: str = Field(
        ...,
        alias="key",
        name="",
        description="",
        example="16491297",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
