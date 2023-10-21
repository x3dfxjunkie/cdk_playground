"""Source Data Contract for Opera New Model"""

from __future__ import annotations
from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel, Field


class Header(BaseModel):
    """Class for header object"""

    ns2_module_name: str = Field(
        ...,
        alias="ns2:ModuleName",
        name="",
        description="",
        example="RESERVATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_action_type: str = Field(
        ...,
        alias="ns2:ActionType",
        name="",
        description="",
        example="NEW RESERVATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_action_id: str = Field(
        ...,
        alias="ns2:ActionId",
        name="",
        description="",
        example="2.010198E7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_primary_key: str = Field(
        ...,
        alias="ns2:PrimaryKey",
        name="",
        description="",
        example="1360803",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_publisher_id: str = Field(
        ...,
        alias="ns2:PublisherId",
        name="",
        description="",
        example="4856.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_created_date_time: datetime = Field(
        ...,
        alias="ns2:CreatedDateTime",
        name="",
        description="",
        example="2023-05-23T15:34:03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_hotel_code: str = Field(
        ...,
        alias="ns2:HotelCode",
        name="",
        description="",
        example="DV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Ns2DetailItem(BaseModel):
    """Class for Detail item object"""

    ns2_data_element: str = Field(
        ...,
        alias="ns2:DataElement",
        name="",
        description="",
        example="USER NAME",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_new_value: Optional[str] = Field(
        None,
        alias="ns2:NewValue",
        name="",
        description="",
        example="DLR-SANIN004@DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_scope_from: Optional[date] = Field(
        None,
        alias="ns2:ScopeFrom",
        name="",
        description="",
        example="2023-05-23",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_scope_to: Optional[date] = Field(
        None,
        alias="ns2:ScopeTo",
        name="",
        description="",
        example="2023-05-24",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Details(BaseModel):
    """Class for Details object"""

    ns2_detail: List[Ns2DetailItem] = Field(
        ...,
        alias="ns2:Detail",
        name="",
        description="",
    )


class OperaBusinessEvent(BaseModel):
    """Class for Opera Business Event object"""

    field_xmlns_ns2: str = Field(
        ...,
        alias="@xmlns:ns2",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    header: Header = Field(
        ...,
        alias="header",
        name="",
        description="",
    )

    details: Details = Field(
        ...,
        alias="details",
        name="",
        description="",
    )


class OperaNewModel(BaseModel):
    """Payload class for OperaNewModel"""

    class Config:
        """Payload Level Metadata"""

        title = "New"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "OperaBusinessEvent.header.ns2:ActionType"
        key_path_value = "NEW RESERVATION"

    opera_business_event: OperaBusinessEvent = Field(
        ...,
        alias="OperaBusinessEvent",
        name="",
        description="",
    )
