"""Source Data Contract for Dreams - Room Fulfillment Disney Vacation Club Points Payment Reference"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Disney Vacation Club Points Payment Reference data"""

    acm_tc_id: int = Field(
        ...,
        alias="ACM_TC_ID",
        name="",
        description="",
        example=1697250129,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2019-09-26T12:49:55.945000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="DANNM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_pt_pmt_ref_id: int = Field(
        ...,
        alias="DVC_PT_PMT_REF_ID",
        name="",
        description="",
        example=25260541,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dvc_pt_pmt_ref_vl: str = Field(
        ...,
        alias="DVC_PT_PMT_REF_VL",
        name="",
        description="",
        example="I:435643938160.001",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2019-09-26T12:49:55.945000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="DANNM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentDvcPtPmtRefModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Disney Vacation Club Points Payment Reference Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Vacation Club Points Payment reference"
        stream_name = ""
        description = "If a reservation is booked using Disney Vacation Club points, this table is populated with a value that references the guest points account."
        unique_identifier = ["data.DVC_PT_PMT_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dvc_pt_pmt_ref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
