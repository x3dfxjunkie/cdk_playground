"""Source Data Contract for DREAMS Campus"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Campus Data"""

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
    cmps_nm: str = Field(
        ...,
        alias="CMPS_NM",
        name="",
        description="",
        example="Walt Disney World",
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
        example="2009-08-11T21:41:09.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingCmpsModel(BaseModel):
    """Payload class for DREAMSAccountingCmpsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Campus"
        stream_name = ""
        description = """The 3 areas that use the CAMPUS system: Pacific Region GMT-10, Walt Disney World, Disneyland"""
        unique_identifier = ["data.CMPS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CMPS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
