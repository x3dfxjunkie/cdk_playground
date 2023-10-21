"""Source Data Contract for DREAMS Group Management Group Party Role"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Group Management Group Party Role Data"""

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="R220740",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pty_id: int = Field(
        ...,
        alias="PTY_ID",
        name="",
        description="",
        example=12345678,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rl_nm: str = Field(
        ...,
        alias="RL_NM",
        name="",
        description="",
        example="Primary Contact",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_pty_rl_dflt_trvl_agcy_in: str = Field(
        ...,
        alias="GRP_PTY_RL_DFLT_TRVL_AGCY_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_pty_rl_strt_dts: Optional[datetime] = Field(
        None,
        alias="GRP_PTY_RL_STRT_DTS",
        name="",
        description="",
        example="2023-07-13T23:04:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_pty_rl_end_dts: Optional[datetime] = Field(
        None,
        alias="GRP_PTY_RL_END_DTS",
        name="",
        description="",
        example="2023-07-13T23:04:29Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-22T12:23:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="BROWK340",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-22T12:23:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="BROWK340",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_cls_nb: int = Field(
        ...,
        alias="JDO_CLS_NB",
        name="",
        description="",
        example=11,
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


class DREAMSGroupManagementGrpPtyRlModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpPtyRlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Group Management Group Party Role"
        stream_name = ""
        description = "This table associates a Group Code to a Party ID by role type, ie: Primary Contact, Speaker, etc"
        unique_identifier = ["data.GRP_CD", "data.PTY_ID", "data.RL_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_pty_rl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
