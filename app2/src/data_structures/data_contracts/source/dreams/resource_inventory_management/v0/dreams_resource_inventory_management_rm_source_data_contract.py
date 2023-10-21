"""Source Data Contract Template for RM.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    cntn_in: str = Field(
        ...,
        alias="CNTN_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-06-10T03:49:15.055885Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DM_SWGS",
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

    linen_chng_intrvl_nb: Optional[int] = Field(
        None,
        alias="LINEN_CHNG_INTRVL_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lkoff_rsrc_id: Optional[int] = Field(
        None,
        alias="LKOFF_RSRC_ID",
        name="",
        description="",
        example=24581,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_adlt_ocpncy_cn: Optional[int] = Field(
        None,
        alias="MAX_ADLT_OCPNCY_CN",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_ds: Optional[str] = Field(
        None,
        alias="RM_DS",
        name="",
        description="",
        example="Standard Cabin",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_end_dt: Optional[datetime] = Field(
        None,
        alias="RM_END_DT",
        name="",
        description="",
        example="2022-11-18T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_id_vl: str = Field(
        ...,
        alias="RM_ID_VL",
        name="",
        description="",
        example="4128",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_nm: Optional[str] = Field(
        None,
        alias="RM_NM",
        name="",
        description="",
        example="4128",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_phn_nb_vl: Optional[str] = Field(
        None,
        alias="RM_PHN_NB_VL",
        name="",
        description="",
        example="4128",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_strt_dt: datetime = Field(
        ...,
        alias="RM_STRT_DT",
        name="",
        description="",
        example="2021-06-10T03:49:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=89331,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_typ_id: int = Field(
        ...,
        alias="RSRC_INVTRY_TYP_ID",
        name="",
        description="",
        example=389202,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_fac_id: int = Field(
        ...,
        alias="RSRT_FAC_ID",
        name="",
        description="",
        example=19295309,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tot_ocpncy_cn: Optional[int] = Field(
        None,
        alias="TOT_OCPNCY_CN",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2021-06-10T03:49:15.055885Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DM_SWGS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRmModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRmModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Room"
        stream_name = ""
        description = """This table ties the reservable resource ID to a physical room at the resorts"""
        unique_identifier = ["data.RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rm"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
