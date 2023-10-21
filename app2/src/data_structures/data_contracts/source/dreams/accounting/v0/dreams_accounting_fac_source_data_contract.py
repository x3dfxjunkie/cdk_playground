"""Source Data Contract for DREAMS Facility"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Facility Data"""

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_sls_org_cd: str = Field(
        ...,
        alias="SAP_SLS_ORG_CD",
        name="",
        description="",
        example="1009",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_ofc_id: int = Field(
        ...,
        alias="SLS_OFC_ID",
        name="",
        description="",
        example=1008,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_nm: str = Field(
        ...,
        alias="FAC_NM",
        name="",
        description="",
        example="Project Crystal",
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
        example="2010-01-27T20:44:48.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingFacModel(BaseModel):
    """Payload class for DREAMSAccountingFacModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Facility"
        stream_name = ""
        description = """Facilities tied to SAP and CAMPUS"""
        unique_identifier = ["data.FAC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FAC"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
