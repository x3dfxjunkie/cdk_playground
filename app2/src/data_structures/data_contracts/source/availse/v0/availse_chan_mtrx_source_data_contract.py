"""Source Data Contract Template for AvailSE - Channel Matrix"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Channel Matrix Data"""

    chan_mtrx_end_dt: Optional[str] = Field(
        None,
        alias="CHAN_MTRX_END_DT",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chan_mtrx_freeze_exp_td: int = Field(
        ...,
        alias="CHAN_MTRX_FREEZE_EXP_TD",
        name="",
        description="",
        example=60,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chan_mtrx_id: str = Field(
        ...,
        alias="CHAN_MTRX_ID",
        name="",
        description="",
        example="aa11aa11-7e54-e501-fa44-ab6a11feac65",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chan_mtrx_strt_dt: datetime = Field(
        ...,
        alias="CHAN_MTRX_STRT_DT",
        name="",
        description="",
        example="2022-06-13T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    comnctn_chan_id: int = Field(
        ...,
        alias="COMNCTN_CHAN_ID",
        name="",
        description="",
        example=13,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-b36a-8dc7-b433-e24472c44adc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: str = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="0001-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    version_sn: int = Field(
        ...,
        alias="VERSION_SN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEChanMtrxModel(BaseModel):
    """Payload class for AvailSE - Channel Matrix Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Channel Matrix"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.CHAN_MTRX_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "chan_mtrx"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
