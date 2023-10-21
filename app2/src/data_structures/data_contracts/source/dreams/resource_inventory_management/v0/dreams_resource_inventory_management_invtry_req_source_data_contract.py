"""Source Data Contract for Dreams Resource Inventory Management Inventory Request"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Inventory Request"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-06T12:05:44.941000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CORTM116",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_id_vl: Optional[str] = Field(
        None,
        alias="GRP_ID_VL",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_end_dts: datetime = Field(
        ...,
        alias="INVTRY_REQ_END_DTS",
        name="",
        description="",
        example="2023-08-15T10:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_req_nm: str = Field(
        ...,
        alias="INVTRY_REQ_REQ_NM",
        name="",
        description="",
        example="CORTM116",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_rsltn_dts: Optional[datetime] = Field(
        None,
        alias="INVTRY_REQ_RSLTN_DTS",
        name="",
        description="",
        example="2023-07-25T20:59:57.134000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_strt_dts: datetime = Field(
        ...,
        alias="INVTRY_REQ_STRT_DTS",
        name="",
        description="",
        example="2023-08-06T12:05:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_sts_nm: Optional[str] = Field(
        None,
        alias="INVTRY_REQ_STS_NM",
        name="",
        description="",
        example="PENDING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_req_typ_nm: str = Field(
        ...,
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
        example=0,
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

    prmy_gst_nm: Optional[str] = Field(
        None,
        alias="PRMY_GST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_invtry_req_cmt_tx: Optional[str] = Field(
        None,
        alias="RM_INVTRY_REQ_CMT_TX",
        name="",
        description="",
        example="res# 530141684560 hold for all stars music guest has 3 reservations",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_tx: Optional[str] = Field(
        None,
        alias="RSN_TX",
        name="",
        description="",
        example="Category Hold",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=818,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_req_id: int = Field(
        ...,
        alias="RSRC_INVTRY_REQ_ID",
        name="",
        description="",
        example=23720587,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_req_id: Optional[str] = Field(
        None,
        alias="SRVC_REQ_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-06T12:05:44.941000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CORTM116",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementInvtryReqModel(BaseModel):
    """Payload class for Dreams Resource Inventory Management Inventory Request"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Request"
        stream_name = ""
        description = """This table tracks the history of inventory requests of
OUT_OF_INVENTORY
CLOSED_FLOOR"""
        unique_identifier = ["data.RSRC_INVTRY_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "invtry_req"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
