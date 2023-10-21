"""Source Data Contract Template for Subjects"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Class for DPI-East Subjects data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=521687,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2019-11-22T14:08:25Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2019-11-22T14:08:25Z",
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

    expirationdate: datetime = Field(
        ...,
        alias="expirationdate",
        name="",
        description="",
        example="2021-01-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    subjectcode: str = Field(
        ...,
        alias="subjectcode",
        name="",
        description="",
        example="TINKERBELL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=510281,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastSubjectsModel(BaseModel):
    """Payload class for DPIEastSubjectsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Subjects"
        stream_name = ""
        description = "Subjects"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "subjects"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
