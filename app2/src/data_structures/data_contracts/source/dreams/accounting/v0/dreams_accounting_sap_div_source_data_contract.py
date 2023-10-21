"""Source Data Contract for DREAMS SAP Division"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Division Data"""

    sap_div_cd: str = Field(
        ...,
        alias="SAP_DIV_CD",
        name="",
        description="",
        example="10",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_div_nm: str = Field(
        ...,
        alias="SAP_DIV_NM",
        name="",
        description="",
        example="Theme Parks",
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T19:46:43.240Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapDivModel(BaseModel):
    """Payload class for DREAMSAccountingSapDivModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Division"
        stream_name = ""
        description = """SAP Division names associated to SAP Division Code"""
        unique_identifier = ["data.SAP_DIV_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_DIV"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
