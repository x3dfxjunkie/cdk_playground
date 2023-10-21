"""Source Data Contract for DPI West Associations Msg"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dpi_west.global_dpi_west_source_data_contract import (
    GlobalDPIWESTMetadata,
)


class Data(BaseModel):
    bundleid: str = Field(
        ...,
        alias="bundleid",
        name="",
        description="",
        example="83edfe83-a780-46e5-9ba7-146da7474a5d",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-08-18T14:22:11Z",
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
        example=52853904,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-08-18T14:22:11Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    photopassid: Optional[str] = Field(
        None,
        alias="photopassid",
        name="",
        description="",
        example="WDWLOSTPHOTOPASS",
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

    xbandid: Optional[str] = Field(
        None,
        alias="xbandid",
        name="",
        description="",
        example="111111111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIWestAssociationsMsgModel(BaseModel):
    """Payload class for DPIWest Associations Msg"""

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
        key_path_value = "associations_msg"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIWESTMetadata = Field(..., alias="metadata")
