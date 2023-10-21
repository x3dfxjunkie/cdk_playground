"""Source Data Contract for Dreams Resource Inventory Management Resource Inventory Type"""


from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2016-09-12T06:04:41Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_invtry_typ_cd: str = Field(
        ...,
        alias="RSRC_INVTRY_TYP_CD",
        name="",
        description="",
        example="1b457c93-a3b8-4330-9165-c82977d26ee6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_invtry_typ_id: int = Field(
        ...,
        alias="RSRC_INVTRY_TYP_ID",
        name="",
        description="",
        example=336200,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="SCHEDULE_EVENTS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcInvtryTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcInvtryTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Inventory Type"
        stream_name = ""
        description = "Inventory type code is associated to the reservable resource type"
        unique_identifier = ["data.RSRC_INVTRY_TYP_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_invtry_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
