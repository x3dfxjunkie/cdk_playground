"""Source Data Contract for Dreams Resource Inventory Management Resort"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
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

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-11-21T00:07:18.832032Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrtModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resort"
        stream_name = ""
        description = "List of Resort (Enterprise) Facility IDs"
        unique_identifier = ["data.RSRT_FAC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
