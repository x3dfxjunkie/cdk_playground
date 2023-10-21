"""Source Data Contract for DPI East MetaVenue"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI East MetaVenue"""

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
        example="AAACONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=1436,
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
        example="AAA Convention",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    onlinegroup: str = Field(
        ...,
        alias="onlinegroup",
        name="",
        description="",
        example="RESOR8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    onsitegroup: str = Field(
        ...,
        alias="onsitegroup",
        name="",
        description="",
        example="MK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prettyname: str = Field(
        ...,
        alias="prettyname",
        name="",
        description="",
        example="Walt Disney World Resort",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rovergroup: str = Field(
        ...,
        alias="rovergroup",
        name="",
        description="",
        example="MISC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sort: Optional[int] = Field(
        None,
        alias="sort",
        name="",
        description="",
        example=99,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastMetaVenueModel(BaseModel):
    """Payload class for DPI East MetaVenue"""

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
        key_path_value = "meta_venue"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
