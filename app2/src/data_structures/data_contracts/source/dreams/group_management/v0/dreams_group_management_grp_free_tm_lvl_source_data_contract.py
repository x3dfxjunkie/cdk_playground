"""Source Data Contract Template for Dreams GroupmanagementGroupfreetimelevel"""
from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_FREE_TM_LVL data"""

    grp_free_tm_lvl_nm: str = Field(
        ...,
        alias="GRP_FREE_TM_LVL_NM",
        name="",
        description="",
        example="High",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpFreeTmLvlModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpFreeTmLvlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Free Time Level"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.GRP_FREE_TM_LVL_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_free_tm_lvl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
