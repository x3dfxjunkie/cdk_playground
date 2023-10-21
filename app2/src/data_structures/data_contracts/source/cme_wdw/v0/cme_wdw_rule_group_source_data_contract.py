"""Source Data Contract Template for CME WDW Rule Group"""


from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_wdw.global_cme_wdw_source_data_contract import (
    GlobalCMEWDWMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for CME Rule Group data"""

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="blocklist-res-not-allowed-for-inv-category-rc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    description: Optional[str] = Field(
        None,
        alias="description",
        name="",
        description="",
        example="Blocklist reservations not allowed for Inventory Category",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_active: int = Field(
        ...,
        alias="is_active",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    last_updated: datetime = Field(
        ...,
        alias="last_updated",
        name="",
        description="",
        example="2021-11-02T14:35:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    update_usr: Optional[str] = Field(
        None,
        alias="update_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_on: Optional[datetime] = Field(
        None,
        alias="created_on",
        name="",
        description="",
        example="2021-11-02T14:35:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_usr: Optional[str] = Field(
        None,
        alias="created_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEWDWRuleGroupModel(BaseModel):
    """Payload class for CMEWDWRuleGroupModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Rule Group"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rule_group"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEWDWMetadata = Field(..., alias="metadata")
