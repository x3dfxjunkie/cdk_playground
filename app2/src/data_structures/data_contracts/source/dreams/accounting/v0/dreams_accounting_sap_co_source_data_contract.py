"""Source Data Contract for DREAMS SAP Company"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Company Data"""

    sap_co_cd: str = Field(
        ...,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_co_nm: str = Field(
        ...,
        alias="SAP_CO_NM",
        name="",
        description="",
        example="WD Parks & Resorts US,Inc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="IM468218",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-06-06T20:28:43.152Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapCoModel(BaseModel):
    """Payload class for DREAMSAccountingSapCoModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Company"
        stream_name = ""
        description = """SAP Company names associated to SAP Company Codes"""
        unique_identifier = ["data.SAP_CO_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_CO"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
