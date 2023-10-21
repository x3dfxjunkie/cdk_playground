"""Source Data Contract Template for DREAMS Group Stage"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Group Stage Data"""

    grp_stg_nm: str = Field(
        ...,
        alias="GRP_STG_NM",
        name="",
        description="",
        example="Cancelled",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpStgModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpStgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Stage"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.GRP_STG_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_stg"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
