"""Source Data Contract  for DPI West Associations"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    """Source Data Contract  for DPI West Associations"""

    association: str = Field(
        ...,
        alias="association",
        name="",
        description="",
        example="PP3P7J4R39A3L79L",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    assoctype: str = Field(
        ...,
        alias="assoctype",
        name="",
        description="",
        example="PHOTOPASS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-08-18T10:24:38Z",
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

    expirationdateviewable: datetime = Field(
        ...,
        alias="expirationdateviewable",
        name="",
        description="",
        example="2023-10-02T10:21:48Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    favorite: Optional[str] = Field(
        None,
        alias="favorite",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    guestid: Optional[str] = Field(
        None,
        alias="guestid",
        name="",
        description="",
        example="{AAAAAAAA-AAAA-1111-8888-AAAAAAAAAAAA}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hidden: Optional[str] = Field(
        None,
        alias="hidden",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=329233110,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-08-18T10:24:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=227287750,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaowned: Optional[str] = Field(
        None,
        alias="mediaowned",
        name="",
        description="",
        example="",
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


class DPIWestAssociationsModel(BaseModel):
    """Payload class for DPI West Associations"""

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
        key_path_value = "associations"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
