"""Source Data Contract Template for DREAMS Resource Inventory Management Campus"""


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime


class Data(BaseModel):
    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_nm: str = Field(
        ...,
        alias="CMPS_NM",
        name="",
        description="",
        example="Disneyland",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_strt_dt: datetime = Field(
        ...,
        alias="CMPS_STRT_DT",
        name="",
        description="",
        example="1955-07-15T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:05:50Z",
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

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2009-09-25T10:09:49.502000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="test1212",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cmps_end_dt: Optional[datetime] = Field(
        None,
        alias="CMPS_END_DT",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementCmpsModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementCmpsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Campus"
        stream_name = ""
        description = """This table associates locations to specific ID:
Pacific Region GMT-10
Disneyland
Walt Disney World"""
        unique_identifier = ["data.CMPS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cmps"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
