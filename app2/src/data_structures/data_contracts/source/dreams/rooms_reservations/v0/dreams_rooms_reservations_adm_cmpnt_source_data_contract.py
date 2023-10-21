"""Source Data Contract Template for Dreams - Room Reservation Admission Component"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservation Admission Component Data"""

    adm_tc_id: int = Field(
        ...,
        alias="ADM_TC_ID",
        name="",
        description="",
        example=1534131813,
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

    ats_tkt_cd: str = Field(
        ...,
        alias="ATS_TKT_CD",
        name="",
        description="",
        example="3JW0E",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2018-06-06T23:53:55Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
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

    tkt_prc_am: Optional[float] = Field(
        None,
        alias="TKT_PRC_AM",
        name="",
        description="",
        example=246.87,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2018-06-06T23:53:55Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_end_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_END_DT",
        name="",
        description="",
        example="2018-12-11T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    validity_strt_dt: Optional[datetime] = Field(
        None,
        alias="VALIDITY_STRT_DT",
        name="",
        description="",
        example="2018-12-04T00:00:00Z",
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


class DREAMSRoomsReservationsAdmCmpntModel(BaseModel):
    """Payload class for Dreams - Room Reservation Admission Component Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Admission Component"
        stream_name = ""
        description = """When a reservation has admission components included, this table provides the enterprise Ticket Product Code that connects ticket product information across multiple applications. It also contains the tickets validity start and end dates which is a key attribute for date based tickets"""
        unique_identifier = ["data.ADM_TC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "adm_cmpnt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
