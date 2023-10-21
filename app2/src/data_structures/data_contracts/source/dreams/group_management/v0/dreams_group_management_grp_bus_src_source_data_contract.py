"""Source Data Contract Template for Dreams GroupmanagementGroupbusinesssource"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_BUS_SRC data"""

    grp_bus_src_nm: str = Field(
        ...,
        alias="GRP_BUS_SRC_NM",
        name="",
        description="",
        example="Banquet",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpBusSrcModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpBusSrcModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Business Source"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.GRP_BUS_SRC_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_bus_src"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
