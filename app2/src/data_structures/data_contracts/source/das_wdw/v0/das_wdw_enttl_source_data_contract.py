"""Source Data Contract for DAS WDW enttl"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW enttl Data
    """

    enttl_id: int = Field(
        ...,
        alias="ENTTL_ID",
        name="",
        description="",
        example=10001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_strt_dts: datetime = Field(
        ...,
        alias="ENTTL_STRT_DTS",
        name="",
        description="",
        example="1976-04-30 02:05:42",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_end_dts: datetime = Field(
        ...,
        alias="ENTTL_END_DTS",
        name="",
        description="",
        example="1972-06-22 00:28:56",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tnc_ver: str = Field(
        ...,
        alias="TNC_VER",
        name="",
        description="",
        example="0.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_fp_booking: Optional[int] = Field(
        None,
        alias="MAX_FP_BOOKING",
        name="",
        description="",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2000-06-04 07:18:14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="DASAPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="1977-12-21 02:08:44",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lgcl_del_in: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    site: str = Field(
        ...,
        alias="SITE",
        name="",
        description="",
        example="WDW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DASWDWEnttlModel(BaseModel):
    """
    Payload class for DAS WDW Enttl
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = "Records attributes about the entitlement that is created when a Guest enrolls themselves and their party into the Disability Access Program such as the start and end dates, number of bookings allowed, and creation time."  # optional
        unique_identifier = ["data.ENTTL_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "enttl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
