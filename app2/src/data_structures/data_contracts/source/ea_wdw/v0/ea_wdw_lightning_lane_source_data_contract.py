"""Source Data Contract for EA WDW Lightning Lane"""
from __future__ import annotations
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class ActivityItem(BaseModel):
    """Data class for Entitlement Activity"""

    activity_date_time: datetime = Field(
        ...,
        alias="activityDateTime",
        name="Activity Date Time",
        description="Date and time of the activity on the entitlement",
        example="2022-04-03T11:12:50.673394000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activity_reason: str = Field(
        ...,
        alias="activityReason",
        name="Activity Reason",
        description="Reason Code for activity on the entitlement",
        example="PUR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activity_status: str = Field(
        ...,
        alias="activityStatus",
        Name="Activity Status",
        description="Activity status of the entitlement",
        example="BOOKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activity_user: str = Field(
        ...,
        alias="activityUser",
        name="Activity User",
        description="ID of the user that performed the activity; this carries the Guest's SWID when activity was performed by the Guest",
        example="SYSTEM",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    correlation_id: Optional[str] = Field(
        None,
        alias="correlationId",
        name="Correlation ID",
        description="Internal identifier used for tracking across services",
        example="2222222-bbbb-2222-a7a4-1111119de2b9",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_date_time: Optional[datetime] = Field(
        None,
        alias="redemptionDateTime",
        name="Redemption Date Time",
        description="The date and time where activity was redeemed",
        example="2022-04-03T11:12:50.673402000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_experience_id: Optional[str] = Field(
        None,
        alias="redemptionExperienceId",
        name="Redemption Experience ID",
        description="The Enterprise/One Source ID for the Experience (Attraction or Show) where redeemption occured",
        example="18375495",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_location_id: Optional[str] = Field(
        None,
        alias="redemptionLocationId",
        name="Redemption Location ID",
        description="The Enterprise/One Source ID for the Location of the Experience (Facility) where redeemption occured",
        example="18375495",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_touch_device_id: Optional[str] = Field(
        None,
        alias="redemptionTouchDeviceId",
        name="Redemption Touch Device ID",
        description="The identifier for the reader the guest's media was read for redemption",
        example="999875636",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    related_entitlement: Optional[str] = Field(
        None,
        alias="relatedEntitlement",
        name="Related Entitlement",
        description="Concatenation of type, guestID etc. of any related entitlement",
        example="INVENTORY_ZZZZZZZ99ZZ9ZZZ9ZZZZZZZ9Z9_9999zz99-99zz-9999-9zzz-z9999999zz99_9999-99-99",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class LocationListItem(BaseModel):
    """Data class for the list of locations for experiences"""

    location_id: str = Field(
        ...,
        alias="locationId",
        name="Location ID",
        description="Location ID for entitlement",
        example="18375495",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location_type: str = Field(
        ...,
        alias="locationType",
        name="Location Type",
        description="Location type for entitlement",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ExperienceListItem(BaseModel):
    """Data class for the list of experiences allowed for the entitlement"""

    experience_id: str = Field(
        ...,
        alias="experienceId",
        name="Experience ID",
        description="The Enterprise/One Source ID for the Experience (Attraction or Show)",
        example="19263736",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    experience_type: str = Field(
        ...,
        alias="experienceType",
        name="Experience Type",
        description="Experience type for entitlement",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location_list: List[LocationListItem] = Field(
        ...,
        alias="locationList",
        name="Location List",
        description="List of location IDs and types for the entitlement",
    )
    park_id: str = Field(
        ...,
        alias="parkId",
        name="Park ID",
        description="Onesource facility ID of the park where the experience is",
        example="80007823",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    remaining_count: int = Field(
        ...,
        alias="remainingCount",
        name="Remaining Count",
        description="Remaining uses for the entitlement",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    uses_allowed: int = Field(
        ...,
        alias="usesAllowed",
        name="Uses Allowed",
        description="Number of uses allowed for the entitlement",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Entitlement(BaseModel):
    """Data class for entitlement details"""

    ttl_time: Optional[int] = Field(
        None,
        alias="TTL_TIME",
        name="Time-to-Live Time",
        description="Internal value used for purging",
        example=1637776500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    activities: List[ActivityItem] = Field(
        ...,
        alias="activities",
        name="Activities",
        description="List of activities that reflects entitlement status changes",
    )
    booking_guest_id: str = Field(
        ...,
        alias="bookingGuestId",
        name="Booking Guest ID",
        description="The ea_link_id of the Guest who booked the entitlement",
        example="AAAAAAAAAAAAAA1AAAAA2AAA3A",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    booking_id: Optional[str] = Field(
        None,
        alias="bookingId",
        name="Booking ID",
        description="Unique identifier for the booking, may contain multiple entitlements",
        example="999999999-zzzz-9999-zzzz-999999z9999z",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    create_user_id: str = Field(
        ...,
        alias="createUserId",
        name="Create User ID",
        description="ID of the user that booked the entitlement; this carries the Guest's SWID when booked by the Guest",
        example="SYSTEM",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    created_date: datetime = Field(
        ...,
        alias="createdDate",
        name="Created Date",
        description="The date and time that the booking was made",
        example="2022-04-03T10:14:03.006702000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement_key: str = Field(
        ...,
        alias="entitlementKey",
        name="Entitlement Key",
        description="Internal value used as a item sort key. Concatenated value of other fields: <type>-<Date portion of enttlStartDate>-<enttlId>",
        example="NONINVENTORY-cccccccc-9999-40ee-8a03-1111118fd7a2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enttl_end_date: datetime = Field(
        ...,
        alias="enttlEndDate",
        name="Entitlement End Date",
        description="The end of the window when the entitlement can be redeemed",
        example="2022-04-04T06:00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enttl_id: UUID = Field(
        ...,
        alias="enttlId",
        name="Entitlement ID",
        description="Unique transaction ID for the Lightning Lane entitlement",
        example=UUID("aaaaaaaa-1111-2222-bbbb-111111de3b2a"),
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    enttl_start_date: datetime = Field(
        ...,
        alias="enttlStartDate",
        name="Entitlement Start Date",
        description="The beginning of the window when the entitlement can be redeemed",
        example="2022-04-03T09:45:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    experience_id: Optional[str] = Field(
        None,
        alias="experienceId",
        name="Experience ID",
        description="The Enterprise/One Source ID for the Experience (Attraction or Show)",
        example="ENT1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    experience_type: Optional[str] = Field(
        None,
        alias="experienceType",
        name="Experience Type",
        description="The Enterprise/One Source type for the Experience",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_id: str = Field(
        ...,
        alias="guestId",
        name="Guest ID",
        description="The ea_link_id of the Guest who will experience the entitlement",
        example="AAAAAAAAAAAAAA1AAAAA2AAA3A",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    inventory_id: Optional[str] = Field(
        None,
        alias="inventoryId",
        name="Inventory Id",
        description="Unique identifier for the inventory bucket that this entitlement was validated against",
        example="GPLUS-18375495-18375495-20210118-1610985600-1610989200",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location_id: Optional[str] = Field(
        None,
        alias="locationId",
        name="Location ID",
        description="The Enterprise/One Source ID for the Location of the Experience (Facility)",
        example="18375495",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location_type: Optional[str] = Field(
        None,
        alias="locationType",
        name="Location Type",
        description="The Enterprise/One Source type for the Location where the Experience occurs (Facility)",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    offer_id: Optional[str] = Field(
        None,
        alias="offerId",
        name="Offer ID",
        description="Concatenated value of other fields: <bookingGuestId>-<enttlId>-<inventoryId>",
        example="AAAAAAAAAAAAAAA9AAAAA9AAA9A_99a99a9a-aaaa-9999-a9aa-99aa9a9999aa_GPLUS-99999999-99999999-99999999_99999999999-9999999999",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    operational_date: Optional[date] = Field(
        None,
        alias="operationalDate",
        name="Operational Date",
        description="The business date for the location. (Shows value when park is open after midnight)",
        example="2022-04-03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    operational_date_park_id: Optional[str] = Field(
        None,
        alias="operational_date-park_id",
        name="Operational Date Park ID",
        description="Concatenated value of other fields: <operationalDate>-<parkId>",
        example="1648958400-80007838",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    park_id: Optional[str] = Field(
        None,
        alias="parkId",
        name="Park ID",
        description="The Enterprise/One Source ID for the Park where the Experience is located",
        example="80007838",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_type: str = Field(
        ...,
        alias="productType",
        name="Product Type",
        description="Product type describes the type of lightning lane - EXT for Individual LL, FLX for Genie+ LL etc.",
        example="FLX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reason: str = Field(
        ...,
        alias="reason",
        name="Reason",
        description="Reason type describes how the LL entitlement was acquired - purchased (PUR), DAS etc.",
        example="PUR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    remaining_count: int = Field(
        ...,
        alias="remainingCount",
        name="Remaining Count",
        description="Remaining uses for the entitlement",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sector_name: Optional[str] = Field(
        None,
        alias="sectorName",
        name="Sector Name",
        description="The Sector of the inventory, only populated for INVENTORY type entitlements",
        example="GPLUS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="Status",
        description="Status of the entitlement - BOOKED, INQUEUE, REDEEMED, CANCELLED",
        example="CANCELLED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Shows whether the entitlement is associated to inventory or not. INVENTORY and NONINVENTORY have different attributes populated",
        example="INVENTORY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    update_user_id: str = Field(
        ...,
        alias="updateUserId",
        name="Update User ID",
        description="ID of the user that made the most recent update to the entitlement; this carries the Guest's SWID when update was made by the Guest",
        example="{AAA99999-A999-9999-A99A-9999999A999A}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    updated_date: datetime = Field(
        ...,
        alias="updatedDate",
        name="Updated Date",
        description="The date and time of the most recent update to the entitlement",
        example="2022-04-03T11:17:20.571026000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    uses_allowed: int = Field(
        ...,
        alias="usesAllowed",
        name="Uses Allowed",
        description="Number of uses allowed for the entitlement; always 1 for INVENTORY entitlements",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    window_override: bool = Field(
        ...,
        alias="windowOverride",
        name="Window Override",
        description="Indicate whether an override was requested by the calling service",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    das_primary_indicator: Optional[bool] = Field(
        None,
        alias="dasPrimaryIndicator",
        name="DAS Primary Indicator",
        description="Indicator of primary individual that availed Disability Access Service",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    experience_list: Optional[List[ExperienceListItem]] = Field(
        None,
        alias="experienceList",
        name="Experience List",
        description="List of experiences that the entitlement could be used at; populated only for non-inventory entitlements",
    )
    das_parent_entitlement_id: Optional[str] = Field(
        None,
        alias="dasParentEntitlementId",
        name="Disability Access Service Parent Entitlement ID",
        description="Identifier that points to the primary Guest that availed Disability Access Service",
        example="NONINVENTORY_ZZZZZZZZZZZZZZZZZZZZZZZ_999999999-9999-9999-9999-999999999999",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    item_id: Optional[str] = Field(
        None,
        alias="itemId",
        name="Item ID",
        description="Travelbox order item id",
        example="21145115#PBP#1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    order_id: Optional[str] = Field(
        None,
        alias="orderId",
        name="Order ID",
        description="Travelbox entitlement order id. Can be joined to travelbox data.",
        example="9z999z99-zz9z-99z9-9zzz-99999999zz99",
        guest_identifier=False,
        transaction_identifier=True,
        identifier_tag="Indirect",
    )
    passenger_id: Optional[str] = Field(
        None,
        alias="passengerId",
        name="Passenger ID",
        description="Travelbox Passenger ID",
        example="99999999-ZZZZ-9999-9999-999999999999",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    passenger_id_type: Optional[str] = Field(
        None,
        alias="passengerIdType",
        name="Passenger ID Type",
        description="TBX Passenger Id Type",
        example="xid",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_content_id: Optional[str] = Field(
        None,
        alias="productContentId",
        name="Product Content ID",
        description="Id used to map to policies/content",
        example="DSEPV1_DSETV1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    product_id: Optional[str] = Field(
        None,
        alias="productId",
        name="Product ID",
        description="Product ID",
        example="EP18375495EXARA12813",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    operational_date_park_id_product_type_status: Optional[str] = Field(
        None,
        alias="operational_date-park_id-product_type-status",
        name="Operational Date - Park ID - Product Type - Status",
        description="Concatenation of operational date, park ID, product type, and status",
        example="1648958400-80007944-NON-BOOKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gsr_code: Optional[str] = Field(
        None,
        alias="gsrCode",
        name="Guest Service Recovery Code",
        description="Guest service recovery code",
        example="96",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gsr_type: Optional[str] = Field(
        None,
        alias="gsrType",
        name="Guest Service Recovery Type",
        description="Guest service recovery type",
        example="SAMEDAY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    original_experience_id: Optional[str] = Field(
        None,
        alias="originalExperienceId",
        name="Original Experience ID",
        description="Original experience id of the experience that this entitlement substitutes for; applies to NONINVENTORY entitlements only",
        example="20041302",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    original_experience_type: Optional[str] = Field(
        None,
        alias="originalExperienceType",
        name="Original Experience Type",
        description="Original experience type of the experience that this entitlement substitutes for; applies to NONINVENTORY entitlements only",
        example="Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    original_create_date_time: Optional[datetime] = Field(
        None,
        alias="originalCreateDateTime",
        name="Original Create Date Time",
        description="The date and time of creation of the original entitlement",
        example="2023-05-08T07:01:50.366046015",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    original_entitlement_id: Optional[str] = Field(
        None,
        alias="originalEntitlementId",
        name="Original Entitlement ID",
        description="Concatenation of type, guestID, date etc.",
        example="1648958400-80007944-NON-BOOKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Item(BaseModel):
    """Data class that represents the EA event and entitlement details"""

    event_id: str = Field(
        ...,
        alias="eventID",
        name="Event ID",
        description="Unique identifier of EA event message",
        example="111112222233333aaaaaac12c517513a",  # pragma: allowlist secret
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_name: str = Field(
        ...,
        alias="eventName",
        name="Event Name",
        description="Describes the event action, whether the entitlement was created (INSERT) or modified (MODIFY)",
        example="INSERT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement: Entitlement = Field(
        ...,
        alias="entitlement",
        name="Entitlement",
        description="Entitlement details",
    )


class EAWDWLightningLaneModel(BaseModel):
    """Data class that represents the main EA WDW Lightning Lane payload"""

    class Config:
        """Payload level metatags"""

        title = "Experience Accelerator WDW Lightning Lane"
        stream_name = "guest360-wdw-lightning-lane-stream"
        description = "WDW Lightning Lane reservation and redemption data"
        unique_identifier = ["item.entitlement.enttlId"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""  # optional
        key_path_value = ""  # optional

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="Correlation ID",
        description="Internal identifier used for tracking across services",
        example="cccccccc-7777-aaaa-bbbb-111111f2862a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_type: str = Field(
        ...,
        alias="eventType",
        name="Event Type",
        description="Represents the GAM event type - IA_SYNC",
        example="IA_SYNC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    key: str = Field(
        ...,
        alias="key",
        name="Key",
        description="Internal value used as an item sort key",
        example="11111aa1a00000011aaaaa12a117513a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    item: Item = Field(
        ...,
        alias="item",
        name="Item",
        description="Main item payload of entitlement details",
    )
