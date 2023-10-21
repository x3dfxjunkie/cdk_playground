"""Source Data Contract Template for SnApp Media"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
    GlobalSnAppAccount,
    GlobalSnAppMediaItem,
    GlobalSnAppTransaction,
)


class Media(BaseModel):
    account: GlobalSnAppAccount = Field(
        ...,
        alias="Account",
        name="",
        description="",
    )

    media: GlobalSnAppMediaItem = Field(
        ...,
        alias="Media",
        name="",
        description="",
    )

    transaction: GlobalSnAppTransaction = Field(
        ...,
        alias="Transaction",
        name="",
        description="",
    )


class Payload(BaseModel):
    media: Media = Field(
        ...,
        alias="Media",
        name="",
        description="",
    )


class SnAppMediaModel(BaseModel):
    """Payload class for SnAppMediaModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp Media"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = ["SnApp.Media.Assign", "SnApp.Media.Disable", "SnApp.Media.Enabled"]

    header: GlobalSnAppHeader = Field(
        ...,
        alias="Header",
        name="Header",
        description="An object that represents header",
    )
    payload: Payload = Field(
        ...,
        alias="Payload",
        name="Payload",
        description="An object that represents payload",
    )
