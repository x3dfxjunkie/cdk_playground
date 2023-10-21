"""Source Data Contract Template for Dreams GroupmanagementGroupcommentroute"""

from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_CMT_RTE data"""

    grp_cmt_id: int = Field(
        ...,
        alias="GRP_CMT_ID",
        name="",
        description="",
        example=3321,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_typ_rte_id: int = Field(
        ...,
        alias="GRP_CMT_TYP_RTE_ID",
        name="",
        description="",
        example=5,
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


class DREAMSGroupManagementGrpCmtRteModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpCmtRteModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Comment Route"
        stream_name = ""
        description = "Child table of Group Comment"
        unique_identifier = ["data.GRP_CMT_ID", "data.GRP_CMT_TYP_RTE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_cmt_rte"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
