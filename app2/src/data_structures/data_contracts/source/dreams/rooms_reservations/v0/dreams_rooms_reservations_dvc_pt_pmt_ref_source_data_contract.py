"""Source Data Contract for Dreams - Room Reservations Disney Vacation Club Points Payment Reference"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservations Disney Vacation Club Points Payment Reference data"""

    acm_tc_id: int = Field(
        ...,
        alias="ACM_TC_ID",
        name="",
        description="",
        example=12097600580,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-21T13:25:21.783000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="24443.2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_pt_pmt_ref_id: int = Field(
        ...,
        alias="DVC_PT_PMT_REF_ID",
        name="",
        description="",
        example=129648353,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_pt_pmt_ref_vl: str = Field(
        ...,
        alias="DVC_PT_PMT_REF_VL",
        name="",
        description="",
        example="I:3379532.1",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-21T13:25:21.783000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="24443.2",
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


class DREAMSRoomsReservationsDvcPtPmtRefModel(BaseModel):
    """Payload class for Dreams - Room Reservations Disney Vacation Club Points Payment Reference Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Vacation Club Points Payment reference"
        stream_name = ""
        description = "If a reservation is booked using Disney Vacation Club points, this table is populated with a value that references the guest points account."
        unique_identifier = ["data.DVC_PT_PMT_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dvc_pt_pmt_ref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
