"""Source Data Contract Template for DREAMS Resource Inventory Management Room Dimension"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-01-07T15:56:40.999447Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_lgth_vl: int = Field(
        ...,
        alias="RM_LGTH_VL",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_measure_nm: str = Field(
        ...,
        alias="RM_MEASURE_NM",
        name="",
        description="",
        example="Feet",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rm_wdth_vl: int = Field(
        ...,
        alias="RM_WDTH_VL",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: int = Field(
        ...,
        alias="RSRC_ID",
        name="",
        description="",
        example=42565,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    struct_typ_nm: str = Field(
        ...,
        alias="STRUCT_TYP_NM",
        name="",
        description="",
        example="ROOM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementRmDimModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRmDimModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Room Dimension"
        stream_name = ""
        description = """This table provides the structure type of a reservable resource:
ROOM
BALCONY"""
        unique_identifier = ["data.RSRC_ID", "data.STRUCT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rm_dim"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
