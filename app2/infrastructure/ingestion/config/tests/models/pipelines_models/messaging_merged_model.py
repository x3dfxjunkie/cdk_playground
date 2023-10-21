"""Source Data Contract Template for MessasingMerged"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.pattern_instance_base_model import PatternInstanceBaseModel
from app.infrastructure.ingestion.config.tests.models.resource_models.messaging_resource_model import MessagingResources


class MessagingPatternInstance(PatternInstanceBaseModel):
    resources: MessagingResources = Field(
        ...,
        alias="resources",
        name="",
        description="",
    )


class MessagingMergedModel(BaseModel):
    class Config:
        """Payload Level Metadata"""

        title = "MessasingMerged"
        stream_name = ""
        description = "MessasingMerged"  # optional
        unique_identifier = [""]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = ""  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = ""
        key_path_value = ""

    stack_extension: str = Field(
        ...,
        alias="stack_extension",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ingest_pattern: str = Field(
        ...,
        alias="ingest_pattern",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    active: bool = Field(
        ...,
        alias="active",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pattern_instances: List[MessagingPatternInstance] = Field(
        ...,
        alias="pattern_instances",
        name="",
        description="",
    )
