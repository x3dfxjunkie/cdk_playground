"""Source Data Contract Template for DREAMS Resource Inventory Management Disney Vacation Club Room Type Cross Reference"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    dvc_rm_typ_xref_id: int = Field(
        ...,
        alias="DVC_RM_TYP_XREF_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_rsrc_invtry_typ_cd: str = Field(
        ...,
        alias="DVC_RSRC_INVTRY_TYP_CD",
        name="",
        description="",
        example="4A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_rsrt_fac_id: int = Field(
        ...,
        alias="DVC_RSRT_FAC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_typ_cd: str = Field(
        ...,
        alias="RSRC_INVTRY_TYP_CD",
        name="",
        description="",
        example="4A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementDvcRmTypXrefModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementDvcRmTypXrefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Vacation Club Room Type Cross Reference"
        stream_name = ""
        description = (
            """This table maps the Disney Vacation Club room type codes to the resource inventory room type codes"""
        )
        unique_identifier = ["data.DVC_RM_TYP_XREF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dvc_rm_typ_xref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
