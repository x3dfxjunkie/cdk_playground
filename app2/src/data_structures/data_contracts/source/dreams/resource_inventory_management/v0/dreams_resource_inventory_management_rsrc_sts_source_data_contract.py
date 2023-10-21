"""Source Data Contract for Dreams Resource Inventory Management RSRC STS"""


from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-12-15T07:52:18Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DPMS CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=11761,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=25540,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_invtry_sts_id: int = Field(
        ...,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_sts_id: int = Field(
        ...,
        alias="RSRC_STS_ID",
        name="",
        description="",
        example=2485346,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-15T11:27:21.324000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="RexRmUpdts-a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcStsModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcStsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Status"
        stream_name = ""
        description = "This table associates resources and resource inventory IDs to a resource status ID"
        unique_identifier = ["data.RSRC_STS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_sts"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
