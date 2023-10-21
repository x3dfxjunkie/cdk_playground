"""Source Data Contract for Dreams ACM CMPNT CHRNLGY"""

from __future__ import annotations
from datetime import datetime
from pydantic import Field, BaseModel
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsAcmTcId,
    GlobalDreamsMetadata,
    GlobalDreamsData,
)


# Any classes using (BaseModel) are net new classes, classes that have other classes inherited are calling those from Global Contract files to bring in fields already defined in another file.
# The class below inherits from the global_dreams_source_data_contract file listed above and uses the GlobalDreamsData and GlobalDreamsAcmTcId classes as base fields
class Data(GlobalDreamsData, GlobalDreamsAcmTcId):
    """Class for Dreams ACM CMPNT CHRNLGY Data"""

    acm_cmpnt_chrnlgy_id: int = Field(
        ...,
        alias="ACM_CMPNT_CHRNLGY_ID",
        name="Accommodation Component Chronology Identification",
        description="The unique identification for the sequence of date/time events that are expected to occur or have occurred in conjunction with an accommodation component.  Such sequences may include but are not constrained to date / time is recorded for the arrival, check in, departure of a guest to/from an accommodation component.",
        example=93930092,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    chrnlgcl_evt_typ_nm: str = Field(
        ...,
        alias="CHRNLGCL_EVT_TYP_NM",
        name="Chronological Event Type Name",
        description="The designation for the kind of date / time sequential events that may occur for the arrival, departure, check-in and check out to/from an accommodation component.  examples of such designations: Estimated Time of Arrival, Estimated Time of Departure, Actual Time, Pickup Date Time, Flight Arrival Date Time.  An accommodation component can be characterized by one or more kind of chronological event.",
        example="ETA",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    chrnlgcl_evt_src_nm: str = Field(
        ...,
        alias="CHRNLGCL_EVT_SRC_NM",
        name="Chronological Event Source Name",
        description="The designation for the source of a particular date time event.  The sources include but are not constrained to: Internet Pre-Arrival, Guest Reported, Disney Magical Express, Transit, Land.",
        example="OLCI",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    acm_cmpnt_dts: datetime = Field(
        ...,
        alias="ACM_CMPNT_DTS",
        name="Accommodation Component Datetime",
        description="The particular date time value for an accommodation component.  This value may represent and estimated arrival datetime, estimated departure datetime, etc.",
        example="2023-05-21T14:59:00Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class DREAMSRoomsFulfillmentAcmCmpntChrnlgyModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentAcmCmpntChrnlgyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Component Chronology"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table has the estimated time of arrival, depature, etc for the accommodation travel component provided by multiple sources. IE: OLCI- online check in, SECURITY_GATE, etc"  # optional
        unique_identifier = ["data.ACM_CMPNT_CHRNLGY_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "acm_cmpnt_chrnlgy"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
