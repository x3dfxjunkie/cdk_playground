"""Source Data Contract for Dreams Resource Inventory Management rsrc own ref"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-15T15:44:59.249000Z",
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
    extnl_own_ref_val: str = Field(
        ...,
        alias="EXTNL_OWN_REF_VAL",
        name="",
        description="",
        example="530671198501",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    own_ref_typ_nm: str = Field(
        ...,
        alias="OWN_REF_TYP_NM",
        name="",
        description="",
        example="TP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-15T15:44:59.249000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsrc_own_id: int = Field(
        ...,
        alias="RSRC_OWN_ID",
        name="",
        description="",
        example=309090806,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcOwnRefModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcOwnRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Owner Reference"
        stream_name = ""
        description = """This table connects resource owner to the reservation IDs:
TP
TPS
TC"""
        unique_identifier = ["data.RSRC_OWN_ID", "data.EXTNL_OWN_REF_VAL"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_own_ref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
