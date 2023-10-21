"""Guest360 Kinesis Base Model"""
from __future__ import annotations
from typing import Any, Optional
from pydantic import BaseModel, Field, validator
from app.infrastructure.ingestion.config.tests.models.mixins.validator_mixins import EncryptionKeyValidatorMixin
from app.infrastructure.ingestion.config.utils.validation_utils import type_validator


class Kinesis(BaseModel, EncryptionKeyValidatorMixin):
    retention_period: Any = Field(
        ...,
        alias="retention_period",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    stream_mode: Any = Field(
        ...,
        alias="stream_mode",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    shard_count: int = Field(
        ...,
        alias="shard_count",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encryption_key: Optional[Any] = Field(
        None,
        alias="encryption_key",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    stream_name: Optional[str] = Field(
        None,
        alias="stream_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    @validator("retention_period")
    def validate_retention_period(cls, v):  # pylint: disable=E0213
        return type_validator(
            value=v,
            lib_path="aws_cdk",
            attr_path="Duration",
        )

    @validator("stream_mode")
    def validate_stream_mode(cls, v):  # pylint: disable=E0213
        return type_validator(
            value=v,
            lib_path="aws_cdk.aws_kinesis",
            attr_path="StreamMode",
        )
