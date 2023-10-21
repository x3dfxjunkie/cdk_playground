"""Source Data Contract for DREAMS SAP Tax"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Tax Data"""

    sap_tax_cd: str = Field(
        ...,
        alias="SAP_TAX_CD",
        name="",
        description="",
        example="I0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_tax_nm: str = Field(
        ...,
        alias="SAP_TAX_NM",
        name="",
        description="",
        example="A/P Tax Exempt (Vertex) - Input Tax",
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
        example="2006-10-18T19:46:43.918Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapTaxModel(BaseModel):
    """Payload class for DREAMSAccountingSapTaxModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Tax"
        stream_name = ""
        description = """SAP Tax names associated to SAP Tax codes"""
        unique_identifier = ["data.SAP_TAX_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_TAX"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
