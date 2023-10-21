"""Source Data Contract for Dreams TC GST"""
from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Data(GlobalDreamsTcId, GlobalDreamsData):
    """Class for Dreams TC GST Data"""

    tc_gst_id: int = Field(
        ...,
        alias="TC_GST_ID",
        name="Travel Component Guest Identification",
        description="The unique identification for the association of a guest to a travel component.",
        example=30349560682,
        guest_identifier=True,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    vst_prps_nm: Optional[str] = Field(
        None,
        alias="VST_PRPS_NM",
        name="Visit Preference Name",
        description="The business name describing why a guest is staying with us.",
        example="Leisure",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    txn_idvl_pty_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_PTY_ID",
        name="Transaction Individual Party Identification",
        description="The identification of the transactional individual who is identified to this travel component.",
        example=744174032,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    txn_pty_rl_id: Optional[int] = Field(
        None,
        alias="TXN_PTY_RL_ID",
        name="",
        description="",
        example=756502774,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_mbrshp_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_MBRSHP_ID",
        name="",
        description="",
        example=756502774,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="Age Type Name",
        description="The designation for a grouping of ages.",
        example="ADULT",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    age_nb: Optional[int] = Field(
        None,
        alias="AGE_NB",
        name="Age Number",
        description="The chronological age of the travel component guest.",
        example=65,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
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
    incognito: Optional[str] = Field(
        None,
        alias="incognito",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTcGstModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsTcGstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Guest"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides the age type and age number for the guests associated to that travel component, as well as the transactional individual ID and the visit purpose."
        unique_identifier = ["data.TC_GST_ID"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_gst"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
