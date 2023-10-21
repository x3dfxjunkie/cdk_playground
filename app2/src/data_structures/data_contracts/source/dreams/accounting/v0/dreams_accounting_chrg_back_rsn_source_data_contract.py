"""Source Data Contract for DREAMS Charge Back Reason"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Charge Back Reason Data"""

    chrg_back_rsn_id: int = Field(
        ...,
        alias="CHRG_BACK_RSN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_rsn_nm: str = Field(
        ...,
        alias="CHRG_BACK_RSN_NM",
        name="",
        description="",
        example="Airport Transfer Rebate",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_rsn_strt_dt: datetime = Field(
        ...,
        alias="CHRG_BACK_RSN_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_back_rsn_end_dt: datetime = Field(
        ...,
        alias="CHRG_BACK_RSN_END_DT",
        name="",
        description="",
        example="2099-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T07:08:03.682Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="PEREB049",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-11-14T14:10:25.706Z",
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


class DREAMSAccountingChrgBackRsnModel(BaseModel):
    """Payload class for DREAMSAccountingChrgBackRsnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Back Reason"
        stream_name = ""
        description = """List of the reasons a charge back would occur this list isn't complete: Poor Service Bell Services
Rehab
Tickets-Lost or Stolen
Noise
Poor Service Housekeeping
Water or Pipe Break
Goodwill or Illness
Poor Service Engineering
Package Handling Fee
Poor Service
No Show Arrival
Poor Service Valet
Poor Experience-Parks"""
        unique_identifier = ["data.CHRG_BACK_RSN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_BACK_RSN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
