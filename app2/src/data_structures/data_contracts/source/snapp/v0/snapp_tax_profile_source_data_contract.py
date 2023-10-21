"""Source Data Class Template for SnApp TaxProfile"""

from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.snapp.global_snapp_source_data_contract import GlobalSnAppHeader


class TaxListItem(BaseModel):
    tax_id: str = Field(
        ...,
        alias="TaxId",
        description="",
        example="",
        guest_identifier="",
        transaction_identifier="",
        identifier_tag="",
    )


class Payload(BaseModel):
    """Class for SnApp Tax Profile Payload"""

    tax_list: List[TaxListItem] = Field(
        ...,
        alias="TaxList",
        name="",
        description="",
    )
    tax_profile_code: str = Field(
        ...,
        alias="TaxProfileCode",
        name="",
        description="",
        example="TXP5010308",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_profile_id: str = Field(
        ...,
        alias="TaxProfileId",
        name="",
        description="",
        example="31651BAB-D003-E6BC-11E4-017CB9090115",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_profile_name: str = Field(
        ...,
        alias="TaxProfileName",
        name="",
        description="",
        example="AK12 MINI GOLF-Florida/Orange County",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SnAppTaxProfileModel(BaseModel):
    """SnAppTaxProfileModel"""

    class Config:
        """Config for SnAppTaxProfileModel"""

        title = "SnApp Tax Profile"
        stream_name = "prd-use1-guest360-snapp-stream"
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "Header.Namespace"
        key_path_value = "SnApp.TaxProfile"

    header: GlobalSnAppHeader = Field(..., alias="Header", description="SnApp data metadata")
    payload: Payload = Field(..., alias="Payload", description="Data payload")
