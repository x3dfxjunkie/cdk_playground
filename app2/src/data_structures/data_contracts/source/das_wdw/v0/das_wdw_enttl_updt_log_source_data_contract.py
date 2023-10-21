"""Source Data Contract for DAS WDW enttl_updt_log"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for XiDas enttl_updt_log Data
    """

    log_id: int = Field(
        ...,
        alias="LOG_ID",
        name="",
        description="",
        example=1000001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    correlation_id: Optional[str] = Field(
        None,
        alias="CORRELATION_ID",
        name="",
        description="",
        example="e6088cca-eb4a-446d-868e-36a5294f99a2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    req_timestamp: Optional[datetime] = Field(
        None,
        alias="REQ_TIMESTAMP",
        name="",
        description="",
        example="2018-04-12 12:29:37",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cst_id: Optional[str] = Field(
        None,
        alias="CST_ID",
        name="",
        description="",
        example="kFYGVJXgDKLQgIzxwxMy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_id: Optional[str] = Field(
        None,
        alias="GST_ID",
        name="",
        description="",
        example="nztwLWdaUghQRuaEniUH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cip: Optional[str] = Field(
        None,
        alias="CIP",
        name="",
        description="",
        example="hbzoigSOdntyshKxtczs",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sys_id: Optional[str] = Field(
        None,
        alias="SYS_ID",
        name="",
        description="",
        example="ryhELvimOscCirdRfCdt",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    orgn_sys_id: Optional[str] = Field(
        None,
        alias="ORGN_SYS_ID",
        name="",
        description="",
        example="UYokjYZWhTcVQeNeTDeJ",
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
        example="2004-08-21 11:27:22",
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
        example="2015-05-16 21:36:07",
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


class DASWDWEnttlUpdtLogModel(BaseModel):
    """
    Payload class for DAS WDW enttl_updt_log
    """

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Update Log"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = (
            "Audit table that logs which cast member users updated/created which DAS entitlements."  # optional
        )
        unique_identifier = ["data.LOG_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "enttl_updt_log"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
