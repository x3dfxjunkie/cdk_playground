"""Source Data Contract for Dreams Profile Gid"""
from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Data Payload for GID"""

    gid_cls_nb: int = Field(
        ...,
        alias="GID_CLS_NB",
        name="",
        description="",
        example=1887,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gid_cls_nm: str = Field(
        ...,
        alias="GID_CLS_NM",
        name="",
        description="",
        example="com.wdw.profile.data.entities.Profile",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSProfileGidModel(BaseModel):
    """Payload class for DREAMSProfileGidModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = ""
        unique_identifier = ["data.GID_CLS_NM"]
        timezone = "UTC"
        pi_category = []
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "gid"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
