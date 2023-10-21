"""Source Data Contract Template for DREAMS Resource Inventory Management Resort Room Ready Configuration"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2019-04-15T08:19:07.719000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_id: int = Field(
        ...,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=8,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_fac_id: int = Field(
        ...,
        alias="RSRT_FAC_ID",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrtRmRdyConfigModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrtRmRdyConfigModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort Room Ready Configuration"
        stream_name = ""
        description = """Resort Facility IDs"""
        unique_identifier = ["data.RSRT_FAC_ID", "data.RSRC_INVTRY_STS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt_rm_rdy_config"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
