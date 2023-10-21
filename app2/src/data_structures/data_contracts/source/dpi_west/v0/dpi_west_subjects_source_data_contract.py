"""Source Data Contract for DPI-WEST Subjects"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI-WEST Subjects"""

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-08-18T12:19:39Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expirationdate: datetime = Field(
        ...,
        alias="expirationdate",
        name="",
        description="",
        example="2024-10-18T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=253210050,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-08-18T12:19:39Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=227306354,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    subjectcode: str = Field(
        ...,
        alias="subjectcode",
        name="",
        description="",
        example="NONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    version: int = Field(
        ...,
        alias="version",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIWestSubjectsModel(BaseModel):
    """Payload class for DPI-WEST Subjects"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "subjects"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
