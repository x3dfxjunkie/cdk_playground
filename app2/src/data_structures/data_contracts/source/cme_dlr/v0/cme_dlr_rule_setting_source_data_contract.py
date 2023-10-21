"""Source Data Contract Template for CME DLR Rule Setting"""


from __future__ import annotations

from datetime import datetime, date
from typing import Optional
from app.src.data_structures.data_contracts.source.cme_dlr.global_cme_dlr_source_data_contract import (
    GlobalCMEDLRMetadata,
)
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for CME Rule Setting data"""

    id: int = Field(
        ...,
        alias="id",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    group_id: str = Field(
        ...,
        alias="group_id",
        name="",
        description="",
        example="ap-res-rule-group",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rule_constraint_id: str = Field(
        ...,
        alias="rule_constraint_id",
        name="",
        description="",
        example="max-ap-res-by-inv-category",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_constrained: int = Field(
        ...,
        alias="is_constrained",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    data_type: str = Field(
        ...,
        alias="data_type",
        name="",
        description="",
        example="int",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    int_val: Optional[int] = Field(
        None,
        alias="int_val",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    applies_to_inv_category: Optional[str] = Field(
        None,
        alias="applies_to_inv_category",
        name="",
        description="",
        example="AP",
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
        example="2020-07-09T17:11:47Z",
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
    created_usr: Optional[str] = Field(
        None,
        alias="created_usr",
        name="",
        description="",
        example="MOUSM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    applies_to_product_type: Optional[str] = Field(
        None,
        alias="applies_to_product_type",
        name="",
        description="",
        example="signature-plus",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    date_val: Optional[date] = Field(
        None,
        alias="date_val",
        name="",
        description="",
        example="2020-07-31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    applies_to_facility: Optional[str] = Field(
        None,
        alias="applies_to_facility",
        name="",
        description="",
        example="DLR_CA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    created_on: Optional[datetime] = Field(
        None,
        alias="created_on",
        name="",
        description="",
        example="2020-07-13T19:20:58Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    double_val: Optional[float] = Field(
        None,
        alias="double_val",
        name="",
        description="",
        example=3.14100003,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bool_val: Optional[int] = Field(
        None,
        alias="bool_val",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    time_val: Optional[str] = Field(
        None,
        alias="time_val",
        name="",
        description="",
        example="01:45:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    start_date_time_val: Optional[datetime] = Field(
        None,
        alias="start_date_time_val",
        name="",
        description="",
        example="2020-07-31T07:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    end_date_time_val: Optional[datetime] = Field(
        None,
        alias="end_date_time_val",
        name="",
        description="",
        example="2020-07-31T12:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    applies_to_inv_slot: Optional[str] = Field(
        None,
        alias="applies_to_inv_slot",
        name="",
        description="",
        example="SOME_SCOPE_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    range_val: Optional[int] = Field(
        None,
        alias="range_val",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    str_val: Optional[str] = Field(
        None,
        alias="str_val",
        name="",
        description="",
        example="BUENA_VISTA_SKU",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class CMEDLRRuleSettingModel(BaseModel):
    """Payload class for CMEDLRRuleSettingModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Rule Setting"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.id"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rule_setting"

    data: Data = Field(..., alias="data")
    metadata: GlobalCMEDLRMetadata = Field(..., alias="metadata")
