"""Source Data Contract Template for Dreams GroupmanagementGroupcomment"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_CMT data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-20T11:41:58Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CRSRDC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0471231",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_id: int = Field(
        ...,
        alias="GRP_CMT_ID",
        name="",
        description="",
        example=3442,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_tx: str = Field(
        ...,
        alias="GRP_CMT_TX",
        name="",
        description="",
        example="2006 CRSR DATA CONVERSION",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-20T11:41:58Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CRSRDC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cmt_fr_gst_tx: Optional[str] = Field(
        None,
        alias="GRP_CMT_FR_GST_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cmt_to_gst_tx: Optional[str] = Field(
        None,
        alias="GRP_CMT_TO_GST_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpCmtModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpCmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Comment"
        stream_name = ""
        description = "Last loaded 9/02/2019"
        unique_identifier = ["data.GRP_CMT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_cmt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
