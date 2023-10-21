"""Source Data Contract Template for DREAMS Resource Inventory Management Resource Inventory Status"""


from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2018-03-28T10:39:53.299000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_srvc_req_in: str = Field(
        ...,
        alias="CREATE_SRVC_REQ_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ALFAJ005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dflt_dy_cn: int = Field(
        ...,
        alias="DFLT_DY_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dflt_hr_cn: int = Field(
        ...,
        alias="DFLT_HR_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_typ_nm: Optional[str] = Field(
        None,
        alias="INVTRY_REQ_TYP_NM",
        name="",
        description="",
        example="OUT_OF_INVENTORY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_id: int = Field(
        ...,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=43400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_strt_dts: datetime = Field(
        ...,
        alias="RSRC_INVTRY_STS_STRT_DTS",
        name="",
        description="",
        example="2018-03-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_typ_nm: str = Field(
        ...,
        alias="RSRC_INVTRY_STS_TYP_NM",
        name="",
        description="",
        example="INVENTORY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sts_ds: str = Field(
        ...,
        alias="STS_DS",
        name="",
        description="",
        example="Planned Maintenance",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sts_nm: str = Field(
        ...,
        alias="STS_NM",
        name="",
        description="",
        example="Planned Maintenance",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2018-07-23T08:55:04.820000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="EDSER001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_end_dts: Optional[datetime] = Field(
        None,
        alias="RSRC_INVTRY_STS_END_DTS",
        name="",
        description="",
        example="2023-01-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcInvtryStsModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcInvtryStsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Inventory Status"
        stream_name = ""
        description = """Provides the status and description for rooms put on closed floor or out of inventory"""
        unique_identifier = ["data.RSRC_INVTRY_STS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_invtry_sts"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
