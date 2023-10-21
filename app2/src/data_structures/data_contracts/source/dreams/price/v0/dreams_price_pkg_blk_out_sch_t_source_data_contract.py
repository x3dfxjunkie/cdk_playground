"""Source Data Contract for Dreams Price Package Block Out Schedule"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Price Package Block Out Schedule Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2007-10-29T12:23:01.210800Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
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

    pkg_blk_out_sch_end_dt: datetime = Field(
        ...,
        alias="PKG_BLK_OUT_SCH_END_DT",
        name="",
        description="",
        example="2007-12-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_blk_out_sch_strt_dt: datetime = Field(
        ...,
        alias="PKG_BLK_OUT_SCH_STRT_DT",
        name="",
        description="",
        example="2007-11-18T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pkg_id: int = Field(
        ...,
        alias="PKG_ID",
        name="",
        description="",
        example=23503,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2007-10-29T12:23:01.210800Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: Optional[str] = Field(
        None,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePkgBlkOutSchTModel(BaseModel):
    """Payload class for DREAMSPricePkgBlkOutSchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Package Block Out Schedule"
        stream_name = ""
        description = "This table provides the dates that a specific package is not available for booking"  # optional
        unique_identifier = ["data.PKG_ID", "data.PKG_BLK_OUT_SCH_STRT_DT"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PKG_BLK_OUT_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
