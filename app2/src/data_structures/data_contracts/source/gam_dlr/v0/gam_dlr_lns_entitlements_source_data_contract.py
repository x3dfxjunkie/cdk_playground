"""Source Data Contract for GAM DLR LNS Entitlements"""
from __future__ import annotations

# from enum import Enum
from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel, Field


class ExternalReferences(BaseModel):
    """ExternalReferences Class"""

    titus_order_id: Optional[str] = Field(
        None,
        alias="titus-order-id",
        name="Titus Order Identifier",
        description="Titus Order Identifier",
        example="1f93a0c9-e3ae-59ed-000a-b84e59a2b6cf",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    titus_entitlement_id: Optional[str] = Field(
        None,
        alias="titus-entitlement-id",
        name="Titus Entitlement Identifier",
        description="Titus Entitlement Identifier",
        example="1fcdb9c5-33b2-0000-9cbb-db8dccdf8923",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    ticket_visual_id: Optional[str] = Field(
        None,
        alias="ticket-visual-id",
        name="Ticket Visual Identifier",
        description="Ticket Visual Identifier",
        example="1066368765616627700000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class ExternalIdentifier(BaseModel):
    """ExternalIdentifier Class"""

    id: Optional[str] = Field(
        None,
        alias="id",
        name="Identifier",
        description="Value of external identifier type",
        example="707440401052091320000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Type of external identifier",
        example="ticket-visual-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Guest(BaseModel):
    """Guest Class"""

    external_identifiers: List[ExternalIdentifier] = Field(
        ...,
        alias="externalIdentifiers",
        name="External Identifiers",
        description="List of external identifiers",
    )
    fulfillment_status: List[str] = Field(
        ...,
        alias="fulfillmentStatus",
        name="Fulfillment Status",
        description="List of fulfillment status",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    leveln_link_id: Optional[str] = Field(
        None,
        alias="levelnLinkId",
        name="Level N Link Identifier",
        description="Level N Link Identifier",
        example="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    relationship: List[str] = Field(
        ...,
        alias="relationship",
        name="Relationship",
        description="List of relationship",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EligibilityDate(BaseModel):
    """EligibilityDate Class"""

    eligibility_end_date: Optional[datetime] = Field(
        None,
        alias="eligibilityEndDate",
        name="Eligibility End Date",
        description="Eligibility End Date",
        example="2023-04-29T06:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    eligibility_start_date: Optional[datetime] = Field(
        None,
        alias="eligibilityStartDate",
        name="Eligibility Start Date",
        description="Eligibility Start Date",
        example="2023-04-28T07:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Constraint(BaseModel):
    """Constraint Class"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Type of constraint",
        example="THEME_PARK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    values: Optional[List[str]] = Field(
        None,
        alias="values",
        name="Values",
        description="Constraint values",
        example=["330339"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Feature(BaseModel):
    """Feature Class"""

    constraints: List[Constraint] = Field(
        ...,
        alias="constraints",
        name="Constraints",
        description="List of constraints",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    eligibility_dates: List[EligibilityDate] = Field(
        ...,
        alias="eligibilityDates",
        name="Eligibility Dates",
        description="List of eligibility dates",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Type of Features on Level N Products",
        example="EXPERIENCE_ACCESS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNProduct(BaseModel):
    """LevelNProduct Class"""

    constraints: List[Constraint] = Field(
        ...,
        alias="constraints",
        name="Constraints",
        description="Constraints",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    features: List[Feature] = Field(
        ...,
        alias="features",
        name="Features",
        description="Features",
    )
    id: Optional[str] = Field(
        None,
        alias="id",
        name="Identifier",
        description="Identifier of Level N Products",
        example="DDSDBDLEXABDL10000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Type of Level N Products",
        example="GeniePlus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class NativeGuestId(BaseModel):
    """NativeGuestId Class"""

    type: Optional[str] = Field(
        None,
        alias="type",
        name="Type",
        description="Type of native guest identifier",
        example="leveln-link-id",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: Optional[str] = Field(
        None,
        alias="value",
        name="Value",
        description="Value of native guest identifier",
        example="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )


class GAMDLRLnsEntitlementsModel(BaseModel):
    """GAMDLRLnsEntitlementsModel Class"""

    class Config:
        """Payload Level Metatags"""

        title = "GAM DLR LNS Entitlements"
        stream_name = "gam-kinesis-gam-lns-entitlements-guest360-dlr"
        description = """DLR Guest LevelN entitlements"""
        unique_identifier = ["entitlementID", "nativeGuestIds.type", "nativeGuestIds.value"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "type"
        key_path_value = "LevelN Entitlement"

    action: str = Field(
        ...,
        alias="action",
        name="Event Action",
        description="Describes whether the entitlement type was created, modified, deleted",
        example="CREATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    actual_expiration_date_time: Optional[datetime] = Field(
        None,
        alias="actualExpirationDateTime",
        name="Actual Expiration Date Time",
        description="Actual Expiration Date Time is deprecated",
        example="2020-12-12T20:20:20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    capture_date: Optional[date] = Field(
        None,
        alias="captureDate",
        name="Capture Date",
        description="Capture date of the entitlement will be present in the response only after redemption of the entitlement",
        example="2023-04-19",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date: Optional[datetime] = Field(
        None,
        alias="endDate",
        name="End Date",
        description="Timestamp of entitlement end date",
        example="2023-04-29T06:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time: Optional[datetime] = Field(
        None,
        alias="endDateTime",
        name="End Date Time",
        description="Timestamp of entitlement end date",
        example="2023-04-29T06:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    enterprise_product_id: Optional[str] = Field(
        None,
        alias="enterpriseProductID",
        name="Enterprise Product Identifier",
        description="The enterprise product ID value",
        example="GeniePlus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entitlement_id: Optional[str] = Field(
        None,
        alias="entitlementID",
        name="Entitlement Identifier",
        description="The value of entitlement ID",
        example="786500000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    entitlement_type: Optional[str] = Field(
        None,
        alias="entitlementType",
        name="Entitlement Type",
        description="The type(s) of the entitlement(s). Currently supported values are on 'List of Possible Values For Level N Entitlement Fields'. One or more values can be provided by comma separated. If no value is provided, all entitlements assigned to the guest that are satisfying other criteria will be returned.",
        example="GeniePlus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    expiration_date: Optional[date] = Field(
        None,
        alias="expirationDate",
        name="Expiration Date",
        description="Expiration Date is deprecated",
        example="2020-12-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    external_references: Optional[ExternalReferences] = Field(
        None,
        alias="externalReferences",
        name="External References",
        description="External References",
    )
    guests: Optional[List[Guest]] = Field(
        None,
        alias="guests",
        name="Guests",
        description="Contains guest's external IDs, fulfillment status, level N link ID and relationship",
    )
    issue_type: Optional[str] = Field(
        None,
        alias="issueType",
        name="Issue Type",
        description="Issue Type",
        example="standard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    level_n_products: Optional[List[LevelNProduct]] = Field(
        None,
        alias="levelNProducts",
        name="Level N Products",
        description="Level N Products",
    )
    maximum_quantity: Optional[str] = Field(
        None,
        alias="maximumQuantity",
        name="Maximum Quantity",
        description="Maximum Quantity",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    minimum_quantity: Optional[str] = Field(
        None,
        alias="minimumQuantity",
        name="Minimum Quantity",
        description="Minimum Quantity",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    native_guest_ids: List[NativeGuestId] = Field(
        ...,
        alias="nativeGuestIds",
        name="Native Guest Identifiers",
        description="Native Guest ID type and value - leveln-link-id",
    )
    online_engagement_date_time: Optional[datetime] = Field(
        None,
        alias="onlineEngagementDateTime",
        name="Online Engagement Date Time",
        description="Online engagement data time entitlement will be present in the response only after claim of the entitlement",
        example="2020-12-20T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    override_guest_count: Optional[str] = Field(
        None,
        alias="overrideGuestCount",
        name="Override Guest Count",
        description="Override Guest Count",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    planned_arrival_date: Optional[date] = Field(
        None,
        alias="plannedArrivalDate",
        name="Planned Arrival Date",
        description="Planned Arrival Date is deprecated",
        example="2020-12-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    purchase_date_time: Optional[datetime] = Field(
        None,
        alias="purchaseDateTime",
        name="Purchase Date Time",
        description="Purchase Date Time",
        example="2023-04-28T04:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    reason: Optional[str] = Field(
        None,
        alias="reason",
        name="Reason",
        description="Reason",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    redemption_date: Optional[date] = Field(
        None,
        alias="redemptionDate",
        name="Redemption Date",
        description="Redemption date of the entitlement will be present in the response only after redemption of the entitlement",
        example="2023-04-19",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    resort_reservation_end_date: Optional[datetime] = Field(
        None,
        alias="resortReservationEndDate",
        name="Resort Reservation End Date",
        description="Resort Reservation End Date",
        example="2023-04-29T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    resort_reservation_start_date: Optional[datetime] = Field(
        None,
        alias="resortReservationStartDate",
        name="Resort Reservation Start Date",
        description="Resort Reservation Start Date",
        example="2023-04-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sales_price: Optional[str] = Field(
        None,
        alias="salesPrice",
        name="Sales Price",
        description="Sales Price",
        example="75.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sales_tax: Optional[str] = Field(
        None,
        alias="salesTax",
        name="Sales Tax",
        description="Sales Tax",
        example="0.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settlement_date: Optional[date] = Field(
        None,
        alias="settlementDate",
        name="Settlement Date",
        description="Settlement Date",
        example="2020-12-12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sites: Optional[List[str]] = Field(
        None,
        alias="sites",
        name="Sites",
        description="Comma separated site value(s). Default is WDW. If site value is WDW, leveln memory maker & geniePlus entitlements (if include-genie is also specified) will be retrieved. If site value is DLR, DLR leveln memory maker entitlements created through MAGENTO will be retrieved.",
        example=["example"],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    source: Optional[str] = Field(
        None,
        alias="source",
        name="Source",
        description="The source attribute will be one of DREAMS, SNAPP, TITUS or TMS, representing the source Level N Status received the entitlement from",
        example="TITUS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date: Optional[datetime] = Field(
        None,
        alias="startDate",
        name="Start Date",
        description="Start Date",
        example="2023-04-28T15:30:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time: Optional[datetime] = Field(
        None,
        alias="startDateTime",
        name="Start Date Time",
        description="Start date time of the entitlement will be present in the response only after claim of the entitlement",
        example="2023-04-28T15:30:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: Optional[str] = Field(
        None,
        alias="status",
        name="Status",
        description="For Genie+ entitlements, the valid entitlement status values are: active,consumed. Consumed is valid as the guest will still be eligible for AR+ benefits after the entitlement end date. Values of created,reserved can be passed in, but no Genie+ entitlement should be using those status values. For MemoryMaker entitlements, the valid entitlement status values are: active,created,reserved. Consumed here would indicate that the entitlement end date has passed, and the batch job has updated it accordingly; there should be no on-going MM benefit.",
        example="active",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    timestamp: Optional[datetime] = Field(
        None,
        alias="timestamp",
        name="Timestamp",
        description="Timestamp",
        example="2023-04-28T19:35:58.390Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    type: str = Field(
        ...,
        alias="type",
        name="Event Type",
        description="Represents the GAM event name - always LevelN Entitlement",
        example="LevelN Entitlement",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
