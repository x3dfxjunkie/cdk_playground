"""Pipelines config dms resource model"""
from __future__ import annotations

from typing import List, Optional

from pydantic import Field, validator
from app.infrastructure.ingestion.config.tests.models.dms_model import (
    DmsReplInstance,
    SourceEndpoint,
    DmsReplTaskItem,
    TargetEndpoint,
)
from app.infrastructure.ingestion.config.tests.models.kinesis_model import Kinesis
from app.infrastructure.ingestion.config.tests.models.kinesis_firehose_model import KinesisFirehose
from app.infrastructure.ingestion.config.tests.models.iam_role_model import Iam
from app.infrastructure.ingestion.config.tests.models.resource_base_model import ResourceBaseModel
from app.infrastructure.ingestion.config.tests.models.networking_model import Networking


class DMSResources(ResourceBaseModel):
    dms_repl_instance: DmsReplInstance = Field(
        ...,
        alias="dms_repl_instance",
        name="",
        description="",
    )

    source_endpoint: SourceEndpoint = Field(
        ...,
        alias="source_endpoint",
        name="",
        description="",
    )

    dms_repl_task: List[DmsReplTaskItem] = Field(
        ...,
        alias="dms_repl_task",
        name="",
        description="",
    )

    stack_extension: str = Field(
        ...,
        max_length=12,
        regex=r"^[a-zA-Z][a-zA-Z0-9-]*$",
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

    source_iam: Iam = Field(
        ...,
        alias="source_iam",
        name="",
        description="",
    )

    target_iam: Iam = Field(
        ...,
        alias="target_iam",
        name="",
        description="",
    )

    target_endpoint: TargetEndpoint = Field(
        ...,
        alias="target_endpoint",
        name="",
        description="",
    )

    networking: Networking = Field(
        ...,
        alias="networking",
        name="",
        description="",
    )

    source_kms_key: str = Field(
        ...,
        alias="source_kms_key",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_ssl_cert: Optional[str] = Field(
        None,
        alias="source_ssl_cert",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    @validator("stack_extension")
    def validate_task_identifier_length(cls, value, values):  # pylint: disable=E0213
        for rep_task in values["dms_repl_task"]:
            len_id = len(rep_task.replication_task_identifier + value)
            if len_id > 16:
                raise ValueError(
                    f"the stack extension and task identifier have exceeded the length limit by: {(len_id - 16)} char(s)"
                )
            return value
