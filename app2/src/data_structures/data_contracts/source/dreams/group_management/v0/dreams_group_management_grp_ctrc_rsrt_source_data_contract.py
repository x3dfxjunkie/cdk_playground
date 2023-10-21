"""Source Data Contract Template for Dreams GroupmanagementGrpctrcrsrt"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_CTRC_RSRT data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-25T10:06:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM008",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="Z060001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_addl_adlt_rt_tx: Optional[str] = Field(
        None,
        alias="GRP_CTRC_RSRT_ADDL_ADLT_RT_TX",
        name="",
        description="",
        example="0.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_end_dt: Optional[datetime] = Field(
        None,
        alias="GRP_CTRC_RSRT_END_DT",
        name="",
        description="",
        example="2006-11-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_id: int = Field(
        ...,
        alias="GRP_CTRC_RSRT_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_nm_tx: Optional[str] = Field(
        None,
        alias="GRP_CTRC_RSRT_NM_TX",
        name="",
        description="",
        example="Boardwalk INn",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_pkg_tx: Optional[str] = Field(
        None,
        alias="GRP_CTRC_RSRT_PKG_TX",
        name="",
        description="",
        example="BOB",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_rm_typ_tx: Optional[str] = Field(
        None,
        alias="GRP_CTRC_RSRT_RM_TYP_TX",
        name="",
        description="",
        example="IA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_rt_tx: Optional[str] = Field(
        None,
        alias="GRP_CTRC_RSRT_RT_TX",
        name="",
        description="",
        example="234.00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_ctrc_rsrt_strt_dt: Optional[datetime] = Field(
        None,
        alias="GRP_CTRC_RSRT_STRT_DT",
        name="",
        description="",
        example="2006-11-18T00:00:00Z",
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

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2006-11-18T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-25T10:06:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM008",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpCtrcRsrtModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpCtrcRsrtModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = "Last load 07/10/2017"
        unique_identifier = ["data.GRP_CTRC_RSRT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_ctrc_rsrt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
