""" Pipelines config resources pipe base model"""
from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.lambda_model import Lambda
from app.infrastructure.ingestion.config.tests.models.app_config_model import AppConfig
from app.infrastructure.ingestion.config.tests.models.sqs_model import Sqs
from app.infrastructure.ingestion.config.tests.models.kinesis_model import Kinesis
from app.infrastructure.ingestion.config.tests.models.event_bridge_pipe_model import (
    EventBridgePipeValidation,
    EventBridgePipeDeadLetterQueue,
)


class ResourceBaseModel(BaseModel):
    event_bridge_pipe_validation: EventBridgePipeValidation = Field(
        ...,
        alias="event_bridge_pipe_validation",
        name="",
        description="",
    )
    event_bridge_pipe_dead_letter_queue: EventBridgePipeDeadLetterQueue = Field(
        ...,
        alias="event_bridge_pipe_dead_letter_queue",
        name="",
        description="",
    )
    lambda_validator: Lambda = Field(
        ...,
        alias="lambda_validator",
        name="",
        description="",
    )
    lambda_dead_letter: Lambda = Field(
        ...,
        alias="lambda_dead_letter",
        name="",
        description="",
    )
    app_config: AppConfig = Field(
        ...,
        alias="app_config",
        name="",
        description="",
    )
    sqs: Sqs = Field(
        ...,
        alias="sqs",
        name="",
        description="",
    )
    kinesis_dmz: Kinesis = Field(
        ...,
        alias="kinesis_dmz",
        name="",
        description="",
    )
