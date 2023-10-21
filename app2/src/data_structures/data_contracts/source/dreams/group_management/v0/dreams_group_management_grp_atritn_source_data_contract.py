"""Source Data Contract for Dreams Group Management Group Attrition"""
from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Attrition Data"""

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0358445",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_atritn_dy_cn: int = Field(
        ...,
        alias="GRP_ATRITN_DY_CN",
        name="",
        description="",
        example=60,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_atritn_dt: datetime = Field(
        ...,
        alias="GRP_ATRITN_DT",
        name="",
        description="",
        example="2021-04-27T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_atritn_pc: float = Field(
        ...,
        alias="GRP_ATRITN_PC",
        name="",
        description="",
        example=5.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_atritn_tx: str = Field(
        ...,
        alias="GRP_ATRITN_TX",
        name="",
        description="",
        example="allowable room drop",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-04-27T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="mouse001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2021-04-27T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="mouse001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
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


class DREAMSGroupManagementGrpAtritnModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpAtritnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Attrition"
        stream_name = ""
        description = "Last Load 11/01/2020"
        unique_identifier = ["data.GRP_CD", "data.GRP_ATRITN_DY_CN"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_atritn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
