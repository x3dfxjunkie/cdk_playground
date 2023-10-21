"""Source Data Contract Template for Dreams GroupmanagementGroupprofileassociation"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_PRFL_ASSC data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-20T11:40:19Z",
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
        example="3417407870",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_prfl_assc_dglt_in: str = Field(
        ...,
        alias="GRP_PRFL_ASSC_DGLT_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_prfl_assc_grp_in: str = Field(
        ...,
        alias="GRP_PRFL_ASSC_GRP_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_prfl_assc_id: int = Field(
        ...,
        alias="GRP_PRFL_ASSC_ID",
        name="",
        description="",
        example=1,
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

    prfl_vl_id: int = Field(
        ...,
        alias="PRFL_VL_ID",
        name="",
        description="",
        example=148,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-13T05:28:50Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="",
        description="",
        example="G0524097",
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


class DREAMSGroupManagementGrpPrflAsscModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpPrflAsscModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Profile Association"
        stream_name = ""
        description = "Last Load 06/16/2015"
        unique_identifier = ["data.GRP_PRFL_ASSC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_prfl_assc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
