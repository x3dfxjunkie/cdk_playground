"""Source Data Contract for Dreams Res Mgmt Req RTE"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams Res Mgmt Req RTE Data"""

    res_mgmt_req_id: int = Field(
        ...,
        alias="RES_MGMT_REQ_ID",
        name="Reservation Management Request Identification",
        description="The identification value for a request made on behalf of or for a reservation managed within LiLo reservation management.  The identification of a request for a feature for a travel component.",
        example=30312955618,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=True,
    )
    res_mgmt_rte_nm: str = Field(
        ...,
        alias="RES_MGMT_RTE_NM",
        name="Reservation Management Routing Name",
        description="The identification of the feature as provided by pricing/product service.",
        example="SE SPL Needs",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="Create User Identification Code",
        description="The identification value for the user or application that created a row in this table.",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="Create Date Time",
        description="The month day century year hour minute and second when a row was created in this table.",
        example="2023-03-29T11:30:10.669000Z",
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


class DREAMSRoomsReservationsResMgmtReqRteModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsResMgmtReqRteModel"""

    class Config:
        """Payload Level Metadata"""

        name = "Reservation Management Request Route"
        stream_name = "guest360-dreams-resm-stream"
        description = ""
        unique_identifier = ["data.RES_MGMT_REQ_ID", "data.RES_MGMT_RTE_NM"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "res_mgmt_req_rte"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
