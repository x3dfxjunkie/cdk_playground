"""Source Data Contract Template for CME DLR Reservation Merge Bck"""

from __future__ import annotations
from datetime import datetime, date
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    age_group: str = Field(
        ...,
        alias="age_group",
        name="",
        description="",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_updated_dts: datetime = Field(
        ...,
        alias="auto_updated_dts",
        name="",
        description="",
        example="2021-11-07T16:11:56.997Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    booking_category: Optional[str] = Field(
        None,
        alias="booking_category",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    conf_id: int = Field(
        ...,
        alias="conf_id",
        name="",
        description="",
        example=123456789123456781,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_dts: datetime = Field(
        ...,
        alias="created_dts",
        name="",
        description="",
        example="2021-09-08T12:33:35.599Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="",
        description="",
        example="f-cme-reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entitlement_expiration: Optional[str] = Field(
        None,
        alias="entitlement_expiration",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exp_date: date = Field(
        ...,
        alias="exp_date",
        name="",
        description="",
        example="2022-02-22",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exp_park: str = Field(
        ...,
        alias="exp_park",
        name="",
        description="",
        example="WDW_AK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exp_slot: str = Field(
        ...,
        alias="exp_slot",
        name="",
        description="",
        example="DAILY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    external_res_id: Optional[int] = Field(
        None,
        alias="external_res_id",
        name="",
        description="",
        example=1234567891,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_email_id: str = Field(
        ...,
        alias="guest_email_id",
        name="",
        description="",
        example="mickey.mouse@disney.com",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_first_name: str = Field(
        ...,
        alias="guest_first_name",
        name="",
        description="",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_last_name: str = Field(
        ...,
        alias="guest_last_name",
        name="",
        description="",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    guest_phone_number: Optional[str] = Field(
        None,
        alias="guest_phone_number",
        name="",
        description="",
        example="",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    inv_bucket_id: str = Field(
        ...,
        alias="inv_bucket_id",
        name="",
        description="",
        example="WDW_AK_AP_DAILY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    or_classification: Optional[str] = Field(
        None,
        alias="or_classification",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    product_id: str = Field(
        ...,
        alias="product_id",
        name="",
        description="",
        example="WDW_AP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    redemption_dts: Optional[datetime] = Field(
        None,
        alias="redemption_dts",
        name="",
        description="",
        example="2022-02-05T10:07:35Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_id: int = Field(
        ...,
        alias="res_id",
        name="",
        description="",
        example=123456789123456789,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_origin: str = Field(
        ...,
        alias="res_origin",
        name="",
        description="",
        example="WEB-TICKETS-PASSES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_status: str = Field(
        ...,
        alias="res_status",
        name="",
        description="",
        example="CANCELED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_ticket_sku: str = Field(
        ...,
        alias="res_ticket_sku",
        name="",
        description="",
        example="N2VA5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    resort_res_id: Optional[int] = Field(
        None,
        alias="resort_res_id",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    show_last_four: int = Field(
        ...,
        alias="show_last_four",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    slot_start_dts: datetime = Field(
        ...,
        alias="slot_start_dts",
        name="",
        description="",
        example="2022-02-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    survey_responder: Optional[str] = Field(
        None,
        alias="survey_responder",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    survey_response: Optional[str] = Field(
        None,
        alias="survey_response",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    survey_response_dts: Optional[datetime] = Field(
        None,
        alias="survey_response_dts",
        name="",
        description="",
        example="2021-10-10T16:52:31Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    survey_sent: int = Field(
        ...,
        alias="survey_sent",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    swid: str = Field(
        ...,
        alias="swid",
        name="",
        description="",
        example="{8C13F0A5-AAAA-BBBB-CCCC-0008C7330D17}",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_visual_id: int = Field(
        ...,
        alias="tkt_visual_id",
        name="",
        description="",
        example=12345678912345678,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_dts: datetime = Field(
        ...,
        alias="updated_dts",
        name="",
        description="",
        example="2021-10-10T16:52:31Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updated_usr: Optional[str] = Field(
        None,
        alias="updated_usr",
        name="",
        description="",
        example="f-cme-reservation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    was_inv_override: int = Field(
        ...,
        alias="was_inv_override",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRReservationMergeBckModel(BaseModel):
    """Payload class for CME DLR Reservation Merge Bck Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Merge Back"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "reservation_merge_bck"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
