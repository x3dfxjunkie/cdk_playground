"""Source Data Contract for DREAMS SAP ISS"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP ISS Data"""

    sap_iss_cd: str = Field(
        ...,
        alias="SAP_ISS_CD",
        name="",
        description="",
        example="760000593306",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_iss_nm: str = Field(
        ...,
        alias="SAP_ISS_NM",
        name="",
        description="",
        example="STD1,PCSS3 ACC",
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
        example="2009-08-27T14:20:13.019Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapIssModel(BaseModel):
    """Payload class for DREAMSAccountingSapIssModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP ISS"
        stream_name = ""
        description = """Can't find any usage of this and no idea what ISS is"""
        unique_identifier = ["data.SAP_ISS_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_ISS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
