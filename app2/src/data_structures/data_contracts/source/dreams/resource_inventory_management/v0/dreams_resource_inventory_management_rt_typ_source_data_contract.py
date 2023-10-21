"""Source Data Contract Template for DREAMS Resource Inventory Management Rate Type"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:06:00Z",
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

    rt_typ_nm: str = Field(
        ...,
        alias="RT_TYP_NM",
        name="",
        description="",
        example="SP1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRtTypModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRtTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Rate Type"
        stream_name = ""
        description = """List of rate types GEN
GRP
PAR
SP1
SP2
SP3
SP4
UPS"""
        unique_identifier = ["data.RT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rt_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
