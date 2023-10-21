"""Source Data Contract for Dreams TC GRP"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Dreams TC GRP Data"""

    tc_grp_nb: int = Field(
        ...,
        alias="TC_GRP_NB",
        name="Travel Component Group Number",
        description="A unique sequential numeric identifier for a Travel Component Grouping.",
        example=530892012034,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=True,
    )

    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="Travel Plan Segment Identification",
        description="A unique numeric identifier for a travel plan segment.",
        example=530891946412,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=True,
    )

    comnctn_chan_id: int = Field(
        ...,
        alias="COMNCTN_CHAN_ID",
        name="Communication Channel Identification",
        description="A unique sequential numeric identifier for a Communication Channel.",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )

    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="Sales Channel Identification",
        description="A unique sequential numeric identifier for a Communication Channel.",
        example=1,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )

    tc_grp_typ_nm: Optional[str] = Field(
        None,
        alias="TC_GRP_TYP_NM",
        name="Travel Component Group Type Name",
        description="The designation for the kind of travel component grouping",
        example="",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )

    adv_internt_chkin_in: str = Field(
        ...,
        alias="ADV_INTERNT_CHKIN_IN",
        name="Advance Internet Checkin Indicator",
        description="Identifies that a grouping of travel components is (Y) or is not (N) from an advance internet checkin.  Default setting is N, the grouping of travel components is not (N) from advance internet checkin.",
        example="ACCOMMODATION",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    add_on_tc_grp_nb: Optional[int] = Field(
        None,
        alias="ADD_ON_TC_GRP_NB",
        name="",
        description="",
        example=453062248322,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTcGrpModel(BaseModel):
    """Payload class for DREAMSRoomsReservationTcGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Group"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table ties together the reservation/package components and it also ties to the reservation information"
        unique_identifier = ["data.TC_GRP_NB"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_grp"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
