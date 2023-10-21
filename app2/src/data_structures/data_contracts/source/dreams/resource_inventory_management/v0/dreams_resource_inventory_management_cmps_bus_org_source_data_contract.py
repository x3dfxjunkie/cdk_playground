"""Source Data Contract Template for DREAMS Resource Inventory Management Campus Business Organization"""


from __future__ import annotations

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime


class Data(BaseModel):
    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bus_org_nm: str = Field(
        ...,
        alias="BUS_ORG_NM",
        name="",
        description="",
        example="WDW SE",
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

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:08:23Z",
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


class DREAMSResourceInventoryManagementCmpsBusOrgModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementCmpsBusOrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Campus Business Organization"
        stream_name = ""
        description = """This table ties the campus locations to different business organizations:BUS_ORG_NM
WDW SE
WDW Resort Ops
WDW DRC
Pacific Region SE
Pacific Region Resort Ops
Pacific Region DRC
DLR SE
DLR Resort Ops
DLR DRC"""
        unique_identifier = ["data.BUS_ORG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "cmps_bus_org"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
