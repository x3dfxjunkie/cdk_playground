"""Source Data Contract Template for DPI-East Associations Msg"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Class for DPI-East Associations Msg data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=263946802,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2020-07-18T16:12:28Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2020-07-18T16:12:28Z",
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
        example="2021-09-18T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bundleid: str = Field(
        ...,
        alias="bundleid",
        name="",
        description="",
        example="9918f123-037a-4b8d-adff-b277b695f118",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    photopassid: str = Field(
        ...,
        alias="photopassid",
        name="",
        description="",
        example="WDWLOSTPHOTOPASS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastAssociationsMsgModel(BaseModel):
    """Payload class for DPIEastAssociationsMsgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "AssociationsMsg"
        stream_name = ""
        description = "AssociationsMsg"  # optional
        unique_identifier = []
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "associations_msg"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
