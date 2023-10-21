"""Source Data Contract for DPI-WEST MetaSubject"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI-WEST MetaSubject"""

    allowinbuilder: int = Field(
        ...,
        alias="allowinbuilder",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code: str = Field(
        ...,
        alias="code",
        name="",
        description="",
        example="AURORA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    copyright: str = Field(
        ...,
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
        example=17723,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    isenabled: int = Field(
        ...,
        alias="isenabled",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="Aurora",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prettyname: str = Field(
        ...,
        alias="prettyname",
        name="",
        description="",
        example="Princess Aurora",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    roverenabled: int = Field(
        ...,
        alias="roverenabled",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIWestMetaSubjectModel(BaseModel):
    """Payload class for DPIWestMetaSubjectModel"""

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
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
