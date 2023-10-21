"""Source Data Contract for Opera Update Model"""


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
        example="UPDATE RESERVATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_action_id: str = Field(
        ...,
        alias="ns2:ActionId",
        name="",
        description="",
        example="2.0099445E7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_primary_key: str = Field(
        ...,
        alias="ns2:PrimaryKey",
        name="",
        description="",
        example="1359679",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_publisher_id: str = Field(
        ...,
        alias="ns2:PublisherId",
        name="",
        description="",
        example="4596.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_created_date_time: datetime = Field(
        ...,
        alias="ns2:CreatedDateTime",
        name="",
        description="",
        example="2023-05-22T08:27:37",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_hotel_code: str = Field(
        ...,
        alias="ns2:HotelCode",
        name="",
        description="",
        example="DH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Ns2DetailItem(BaseModel):
    """Class for Detail Item object"""

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

    ns2_old_value: Optional[str] = Field(
        None,
        alias="ns2:OldValue",
        name="",
        description="",
        example="DLR-KATAS017@DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_new_value: Optional[str] = Field(
        None,
        alias="ns2:NewValue",
        name="",
        description="",
        example="DLR-KATAS017@DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_element_sequence: Optional[str] = Field(
        None,
        alias="ns2:ElementSequence",
        name="",
        description="",
        example="1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_element_type: Optional[str] = Field(
        None,
        alias="ns2:ElementType",
        name="",
        description="",
        example="CRSREFID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_scope_from: Optional[date] = Field(
        None,
        alias="ns2:ScopeFrom",
        name="",
        description="",
        example="2023-05-20",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ns2_scope_to: Optional[date] = Field(
        None,
        alias="ns2:ScopeTo",
        name="",
        description="",
        example="2023-05-21",
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


class OperaUpdateModel(BaseModel):
    """Payload class for OperaUpdateModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Update"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "OperaBusinessEvent.header.ns2:ActionType"
        key_path_value = "UPDATE RESERVATION"

    opera_business_event: OperaBusinessEvent = Field(
        ...,
        alias="OperaBusinessEvent",
        name="",
        description="",
    )
