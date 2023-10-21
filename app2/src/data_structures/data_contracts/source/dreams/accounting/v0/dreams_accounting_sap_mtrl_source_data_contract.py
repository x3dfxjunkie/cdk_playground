"""Source Data Contract for DREAMS SAP Material"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Material Data"""

    sap_mtrl_cd: str = Field(
        ...,
        alias="SAP_MTRL_CD",
        name="",
        description="",
        example="BVEXTKT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_mtrl_nm: str = Field(
        ...,
        alias="SAP_MTRL_NM",
        name="",
        description="",
        example="GRAND FLORIDIAN TICKET VOIDS",
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
        example="2010-01-20T06:40:32.973Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapMtrlModel(BaseModel):
    """Payload class for DREAMSAccountingSapMtrlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Material"
        stream_name = ""
        description = """SAP Material Names associated to SAP Material Codes"""
        unique_identifier = ["data.SAP_MTRL_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_MTRL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
