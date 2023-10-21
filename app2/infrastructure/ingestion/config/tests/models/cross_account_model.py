"""Pipelines config cross account model"""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossAccount(BaseModel):
    cross_account_type: Optional[str] = Field(
        None,
        alias="cross_account_type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cross_account_id: Optional[str] = Field(
        None,
        alias="cross_account_id",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cross_account_role_name: Optional[str] = Field(
        None,
        alias="cross_account_role_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
