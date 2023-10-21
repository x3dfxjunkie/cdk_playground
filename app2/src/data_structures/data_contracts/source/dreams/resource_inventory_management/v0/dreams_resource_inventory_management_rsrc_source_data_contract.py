"""Source Data Contract for Dreams Resource Inventory Management Resource"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Resource"""

    asgn_ownr_id: Optional[int] = Field(
        None,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=343263416,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2015-01-27T03:24:45.430939Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DM_POLY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1390,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=82601,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_req_nm: Optional[str] = Field(
        None,
        alias="RSRC_REQ_NM",
        name="",
        description="",
        example="POLY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="ROOM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-25T14:24:40.515000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="RexRmUpdts-a",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRsrcModel(BaseModel):

    """Payload Class for Dreams Resource Inventory Management Resource"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource"
        stream_name = ""
        description = """This table holds the inventory of the reservable resources, soon to be room only and not any dining inventory"""
        unique_identifier = ["data.RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
