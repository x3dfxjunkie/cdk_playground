"""Source Data Contract Template for CME WDW Users"""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class data"""

    created_on: datetime = Field(
        ...,
        alias="created_on",
        name="",
        description="",
        example="2021-12-30T11:54:54Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="",
        description="",
        example="AAAAA111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    email: Optional[str] = Field(
        None,
        alias="email",
        name="",
        description="",
        example="",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    first_name: str = Field(
        ...,
        alias="first_name",
        name="",
        description="",
        example="Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_name: str = Field(
        ...,
        alias="last_name",
        name="",
        description="",
        example="Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="",
        description="",
        example="2022-02-03T15:29:14Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    role_id: str = Field(
        ...,
        alias="role_id",
        name="",
        description="",
        example="PROVISION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    update_usr: str = Field(
        ...,
        alias="update_usr",
        name="",
        description="",
        example="AAAAA111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    username: str = Field(
        ...,
        alias="username",
        name="",
        description="",
        example="AAAAA111",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWUsersModel(BaseModel):
    """Payload class for CME WDW Users Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Users"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.username"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "users"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
