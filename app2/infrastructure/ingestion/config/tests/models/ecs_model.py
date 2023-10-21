"""Guest360 ECS Model"""
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.iam_role_model import Iam
from app.infrastructure.ingestion.config.tests.models.networking_model import Networking


class Ecr(BaseModel):
    repository_name: str = Field(
        ...,
        alias="repository_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class S3(BaseModel):
    bucket_name: str = Field(
        ...,
        alias="bucket_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Environment(BaseModel):
    default_batch_size: int = Field(
        ...,
        alias="DEFAULT_BATCH_SIZE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_max_retry_attempt: int = Field(
        ...,
        alias="DEFAULT_MAX_RETRY_ATTEMPT",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_retry_batch_size: int = Field(
        ...,
        alias="DEFAULT_RETRY_BATCH_SIZE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_max_wait_millisecs: int = Field(
        ...,
        alias="DEFAULT_MAX_WAIT_MILLISECS",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_batch_size: int = Field(
        ...,
        alias="MAX_BATCH_SIZE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_wait_millisecs: int = Field(
        ...,
        alias="MAX_WAIT_MILLISECS",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    loglevel: Optional[str] = Field(
        None,
        alias="LOGLEVEL",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    environment: str = Field(
        ...,
        alias="ENVIRONMENT",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    region: Optional[str] = Field(
        None,
        alias="REGION",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis_stream: str = Field(
        ...,
        alias="KINESIS_STREAM",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis_partitions: Optional[int] = Field(
        None,
        alias="KINESIS_PARTITIONS",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis_batch_size: Optional[int] = Field(
        None,
        alias="KINESIS_BATCH_SIZE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis_retry_batch_size: Optional[int] = Field(
        None,
        alias="KINESIS_RETRY_BATCH_SIZE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    kinesis_max_wait_millisecs: Optional[int] = Field(
        None,
        alias="KINESIS_MAX_WAIT_MILLISECS",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    failed_msg_bucket_name: str = Field(
        ...,
        alias="FAILED_MSG_BUCKET_NAME",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    failed_msg_bucket_path: str = Field(
        ...,
        alias="FAILED_MSG_BUCKET_PATH",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    max_retry_attempt: int = Field(
        ...,
        alias="MAX_RETRY_ATTEMPT",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_secret_path: Optional[str] = Field(
        None,
        alias="RABBITMQ_SECRET_PATH",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_host: Optional[str] = Field(
        None,
        alias="RABBITMQ_HOST",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_vhost: Optional[str] = Field(
        None,
        alias="RABBITMQ_VHOST",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_port: Optional[int] = Field(
        None,
        alias="RABBITMQ_PORT",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_queue: Optional[str] = Field(
        None,
        alias="RABBITMQ_QUEUE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_queue_durable: Optional[bool] = Field(
        None,
        alias="RABBITMQ_QUEUE_DURABLE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_qos_prefetch_count: Optional[int] = Field(
        None,
        alias="RABBITMQ_QOS_PREFETCH_COUNT",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_routing_key: Optional[str] = Field(
        None,
        alias="RABBITMQ_ROUTING_KEY",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_exchange: Optional[str] = Field(
        None,
        alias="RABBITMQ_EXCHANGE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_exchange_type: Optional[str] = Field(
        None,
        alias="RABBITMQ_EXCHANGE_TYPE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_exchange_passive: Optional[bool] = Field(
        None,
        alias="RABBITMQ_EXCHANGE_PASSIVE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_exchange_durable: Optional[bool] = Field(
        None,
        alias="RABBITMQ_EXCHANGE_DURABLE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rabbitmq_exchange_auto_delete: Optional[bool] = Field(
        None,
        alias="RABBITMQ_EXCHANGE_AUTO_DELETE",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Service(BaseModel):
    service_name: str = Field(
        ...,
        alias="service_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    image_tag: str = Field(
        ...,
        alias="image_tag",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    desired_count: int = Field(
        ...,
        alias="desired_count",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cloudmap: bool = Field(
        ...,
        alias="cloudmap",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    environment: Environment = Field(
        ...,
        alias="environment",
        name="",
        description="",
    )


class Ecs(BaseModel):
    region: str = Field(
        ...,
        alias="region",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    memory_mib: int = Field(
        ...,
        alias="memory_mib",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpu_limitmb: int = Field(
        ...,
        alias="cpu_limitmb",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    networking: Networking = Field(
        ...,
        alias="networking",
        name="",
        description="",
    )

    iam: Iam = Field(
        ...,
        alias="iam",
        name="",
        description="",
    )

    ecr: Ecr = Field(
        ...,
        alias="ecr",
        name="",
        description="",
    )

    secret_name: str = Field(
        ...,
        alias="secret_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    s3: S3 = Field(
        ...,
        alias="s3",
        name="",
        description="",
    )

    services: List[Service] = Field(
        ...,
        alias="services",
        name="",
        description="",
    )
