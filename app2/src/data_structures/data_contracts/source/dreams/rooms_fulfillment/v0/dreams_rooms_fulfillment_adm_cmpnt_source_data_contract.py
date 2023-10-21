"""Source Data Contract for Dreams - Rooms Fulfillment Admission Component"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Dreams - Rooms Fulfillment Admission Component Data"""

    adm_tc_id: int = Field(
        ...,
        alias="ADM_TC_ID",
        name="",
        description="",
        example=12356464,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ats_tkt_cd: str = Field(
        ...,
        alias="ATS_TKT_CD",
        name="",
        description="",
        example="2XZYA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tkt_prc_am: Optional[float] = Field(
        None,
        alias="TKT_PRC_AM",
        name="",
        description="",
        example=13.37,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ats_recon_in: str = Field(
        ...,
        alias="ATS_RECON_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_strt_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_STRT_DT",
        name="",
        description="",
        example="2023-05-25T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    validity_end_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_END_DT",
        name="",
        description="",
        example="2023-05-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentAdmCmpntModel(BaseModel):
    """Payload class for Dreams - Rooms Fulfillment Admission Component Model"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Rooms Fulfillment Admission Component"
        stream_name = ""
        description = "When a reservation has admission components included, this table provides the enterprise Ticket Product Code that connects ticket product information across multiple applications. It also contains the tickets validity start and end dates which is a key attribute for date based tickets"
        unique_identifier = ["data.ADM_TC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "adm_cmpnt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
