"""Pipelines config messaging resource model"""
from __future__ import annotations
from pydantic import Field
from app.infrastructure.ingestion.config.tests.models.kinesis_model import Kinesis
from app.infrastructure.ingestion.config.tests.models.kinesis_firehose_model import KinesisFirehose
from app.infrastructure.ingestion.config.tests.models.ecs_model import Ecs
from app.infrastructure.ingestion.config.tests.models.resource_base_model import ResourceBaseModel


class MessagingResources(ResourceBaseModel):
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

    ecs: Ecs = Field(
        ...,
        alias="ecs",
        name="",
        description="",
    )

    cluster_name: str = Field(
        ...,
        alias="cluster_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
