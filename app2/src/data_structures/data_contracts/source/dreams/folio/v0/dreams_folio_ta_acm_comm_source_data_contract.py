"""Source Data Contract for Dreams Folio Travel Agency Accommodation Commission"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Travel Agency Accommodation Commission Data"""

    trvl_agcy_acm_comm_id: int = Field(
        ...,
        alias="TRVL_AGCY_ACM_COMM_ID",
        name="",
        description="",
        example=14026579,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80010385,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rm_id_vl: str = Field(
        ...,
        alias="RM_ID_VL",
        name="",
        description="",
        example="6104",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_comm_strt_dt: datetime = Field(
        ...,
        alias="ACM_COMM_STRT_DT",
        name="",
        description="",
        example="2023-06-03T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_comm_end_dt: datetime = Field(
        ...,
        alias="ACM_COMM_END_DT",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T02:29:06.672256Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTaAcmCommModel(BaseModel):
    """Payload class for DREAMSFolioTaAcmCommModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Agency Accommodation Commission"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.TRVL_AGCY_ACM_COMM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TA_ACM_COMM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
