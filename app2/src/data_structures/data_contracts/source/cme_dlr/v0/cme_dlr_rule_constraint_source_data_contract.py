"""Source Data Contract Template for CME DLR Rule Constraint"""


from __future__ import annotations

from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for CME Rule Constraint data"""

    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="book-into-resort-bucket-config",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rule_group_id: str = Field(
        ...,
        alias="rule_group_id",
        name="",
        description="",
        example="book-into-resort-bucket-config",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    description: Optional[str] = Field(
        None,
        alias="description",
        name="",
        description="",
        example="This rule set enables us to turn on/off booking into a special RESORT inventory bucket when the reservation flow originates from a resort reservation. This will be used by DLR initially and will be turned off for DLP. The boolean value turns the booking on/off to the specified inventory category, thereby overriding the usual RESORT_PH_PLU/RESORT_TICKET_PLU -> inv category mappings",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    data_type: str = Field(
        ...,
        alias="data_type",
        name="",
        description="",
        example="BOOLEAN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    requires_product_type: int = Field(
        ...,
        alias="requires_product_type",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    requires_inv_category: int = Field(
        ...,
        alias="requires_inv_category",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    requires_inv_bucket: int = Field(
        ...,
        alias="requires_inv_bucket",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    requires_facility: int = Field(
        ...,
        alias="requires_facility",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    requires_inv_slot: int = Field(
        ...,
        alias="requires_inv_slot",
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
        example="2020-07-28T14:12:52Z",
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
        example="2020-07-28T14:12:52Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_usr: str = Field(
        ...,
        alias="created_usr",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    int_min: Optional[int] = Field(
        None,
        alias="int_min",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    int_max: Optional[int] = Field(
        None,
        alias="int_max",
        name="",
        description="",
        example=60,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    str_allowed_values: Optional[str] = Field(
        None,
        alias="str_allowed_values",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRRuleConstraintModel(BaseModel):
    """Payload class for CMEDLRRuleConstraintModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Rule Constraint"
        stream_name = ""
        description = ""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rule_constraint"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
