"""Source Data Contract for DREAMS Group Management Group Link"""

from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Link Data"""

    prmy_grp_cd: str = Field(
        ...,
        alias="PRMY_GRP_CD",
        name="",
        description="",
        example="G0371058",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sec_grp_cd: str = Field(
        ...,
        alias="SEC_GRP_CD",
        name="",
        description="",
        example="G0512484",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpLnkModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpLnkModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Group Management Group Link"
        stream_name = ""
        description = "Last load 06-18-2019"
        unique_identifier = ["data.PRMY_GRP_CD", "data.SEC_GRP_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
