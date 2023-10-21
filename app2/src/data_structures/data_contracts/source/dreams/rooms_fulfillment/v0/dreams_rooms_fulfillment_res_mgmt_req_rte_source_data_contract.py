"""Source Data Contract Template for res_mgmt_req_rte.json"""


from __future__ import annotations

from typing import List

from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-21T15:06:20.280000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TESTA003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="",
        description="",
        example=11111941490,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    res_mgmt_rte_nm: str = Field(
        ...,
        alias="RES_MGMT_RTE_NM",
        name="",
        description="",
        example="Reservation and Confirmation",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentResMgmtReqRteModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentResMgmtReqRteModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Management Request Route"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RES_MGMT_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_mgmt_req_rte"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
