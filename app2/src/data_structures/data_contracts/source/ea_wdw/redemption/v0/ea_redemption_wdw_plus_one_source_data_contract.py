"""Source Data Contract for EA Redemption PLUS ONE"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class PlusOne(BaseModel):
    """
    Class For EA PLUS_ONE PlusOne Data
    """

    date_time: datetime = Field(
        ...,
        alias="dateTime",
        name="DateTime",
        description="Local time when the plus one occurred",
        example="2023-07-25T13:28:04",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    number_of_guests: int = Field(
        ...,
        alias="numberOfGuests",
        name="Number Of Guests",
        description="Number of Guests added",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    show_start_date_time: datetime = Field(
        ...,
        alias="showStartDateTime",
        name="Show Start DateTime",
        description="Optional - Local Show time",
        example="2023-07-25T14:30:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Item(BaseModel):
    """
    Class For EA PLUS_ONE Item Data
    """

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="Correlation ID",
        description="",
        example="b65ccea7-2ac3-40fb-9ff2-7053b066a48f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    experience_id: str = Field(
        ...,
        alias="experienceId",
        name="Experience ID",
        description="The experience id  where the plus one occured",
        example="12432",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    location_id: str = Field(
        ...,
        alias="locationId",
        name="Location ID",
        description="The location id  where the plus one occured",
        example="17920702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plus_one: PlusOne = Field(
        ...,
        alias="plusOne",
        name="Plus One",
        description="",
    )

    publish_key: str = Field(
        ...,
        alias="publishKey",
        name="Publish Key",
        description="",
        example="17920702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redemption_event_type: str = Field(
        ...,
        alias="redemptionEventType",
        name="Redemption Event Type",
        description="Redemption event type",
        example="PLUS_ONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EARedemptionWDWPlusOneModel(BaseModel):
    """
    Payload class for EARedemptionWDWPlusOneModel
    """

    class Config:
        """Payload Level Metadata"""

        title = "Plus One"
        stream_name = "prd-use1-guest360-ea-stream"
        description = "Provides all events for plus one overrides that are performed by a Cast Member at a touch point. A plus one is when a Cast Member allows the Guest who taps their media to also bring in additional Guests such as a family or friend."  # optional
        unique_identifier = ["correlationId"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "item.redemptionEventType"
        key_path_value = "PLUS_ONE"

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="Correlation ID",
        description="",
        example="b65ccea7-2ac3-40fb-9ff2-7053b066a48f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    event_type: str = Field(
        ...,
        alias="eventType",
        name="Event Type",
        description="",
        example="REDEMPTION_REPORTING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    item: Item = Field(
        ...,
        alias="item",
        name="Item",
        description="",
    )

    key: str = Field(
        ...,
        alias="key",
        name="Key",
        description="",
        example="17920702",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
