"""Source Data Contract for Dreams Rooms Fulfillment Reservation Management Feature Request"""
from __future__ import annotations
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for Dreams Reservation Management Feature Request Data"""

    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="",
        description="",
        example=1282234577,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=253,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ELIAJ032",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-04-17T10:12:14.807000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ELIAJ032",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-04-17T10:12:14.807000Z",
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


class DREAMSRoomsFulfillmentResMgmtFeatReqModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentResMgmtFeatReqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Management Feature Request"
        stream_name = ""
        description = "This table associated a FEATURE ID to the Reservation Management Request"  # optional
        unique_identifier = ["data.RES_MGMT_REQ_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_mgmt_feat_req"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
