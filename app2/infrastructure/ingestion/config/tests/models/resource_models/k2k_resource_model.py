"""Pipelines config kinesis to kinesis resource model"""
from __future__ import annotations
from pydantic import Field
from app.infrastructure.ingestion.config.tests.models.kinesis_model import Kinesis
from app.infrastructure.ingestion.config.tests.models.kinesis_firehose_model import KinesisFirehose
from app.infrastructure.ingestion.config.tests.models.resource_base_model import ResourceBaseModel
from app.infrastructure.ingestion.config.tests.models.cross_account_model import CrossAccount


class K2KResources(ResourceBaseModel):
    stack_extension: str = Field(
        ...,
        alias="stack_extension",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis: Kinesis = Field(
        ...,
        alias="kinesis",
        name="",
        description="",
    )

    kinesis_firehose: KinesisFirehose = Field(
        ...,
        alias="kinesis_firehose",
        name="",
        description="",
    )

    cross_account: CrossAccount = Field(
        ...,
        alias="cross_account",
        name="",
        description="",
    )
