"""Source Data Contract Template for AvailSE - Resort Guest Hold Block Configuration"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Resort Guest Hold Block Configuration Data"""

    end_dt: Optional[datetime] = Field(
        None,
        alias="END_DT",
        name="",
        description="",
        example="2024-12-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_tm: datetime = Field(
        ...,
        alias="END_TM",
        name="",
        description="",
        example="1970-01-01T20:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrps_fac_id: int = Field(
        ...,
        alias="ENTRPS_FAC_ID",
        name="",
        description="",
        example=90001548,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_gst_hldbck_config_id: str = Field(
        ...,
        alias="RSRT_GST_HLDBCK_CONFIG_ID",
        name="",
        description="",
        example="aa11aa11-21bc-6e63-1c68-7d2c3cd2638f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_gst_hldbck_pct: float = Field(
        ...,
        alias="RSRT_GST_HLDBCK_PCT",
        name="",
        description="",
        example=0.2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_dt: Optional[datetime] = Field(
        None,
        alias="STRT_DT",
        name="",
        description="",
        example="2023-08-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    strt_tm: datetime = Field(
        ...,
        alias="STRT_TM",
        name="",
        description="",
        example="1970-01-01T18:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU773",
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


class AvailSERsrtGstHldbckConfigModel(BaseModel):
    """Payload class for AvailSE - Resort Guest Hold Block Configuration Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort Guest Hold Block Configuration"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRT_GST_HLDBCK_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_gst_hldbck_config"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
