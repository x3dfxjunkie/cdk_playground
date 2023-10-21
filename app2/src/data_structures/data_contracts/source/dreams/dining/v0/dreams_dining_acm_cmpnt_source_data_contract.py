"""Source Data Contract for Dreams ACM CMPNT"""

from __future__ import annotations
from pydantic import Field, BaseModel
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsAcmTcId,
    GlobalDreamsData,
    GlobalDreamsMetadata,
)
from typing import Optional


# Any classes using (BaseModel) are net new classes, classes that have other classes inherited are calling those from Global Contract files to bring in fields already defined in another file.
# The class below inherits from the global_dreams_source_data_contract file listed above and uses the GlobalDreamsData and GlobalDreamsAcmTcId classes as base fields
class Data(GlobalDreamsData, GlobalDreamsAcmTcId):
    """Class for Dreams ACM CMPNT Data"""

    dvc_res_typ_nm: str = Field(
        ...,
        alias="DVC_RES_TYP_NM",
        name="Disney Vacation Club Reservation Type Name",
        description="The designation for the kind of Disney Vacation Club reservation.  It can be (Disney Collection, Exchange In, Exchange Out, Members Point, Non Member Cash, Member Discounted Cash",
        example="Non Member Cash",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trms_cndtns_vers_nb: Optional[str] = Field(
        None,
        alias="TRMS_CNDTNS_VERS_NB",
        name="Terms Conditions Version Number",
        description="Version number of the terms and conditions card the guest electronically accepted when completing the internet pre-arrival process.",
        example="11.27.2012_4_1.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    onst_phn_nb: Optional[str] = Field(
        None,
        alias="ONST_PHN_NB",
        name="Onsite Phone Number",
        description="Local area contact phone number for the primary guest on the travel plan segment",
        example="7654652998",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    shr_in: str = Field(
        ...,
        alias="SHR_IN",
        name="Share Indicator",
        description="Identifies that an accommodation component is (Y) or is not (N) shared by another guest.  The default setting is N, the accommodation component is not shared by another guest.",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    lt_chkot_in: str = Field(
        ...,
        alias="LT_CHKOT_IN",
        name="Late Check Out Indicator",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    spcl_need_req_in: str = Field(
        ...,
        alias="SPCL_NEED_REQ_IN",
        name="Special Need Requested Indicator",
        description="Records the fact a guest requested a room that has been labeled accordingly to American Disabilities Act regulations.",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[str] = Field(
        None,
        alias="REV_CLS_ID",
        name="Revenue Classification Identification",
        description="The unique identifier of Revenue Classification.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bus_nb: Optional[str] = Field(
        None,
        alias="BUS_NB",
        name="",
        description="",
        example="3210",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningAcmCmpntModel(BaseModel):
    """Payload class for DREAMSDiningAcmCmpntModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Component "
        stream_name = "guest360-dreams-resm-stream"
        description = "This table contains only Accommodation components and it provides indicators for rooms with a Late Check Out, Special Need Request, or a room that have more than one reservation associated to that room, a sharewith. This table also provides the Disney Vacation Club reservation type for each accommodation ie: Non Member Cash; Member Points; Member Non Discounted Cash; Member Discounted Cash)"  # optional
        unique_identifier = ["data.ACM_TC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "acm_cmpnt"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
