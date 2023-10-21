"""Source Data Contract for DREAMS Disney System"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Disney System Data"""

    dsny_sys_cd: str = Field(
        ...,
        alias="DSNY_SYS_CD",
        name="",
        description="",
        example="PROTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dsny_sys_nm: str = Field(
        ...,
        alias="DSNY_SYS_NM",
        name="",
        description="",
        example="PROTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Winter 07",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2007-12-12T06:44:34.694Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingDsnySysModel(BaseModel):
    """Payload class for DREAMSAccountingDsnySysModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney System"
        stream_name = ""
        description = """A list of Codes related to Disney and the Disney system names the correlate with. Examples: Walt Disney World Scheduled Events Back Office
Pacific Region Lilo Express Checkout
Walt Disney World Scheduled Events Call Center
Walt Disney World DREAMS Back Office
Walt Disney World DREAMS Internet"""
        unique_identifier = ["data.DSNY_SYS_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "DSNY_SYS"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
