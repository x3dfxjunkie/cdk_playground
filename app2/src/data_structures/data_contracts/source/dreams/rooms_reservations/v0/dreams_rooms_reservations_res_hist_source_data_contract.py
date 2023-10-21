"""Source Data Contract Template for Dreams - Room Reservation Reservation History"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservation Reservation History Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-25T16:32:48Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
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

    proc_dts: Optional[datetime] = Field(
        None,
        alias="PROC_DTS",
        name="",
        description="",
        example="2023-07-25T16:32:49Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_hist_id: int = Field(
        ...,
        alias="RES_HIST_ID",
        name="",
        description="",
        example=30041388155,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_hist_loc_nm: str = Field(
        ...,
        alias="RES_HIST_LOC_NM",
        name="",
        description="",
        example="DEFAULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_hist_proc_ds: str = Field(
        ...,
        alias="RES_HIST_PROC_DS",
        name="",
        description="",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    res_hist_tx: Optional[str] = Field(
        None,
        alias="RES_HIST_TX",
        name="",
        description="",
        example="07/25/23 16:32 PM,NA,Be Our Guest Restaurant,08/05/2023-08/05/2023,$0.0,953178701392",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_grp_nm: int = Field(
        ...,
        alias="TC_GRP_NM",
        name="",
        description="",
        example=653178432575,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: Optional[int] = Field(
        None,
        alias="TC_ID",
        name="",
        description="",
        example=32112156617,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="",
        description="",
        example=353178399670,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="",
        description="",
        example=953178701392,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-25T16:32:48Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
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


class DREAMSRoomsReservationsResHistModel(BaseModel):
    """Payload class for Dreams - Room Reservation Reservation History Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation History"
        stream_name = ""
        description = """This is a copy of the reservation history that is shown online, it is created by the source."""
        unique_identifier = ["data.RES_HIST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_hist"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
