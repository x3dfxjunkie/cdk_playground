"""Source Data Contract for Dreams Resource Inventory Management rsrt feat"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Resource Inventory Management data"""

    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=801,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrt_fac_id: int = Field(
        ...,
        alias="RSRT_FAC_ID",
        name="",
        description="",
        example=80010395,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrtFeatModel(BaseModel):
    """DREAMSResourceInventoryManagementRsrtFeatModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Dreams Resource Inventory Management Resort Feature"
        stream_name = ""
        description = "List of Feature IDs associated to Resort Facility IDs"  # optional
        unique_identifier = ["data.RSRT_FAC_ID", "data.FEAT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
