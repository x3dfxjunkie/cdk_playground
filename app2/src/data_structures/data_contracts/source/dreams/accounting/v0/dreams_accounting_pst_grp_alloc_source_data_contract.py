"""Source Data Contract for DREAMS Post Group Allocation"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Post Group Allocation Data"""

    pst_grp_alloc_id: int = Field(
        ...,
        alias="PST_GRP_ALLOC_ID",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_id: int = Field(
        ...,
        alias="PST_GRP_ID",
        name="",
        description="",
        example=1001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_acct_id: int = Field(
        ...,
        alias="PST_ACCT_ID",
        name="",
        description="",
        example=20001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_alloc_strt_dt: datetime = Field(
        ...,
        alias="PST_GRP_ALLOC_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_alloc_end_dt: datetime = Field(
        ...,
        alias="PST_GRP_ALLOC_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_alloc_ord_nb: int = Field(
        ...,
        alias="PST_GRP_ALLOC_ORD_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_alloc_pc: Optional[int] = Field(
        None,
        alias="PST_GRP_ALLOC_PC",
        name="",
        description="",
        example=100,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pst_grp_flat_alloc_am: Optional[str] = Field(
        None,
        alias="PST_GRP_FLAT_ALLOC_AM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    flat_am_crncy_cd: Optional[str] = Field(
        None,
        alias="FLAT_AM_CRNCY_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SC4_SS_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-03-02T02:43:57.314Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC4_SS_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-03-02T02:43:57.314Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingPstGrpAllocModel(BaseModel):
    """Payload class for DREAMSAccountingPstGrpAllocModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Post Group Allocation"
        stream_name = ""
        description = (
            """Post Group and Post Accounts associated to the allocation percentage for a specific time frame"""
        )
        unique_identifier = ["data.PST_GRP_ALLOC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PST_GRP_ALLOC"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
