"""Source Data Contract Template for DPIEast MetaSubject"""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Data Class for DPIEast MetaSubject"""

    allowinbuilder: int = Field(
        ...,
        alias="allowinbuilder",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code: str = Field(
        ...,
        alias="code",
        name="",
        description="",
        example="FIGMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    copyright: Optional[str] = Field(
        None,
        alias="copyright",
        name="",
        description="",
        example="(c)Disney",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    family: str = Field(
        ...,
        alias="family",
        name="",
        description="",
        example="DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=17737,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    isenabled: int = Field(
        ...,
        alias="isenabled",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Figment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prettyname: str = Field(
        ...,
        alias="prettyname",
        name="",
        description="",
        example="Figment",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    roverenabled: int = Field(
        ...,
        alias="roverenabled",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastMetaSubjectModel(BaseModel):
    """Payload class for DPIEast MetaSubject"""

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
        key_path_value = "meta_subject"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
