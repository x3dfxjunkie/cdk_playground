"""Source Data Contract Template for DPI-East Media"""


from __future__ import annotations

from datetime import datetime, date

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Class for DPI-East Media data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=522279,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2020-01-08T15:19:44Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2020-01-08T15:19:44Z",
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
        example="2021-03-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asset_type: str = Field(
        ...,
        alias="asset_type",
        name="",
        description="",
        example="PICTURE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bundleid: str = Field(
        ...,
        alias="bundleid",
        name="",
        description="",
        example="ab22b99c-7a8f-4652-aab4-0409defd3ae2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    category: str = Field(
        ...,
        alias="category",
        name="",
        description="",
        example="ROVER",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    externalid: str = Field(
        ...,
        alias="externalid",
        name="",
        description="",
        example="tests/chewbacca002_cropAndZoom_0.jpg",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    locationcode: str = Field(
        ...,
        alias="locationcode",
        name="",
        description="",
        example="GLOBALLPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaowned: bool = Field(
        ...,
        alias="mediaowned",
        name="",
        description="",
        example=True,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    parentmediaid: int = Field(
        ...,
        alias="parentmediaid",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    photog: str = Field(
        ...,
        alias="photog",
        name="",
        description="",
        example="12345",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    statecode: str = Field(
        ...,
        alias="statecode",
        name="",
        description="",
        example="UNMODERATED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    takendate: datetime = Field(
        ...,
        alias="takendate",
        name="",
        description="",
        example="2019-02-01T10:10:46Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    venuecode: str = Field(
        ...,
        alias="venuecode",
        name="",
        description="",
        example="GLOBALLPP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    takenbusdate: date = Field(
        ...,
        alias="takenbusdate",
        name="",
        description="",
        example="2019-02-01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastMediaModel(BaseModel):
    """Payload class for DPIEastMediaModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Media"
        stream_name = ""
        description = "Media"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "media"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
