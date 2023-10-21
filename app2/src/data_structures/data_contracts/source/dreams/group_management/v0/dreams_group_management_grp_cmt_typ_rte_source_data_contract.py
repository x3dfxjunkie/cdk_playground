"""Source Data Contract Template for Dreams GroupmanagementGroupcommenttyperoute"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams GRP_CMT_TYP_RTE data"""

    grp_cmt_lvl_nm: str = Field(
        ...,
        alias="GRP_CMT_LVL_NM",
        name="",
        description="",
        example="Group Profile",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_sect_nm: str = Field(
        ...,
        alias="GRP_CMT_SECT_NM",
        name="",
        description="",
        example="Billing Details",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_typ_nm: str = Field(
        ...,
        alias="GRP_CMT_TYP_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cmt_typ_rte_id: int = Field(
        ...,
        alias="GRP_CMT_TYP_RTE_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rte_nm: str = Field(
        ...,
        alias="RTE_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementGrpCmtTypRteModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpCmtTypRteModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group Comment Type Route"
        stream_name = ""
        description = "Child table of Group Comment"
        unique_identifier = ["data.GRP_CMT_TYP_RTE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp_cmt_typ_rte"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
