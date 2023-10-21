"""Source Data Contract Template for DREAMS Resource Inventory Management Campus Facility"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementCmpsFacModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementCmpsFacModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Campus Facility"
        stream_name = ""
        description = """This table associates a facility ID to its respective campus"""
        unique_identifier = ["data.FAC_ID", "data.CMPS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cmps_fac"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
