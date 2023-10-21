"""Source Data Contract Template for DPI-East Associations"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dpi_east.global_dpi_east_source_data_contract import (
    GlobalDPIEASTMetadata,
)


class Data(BaseModel):
    """Class for DPI-East Associations data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=382439,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    createdate: datetime = Field(
        ...,
        alias="createdate",
        name="",
        description="",
        example="2023-04-19T13:52:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lastmodifieddate: datetime = Field(
        ...,
        alias="lastmodifieddate",
        name="",
        description="",
        example="2023-04-19T13:52:30Z",
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
        example="2024-06-19T13:52:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    expirationdateviewable: datetime = Field(
        ...,
        alias="expirationdateviewable",
        name="",
        description="",
        example="2024-06-19T13:52:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    association: str = Field(
        ...,
        alias="association",
        name="",
        description="",
        example="1111111111111111",
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

    guestid: str = Field(
        ...,
        alias="guestid",
        name="",
        description="",
        example="{AAAAAAAA-ABCD-ABCD-1111-931E357990BA}",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mediaid: int = Field(
        ...,
        alias="mediaid",
        name="",
        description="",
        example=913603,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DPIEastAssociationsModel(BaseModel):
    """Payload class for DPIEastAssociationsModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = ""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "associations"

    data: Data = Field(..., alias="data")
    metadata: GlobalDPIEASTMetadata = Field(..., alias="metadata")
