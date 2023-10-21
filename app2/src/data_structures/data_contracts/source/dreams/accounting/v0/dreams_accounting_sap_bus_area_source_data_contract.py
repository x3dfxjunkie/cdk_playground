"""Source Data Contract for DREAMS SAP Business Area"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Business Data"""

    sap_bus_area_cd: str = Field(
        ...,
        alias="SAP_BUS_AREA_CD",
        name="",
        description="",
        example="101",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_bus_area_nm: str = Field(
        ...,
        alias="SAP_BUS_AREA_NM",
        name="",
        description="",
        example="Disneyland Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="RFC2174241",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-05-02T01:37:02.677Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapBusAreaModel(BaseModel):
    """Payload class for DREAMSAccountingSapBusAreaModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Business Area"
        stream_name = ""
        description = """SAP Business Area names associated to SAP Business Area Codes"""
        unique_identifier = ["data.SAP_BUS_AREA_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_BUS_AREA"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
