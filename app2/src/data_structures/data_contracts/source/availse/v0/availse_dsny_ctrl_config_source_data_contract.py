"""Source Data Contract Template for AvailSE - Disney Control Configuration"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Disney Control Configuration Data"""

    dsny_ctrl_config_id: str = Field(
        ...,
        alias="DSNY_CTRL_CONFIG_ID",
        name="",
        description="",
        example="aa11aa11-b8f5-4b5d-b33c-e8c8db257b4d",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_dt: Optional[datetime] = Field(
        None,
        alias="END_DT",
        name="",
        description="",
        example="2023-07-29T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_tm: datetime = Field(
        ...,
        alias="END_TM",
        name="",
        description="",
        example="1970-01-01T09:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_rtain_cn: int = Field(
        ...,
        alias="MAX_RTAIN_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-e71d-422b-9a36-41e1f6ecb828",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_dt: Optional[datetime] = Field(
        None,
        alias="STRT_DT",
        name="",
        description="",
        example="2023-07-16T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_tm: datetime = Field(
        ...,
        alias="STRT_TM",
        name="",
        description="",
        example="1970-01-01T09:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="fakeu002",
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


class AvailSEDsnyCtrlConfigModel(BaseModel):
    """Payload class for AvailSE - Disney Control Configuration Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Control Configuration"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.DSNY_CTRL_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dsny_ctrl_config"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
