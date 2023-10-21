"""Source Data Contract Template for DmsMerged"""

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.pattern_instance_base_model import PatternInstanceBaseModel
from app.infrastructure.ingestion.config.tests.models.resource_models.dms_resource_model import DMSResources


class DmsPatternInstance(PatternInstanceBaseModel):
    resources: DMSResources = Field(
        ...,
        alias="resources",
        name="",
        description="",
    )


class DmsMergedModel(BaseModel):
    class Config:
        """Payload Level Metadata"""

        title = "DmsMerged"
        stream_name = ""
        description = "DmsMerged"  # optional
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
        max_length=12,
        regex=r"^[a-zA-Z][a-zA-Z0-9-]*$",
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

    feature_branch: bool = Field(
        ...,
        alias="feature_branch",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pattern_instances: List[DmsPatternInstance] = Field(
        ...,
        alias="pattern_instances",
        name="",
        description="",
    )
