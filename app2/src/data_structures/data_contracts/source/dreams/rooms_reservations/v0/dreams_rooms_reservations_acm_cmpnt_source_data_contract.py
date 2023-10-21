"""Source Data Contract for Dreams - Room Reservation Accommodation Component"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservation Accommodation Component Data"""

    acm_tc_id: int = Field(
        ...,
        alias="ACM_TC_ID",
        name="",
        description="",
        example=12099680261,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bus_nb: Optional[str] = Field(
        None,
        alias="BUS_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-12T16:48:10.360000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="5435081.2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_res_typ_nm: str = Field(
        ...,
        alias="DVC_RES_TYP_NM",
        name="",
        description="",
        example="Member Points",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lt_chkot_in: str = Field(
        ...,
        alias="LT_CHKOT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    onst_phn_nb: Optional[str] = Field(
        None,
        alias="ONST_PHN_NB",
        name="",
        description="",
        example="8439071064",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[str] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    shr_in: str = Field(
        ...,
        alias="SHR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    spcl_need_req_in: str = Field(
        ...,
        alias="SPCL_NEED_REQ_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trms_cndtns_vers_nb: Optional[str] = Field(
        None,
        alias="TRMS_CNDTNS_VERS_NB",
        name="",
        description="",
        example="11.27.2012_4_1.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-21T19:48:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="5435081.2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsAcmCmpntModel(BaseModel):
    """Payload class for Dreams - Room Reservation Accommodation Component Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Component "
        stream_name = ""
        description = """This table contains only Accommodation components and it provides indicators for rooms with a Late Check Out, Special Need Request, or a room that have more than one reservation associated to that room, a sharewith.  This table also provides the Disney Vacation Club reservation type for each accommodation ie: Non Member Cash Member Points Member Non Discounted Cash Member Discounted Cash"""
        unique_identifier = ["data.ACM_TC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "acm_cmpnt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
