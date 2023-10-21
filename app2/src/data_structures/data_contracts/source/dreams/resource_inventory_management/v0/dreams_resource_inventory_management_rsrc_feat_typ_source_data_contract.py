"""Source Data Contract Template for DREAMS Resource Inventory Management Resource Feature Type"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    feat_typ_nm: str = Field(
        ...,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="Side",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="ROOM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcFeatTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcFeatTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Feature Type"
        stream_name = ""
        description = """List of Room Feature types"""
        unique_identifier = ["data.FEAT_TYP_NM", "data.RSRC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_feat_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
