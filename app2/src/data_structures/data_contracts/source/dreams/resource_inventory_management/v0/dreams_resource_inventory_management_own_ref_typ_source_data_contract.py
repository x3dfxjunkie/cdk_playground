"""Source Data Contract for Dreams Resource Inventory Management Feature Type"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:05:55Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    own_ref_typ_nm: str = Field(
        ...,
        alias="OWN_REF_TYP_NM",
        name="",
        description="",
        example="DPMS_RES_NUMBER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementOwnRefTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementOwnRefTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Owner Reference Type"
        stream_name = ""
        description = """List of owner reference types: OWN_REF_TYP_NM
FREEZE_ID
ORIGINAL_TC
TEAM_NM
SE_RSRC_NO
TC
TP
DPMS_RES_NUMBER
TPS
INVTRY_TRACKING_ID
INVENTORY_REQUEST
PARENT_ASGNT_OWN
DPMS_TC"""
        unique_identifier = ["data.OWN_REF_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "own_ref_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
