"""Source Data Contract Template for res_mgmt_feat_req.json"""


from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Reservation Management Feature Request"""

    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="",
        description="",
        example=11111117626,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=11111117626,
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


class DREAMSRoomsReservationsResMgmtFeatReqModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsResMgmtFeatReqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservation Management Feature Request"
        stream_name = ""
        description = """This table associated a FEATURE ID to the Reservation Management Request"""
        unique_identifier = ["data.RES_MGMT_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "res_mgmt_feat_req"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
