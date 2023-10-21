"""Source Data Contract for DPI-West MetaVenue"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI-West MetaVenue"""

    campuscode: str = Field(
        ...,
        alias="campuscode",
        name="",
        description="",
        example="DLR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code: str = Field(
        ...,
        alias="code",
        name="",
        description="",
        example="SPCLEVENTDCA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=1560,
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
        example="Special Event DCA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    onlinegroup: str = Field(
        ...,
        alias="onlinegroup",
        name="",
        description="",
        example="DISNE11",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    onsitegroup: str = Field(
        ...,
        alias="onsitegroup",
        name="",
        description="",
        example="DLPCA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prettyname: str = Field(
        ...,
        alias="prettyname",
        name="",
        description="",
        example="Special Events at DCA",
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


class DPIWestMetaVenueModel(BaseModel):
    """Payload class for DPI-WEST MetaVenue"""

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
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
