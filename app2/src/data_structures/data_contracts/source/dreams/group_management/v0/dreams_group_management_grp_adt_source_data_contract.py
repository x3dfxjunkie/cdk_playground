"""Source Data Contract for Dreams Group Management Group Audit"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Audit Data"""

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0833187",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="updt_dts",
        name="",
        description="",
        example="2023-07-12T09:52:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_stg_nm: str = Field(
        ...,
        alias="GRP_STG_NM",
        name="",
        description="",
        example="Definite",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="BARRL055",
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


class DREAMSGroupManagementGrpAdtModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpAdtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Audit"
        stream_name = ""
        description = """This table ties the Group Code to the Stage the Group is in : GRP_STG_NM
                        Checked Out
                        In-House
                        Cancelled
                        Tentative
                        Definite"""  # optional
        unique_identifier = ["data.GRP_CD", "data.updt_dts"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_adt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
