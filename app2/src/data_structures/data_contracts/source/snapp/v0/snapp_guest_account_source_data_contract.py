"""Source Data Contract for SnApp Guest Account"""

from __future__ import annotations
from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import (
    GlobalSnAppHeader,
    GlobalSnAppAccount,
)


class GuestAccount(BaseModel):
    account: GlobalSnAppAccount = Field(
        ...,
        alias="Account",
        name="",
        description="",
    )


class Payload(BaseModel):
    guest_account: GuestAccount = Field(
        ...,
        alias="GuestAccount",
        name="",
        description="",
    )


class SnAppGuestAccountModel(BaseModel):
    """Payload class for SnAppGuestAccountModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SnApp - Guest Account Update"
        stream_name = ""
        description = """SnApp - Guest Account - Changes to guest information """
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = ["SnApp.GuestAccount.UpdateDemographics"]

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(
        ...,
        alias="Payload",
        description="Data payload",
    )
