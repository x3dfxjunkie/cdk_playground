"""Source Data Contract Template for DREAMS Group Confirmation Destination"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Group Confirmation Destination Data"""

    grp_cnfirm_dest_nm: str = Field(
        ...,
        alias="GRP_CNFIRM_DEST_NM",
        name="",
        description="",
        example="External",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpCnfirmDestModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpCnfirmDestModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Confirmation Destination"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.GRP_CNFIRM_DEST_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_cnfirm_dest"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
