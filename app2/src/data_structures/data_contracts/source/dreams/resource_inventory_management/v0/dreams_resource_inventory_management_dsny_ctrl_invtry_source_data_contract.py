"""Source Data Contract Template for DREAMS Resource Inventory Management Disney Controlled Inventory"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=345398004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dsny_ctrl_invtry_in: Optional[str] = Field(
        None,
        alias="DSNY_CTRL_INVTRY_IN",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementDsnyCtrlInvtryModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementDsnyCtrlInvtryModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Controlled Inventory"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.ASGN_OWNR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dsny_ctrl_invtry"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
