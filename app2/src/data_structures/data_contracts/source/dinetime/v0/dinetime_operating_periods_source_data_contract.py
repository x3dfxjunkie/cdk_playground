"""Source Data Contract for dinetime-operatingperiods"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


class OperatingPeriodItem(BaseModel):
    """OperatingPeriodItem Class"""

    iid: int = Field(
        ...,
        alias="IID",
        name="Integer Identifier",
        description="Operation period integer identifier ",
        example=123456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    session: str = Field(
        ...,
        alias="Session",
        name="Session Name",
        description="Name of the session record",
        example="Lunch",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="Status",
        name="Operating Period Status",
        description="Operating status of the operating period. The following are considered accepted values: ‘Open’, ‘Closed’ and ‘Unknown’",
        example="Open",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_time: datetime = Field(
        ...,
        alias="StartTime",
        name="Operating Period Start Time",
        description="Start time in ISO 8601 format",
        example="2023-05-17T10:45:00+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_time: datetime = Field(
        ...,
        alias="EndTime",
        name="Operating Period End Time",
        description="End time in ISO 8601 format",
        example="2023-05-17T16:00:00+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    creation_time: datetime = Field(
        ...,
        alias="CreationTime",
        name="Operating Period Creation Type",
        description="Creation time in ISO 8601 format",
        example="2022-08-01T19:06:01+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_update: datetime = Field(
        ...,
        alias="LastUpdate",
        name="Operating Period Last Update",
        description="The date/time of the most recent change/update to the resource datapoint",
        example="2022-08-01T19:06:01+00:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DineTimeOperatingPeriodsModel(BaseModel):
    """DineTimeOperatingPeriodsModel Class"""

    class Config:
        """Payload Level Metadata"""

        title = "Dinetime Operating Period Model"
        stream_name = "guest360-dinetime-teammember-event-stream"
        description = "Dinetime Operating Period Model"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    operating_period: List[OperatingPeriodItem] = Field(
        ...,
        alias="OperatingPeriod",
        name="Operating Period",
        description="Operating period list that contains breakfast, lunch, and dinner details.",
    )
    site_id: str = Field(
        ...,
        alias="SiteId",
        name="Operating Period Site Identifier",
        description="Globally unique identifier of the site",
        example="99999999-8b88-4ff3-b4bc-a9754f01ab4c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
