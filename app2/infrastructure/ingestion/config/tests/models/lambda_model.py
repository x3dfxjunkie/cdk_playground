"""Guest360 Lambda model"""
from __future__ import annotations
from typing import Any, Optional
from pydantic import BaseModel, Field, validator
from app.infrastructure.ingestion.config.utils.validation_utils import type_validator


class Lambda(BaseModel):
    function_name: str = Field(
        ...,
        alias="function_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    handler: str = Field(
        ...,
        alias="handler",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    code: str = Field(
        ...,
        alias="code",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
