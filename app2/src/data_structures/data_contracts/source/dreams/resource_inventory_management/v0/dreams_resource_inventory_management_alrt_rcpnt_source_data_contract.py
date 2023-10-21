"""Source Data Contract Template for DREAMS Resource Inventory Management Alert Component"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    alrt_rcpnt_id: int = Field(
        ...,
        alias="ALRT_RCPNT_ID",
        name="",
        description="",
        example=20001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    alrt_rcpnt_rl_nm: str = Field(
        ...,
        alias="ALRT_RCPNT_RL_NM",
        name="",
        description="",
        example="HOUSEKEEPING_MANAGER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_id: int = Field(
        ...,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=15132,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementAlrtRcpntModel(BaseModel):
    """Payload class forDREAMSResourceInventoryManagementAlrtRcpntModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Alert Recipient"
        stream_name = ""
        description = """This table identifies the recipients of alerts regarding the resource inventory status. The recipients:
HOUSEKEEPING_MANAGER
RESORT_MANAGER
ROOM_ASSIGNER"""
        unique_identifier = ["data.ALRT_RCPNT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "alrt_rcpnt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
