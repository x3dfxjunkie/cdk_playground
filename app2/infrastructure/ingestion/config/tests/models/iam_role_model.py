"""Guest360 IAM Role Base Model"""
from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field, validator
from app.infrastructure.ingestion.config.utils.validation_utils import type_validator


class Iam(BaseModel):
    role_name: str = Field(
        ...,
        alias="role_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    assumed_by: Any = Field(
        ...,
        alias="assumed_by",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    description: str = Field(
        ...,
        alias="description",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    @validator("assumed_by")
    def validate_assumed_by(cls, v):  # pylint: disable=E0213
        return type_validator(
            value=v,
            lib_path="aws_cdk.aws_iam",
            attr_path="ServicePrincipal",
        )
