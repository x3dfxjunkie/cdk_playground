"""Source Data Contract for Dreams - Room Reservations Pre-Defined Travel Component Reason"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservations Pre-Defined Travel Component Reason data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:43:23Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
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

    lgcy_rsn_cd: Optional[str] = Field(
        None,
        alias="LGCY_RSN_CD",
        name="",
        description="",
        example="AIR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prdf_tc_rsn_id: int = Field(
        ...,
        alias="PRDF_TC_RSN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_nm: str = Field(
        ...,
        alias="TC_RSN_NM",
        name="",
        description="",
        example="Air not available",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_typ_nm: str = Field(
        ...,
        alias="TC_RSN_TYP_NM",
        name="",
        description="",
        example="Cancel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2006-10-18T15:43:23Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsPrdfTcRsnModel(BaseModel):
    """Payload class for Dreams - Room Reservations Pre-Defined Travel Component Reason Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Pre-defined Travel Component Reason"
        stream_name = ""
        description = "If something was updated in a Travel Component, this table provides the types of of reasons why the update occured."
        unique_identifier = ["data.PRDF_TC_RSN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prdf_tc_rsn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
