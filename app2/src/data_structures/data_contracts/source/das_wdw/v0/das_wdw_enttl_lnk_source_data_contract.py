"""Source Data Contract for DAS WDW enttl_lnk"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW enttl_lnk Data
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

    lnk_id: str = Field(
        ...,
        alias="LNK_ID",
        name="",
        description="",
        example="B3D19259F6484D84871ED8BF2996CA65",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_lnk_strt_dts: datetime = Field(
        ...,
        alias="ENTTL_LNK_STRT_DTS",
        name="",
        description="",
        example="2017-04-01 15:54:10",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_lnk_end_dts: Optional[datetime] = Field(
        None,
        alias="ENTTL_LNK_END_DTS",
        name="",
        description="",
        example="1972-08-30 22:11:31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gwd_rl: str = Field(
        ...,
        alias="GWD_RL",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    under3: str = Field(
        ...,
        alias="UNDER3",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hs_opt_out: str = Field(
        ...,
        alias="HS_OPT_OUT",
        name="",
        description="",
        example="N",
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
        example="1989-08-02 14:20:00",
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
        example="1989-08-28 00:38:40",
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


class DASWDWEnttlLnkModel(BaseModel):
    """
    Payload class for DAS WDW enttl_lnk
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Link"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = (
            "Linkage table that contains relationship between the DAS entitlement and the Guest ID."  # optional
        )
        unique_identifier = ["data.ENTTL_ID", "data.LNK_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "enttl_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
