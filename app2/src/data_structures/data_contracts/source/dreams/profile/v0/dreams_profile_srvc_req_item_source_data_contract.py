"""Source Data Contract for Dreams Profile SrvcReqItem"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Data Payload for SrvcReqItem"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-12T11:05:01Z",
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

    item_ds: str = Field(
        ...,
        alias="ITEM_DS",
        name="",
        description="",
        example="GTD BABY GATES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=53,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mxmo_item_nb: str = Field(
        ...,
        alias="MXMO_ITEM_NB",
        name="",
        description="",
        example="170012",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_id: Optional[int] = Field(
        None,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=95,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_typ_nm: str = Field(
        ...,
        alias="SRVC_TYP_NM",
        name="",
        description="",
        example="Delivery",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-08-12T11:05:01Z",
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


class DREAMSProfileSrvcReqItemModel(BaseModel):
    """Payload class for DREAMSProfileSrvcReqItemModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Service Request Item"
        stream_name = ""
        description = ""
        unique_identifier = ["data.MXMO_ITEM_NB", "data.SRVC_TYP_NM"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "srvc_req_item"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
