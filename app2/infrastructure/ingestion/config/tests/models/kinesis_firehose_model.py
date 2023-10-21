""" Guest360 Kinesis Firehose Model"""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BufferingHints(BaseModel):
    interval: int = Field(
        ...,
        alias="interval",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit_of_time: str = Field(
        ...,
        alias="unit_of_time",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Dynamic(BaseModel):
    enabled: bool = Field(
        ...,
        alias="enabled",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    keys: Optional[dict] = Field(
        None,
        alias="keys",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Partitioning(BaseModel):
    dynamic: Dynamic = Field(
        ...,
        alias="dynamic",
        name="",
        description="",
    )

    custom_keys: Optional[dict] = Field(
        None,
        alias="custom_keys",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class KinesisFirehose(BaseModel):
    enabled: bool = Field(
        ...,
        alias="enabled",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bucket_name: str = Field(
        ...,
        alias="bucket_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    buffering_hints: BufferingHints = Field(
        ...,
        alias="buffering_hints",
        name="",
        description="",
    )

    partitioning: Partitioning = Field(
        ...,
        alias="partitioning",
        name="",
        description="",
    )
