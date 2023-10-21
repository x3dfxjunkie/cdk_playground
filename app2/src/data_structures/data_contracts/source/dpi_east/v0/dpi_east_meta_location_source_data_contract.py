"""Source Data Contract Template for DPIEastMetaLocationModel"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Data Class for DPIEastMetaLocationModel"""

    campuscode: str = Field(
        ...,
        alias="campuscode",
        name="",
        description="",
        example="WDWPR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code: str = Field(
        ...,
        alias="code",
        name="",
        description="",
        example="IMAGNTON",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=50438,
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
        example="Imagination - Character",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prettyname: str = Field(
        ...,
        alias="prettyname",
        name="",
        description="",
        example="Imagination! at Epcot",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    venuecode: str = Field(
        ...,
        alias="venuecode",
        name="",
        description="",
        example="EPCOT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    xcoord: int = Field(
        ...,
        alias="xcoord",
        name="",
        description="",
        example=539,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ycoord: int = Field(
        ...,
        alias="ycoord",
        name="",
        description="",
        example=436,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastMetaLocationModel(BaseModel):
    """Payload class for DPIEastMetaLocationModel"""

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
        key_path_value = "meta_location"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
