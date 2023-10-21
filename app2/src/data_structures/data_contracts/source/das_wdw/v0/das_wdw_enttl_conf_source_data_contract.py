"""Source Data Contract for DAS WDW enttl_conf"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW enttl_conf Data
    """

    conf_nm: str = Field(
        ...,
        alias="CONF_NM",
        name="",
        description="",
        example="ENTTL_DEFAULT_DURATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    conf_ds: Optional[str] = Field(
        None,
        alias="CONF_DS",
        name="",
        description="",
        example="Entitlement default duration in days",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    conf_val: str = Field(
        ...,
        alias="CONF_VAL",
        name="",
        description="",
        example="60",
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
        example="1982-10-07 02:11:20",
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
        example="2017-03-30 14:45:12",
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


class DASWDWEnttlConfModel(BaseModel):
    """
    Payload class for DAS WDW enttl_conf
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Configuration"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = (
            "Reference table on configuration short names and their descriptions for the DAS entitlements."  # optional
        )
        unique_identifier = ["data.CONF_NM"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "enttl_conf"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
