"""Source Data Contract Template for DREAMS Resource Inventory Management Resource Assignment Owner"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime


class Data(BaseModel):
    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=98305,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_ownr_typ_nm: str = Field(
        ...,
        alias="ASGN_OWNR_TYP_NM",
        name="",
        description="",
        example="INVENTORY_REQUEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-10-13T05:25:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    dvc_res_typ_nm: Optional[str] = Field(
        None,
        alias="DVC_RES_TYP_NM",
        name="",
        description="",
        example="OUT_OF_ORDER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80010408,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guar_in: str = Field(
        ...,
        alias="GUAR_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ownr_end_dts: datetime = Field(
        ...,
        alias="OWNR_END_DTS",
        name="",
        description="",
        example="2007-08-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ownr_rsrt_trfr_in: str = Field(
        ...,
        alias="OWNR_RSRT_TRFR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ownr_strt_dts: datetime = Field(
        ...,
        alias="OWNR_STRT_DTS",
        name="",
        description="",
        example="2007-08-19T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ownr_sts_nm: str = Field(
        ...,
        alias="OWNR_STS_NM",
        name="",
        description="",
        example="COMPLETED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_typ_id: int = Field(
        ...,
        alias="RSRC_INVTRY_TYP_ID",
        name="",
        description="",
        example=68,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    spcl_need_req_in: str = Field(
        ...,
        alias="SPCL_NEED_REQ_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-10-13T05:25:22Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    vip_in: str = Field(
        ...,
        alias="VIP_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    whsl_in: str = Field(
        ...,
        alias="WHSL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_asgn_ownr_id: Optional[int] = Field(
        None,
        alias="PRNT_ASGN_OWNR_ID",
        name="",
        description="",
        example=268610796,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    eff_rt_ctgy_nm: Optional[str] = Field(
        None,
        alias="EFF_RT_CTGY_NM",
        name="",
        description="",
        example="SP1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_asgn_rsrc_id: Optional[int] = Field(
        None,
        alias="AUTO_ASGN_RSRC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="",
        description="",
        example="04528",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_id_vl: Optional[str] = Field(
        None,
        alias="GRP_ID_VL",
        name="",
        description="",
        example="1111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_own_lnk_id: Optional[int] = Field(
        None,
        alias="DVC_OWN_LNK_ID",
        name="",
        description="",
        example=20204039,
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


class DREAMSResourceInventoryManagementRsrcAsgnOwnrModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcAsgnOwnrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Assignment Owner"
        stream_name = ""
        description = """This table assigns the owner to a room type indicated by the resource inventory type ID"""
        unique_identifier = ["data.ASGN_OWNR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_asgn_ownr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
