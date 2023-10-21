"""Source Data Contract for DREAMS SAP Sales Organization"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Sales Organization Data"""

    sap_sls_org_cd: str = Field(
        ...,
        alias="SAP_SLS_ORG_CD",
        name="",
        description="",
        example="1008",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_sls_org_nm: str = Field(
        ...,
        alias="SAP_SLS_ORG_NM",
        name="",
        description="",
        example="Walt Disney World Co",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-15T04:00:01.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapSlsOrgModel(BaseModel):
    """Payload class for DREAMSAccountingSapSlsOrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Sales Organization"
        stream_name = ""
        description = """SAP Sales Organization names associated organization code"""
        unique_identifier = ["data.SAP_SLS_ORG_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_SLS_ORG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
