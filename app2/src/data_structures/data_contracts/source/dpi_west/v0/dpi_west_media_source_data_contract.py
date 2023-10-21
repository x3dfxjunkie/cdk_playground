"""Source Data Contract for DPI West Media"""

from __future__ import annotations
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Data Class for DPI West Media"""

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
        example="9f5bc586-eb06-4312-a0b3-3796b9b83b2f",
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

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-09-07T12:45:19Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expirationdate: datetime = Field(
        ...,
        alias="expirationdate",
        name="",
        description="",
        example="2024-11-07T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    externalid: str = Field(
        ...,
        alias="externalid",
        name="",
        description="",
        example="2032810405-59355806-20230907T124450-689575360-DSC_5568.JPG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=229560056,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-09-07T12:45:19Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    locationcode: str = Field(
        ...,
        alias="locationcode",
        name="",
        description="",
        example="CARSLANDSTANLEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    logicalmediaid: Optional[str] = Field(
        None,
        alias="logicalmediaid",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediamigtype: Optional[str] = Field(
        None,
        alias="mediamigtype",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaowned: int = Field(
        ...,
        alias="mediaowned",
        name="",
        description="",
        example=0,
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
        example="1528624",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    statecode: str = Field(
        ...,
        alias="statecode",
        name="",
        description="",
        example="MODERATED_UNSUPPRESSED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    takenbusdate: date = Field(
        ...,
        alias="takenbusdate",
        name="",
        description="",
        example="2023-09-07",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    takendate: datetime = Field(
        ...,
        alias="takendate",
        name="",
        description="",
        example="2023-09-07T12:44:50Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    vendormediaid: str = Field(
        ...,
        alias="vendormediaid",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    venuecode: str = Field(
        ...,
        alias="venuecode",
        name="",
        description="",
        example="DCA",
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


class DPIWestMediaModel(BaseModel):
    """Payload class for DPI West Media"""

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
        key_path_value = "media"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
