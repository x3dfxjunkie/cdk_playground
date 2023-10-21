""" Guest360 Event Bridge Pipe Model"""
from typing import Optional
from pydantic import BaseModel, Field


class DeadLetterConfig(BaseModel):
    arn: Optional[str] = Field(
        None,
        alias="arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceKinesisStreamParameters(BaseModel):
    starting_position: str = Field(
        ...,
        alias="startingPosition",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    batch_size: int = Field(
        ...,
        alias="batchSize",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    maximum_retry_attempts: int = Field(
        ...,
        alias="maximumRetryAttempts",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    maximum_record_age_in_seconds: Optional[int] = Field(
        None,
        alias="maximumRecordAgeInSeconds",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dead_letter_config: DeadLetterConfig = Field(
        ...,
        alias="deadLetterConfig",
        name="",
        description="",
    )


class ValidationPipeSourceParameters(BaseModel):
    kinesis_stream_parameters: SourceKinesisStreamParameters = Field(
        ...,
        alias="kinesis_stream_parameters",
        name="",
        description="",
    )

    sqs_queue_parameters: Optional[dict] = Field(
        None,
        alias="sqs_queue_parameters",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TargetKinesisStreamParameters(BaseModel):
    partition_key: str = Field(
        ...,
        alias="partitionKey",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class ValidationPipeTargetParameters(BaseModel):
    kinesis_stream_parameters: TargetKinesisStreamParameters = Field(
        ...,
        alias="kinesis_stream_parameters",
        name="",
        description="",
    )

    lambda_function_parameters: Optional[dict] = Field(
        None,
        alias="lambda_function_parameters",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EventBridgePipeValidation(BaseModel):
    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    role_arn: Optional[str] = Field(
        None,
        alias="role_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pipe_source_parameters: ValidationPipeSourceParameters = Field(
        ...,
        alias="pipe_source_parameters",
        name="",
        description="",
    )

    pipe_target_parameters: ValidationPipeTargetParameters = Field(
        ...,
        alias="pipe_target_parameters",
        name="",
        description="",
    )


class DeadLetterPipeSourceParameters(BaseModel):
    sqs_queue_parameters: Optional[dict] = Field(
        None,
        alias="sqs_queue_parameters",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DeadLetterPipeTargetParameters(BaseModel):
    lambda_function_parameters: Optional[dict] = Field(
        None,
        alias="lambda_function_parameters",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class EventBridgePipeDeadLetterQueue(BaseModel):
    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    role_arn: Optional[str] = Field(
        None,
        alias="role_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pipe_source_parameters: DeadLetterPipeSourceParameters = Field(
        ...,
        alias="pipe_source_parameters",
        name="",
        description="",
    )

    pipe_target_parameters: DeadLetterPipeTargetParameters = Field(
        ...,
        alias="pipe_target_parameters",
        name="",
        description="",
    )
