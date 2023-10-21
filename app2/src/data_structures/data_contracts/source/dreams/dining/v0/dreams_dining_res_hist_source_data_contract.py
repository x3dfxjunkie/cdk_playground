"""Source Data Contract for Dreams Dining Reservation History"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
    GlobalDreamsTpId,
    GlobalDreamsTpsId,
    GlobalDreamsTcId,
    GlobalDreamsData,
)


class Data(GlobalDreamsTpId, GlobalDreamsTpsId, GlobalDreamsTcId, GlobalDreamsData):
    """Class for Dreams Dining Reservation History Data"""

    res_hist_id: int = Field(
        ...,
        alias="RES_HIST_ID",
        name="Reservation History Identification",
        description="",
        example=99926885356,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_hist_loc_nm: str = Field(
        ...,
        alias="RES_HIST_LOC_NM",
        name="Reservation History Location Name",
        description="The designation for the location where the reservation occurred",
        example="DEFAULT",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_grp_nm: int = Field(
        ...,
        alias="TC_GRP_NM",
        name="Travel Component Group Name",
        description="The travel component grouping for a particular reservation.",
        example=999073647223,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_hist_tx: str = Field(
        ...,
        alias="RES_HIST_TX",
        name="Reservation History Text",
        description="The reservation history as a character large object.",
        example="03/30/23 19:46 PM,NA,Steakhouse 71,04/14/2023-04/14/2023,$0.0,953073075150",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    res_hist_proc_ds: str = Field(
        ...,
        alias="RES_HIST_PROC_DS",
        name="",
        description="Narrative about the process for the reservation history",
        example="Booked",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    proc_dts: datetime = Field(
        ...,
        alias="PROC_DTS",
        name="Processed Date",
        description="The month day century and year hour minute and second when the reservation was processed.",
        example="2023-03-30T19:46:27Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
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


class DREAMSDiningResHistModel(BaseModel):
    """Payload class for DREAMSDiningResHistModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation History"
        stream_name = ""
        description = """This is a copy of the reservation history that is shown online, it is created by the source."""
        unique_identifier = ["data.RES_HIST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_hist"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
