"""Source Data Contract for Dreams Entitlement Plan External Reference"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Entitlement Plan External Reference Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-17T11:27:07.699000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_extnl_src_nm: str = Field(
        ...,
        alias="ENTTL_EXTNL_SRC_NM",
        name="",
        description="",
        example="DREAMS_TC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_extnl_src_ref_vl: str = Field(
        ...,
        alias="ENTTL_EXTNL_SRC_REF_VL",
        name="",
        description="",
        example="11111111894",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_ext_ref_typ_nm: str = Field(
        ...,
        alias="ENTTL_EXT_REF_TYP_NM",
        name="",
        description="",
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_plan_ext_ref_id: int = Field(
        ...,
        alias="ENTTL_PLAN_EXT_REF_ID",
        name="",
        description="",
        example=111111410,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_id: int = Field(
        ...,
        alias="ENTTL_PLN_ID",
        name="",
        description="",
        example=11111102,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsEnttlPlnExtRefTModel(BaseModel):
    """Payload class for DREAMSEntitlementsEnttlPlnExtRefTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Plan External Reference"
        stream_name = ""
        description = """This table ties the external reference from Reservation Management to the Entitlement Plan based on: ENTTL_EXT_REF_TYP_NM
        Facility
        Room
        Travel Plan
        Travel Component Grouping
        and
        ENTTL_EXTNL_SRC_NM
        DREAMS_TC
        DREAMS_TCG
        DREAMS_TP
        FACILITY_ID
        ROOM"""
        unique_identifier = ["data.ENTTL_PLAN_EXT_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_PLN_EXT_REF_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
