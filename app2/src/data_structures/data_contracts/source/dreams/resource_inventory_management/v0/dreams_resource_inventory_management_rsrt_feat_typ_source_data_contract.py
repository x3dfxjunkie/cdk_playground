"""Source Data Contract Template for DREAMS Resource Inventory Management Resort Feature Type"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    feat_typ_nm: str = Field(
        ...,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="Bedding",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_fac_id: int = Field(
        ...,
        alias="RSRT_FAC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrtFeatTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrtFeatTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort Feature Type"
        stream_name = ""
        description = """List of Feature type names associated to Resort Facility IDs"""
        unique_identifier = ["data.FEAT_TYP_NM", "data.RSRT_FAC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_feat_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
