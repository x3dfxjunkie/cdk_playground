"""Source Data Contract for DAS WDW lnk_assc"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.das_wdw.global_das_wdw_source_data_contract import (
    GlobalDASWDWMetadata,
)


class Data(BaseModel):
    """
    Class for DAS WDW lnk_assc Data
    """

    actv_lnk_id: str = Field(
        ...,
        alias="ACTV_LNK_ID",
        name="",
        description="",
        example="35EB87F1C8574940ACE9221A9230D614",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mergd_lnk_id: str = Field(
        ...,
        alias="MERGD_LNK_ID",
        name="",
        description="",
        example="73D44E7BC937444C9C8BD0EDE74BBF1E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mergd_lnk_dts: datetime = Field(
        ...,
        alias="MERGD_LNK_DTS",
        name="",
        description="",
        example="2007-03-26 13:22:21",
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
        example="1999-05-02 20:46:43",
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
        example="1997-04-05 13:21:53",
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


class DASWDWLnkAsscModel(BaseModel):
    """
    Payload class for DAS WDW lnk_assc
    """

    class Config:
        """Payload Level Metadata"""

        title = "Link Association"
        stream_name = "prd-use1-guest360-das-wdw-stream"
        description = "Table to track when links are merged in DAS."  # optional
        unique_identifier = ["data.ACTV_LNK_ID", "data.MERGD_LNK_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "lnk_assc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDASWDWMetadata = Field(..., alias="metadata")
